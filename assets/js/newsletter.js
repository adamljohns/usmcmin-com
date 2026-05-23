/* USMC Ministries — newsletter signup
 *
 * Default behavior (2026-05-23 onwards): silently POSTs the email to
 * FormSubmit, which relays it to the USMC business mailbox. No mail-client
 * popup, no "open your mail app and hit send" friction — the visitor stays
 * on the page and we capture every signup.
 *
 * To upgrade to a first-party API endpoint later, set
 *   window.USMC_NEWSLETTER_ENDPOINT = "https://api.example.com/subscribe"
 * before this script runs and the FormSubmit fallback is skipped.
 *
 * Forms must have:
 *   <form data-newsletter [data-source="page-name"]>
 *     <input type="email" name="email" required>
 *     <button type="submit">Join</button>
 *   </form>
 */
(function () {
  'use strict';

  var FORMSUBMIT_URL = 'https://formsubmit.co/ajax/usmcministries2022@gmail.com';

  document.querySelectorAll('form[data-newsletter]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = form.querySelector('input[type="email"]');
      var email = (input && input.value || '').trim();
      if (!email) return;

      var source = form.getAttribute('data-source') || (location.pathname || '/');
      var endpoint = window.USMC_NEWSLETTER_ENDPOINT;
      var note = form.querySelector('.email-status');

      function showStatus(msg, ok) {
        if (note) {
          note.textContent = msg;
          note.style.color = ok ? '' : 'var(--red, #C0392B)';
        }
      }

      if (endpoint) {
        // API mode — POST JSON to a first-party subscribe endpoint.
        fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: email, source: source })
        }).then(function (r) {
          return r.json().catch(function () { return { success: r.ok }; });
        }).then(function (data) {
          if (data && data.success) {
            form.reset();
            showStatus(data.message || "You're in. Welcome to the brotherhood.", true);
          } else {
            showStatus((data && data.error) || 'Subscribe failed. Try again.', false);
          }
        }).catch(function () {
          showStatus('Network error. Please try again.', false);
        });
      } else {
        // FormSubmit relay — emails the subscriber's address to USMC.
        var payload = {
          _subject: 'USMC Field Brief — new subscriber',
          _template: 'table',
          _captcha: 'false',
          email: email,
          source: source,
          submittedAt: new Date().toISOString()
        };
        fetch(FORMSUBMIT_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(payload)
        }).then(function (r) {
          return r.ok ? r.json().catch(function () { return { success: true }; }) : { success: false };
        }).then(function (data) {
          if (data && (data.success || data.success === undefined)) {
            form.reset();
            showStatus("You're in. Welcome to the brotherhood.", true);
          } else {
            showStatus('Subscribe failed. Please try again.', false);
          }
        }).catch(function () {
          showStatus('Network error. Please try again.', false);
        });
      }
    });
  });
})();
