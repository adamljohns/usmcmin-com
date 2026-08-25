/*
 * TMC Husband Firebase adapter v1.
 * Optional by design: static course pages may omit this file entirely.
 * Firebase's modular SDK is dependency-injected through createFirebaseServices();
 * no unpinned network imports or page-DOM access live here.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.TmcHusbandFirebase = api;
}(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const MODULE_KEYS = Object.freeze(['m01', 'm02', 'm03', 'm04', 'm05', 'm06', 'm07']);
  const COURSE_ID = 'tmc-husband-v1';
  const CONSENT_SOURCE = 'tmc-husband-course';
  const CONSENT_KEYS = Object.freeze(['email', 'subscribed', 'consentVersion', 'source']);
  const CONFLICT_CODES = new Set(['auth/credential-already-in-use', 'auth/email-already-in-use', 'auth/account-exists-with-different-credential']);
  const hasOwn = (object, key) => Object.prototype.hasOwnProperty.call(object, key);

  function emptyModules() {
    return Object.fromEntries(MODULE_KEYS.map((key) => [key, false]));
  }

  function isRecord(value) {
    return value !== null && typeof value === 'object' && !Array.isArray(value);
  }

  function normalizeProgress(input) {
    const source = isRecord(input) ? input : {};
    const sourceModules = isRecord(source.modules) ? source.modules : {};
    const modules = emptyModules();
    for (const key of MODULE_KEYS) {
      modules[key] = hasOwn(sourceModules, key) && sourceModules[key] === true;
    }
    return {
      modules,
      lastModule: MODULE_KEYS.includes(source.lastModule) ? source.lastModule : null
    };
  }

  function mergeProgress(localInput, cloudInput) {
    const local = normalizeProgress(localInput);
    const cloud = normalizeProgress(cloudInput);
    const modules = emptyModules();
    for (const key of MODULE_KEYS) modules[key] = local.modules[key] || cloud.modules[key];
    return {
      modules,
      lastModule: local.lastModule || cloud.lastModule || null
    };
  }

  function normalizeConsent(input) {
    if (!isRecord(input) || Object.keys(input).some((key) => !CONSENT_KEYS.includes(key))) {
      throw new TypeError('Consent must contain only approved fields');
    }
    if (typeof input.email !== 'string') throw new TypeError('A valid email is required');
    const email = input.email.trim().toLowerCase();
    if (email.length < 3 || email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      throw new TypeError('A valid email of at most 254 characters is required');
    }
    if (typeof input.subscribed !== 'boolean') throw new TypeError('Subscribed must be a boolean');
    if (input.consentVersion !== 1) throw new TypeError('Unknown consent version');
    if (input.source !== CONSENT_SOURCE) throw new TypeError('Unknown consent source');
    return {email, subscribed: input.subscribed, consentVersion: 1, source: CONSENT_SOURCE};
  }

  function requireService(services, method) {
    if (!services || typeof services[method] !== 'function') throw new Error(`Firebase service ${method} is unavailable`);
    return services[method].bind(services);
  }

  function createFirebaseAdapter(options) {
    const settings = options || {};
    const enabled = settings.enabled !== false;
    const services = settings.services || {};

    async function writeMerged(uid, localProgress, cloudProgress) {
      const progress = mergeProgress(localProgress, cloudProgress);
      await requireService(services, 'writeProgress')(uid, progress);
      return progress;
    }

    return Object.freeze({
      enabled,

      async initialize(localInput) {
        const local = normalizeProgress(localInput);
        if (!enabled) return {user: null, progress: local, syncStatus: 'disabled', dirty: false};
        try {
          const user = await requireService(services, 'ensureAnonymous')();
          if (typeof services.writeUserProfile === 'function') await services.writeUserProfile(user);
          const cloud = await requireService(services, 'readProgress')(user.uid);
          const progress = await writeMerged(user.uid, local, cloud);
          return {user, progress, syncStatus: 'synced', dirty: false};
        } catch (error) {
          return {user: null, progress: local, syncStatus: 'pending', dirty: true, error};
        }
      },

      async syncProgress(uid, localInput) {
        const progress = normalizeProgress(localInput);
        if (!enabled) return {progress, syncStatus: 'disabled', dirty: false};
        try {
          await requireService(services, 'writeProgress')(uid, progress);
          return {progress, syncStatus: 'synced', dirty: false};
        } catch (error) {
          return {progress, syncStatus: 'pending', dirty: true, error};
        }
      },

      async linkGoogle(localInput) {
        const local = normalizeProgress(localInput);
        if (!enabled) return {user: null, progress: local, syncStatus: 'disabled', dirty: false};
        let user;
        let accountMerge = 'linked';
        try {
          user = await requireService(services, 'linkGoogle')();
        } catch (error) {
          if (!CONFLICT_CODES.has(error && error.code)) {
            return {user: null, progress: local, syncStatus: 'pending', dirty: true, error};
          }
          try {
            user = await requireService(services, 'signInGoogle')(error.credential || null);
            accountMerge = 'existing-account';
          } catch (fallbackError) {
            return {user: null, progress: local, syncStatus: 'pending', dirty: true, error: fallbackError};
          }
        }
        try {
          if (typeof services.writeUserProfile === 'function') await services.writeUserProfile(user);
          const cloud = await requireService(services, 'readProgress')(user.uid);
          const progress = await writeMerged(user.uid, local, cloud);
          return {user, progress, accountMerge, syncStatus: 'synced', dirty: false};
        } catch (error) {
          return {user, progress: local, accountMerge, syncStatus: 'pending', dirty: true, error};
        }
      },

      async saveConsent(uid, input) {
        const consent = normalizeConsent(input);
        if (!enabled) return {consent, syncStatus: 'disabled', dirty: false};
        try {
          await requireService(services, 'writeConsent')(uid, consent);
          return {consent, syncStatus: 'synced', dirty: false};
        } catch (error) {
          return {consent, syncStatus: 'pending', dirty: true, error};
        }
      }
    });
  }

  function createFirebaseServices(options) {
    const settings = options || {};
    const sdk = settings.sdk;
    const config = settings.config;
    if (!sdk || !isRecord(config)) throw new TypeError('Pinned Firebase SDK functions and public config must be injected');
    const required = ['initializeApp', 'getAuth', 'getFirestore', 'signInAnonymously', 'GoogleAuthProvider',
      'linkWithPopup', 'signInWithCredential', 'doc', 'getDoc', 'setDoc', 'serverTimestamp'];
    for (const name of required) if (typeof sdk[name] !== 'function') throw new TypeError(`Missing Firebase SDK function: ${name}`);

    const app = sdk.initializeApp(config);
    const auth = sdk.getAuth(app);
    const db = sdk.getFirestore(app);
    const provider = new sdk.GoogleAuthProvider();
    const progressRef = (uid) => sdk.doc(db, 'users', uid, 'courseProgress', COURSE_ID);

    return Object.freeze({
      async ensureAnonymous() {
        if (auth.currentUser) return auth.currentUser;
        return (await sdk.signInAnonymously(auth)).user;
      },
      async linkGoogle() {
        if (!auth.currentUser) throw new Error('Anonymous session must initialize before Google linking');
        return (await sdk.linkWithPopup(auth.currentUser, provider)).user;
      },
      async signInGoogle(credential) {
        if (!credential) throw new Error('Existing-account fallback requires a Google credential');
        return (await sdk.signInWithCredential(auth, credential)).user;
      },
      async writeUserProfile(user) {
        const ref = sdk.doc(db, 'users', user.uid);
        const prior = await sdk.getDoc(ref);
        const createdAt = prior.exists() && prior.data().createdAt ? prior.data().createdAt : sdk.serverTimestamp();
        await sdk.setDoc(ref, {
          schemaVersion: 1,
          createdAt,
          lastSeenAt: sdk.serverTimestamp(),
          authKind: user.isAnonymous ? 'anonymous' : 'google'
        });
      },
      async readProgress(uid) {
        const snapshot = await sdk.getDoc(progressRef(uid));
        return snapshot.exists() ? snapshot.data() : null;
      },
      async writeProgress(uid, input) {
        const progress = normalizeProgress(input);
        const ref = progressRef(uid);
        const prior = await sdk.getDoc(ref);
        const priorData = prior.exists() ? prior.data() : {};
        const completed = MODULE_KEYS.every((key) => progress.modules[key]);
        await sdk.setDoc(ref, {
          courseId: COURSE_ID,
          contentVersion: 1,
          modules: progress.modules,
          lastModule: progress.lastModule,
          startedAt: priorData.startedAt || sdk.serverTimestamp(),
          updatedAt: sdk.serverTimestamp(),
          completedAt: completed ? (priorData.completedAt || sdk.serverTimestamp()) : null
        });
      },
      async writeConsent(uid, input) {
        const consent = normalizeConsent(input);
        const ref = sdk.doc(db, 'users', uid, 'consents', 'field-brief');
        const prior = await sdk.getDoc(ref);
        const priorData = prior.exists() ? prior.data() : {};
        await sdk.setDoc(ref, {
          ...consent,
          consentedAt: priorData.consentedAt || sdk.serverTimestamp(),
          unsubscribedAt: consent.subscribed ? null : sdk.serverTimestamp()
        });
      }
    });
  }

  return Object.freeze({
    MODULE_KEYS,
    COURSE_ID,
    CONSENT_SOURCE,
    normalizeProgress,
    mergeProgress,
    normalizeConsent,
    createFirebaseAdapter,
    createFirebaseServices
  });
}));
