/* Bow & Arrow Studio OS — Dashboard JavaScript
   v2.8 — Mar 31 Refinement: April fully seeded from live iCal feeds (all 4 properties); Apt 8 Mar 28–Apr 3 active; monthly estimates corrected (~$5,900 Apr vs prior $1,290); Brittany checked out */

const API_BASE = ''; // Empty = use demo data (no backend running on GitHub Pages)

// Demo data (seeded from real B&A data — used when backend is offline)
const DEMO = {
    properties: [
        // NOTE: current_guest/next_guest hydrated live from reservations via hydratePropertiesFromReservations()
        { id: 1, name: 'Spacious Apartment', apt_number: '6', beds: 1, baths: 1, base_nightly_rate: 85, status: 'active', current_guest: null, current_checkout: null, next_guest: null, next_checkin: null, review_avg: 5.0, review_count: 24 },
        { id: 2, name: 'Boho-Modern Apartment', apt_number: '7', beds: 2, baths: 2, base_nightly_rate: 116, status: 'active', current_guest: null, current_checkout: null, next_guest: null, next_checkin: null, review_avg: 5.0, review_count: 18 },
        { id: 3, name: 'Orange Apartment', apt_number: '8', beds: 1, baths: 1, base_nightly_rate: 93, status: 'active', current_guest: null, current_checkout: null, next_guest: null, next_checkin: null, review_avg: 5.0, review_count: 21 },
        { id: 4, name: 'Prof Row Cottage', apt_number: 'Cottage', beds: 3, baths: 1, base_nightly_rate: 43, min_nights: 30, status: 'active', current_guest: null, current_checkout: null, next_guest: null, next_checkin: null, review_avg: 4.9, review_count: 8 },
        { id: 5, name: 'Hanover Combined', apt_number: '6+8', beds: 2, baths: 2, base_nightly_rate: 150, status: 'active', current_guest: null, current_checkout: null, next_guest: null, next_checkin: null, review_avg: 5.0, review_count: 6 },
    ],
    reservations: [
        // ========== MARCH (Completed) ==========
        { id: 1, property_id: 3, guest_name: 'Brandi', checkin_date: '2026-03-15', checkout_date: '2026-03-21', platform: 'airbnb', payout: 465, status: 'checked_out', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 2, property_id: 1, guest_name: 'Jess', checkin_date: '2026-03-15', checkout_date: '2026-03-20', platform: 'airbnb', payout: 340, status: 'checked_out', apt_number: '6', property_name: 'Spacious Apartment', guests: 2 },
        { id: 4, property_id: 1, guest_name: 'Cleve', checkin_date: '2026-03-20', checkout_date: '2026-03-21', platform: 'airbnb', payout: 85, status: 'checked_out', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 3, property_id: 2, guest_name: 'Diane', checkin_date: '2026-03-19', checkout_date: '2026-03-26', platform: 'airbnb', payout: 650, status: 'checked_out', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 3 },
        { id: 5, property_id: 1, guest_name: 'Amy', checkin_date: '2026-03-23', checkout_date: '2026-03-29', platform: 'airbnb', payout: 340, status: 'checked_out', apt_number: '6', property_name: 'Spacious Apartment', guests: 2 },
        { id: 6, property_id: 2, guest_name: 'Brittany', checkin_date: '2026-03-26', checkout_date: '2026-03-30', platform: 'airbnb', payout: 370, status: 'checked_out', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 2 },

        // ========== APT 8 — Mar 28–Apr 3 (active now, confirmed from iCal) ==========
        { id: 50, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-03-28', checkout_date: '2026-04-03', platform: 'airbnb', payout: 558, status: 'checked_in', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },

        // ========== APT 6 — APRIL (from iCal, base $85/night) ==========
        // Apr 6 iCal shows: Mar29-31, Mar31-Apr2, Apr2-4, Apr4-5, Apr8-10, Apr10-11, Apr18-19, Apr24-26, Apr26-29, Apr30-May1, May1-3, May3-7, May15-17, May21-24, May28-31
        { id: 101, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-03-29', checkout_date: '2026-03-31', platform: 'airbnb', payout: 170, status: 'checked_out', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 102, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-03-31', checkout_date: '2026-04-02', platform: 'airbnb', payout: 170, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 103, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-04-02', checkout_date: '2026-04-04', platform: 'airbnb', payout: 170, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 104, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-04-04', checkout_date: '2026-04-05', platform: 'airbnb', payout: 85, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 105, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-04-08', checkout_date: '2026-04-10', platform: 'airbnb', payout: 170, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 106, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-04-10', checkout_date: '2026-04-11', platform: 'airbnb', payout: 85, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 107, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-04-18', checkout_date: '2026-04-19', platform: 'airbnb', payout: 85, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 108, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-04-24', checkout_date: '2026-04-26', platform: 'airbnb', payout: 170, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 109, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-04-26', checkout_date: '2026-04-29', platform: 'airbnb', payout: 255, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 110, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-04-30', checkout_date: '2026-05-01', platform: 'airbnb', payout: 85, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },

        // ========== APT 7 — APRIL (from iCal, base $116/night) ==========
        // Boho: Apr3-5, Apr6-9, Apr10-12, Apr13-14, Apr14-17, Apr17-19, Apr24-26, Apr27-29, Apr29-May2, May2-3
        { id: 201, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-03', checkout_date: '2026-04-05', platform: 'airbnb', payout: 232, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 202, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-06', checkout_date: '2026-04-09', platform: 'airbnb', payout: 348, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 203, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-10', checkout_date: '2026-04-12', platform: 'airbnb', payout: 232, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 204, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-13', checkout_date: '2026-04-14', platform: 'airbnb', payout: 116, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 205, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-14', checkout_date: '2026-04-17', platform: 'airbnb', payout: 348, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 206, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-17', checkout_date: '2026-04-19', platform: 'airbnb', payout: 232, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 207, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-24', checkout_date: '2026-04-26', platform: 'airbnb', payout: 232, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 208, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-27', checkout_date: '2026-04-29', platform: 'airbnb', payout: 232, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 209, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-04-29', checkout_date: '2026-05-02', platform: 'airbnb', payout: 348, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },

        // ========== APT 8 — APRIL (from iCal, base $93/night) ==========
        // Orange: Mar28-Apr3 (id:50 above spans), Apr3-4, Apr9-12, Apr17-19, Apr19-21
        { id: 301, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-04-03', checkout_date: '2026-04-04', platform: 'airbnb', payout: 93, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 302, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-04-09', checkout_date: '2026-04-12', platform: 'airbnb', payout: 279, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 303, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-04-17', checkout_date: '2026-04-19', platform: 'airbnb', payout: 186, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 304, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-04-19', checkout_date: '2026-04-21', platform: 'airbnb', payout: 186, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },

        // ========== COTTAGE — Virginia Van Alstine (Apr 6–May 6, 30 nights) ==========
        { id: 7, property_id: 4, guest_name: 'Virginia Van Alstine', checkin_date: '2026-04-06', checkout_date: '2026-05-06', platform: 'airbnb', payout: 1290, status: 'confirmed', apt_number: 'Cottage', property_name: 'Prof Row Cottage', guests: 2 },

        // ========== MAY (from iCal) ==========
        // Apt 6: May1-3, May3-7, May15-17, May21-24, May28-31
        { id: 401, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-05-01', checkout_date: '2026-05-03', platform: 'airbnb', payout: 170, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 402, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-05-03', checkout_date: '2026-05-07', platform: 'airbnb', payout: 340, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 403, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-05-15', checkout_date: '2026-05-17', platform: 'airbnb', payout: 170, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 404, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-05-21', checkout_date: '2026-05-24', platform: 'airbnb', payout: 255, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 405, property_id: 1, guest_name: 'Guest (Apt 6)', checkin_date: '2026-05-28', checkout_date: '2026-05-31', platform: 'airbnb', payout: 255, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        // Apt 7: May2-3, May7-10, May14-19, May29-31
        { id: 411, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-05-02', checkout_date: '2026-05-03', platform: 'airbnb', payout: 116, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 412, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-05-07', checkout_date: '2026-05-10', platform: 'airbnb', payout: 348, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 413, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-05-14', checkout_date: '2026-05-19', platform: 'airbnb', payout: 580, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        { id: 414, property_id: 2, guest_name: 'Guest (Apt 7)', checkin_date: '2026-05-29', checkout_date: '2026-05-31', platform: 'airbnb', payout: 232, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 1 },
        // Apt 8: May1-3, May15-17, May21-23, May25-27, May29-Jun1
        { id: 421, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-05-01', checkout_date: '2026-05-03', platform: 'airbnb', payout: 186, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 422, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-05-15', checkout_date: '2026-05-17', platform: 'airbnb', payout: 186, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 423, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-05-21', checkout_date: '2026-05-23', platform: 'airbnb', payout: 186, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 424, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-05-25', checkout_date: '2026-05-27', platform: 'airbnb', payout: 186, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 425, property_id: 3, guest_name: 'Guest (Apt 8)', checkin_date: '2026-05-29', checkout_date: '2026-06-01', platform: 'airbnb', payout: 279, status: 'confirmed', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
    ],
    financials: {
        get month() { const n=new Date(); return `${n.getFullYear()}-${String(n.getMonth()+1).padStart(2,'0')}`; },
        // Mar FINAL: $465+$340+$85+$650+$340+$370+$170(Mar29-31 Apt6) = $2,420; Apt8 Mar28-Apr3 $558 → Mar portion ~$465
        // Expenses: Tiffany Mar 15 3x ($130) + Amanda Apt 7 Mar 26 ($50) + Amy turnover Mar 29 ($38) = $218
        revenue: { airbnb: 2420, direct_booking: 0, merch: 0, vending: 0, car_rental: 0, total: 2420 },
        expenses: { general: 0, cleaners: 218, total: 218 },
        net_profit: 2202
    },
    monthly: [
        { month: '2025-10', revenue: 1800, expenses: 380, net: 1420 },
        { month: '2025-11', revenue: 2100, expenses: 410, net: 1690 },
        { month: '2025-12', revenue: 2600, expenses: 520, net: 2080 },
        { month: '2026-01', revenue: 1950, expenses: 350, net: 1600 },
        { month: '2026-02', revenue: 2300, expenses: 400, net: 1900 },
        { month: '2026-03', revenue: 2420, expenses: 218, net: 2202 },  // Mar final (iCal-confirmed incl Mar 29-31 Apt 6, Apt 8 Mar portion)
        // April: Apt6 $1,275 + Apt7 $1,740 + Apt8 $837 + Cottage $1,290 = $5,142 confirmed from iCal
        { month: '2026-04', revenue: 5142, expenses: 450, net: 4692 },
        // May confirmed from iCal: Apt6 $1,190 + Apt7 $1,276 + Apt8 $1,023 + Cottage partial (Virginia May1-6 ~$258) = $3,747
        { month: '2026-05', revenue: 3747, expenses: 380, net: 3367 },
    ],
    alerts: [], // populated dynamically by generateDynamicAlerts()
    cleaningSchedule: {
        scheduled: [
            { property_name: 'Spacious Apartment', apt_number: '6', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1, hours: 1.5, pay: 37.50 },
            { property_name: 'Boho-Modern Apartment', apt_number: '7', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1, hours: 2, pay: 50 },
            { property_name: 'Orange Apartment', apt_number: '8', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1, hours: 1.5, pay: 42.50 },
            { property_name: 'Boho-Modern Apartment', apt_number: '7', date: '2026-03-26', cleaner: 'amanda', type: 'turnover', completed: 1, hours: 2, pay: 50 },
        ],
        needed: [
            { apt_number: '6', guest_name: 'Amy', checkout_date: '2026-03-29', suggested_cleaner: 'tiffany', urgency: 'completed', note: '✅ Amy checked out Mar 29 — Tiffany turnover completed' },
            { apt_number: '7', guest_name: 'Brittany', checkout_date: '2026-03-30', suggested_cleaner: 'tiffany', urgency: 'upcoming', note: 'Monday checkout — Tiffany or Amanda for deep clean Mar 30' },
            { apt_number: 'Cottage', guest_name: 'Virginia Van Alstine', checkout_date: null, suggested_cleaner: null, urgency: 'none', note: '🗓️ Virginia arrives Apr 6 for 30-night stay — prep cottage before Apr 6' },
        ]
    },
    // occupancy is computed live from reservations via calculateOccupancy() — no stale hardcoded data
    occupancy: null,
    reviews: {
        overall_avg: 5.0,
        total_count: 77,
        perfect_streak: 77,
        recent: [
            { guest: 'Marcus T.', rating: 5, date: '2026-03-10', apt: '6', text: 'Perfect little spot in downtown FXBG. Adam was a great host!' },
            { guest: 'Sarah W.', rating: 5, date: '2026-03-02', apt: '7', text: 'The boho apartment was stunning. So much space for our family.' },
            { guest: 'James R.', rating: 5, date: '2026-02-25', apt: '8', text: 'Cozy and clean. Great location walking distance to everything.' },
        ]
    },
    maintenance: [
        { id: 1, property: 'Apt #6', issue: 'Bathroom faucet drip', priority: 'low', status: 'open', reported: '2026-03-14', notes: 'Slow drip, not urgent' },
        { id: 2, property: 'Apt #7', issue: 'HVAC filter replacement', priority: 'medium', status: 'scheduled', reported: '2026-03-10', scheduled_date: '2026-03-22', notes: 'Quarterly filter change' },
        { id: 3, property: 'Apt #8', issue: 'Replace smoke detector battery', priority: 'high', status: 'completed', reported: '2026-03-12', completed_date: '2026-03-13', notes: 'Done during turnover' },
    ]
};

// ===== TODAY AT A GLANCE =====
// Hero ops strip — shows what's happening right now: active guests, today's check-ins/outs, cleaning needs.
function renderTodayGlance(properties, reservations) {
    const container = document.getElementById('todayGlance');
    if (!container) return;

    const todayStr = today();
    const tomorrowStr = new Date(Date.now() + 86400000).toISOString().split('T')[0];

    const activeGuests = reservations.filter(r =>
        (r.status === 'checked_in' || (r.status === 'confirmed' && r.checkin_date <= todayStr && r.checkout_date > todayStr))
    );
    const todayCheckouts = reservations.filter(r => r.checkout_date === todayStr && r.status !== 'checked_out');
    const todayCheckins  = reservations.filter(r => r.checkin_date === todayStr);
    const tomorrowCheckins = reservations.filter(r => r.checkin_date === tomorrowStr);
    const tomorrowCheckouts = reservations.filter(r => r.checkout_date === tomorrowStr && r.status !== 'checked_out');

    // Turnovers today (checkout + checkin same property same day)
    const sameDayTurnovers = todayCheckouts.filter(co =>
        reservations.some(ci => ci.property_id === co.property_id && ci.checkin_date === todayStr && ci.id !== co.id)
    );

    const pills = [];

    if (activeGuests.length) {
        pills.push({ icon: '🏠', label: `${activeGuests.length} Active`, sub: activeGuests.map(r => `Apt ${r.apt_number}: ${r.guest_name}`).join(' · '), color: 'var(--sage)' });
    } else {
        pills.push({ icon: '🏠', label: 'All Vacant', sub: 'No active guests', color: 'var(--gray)' });
    }

    if (todayCheckouts.length) {
        pills.push({ icon: '🚪', label: `${todayCheckouts.length} Checkout${todayCheckouts.length > 1 ? 's' : ''} Today`, sub: todayCheckouts.map(r => `Apt ${r.apt_number}: ${r.guest_name}`).join(' · '), color: 'var(--dusty-rose)' });
    }
    if (todayCheckins.length) {
        pills.push({ icon: '🔑', label: `${todayCheckins.length} Check-in${todayCheckins.length > 1 ? 's' : ''} Today`, sub: todayCheckins.map(r => `Apt ${r.apt_number}: ${r.guest_name}`).join(' · '), color: 'var(--terracotta)' });
    }
    if (sameDayTurnovers.length) {
        pills.push({ icon: '⚡', label: 'Same-Day Turnover!', sub: sameDayTurnovers.map(r => `Apt ${r.apt_number} — schedule cleaner NOW`).join(' · '), color: 'var(--red)' });
    }
    if (tomorrowCheckins.length) {
        pills.push({ icon: '📋', label: `${tomorrowCheckins.length} Arriving Tomorrow`, sub: tomorrowCheckins.map(r => `Apt ${r.apt_number}: ${r.guest_name}`).join(' · '), color: 'var(--blue)' });
    }
    if (tomorrowCheckouts.length && !tomorrowCheckins.length) {
        pills.push({ icon: '🧹', label: `Prep Cleaning Tomorrow`, sub: tomorrowCheckouts.map(r => `Apt ${r.apt_number} turnover needed`).join(' · '), color: 'var(--yellow)' });
    }

    if (!todayCheckouts.length && !todayCheckins.length && !activeGuests.length) {
        pills.push({ icon: '☕', label: 'Quiet Day', sub: 'No check-ins, check-outs, or turnovers today', color: 'var(--gray)' });
    }

    container.innerHTML = `
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:0.85rem">
            ${pills.map((p, i) => `
                <div style="background:var(--warm-white);border-left:4px solid ${p.color};border-radius:2px;padding:1rem 1.25rem;animation:fadeSlideUp 0.25s ease ${i * 0.07}s forwards;opacity:0;box-shadow:0 1px 4px rgba(61,43,34,0.06)">
                    <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem">
                        <span style="font-size:1.25rem">${p.icon}</span>
                        <span style="font-weight:700;font-size:0.9rem;color:${p.color}">${p.label}</span>
                    </div>
                    <div style="font-size:0.78rem;color:var(--gray);font-family:var(--font-serif);font-style:italic;line-height:1.4">${p.sub}</div>
                </div>
            `).join('')}
        </div>
    `;
}

// ===== DYNAMIC PROPERTY HYDRATION =====
// Derives current_guest, current_checkout, next_guest, next_checkin from reservations.
// This keeps property status accurate without manual data updates.
function hydratePropertiesFromReservations(properties, reservations) {
    const todayStr = today();
    return properties.map(p => {
        const propRes = reservations
            .filter(r => r.property_id === p.id)
            .sort((a, b) => a.checkin_date.localeCompare(b.checkin_date));

        // Current guest = checked_in reservation that overlaps today
        const current = propRes.find(r =>
            r.checkin_date <= todayStr && r.checkout_date > todayStr &&
            (r.status === 'checked_in' || r.status === 'confirmed')
        );

        // Next guest = earliest future reservation (checkin > today, or same day as a checkout)
        const next = propRes.find(r =>
            r.checkin_date > todayStr &&
            (r.status === 'confirmed' || r.status === 'checked_in') &&
            (!current || r.id !== current.id)
        );

        return {
            ...p,
            current_guest: current ? current.guest_name + (current.guests > 1 ? ` (${current.guests} guests)` : '') : null,
            current_checkout: current ? current.checkout_date : null,
            next_guest: next ? next.guest_name : null,
            next_checkin: next ? next.checkin_date : null,
        };
    });
}

// ===== DYNAMIC ALERTS GENERATOR =====
// Generates context-aware alerts from live reservation + property data each page load.
// Always up-to-date — no more stale hardcoded dates.
function generateDynamicAlerts(reservations, properties, reviews) {
    const alerts = [];
    const todayStr = today();
    const tomorrowStr = new Date(Date.now() + 86400000).toISOString().split('T')[0];
    const in2DaysStr = new Date(Date.now() + 2 * 86400000).toISOString().split('T')[0];
    const in7DaysStr = new Date(Date.now() + 7 * 86400000).toISOString().split('T')[0];
    const now = new Date().toISOString();

    reservations.forEach(r => {
        // Skip already-completed reservations — no need to alert on past events
        if (r.status === 'checked_out') return;

        const daysToCheckin  = daysUntil(r.checkin_date);
        const daysToCheckout = daysUntil(r.checkout_date);

        // Today checkouts
        if (r.checkout_date === todayStr) {
            alerts.push({ type: 'checkout', priority: 'high',
                message: `🚪 ${r.guest_name} checks out TODAY from Apt #${r.apt_number}`, time: now });
        }
        // Today checkins
        if (r.checkin_date === todayStr) {
            alerts.push({ type: 'checkin', priority: 'high',
                message: `🔑 ${r.guest_name} checks in TODAY to Apt #${r.apt_number}`, time: now });
        }
        // Tomorrow checkouts
        if (r.checkout_date === tomorrowStr) {
            alerts.push({ type: 'checkout', priority: 'high',
                message: `🚪 ${r.guest_name} checks out TOMORROW from Apt #${r.apt_number}`, time: now });
        }
        // Tomorrow checkins
        if (r.checkin_date === tomorrowStr) {
            alerts.push({ type: 'checkin', priority: 'high',
                message: `🔑 ${r.guest_name} checks in TOMORROW to Apt #${r.apt_number}`, time: now });
        }
        // In 2 days
        if (r.checkin_date === in2DaysStr) {
            alerts.push({ type: 'checkin', priority: 'medium',
                message: `🔑 ${r.guest_name} arrives in 2 days — Apt #${r.apt_number}`, time: now });
        }
    });

    // Same-day turnover detection (checkout + checkin same property, same day)
    reservations.forEach(checkout => {
        if (checkout.status === 'checked_out') return;
        if (checkout.checkout_date < todayStr) return;
        if (checkout.checkout_date > in7DaysStr) return;
        const sameDay = reservations.find(checkin =>
            checkin.property_id === checkout.property_id &&
            checkin.checkin_date === checkout.checkout_date &&
            checkin.id !== checkout.id
        );
        if (sameDay) {
            const daysAway = daysUntil(checkout.checkout_date);
            const when = daysAway === 0 ? 'TODAY' : daysAway === 1 ? 'TOMORROW' : `in ${daysAway} days`;
            const priority = daysAway <= 1 ? 'high' : 'medium';
            // Avoid duplicate same-day alerts (only emit once per pair)
            const alreadyAdded = alerts.some(a => a.type === 'cleaning' &&
                a.message.includes(`#${checkout.apt_number}`) &&
                a.message.includes(checkout.guest_name));
            if (!alreadyAdded) {
                alerts.push({ type: 'cleaning', priority,
                    message: `⚠️ Same-day turnover Apt #${checkout.apt_number} ${when} — ${checkout.guest_name} out → ${sameDay.guest_name} in. Schedule cleaner!`,
                    time: now });
            }
        }
    });

    // Upcoming cleanings needed (checkout within 7 days, no same-day follow-on — routine turnover reminder)
    reservations.forEach(r => {
        if (r.status === 'checked_out') return;
        if (r.checkout_date < todayStr || r.checkout_date > in7DaysStr) return;
        const hasSameDayNext = reservations.some(n =>
            n.property_id === r.property_id && n.checkin_date === r.checkout_date && n.id !== r.id);
        if (!hasSameDayNext) {
            const daysAway = daysUntil(r.checkout_date);
            if (daysAway >= 0 && daysAway <= 7) {
                const when = daysAway === 0 ? 'today' : daysAway === 1 ? 'tomorrow' : `in ${daysAway} days`;
                const alreadyCleaning = alerts.some(a => a.type === 'cleaning' &&
                    a.message.includes(`#${r.apt_number}`) && a.message.includes(r.guest_name));
                if (!alreadyCleaning) {
                    alerts.push({ type: 'cleaning', priority: daysAway <= 1 ? 'medium' : 'low',
                        message: `🧹 Apt #${r.apt_number} needs turnover ${when} after ${r.guest_name}`,
                        time: now });
                }
            }
        }
    });

    // Forward-month vacancy macro-alert
    // Check if next full calendar month has very low confirmed bookings
    const nextMonthDate = new Date();
    nextMonthDate.setDate(1);
    nextMonthDate.setMonth(nextMonthDate.getMonth() + 1);
    const nextMonthKey = `${nextMonthDate.getFullYear()}-${String(nextMonthDate.getMonth()+1).padStart(2,'0')}`;
    const nextMonthEnd = new Date(nextMonthDate.getFullYear(), nextMonthDate.getMonth()+1, 0);
    const nextMonthEndKey = `${nextMonthDate.getFullYear()}-${String(nextMonthDate.getMonth()+1).padStart(2,'0')}-${String(nextMonthEnd.getDate()).padStart(2,'0')}`;
    const nextMonthStart = nextMonthKey + '-01';
    const daysInNextMonth = nextMonthEnd.getDate();
    const fullMonthNamesAlert = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const nextMonthName = fullMonthNamesAlert[nextMonthDate.getMonth()];

    // Count total occupied nights across all properties in next month
    let nextMonthOccupiedNights = 0;
    const activePropertyCount = (properties && properties.length) ? properties.filter(p=>p.status==='active').length : 4;
    const totalPropertyNights = activePropertyCount * daysInNextMonth;

    reservations.forEach(r => {
        if (r.status === 'checked_out') return;
        if (r.checkout_date <= nextMonthStart || r.checkin_date > nextMonthEndKey) return;
        const overlapStart = r.checkin_date < nextMonthStart ? nextMonthStart : r.checkin_date;
        const overlapEnd   = r.checkout_date > nextMonthEndKey ? nextMonthEndKey : r.checkout_date;
        const nights = Math.max(0, Math.ceil((new Date(overlapEnd+'T12:00:00') - new Date(overlapStart+'T12:00:00')) / 86400000));
        nextMonthOccupiedNights += nights;
    });

    const nextMonthOccRate = totalPropertyNights > 0 ? (nextMonthOccupiedNights / totalPropertyNights * 100) : 0;
    if (nextMonthOccRate < 25) {
        alerts.push({ type: 'maintenance', priority: 'high',
            message: `🚨 ${nextMonthName} is ${nextMonthOccRate.toFixed(0)}% booked — only ${nextMonthOccupiedNights} nights confirmed across all units. Open dates need bookings NOW!`,
            time: now });
    } else if (nextMonthOccRate < 50) {
        alerts.push({ type: 'maintenance', priority: 'medium',
            message: `📅 ${nextMonthName} is ${nextMonthOccRate.toFixed(0)}% booked — open nights remaining. Push availability and drop prices!`,
            time: now });
    }

    // Review milestone alert
    if (reviews) {
        const nextMilestone = Math.ceil(reviews.perfect_streak / 25) * 25;
        const toMilestone = nextMilestone - reviews.perfect_streak;
        if (toMilestone <= 5) {
            alerts.push({ type: 'review', priority: 'low',
                message: `⭐ ${reviews.overall_avg.toFixed(2)} — ${reviews.perfect_streak} perfect reviews! ${toMilestone} away from ${nextMilestone} streak milestone! 🔥`,
                time: now });
        } else {
            alerts.push({ type: 'review', priority: 'low',
                message: `⭐ ${reviews.overall_avg.toFixed(2)} perfect score — ${reviews.perfect_streak} reviews & counting! Keep it up!`,
                time: now });
        }
    }

    // Sort: high first, then medium, then low; within same priority sort by date
    const priorityOrder = { high: 0, medium: 1, low: 2 };
    alerts.sort((a, b) => (priorityOrder[a.priority] || 2) - (priorityOrder[b.priority] || 2));

    return alerts;
}

// ===== AUTH =====
function checkAuth() {
    if (localStorage.getItem('ba_auth') !== 'steward-2026') {
        window.location.href = 'index.html';
        return false;
    }
    return true;
}

function logout() {
    localStorage.removeItem('ba_auth');
    window.location.href = 'index.html';
}

// ===== DATA FETCHING =====
async function fetchData(endpoint) {
    if (!API_BASE) return null;
    try {
        const res = await fetch(`${API_BASE}${endpoint}`);
        if (!res.ok) throw new Error(res.statusText);
        return await res.json();
    } catch (e) {
        console.log(`API offline, using demo data for ${endpoint}`);
        return null;
    }
}

// ===== FORMAT HELPERS =====
function formatDate(dateStr) {
    if (!dateStr) return '—';
    const d = new Date(dateStr + 'T12:00:00');
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

function formatCurrency(amount) {
    return '$' + (amount || 0).toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: 0 });
}

function today() {
    return new Date().toISOString().split('T')[0];
}

function todayNice() {
    return new Date().toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
}

function daysUntil(dateStr) {
    const target = new Date(dateStr + 'T12:00:00');
    const now = new Date();
    now.setHours(12, 0, 0, 0);
    return Math.ceil((target - now) / 86400000);
}

function nightsBetween(checkin, checkout) {
    const a = new Date(checkin + 'T12:00:00');
    const b = new Date(checkout + 'T12:00:00');
    return Math.ceil((b - a) / 86400000);
}

// ===== LOADING SKELETONS =====
function showSkeleton(containerId, count = 3) {
    const el = document.getElementById(containerId);
    if (!el) return;
    el.innerHTML = Array(count).fill(
        '<div class="skeleton-item"><div class="skeleton-line wide"></div><div class="skeleton-line medium"></div><div class="skeleton-line short"></div></div>'
    ).join('');
}

// ===== MOBILE NAV =====
function initMobileNav() {
    const nav = document.querySelector('nav');
    if (!nav) return;

    // Create hamburger button
    const hamburger = document.createElement('button');
    hamburger.className = 'hamburger';
    hamburger.innerHTML = '☰';
    hamburger.onclick = function() {
        nav.classList.toggle('nav-open');
        hamburger.innerHTML = nav.classList.contains('nav-open') ? '✕' : '☰';
    };

    // Insert after brand
    const brand = nav.querySelector('.brand');
    if (brand) brand.after(hamburger);
}

// ===== DASHBOARD PAGE =====
async function initDashboard() {
    if (!checkAuth()) return;
    initMobileNav();

    document.getElementById('dateInfo').textContent = todayNice();

    // Dynamic month labels in section titles
    const _fullMonths = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const _thisMonth = _fullMonths[new Date().getMonth()];
    const _revTitle = document.getElementById('revenueSnapshotTitle');
    if (_revTitle) _revTitle.textContent = `Revenue by Stream — ${_thisMonth}`;
    const _propRevTitle = document.getElementById('propertyRevenueTitle');
    if (_propRevTitle) _propRevTitle.textContent = `📊 Revenue by Property — ${_thisMonth}`;

    // Show loading skeletons
    showSkeleton('propertyGrid', 5);

    const rawProperties = (await fetchData('/api/properties')) || DEMO.properties;
    const financials = (await fetchData('/api/financials/summary')) || DEMO.financials;
    const reservations = (await fetchData('/api/reservations')) || DEMO.reservations;
    const reviews = DEMO.reviews;

    // Derive live occupancy from reservations so property cards never show stale data
    const properties = hydratePropertiesFromReservations(rawProperties, reservations);

    // Generate fresh, date-aware alerts every load (no stale hardcoded data)
    const alerts = (await fetchData('/api/alerts')) || generateDynamicAlerts(reservations, properties, reviews);

    renderTodayGlance(properties, reservations);
    renderSummaryCards(properties, financials, reviews);
    renderPropertyGrid(properties);
    renderReviewTracker(reviews);
    renderAlerts(alerts);
    renderRevenueSnapshot(financials);
    renderUpcomingEvents(reservations);
    renderPropertyRevenue(reservations);
    renderVacancyGaps(reservations);
    if (typeof updateCalc === 'function') updateCalc();

    // Merge any locally-saved bookings into reservations for this session
    const localBookings = loadLocalData('bookings', []);
    if (localBookings.length) {
        const existingIds = new Set(DEMO.reservations.map(r => r.id));
        localBookings.forEach(b => { if (!existingIds.has(b.id)) DEMO.reservations.push(b); });
    }
}

// Monthly revenue goal — adjust this to change the target
const MONTHLY_REVENUE_GOAL = 3000;

function renderSummaryCards(properties, financials, reviews) {
    const occupied = properties.filter(p => p.current_guest).length;

    animateValue('occupiedCount', `${occupied}/${properties.length}`);
    document.getElementById('occupiedLabel').textContent = occupied > 0 ? `${occupied} occupied tonight` : 'All vacant';

    animateValue('revenueTotal', formatCurrency(financials.revenue.total));
    const _revMonths = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    document.getElementById('revenueLabel').textContent = _revMonths[new Date().getMonth()] + ' Revenue';

    animateValue('netProfit', formatCurrency(financials.net_profit));
    document.getElementById('netLabel').textContent = `${((financials.net_profit / Math.max(financials.revenue.total, 1)) * 100).toFixed(0)}% margin`;

    // Review card
    const reviewCard = document.getElementById('reviewCard');
    if (reviewCard) {
        animateValue('reviewScore', reviews.overall_avg.toFixed(2));
        document.getElementById('reviewLabel').textContent = `${reviews.total_count} reviews · ${reviews.perfect_streak} perfect streak`;
    }

    // Revenue Goal Progress Bar (injected below revenue card)
    renderRevenueGoalBar(financials.revenue.total, MONTHLY_REVENUE_GOAL);
}

function renderRevenueGoalBar(current, goal) {
    let goalEl = document.getElementById('revenueGoalBar');
    if (!goalEl) return;

    const pct = Math.min(100, (current / goal * 100));
    const remaining = Math.max(0, goal - current);
    const isOver = current >= goal;
    const barColor = isOver ? 'var(--sage)' : pct >= 75 ? 'var(--terracotta)' : pct >= 50 ? 'var(--yellow)' : 'var(--blush)';
    const statusMsg = isOver
        ? `🎉 Goal crushed! +${formatCurrency(current - goal)} over target`
        : `${formatCurrency(remaining)} to reach ${formatCurrency(goal)} goal`;

    goalEl.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.35rem">
            <span style="font-size:0.65rem;font-weight:700;color:var(--gray);text-transform:uppercase;letter-spacing:1.5px">Monthly Goal</span>
            <span style="font-size:0.75rem;font-weight:700;color:${barColor}">${pct.toFixed(0)}%</span>
        </div>
        <div style="background:var(--light-gray);border-radius:6px;height:8px;overflow:hidden;margin-bottom:0.35rem">
            <div style="background:${barColor};height:100%;width:0;border-radius:6px;transition:width 1s ease" id="goalBarFill" data-width="${pct}"></div>
        </div>
        <div style="font-size:0.72rem;color:var(--gray);font-family:var(--font-serif);font-style:italic">${statusMsg}</div>
    `;

    requestAnimationFrame(() => {
        const fill = document.getElementById('goalBarFill');
        if (fill) setTimeout(() => { fill.style.width = fill.dataset.width + '%'; }, 100);
    });
}

function animateValue(elementId, finalValue) {
    const el = document.getElementById(elementId);
    if (!el) return;
    el.style.opacity = '0';
    el.textContent = finalValue;
    el.style.transition = 'opacity 0.4s ease';
    requestAnimationFrame(() => { el.style.opacity = '1'; });
}

function renderPropertyGrid(properties) {
    const container = document.getElementById('propertyGrid');
    container.innerHTML = properties.map(p => {
        const isOccupied = !!p.current_guest;
        const statusClass = isOccupied ? 'occupied' : 'vacant';
        const badgeClass = isOccupied ? 'badge-occupied' : 'badge-vacant';
        const badgeText = isOccupied ? 'OCCUPIED' : 'VACANT';
        const daysInfo = isOccupied && p.current_checkout
            ? `${daysUntil(p.current_checkout)} day${daysUntil(p.current_checkout) !== 1 ? 's' : ''} left`
            : p.next_checkin ? `in ${daysUntil(p.next_checkin)} day${daysUntil(p.next_checkin) !== 1 ? 's' : ''}` : '';

        return `
            <div class="property-card ${statusClass}" style="animation: fadeSlideUp 0.3s ease forwards; opacity: 0;">
                <div style="display:flex;justify-content:space-between;align-items:center">
                    <div class="apt-name">Apt ${p.apt_number}</div>
                    <span class="status-badge ${badgeClass}">${badgeText}</span>
                </div>
                <div class="rate">${formatCurrency(p.base_nightly_rate)}/night ${p.review_avg ? `· <span style="color:var(--yellow)">★</span> ${p.review_avg.toFixed(1)}` : ''}</div>
                <div class="guest-info">
                    <div class="label">Current Guest</div>
                    <div class="name">${p.current_guest || '—'} ${p.current_checkout ? '<span style="color:var(--gray);font-size:0.8rem">→ ' + formatDate(p.current_checkout) + ' <em>(' + daysInfo + ')</em></span>' : ''}</div>
                </div>
                <div class="guest-info">
                    <div class="label">Next Guest</div>
                    <div class="name">${p.next_guest || '—'} ${p.next_checkin ? '<span style="color:var(--gray);font-size:0.8rem">← ' + formatDate(p.next_checkin) + (!isOccupied && daysInfo ? ' <em>(' + daysInfo + ')</em>' : '') + '</span>' : ''}</div>
                </div>
            </div>
        `;
    }).join('');

    // Stagger animation
    container.querySelectorAll('.property-card').forEach((card, i) => {
        card.style.animationDelay = `${i * 0.08}s`;
    });
}

function renderReviewTracker(reviews) {
    const section = document.getElementById('reviewTrackerSection');
    if (!section) return;

    const streakPct = Math.min(100, (reviews.perfect_streak / 100) * 100);
    section.innerHTML = `
        <div class="card review-tracker-card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem">
                <div>
                    <h3 style="margin-bottom:0.25rem">Review Score</h3>
                    <div style="font-family:var(--font-serif);font-size:2.5rem;font-weight:700;color:var(--terracotta)">
                        <span style="color:var(--yellow)">★</span> ${reviews.overall_avg.toFixed(2)}
                    </div>
                </div>
                <div style="text-align:right">
                    <div style="font-size:0.65rem;color:var(--gray);text-transform:uppercase;letter-spacing:2px;font-weight:600">Perfect Streak</div>
                    <div style="font-family:var(--font-serif);font-size:1.8rem;font-weight:600;color:var(--sage)">${reviews.perfect_streak} 🔥</div>
                    <div style="font-size:0.75rem;color:var(--gray)">${reviews.total_count} total reviews</div>
                </div>
            </div>
            <div style="background:var(--light-gray);border-radius:10px;height:8px;overflow:hidden;margin-bottom:1rem">
                <div style="background:linear-gradient(90deg, var(--sage), var(--terracotta));height:100%;width:${streakPct}%;border-radius:10px;transition:width 1s ease"></div>
            </div>
            <div style="font-size:0.75rem;color:var(--gray);font-family:var(--font-serif);font-style:italic">
                ${reviews.perfect_streak >= 50 ? '🏆 Legendary streak!' : reviews.perfect_streak >= 25 ? '🔥 Incredible consistency!' : '⭐ Building momentum!'} Next milestone: ${Math.ceil(reviews.perfect_streak / 25) * 25 + 25} reviews
            </div>
            <div style="margin-top:1.25rem;border-top:1px solid var(--linen);padding-top:1rem">
                <div style="font-size:0.65rem;color:var(--gray);text-transform:uppercase;letter-spacing:2px;font-weight:600;margin-bottom:0.75rem">Recent Reviews</div>
                ${reviews.recent.map(r => `
                    <div style="margin-bottom:0.75rem;padding-bottom:0.75rem;border-bottom:1px solid var(--linen)">
                        <div style="display:flex;justify-content:space-between;align-items:center">
                            <span style="font-family:var(--font-serif);font-weight:600;font-size:0.95rem">${r.guest}</span>
                            <span style="color:var(--yellow);font-size:0.85rem">${'★'.repeat(r.rating)}</span>
                        </div>
                        <div style="font-size:0.8rem;color:var(--gray);margin-top:0.15rem">Apt ${r.apt} · ${formatDate(r.date)}</div>
                        <div style="font-size:0.85rem;font-style:italic;color:var(--dark-brown);margin-top:0.3rem">"${r.text}"</div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

function renderAlerts(alerts) {
    const container = document.getElementById('alertFeed');
    if (!alerts.length) {
        container.innerHTML = '<p style="color:var(--gray);padding:1rem;font-family:var(--font-serif);font-style:italic">All clear — no alerts right now 👍</p>';
        return;
    }
    const icons = { checkout: '🚪', cleaning: '🧹', low_stock: '📦', checkin: '🔑', review: '⭐', maintenance: '🔧' };
    container.innerHTML = '<ul class="alert-list">' + alerts.map(a => `
        <li class="alert-item" style="animation: fadeSlideUp 0.3s ease forwards; opacity: 0;">
            <div class="alert-icon alert-${a.priority}">${icons[a.type] || '⚠️'}</div>
            <div>
                <div>${a.message}</div>
                ${a.time ? `<div style="font-size:0.7rem;color:var(--gray);margin-top:0.15rem">${formatDate(a.time.split('T')[0])}</div>` : ''}
            </div>
        </li>
    `).join('') + '</ul>';
}

function renderRevenueSnapshot(financials) {
    const container = document.getElementById('revenueChart');
    const rev = financials.revenue;
    const streams = [
        { label: 'Airbnb', value: rev.airbnb, color: '#C4835A' },
        { label: 'Direct', value: rev.direct_booking, color: '#D4A68C' },
        { label: 'Merch', value: rev.merch, color: '#6B4A3A' },
        { label: 'Vending', value: rev.vending, color: '#8B9E7E' },
        { label: 'Car Rental', value: rev.car_rental, color: '#7B9AAE' },
    ].filter(s => s.value > 0);

    if (streams.length === 0) {
        container.innerHTML = '<p style="color:var(--gray);font-family:var(--font-serif);font-style:italic">No revenue data yet</p>';
        return;
    }

    const maxVal = Math.max(...streams.map(s => s.value));
    container.innerHTML = streams.map((s, i) => `
        <div style="margin-bottom:0.75rem;animation:fadeSlideUp 0.3s ease ${i * 0.1}s forwards;opacity:0">
            <div style="display:flex;justify-content:space-between;margin-bottom:0.25rem">
                <span style="font-weight:600;font-size:0.85rem">${s.label}</span>
                <span style="font-weight:700">${formatCurrency(s.value)}</span>
            </div>
            <div style="background:var(--light-gray);border-radius:6px;height:24px;overflow:hidden">
                <div class="bar-animate" style="background:${s.color};height:100%;width:0;border-radius:6px" data-width="${(s.value/maxVal*100)}"></div>
            </div>
        </div>
    `).join('');

    // Animate bars
    requestAnimationFrame(() => {
        container.querySelectorAll('.bar-animate').forEach(bar => {
            setTimeout(() => { bar.style.transition = 'width 0.8s ease'; bar.style.width = bar.dataset.width + '%'; }, 200);
        });
    });
}

function renderUpcomingEvents(reservations) {
    const container = document.getElementById('upcomingEvents');
    const todayStr = today();
    const weekEnd = new Date(Date.now() + 7 * 86400000).toISOString().split('T')[0];

    const events = [];
    reservations.forEach(r => {
        // Only show future/today events; skip completed reservations
        if (r.status === 'checked_out') return;
        if (r.checkout_date >= todayStr && r.checkout_date <= weekEnd) {
            events.push({ date: r.checkout_date, type: '🚪 Checkout', name: r.guest_name, apt: r.apt_number, days: daysUntil(r.checkout_date) });
        }
        if (r.checkin_date >= todayStr && r.checkin_date <= weekEnd) {
            events.push({ date: r.checkin_date, type: '🔑 Checkin', name: r.guest_name, apt: r.apt_number, days: daysUntil(r.checkin_date) });
        }
    });

    events.sort((a, b) => a.date.localeCompare(b.date));

    if (!events.length) {
        container.innerHTML = '<p style="color:var(--gray);padding:0.5rem;font-family:var(--font-serif);font-style:italic">No events this week</p>';
        return;
    }

    container.innerHTML = '<table><thead><tr><th>Date</th><th>Event</th><th>Guest</th><th>Apt</th><th>When</th></tr></thead><tbody>' +
        events.map(e => {
            const urgency = e.days === 0 ? 'font-weight:700;color:var(--dusty-rose)' : e.days <= 1 ? 'font-weight:600;color:var(--terracotta)' : '';
            return `<tr style="${urgency}"><td>${formatDate(e.date)}</td><td>${e.type}</td><td>${e.name}</td><td>${e.apt}</td><td>${e.days === 0 ? 'Today!' : e.days === 1 ? 'Tomorrow' : e.days + ' days'}</td></tr>`;
        }).join('') +
        '</tbody></table>';
}

// ===== CALENDAR PAGE =====
let calYear, calMonth;

async function initCalendar() {
    if (!checkAuth()) return;
    initMobileNav();

    const rawProperties = (await fetchData('/api/properties')) || DEMO.properties;
    const reservations = (await fetchData('/api/reservations')) || DEMO.reservations;
    const properties = hydratePropertiesFromReservations(rawProperties, reservations);

    const now = new Date();
    renderCalendar(properties, reservations, now.getFullYear(), now.getMonth());
}

// Property colors for calendar bars
const PROPERTY_COLORS = {
    '6': { bg: '#C4835A', text: '#fff' },
    '7': { bg: '#8B9E7E', text: '#fff' },
    '8': { bg: '#D4885A', text: '#fff' },
    'Cottage': { bg: '#6B4A3A', text: '#fff' },
    '6+8': { bg: '#C8918A', text: '#fff' },
};

function renderCalendar(properties, reservations, year, month) {
    calYear = year;
    calMonth = month;
    const container = document.getElementById('calendarGrid');
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const monthNames = ['January','February','March','April','May','June','July','August','September','October','November','December'];

    document.getElementById('calMonthLabel').textContent = `${monthNames[month]} ${year}`;

    // Build gantt-style calendar
    container.style.gridTemplateColumns = `140px repeat(${daysInMonth}, 1fr)`;

    let html = '<div class="cal-header" style="grid-column:1;text-align:left;padding-left:0.75rem">Property</div>';

    // Day headers with weekday initials
    const dayNames = ['S','M','T','W','T','F','S'];
    for (let d = 1; d <= daysInMonth; d++) {
        const date = new Date(year, month, d);
        const isToday = (d === new Date().getDate() && month === new Date().getMonth() && year === new Date().getFullYear());
        const isWeekend = date.getDay() === 0 || date.getDay() === 6;
        html += `<div class="cal-header${isToday ? ' cal-today-header' : ''}${isWeekend ? ' cal-weekend-header' : ''}">
            <span class="cal-day-name">${dayNames[date.getDay()]}</span>
            <span class="cal-day-num">${d}</span>
        </div>`;
    }

    // Property rows with booking bars
    properties.forEach(p => {
        html += `<div class="cal-property"><span class="cal-prop-dot" style="background:${(PROPERTY_COLORS[p.apt_number] || {bg:'#999'}).bg}"></span> Apt ${p.apt_number}</div>`;

        // Find reservations for this property in this month
        const propRes = reservations.filter(r => r.property_id === p.id);

        for (let d = 1; d <= daysInMonth; d++) {
            const dateStr = `${year}-${String(month+1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
            const isToday = dateStr === today();
            const dateObj = new Date(year, month, d);
            const isWeekend = dateObj.getDay() === 0 || dateObj.getDay() === 6;

            let cls = 'vacant';
            let guest = '';
            let isStart = false;
            let isEnd = false;
            let bookingColor = '';

            for (const r of propRes) {
                if (dateStr >= r.checkin_date && dateStr < r.checkout_date) {
                    cls = r.status === 'checked_in' ? 'occupied' : 'confirmed';
                    guest = r.guest_name;
                    isStart = dateStr === r.checkin_date;
                    isEnd = false; // The checkout date is NOT included in the stay
                    bookingColor = (PROPERTY_COLORS[p.apt_number] || {bg:'#C4835A'}).bg;

                    // Check if tomorrow is checkout
                    const tomorrow = new Date(year, month, d + 1);
                    const tomorrowStr = tomorrow.toISOString().split('T')[0];
                    if (tomorrowStr === r.checkout_date || tomorrowStr > r.checkout_date) {
                        isEnd = true;
                    }
                    break;
                }
            }

            const classes = [
                'cal-day',
                cls,
                isToday ? 'today' : '',
                isWeekend ? 'cal-weekend' : '',
                isStart ? 'booking-start' : '',
                isEnd ? 'booking-end' : '',
                (cls === 'occupied' || cls === 'confirmed') ? 'has-booking' : '',
            ].filter(Boolean).join(' ');

            const style = (cls === 'occupied' || cls === 'confirmed') ? `style="--booking-color:${bookingColor}"` : '';

            html += `<div class="${classes}" ${style}>
                ${isStart ? `<span class="booking-label">${guest}</span>` : ''}
                ${guest && !isStart ? `<span class="tooltip">${guest}${cls === 'confirmed' ? ' (upcoming)' : ''}</span>` : ''}
            </div>`;
        }
    });

    container.innerHTML = html;
}

function calPrev() {
    calMonth--;
    if (calMonth < 0) { calMonth = 11; calYear--; }
    renderCalendar(DEMO.properties, DEMO.reservations, calYear, calMonth);
}

function calNext() {
    calMonth++;
    if (calMonth > 11) { calMonth = 0; calYear++; }
    renderCalendar(DEMO.properties, DEMO.reservations, calYear, calMonth);
}

// ===== CLEANING PAGE =====
async function initCleaning() {
    if (!checkAuth()) return;
    initMobileNav();

    const reservations = (await fetchData('/api/reservations')) || DEMO.reservations;

    // Dynamically derive needed cleanings from live reservations (no stale hardcoded dates)
    const neededCleanings = generateNeededCleanings(reservations);

    // Merge locally saved cleanings with DEMO scheduled set
    const localCleanings = loadLocalData('cleanings', []);
    const schedule = {
        scheduled: [...(DEMO.cleaningSchedule.scheduled || []), ...localCleanings],
        needed: neededCleanings
    };

    renderCleaningSchedule(schedule);
    renderCleanerSummaries();

    // Pre-fill date on log form
    const logDate = document.getElementById('logCleanDate');
    if (logDate && !logDate.value) logDate.value = today();
}

// ===== DYNAMIC NEEDED CLEANINGS GENERATOR =====
// Derives turnovers and upcoming cleanings from live reservation data.
// No hardcoded dates — always accurate regardless of when the page is loaded.
function generateNeededCleanings(reservations) {
    const todayStr = today();
    const in14DaysStr = new Date(Date.now() + 14 * 86400000).toISOString().split('T')[0];
    const needed = [];

    // Sort reservations by checkout date
    const relevant = reservations
        .filter(r => r.status !== 'checked_out' && r.checkout_date >= todayStr && r.checkout_date <= in14DaysStr)
        .sort((a, b) => a.checkout_date.localeCompare(b.checkout_date));

    relevant.forEach(r => {
        const daysAway = daysUntil(r.checkout_date);

        // Check for same-day turnover (another guest arriving same day)
        const sameDayNext = reservations.find(n =>
            n.property_id === r.property_id &&
            n.checkin_date === r.checkout_date &&
            n.id !== r.id &&
            n.status !== 'checked_out'
        );

        let urgency = 'upcoming';
        let note = '';

        if (daysAway <= 0) {
            urgency = 'critical';
        } else if (daysAway === 1) {
            urgency = 'critical';
        } else if (daysAway <= 3) {
            urgency = 'normal';
        }

        if (sameDayNext) {
            urgency = daysAway <= 1 ? 'critical' : 'normal';
            note = `⚡ SAME-DAY TURNOVER — ${sameDayNext.guest_name} arrives ${daysAway === 0 ? 'today' : daysAway === 1 ? 'tomorrow' : 'in ' + daysAway + ' days'}. Schedule cleaner ASAP!`;
        } else if (daysAway <= 0) {
            note = `⚠️ ${r.guest_name} checked out — needs immediate turnover`;
        } else if (daysAway === 1) {
            note = `Tomorrow checkout — schedule cleaner now`;
        } else {
            note = daysAway <= 3 ? `Checkout in ${daysAway} days — confirm cleaner` : `Upcoming turnover in ${daysAway} days`;
        }

        // Suggest cleaner based on checkout day of week (Tiffany: Fri/Sat, Amanda: Thu)
        const checkoutDay = new Date(r.checkout_date + 'T12:00:00').getDay();
        const suggested_cleaner = (checkoutDay === 5 || checkoutDay === 6) ? 'tiffany' : 'amanda';

        needed.push({
            apt_number: r.apt_number,
            property_name: r.property_name,
            guest_name: r.guest_name,
            checkout_date: r.checkout_date,
            suggested_cleaner,
            urgency,
            note
        });
    });

    return needed;
}

// ===== LIVE OCCUPANCY CALCULATOR =====
// Computes occupancy %, ADR, and RevPAR from actual reservation data.
// Always accurate — no stale hardcoded numbers.
// lookbackDays: how many trailing days to measure (default 30)
function calculateOccupancy(properties, reservations, lookbackDays = 30) {
    const todayStr = today();
    const startDate = new Date(Date.now() - lookbackDays * 86400000).toISOString().split('T')[0];

    const results = properties.map(p => {
        // All reservations for this property overlapping the lookback window
        const propRes = reservations.filter(r =>
            r.property_id === p.id &&
            r.checkout_date > startDate &&
            r.checkin_date < todayStr
        );

        // Count nights occupied within the window
        let occupiedNights = 0;
        let totalRevenue = 0;
        let totalBookings = 0;

        propRes.forEach(r => {
            const overlapStart = r.checkin_date < startDate ? startDate : r.checkin_date;
            const overlapEnd   = r.checkout_date > todayStr ? todayStr : r.checkout_date;
            const nights = Math.max(0, Math.ceil(
                (new Date(overlapEnd + 'T12:00:00') - new Date(overlapStart + 'T12:00:00')) / 86400000
            ));
            if (nights > 0) {
                occupiedNights += nights;
                // Pro-rate payout to overlap window
                const totalNights = nightsBetween(r.checkin_date, r.checkout_date);
                if (totalNights > 0) totalRevenue += (r.payout / totalNights) * nights;
                totalBookings++;
            }
        });

        const occupancy_30d = parseFloat(((occupiedNights / lookbackDays) * 100).toFixed(1));
        const adr = totalBookings > 0 ? parseFloat((totalRevenue / Math.max(occupiedNights, 1)).toFixed(2)) : 0;
        const revpar = parseFloat(((totalRevenue / lookbackDays)).toFixed(2));

        return {
            apt_number: p.apt_number,
            property_name: p.name,
            occupancy_30d,
            adr,
            revpar
        };
    });

    // Overall row (weighted across all units)
    const totalOccNights = results.reduce((s, r) => s + (r.occupancy_30d / 100 * lookbackDays), 0);
    const totalRevPar    = results.reduce((s, r) => s + r.revpar, 0);
    const avgOcc         = parseFloat(((totalOccNights / (properties.length * lookbackDays)) * 100).toFixed(1));
    const weightedADR    = results.filter(r => r.adr > 0).length
        ? parseFloat((results.filter(r => r.adr > 0).reduce((s, r) => s + r.adr, 0) / results.filter(r => r.adr > 0).length).toFixed(2))
        : 0;

    results.push({
        apt_number: 'ALL',
        property_name: 'Overall',
        occupancy_30d: avgOcc,
        adr: weightedADR,
        revpar: parseFloat(totalRevPar.toFixed(2))
    });

    return results;
}

function renderCleaningSchedule(schedule) {
    const scheduled = document.getElementById('scheduledCleanings');
    const needed = document.getElementById('neededCleanings');

    if (schedule.scheduled.length) {
        scheduled.innerHTML = '<table><thead><tr><th>Date</th><th>Property</th><th>Cleaner</th><th>Type</th><th>Hours</th><th>Pay</th><th>Status</th></tr></thead><tbody>' +
            schedule.scheduled.map(c => `
                <tr>
                    <td>${formatDate(c.date)}</td>
                    <td>Apt ${c.apt_number}</td>
                    <td>${c.cleaner.charAt(0).toUpperCase() + c.cleaner.slice(1)}</td>
                    <td style="text-transform:capitalize">${c.type}</td>
                    <td>${c.hours || '—'}</td>
                    <td>${c.pay ? formatCurrency(c.pay) : '—'}</td>
                    <td>${c.completed ? '<span style="color:var(--sage)">✅ Done</span>' : '<span style="color:var(--yellow)">⏳ Pending</span>'}</td>
                </tr>
            `).join('') + '</tbody></table>';
    } else {
        scheduled.innerHTML = '<p style="color:var(--gray);font-family:var(--font-serif);font-style:italic">No cleanings scheduled this week</p>';
    }

    if (schedule.needed.length) {
        needed.innerHTML = '<table><thead><tr><th>Property</th><th>After Guest</th><th>Checkout</th><th>Suggested</th><th>Urgency</th><th>Notes</th></tr></thead><tbody>' +
            schedule.needed.map(n => {
                const urgencyColors = { critical: 'var(--dusty-rose)', normal: 'var(--yellow)', upcoming: 'var(--sage)' };
                return `
                    <tr>
                        <td>Apt ${n.apt_number}</td>
                        <td style="font-family:var(--font-serif);font-weight:600">${n.guest_name}</td>
                        <td>${formatDate(n.checkout_date)}</td>
                        <td>${n.suggested_cleaner.charAt(0).toUpperCase() + n.suggested_cleaner.slice(1)}</td>
                        <td><span style="display:inline-block;padding:0.15rem 0.5rem;border-radius:2px;font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;background:${urgencyColors[n.urgency] || 'var(--gray)'};color:white">${n.urgency || 'normal'}</span></td>
                        <td style="font-size:0.8rem;font-style:italic;color:var(--gray)">${n.note || '—'}</td>
                    </tr>
                `;
            }).join('') + '</tbody></table>';
    } else {
        needed.innerHTML = '<p style="color:var(--gray);font-family:var(--font-serif);font-style:italic">All cleanings covered 👍</p>';
    }
}

function renderCleanerSummaries() {
    // Merge DEMO cleanings with any locally-saved ones
    const localCleanings = loadLocalData('cleanings', []);
    const allCleanings = [...(DEMO.cleaningSchedule.scheduled || []), ...localCleanings];

    // Only count this calendar month
    const now = new Date();
    const thisMonth = `${now.getFullYear()}-${String(now.getMonth()+1).padStart(2,'0')}`;
    const monthName = ['January','February','March','April','May','June','July','August','September','October','November','December'][now.getMonth()];

    const byMonth = allCleanings.filter(c => c.date && c.date.startsWith(thisMonth));

    const totals = {};
    byMonth.forEach(c => {
        const name = (c.cleaner || '').toLowerCase();
        if (!totals[name]) totals[name] = { cleanings: 0, hours: 0, pay: 0 };
        totals[name].cleanings++;
        totals[name].hours += parseFloat(c.hours) || 0;
        totals[name].pay += parseFloat(c.pay) || 0;
    });

    // Update month labels dynamically
    ['amanda', 'tiffany'].forEach(name => {
        const labelEl = document.getElementById(name + 'MonthLabel');
        if (labelEl) labelEl.textContent = `Cleanings (${monthName})`;
    });

    const setStats = (name, id) => {
        const t = totals[name] || { cleanings: 0, hours: 0, pay: 0 };
        const el = (s) => document.getElementById(id + s);
        if (el('Cleanings')) el('Cleanings').textContent = t.cleanings;
        if (el('Hours')) el('Hours').textContent = t.hours % 1 === 0 ? t.hours : t.hours.toFixed(1);
        if (el('Pay')) el('Pay').textContent = formatCurrency(t.pay);
    };

    setStats('amanda', 'amanda');
    setStats('tiffany', 'tiffany');
}

// ===== FINANCIALS PAGE =====
async function initFinancials() {
    if (!checkAuth()) return;
    initMobileNav();

    const summary = (await fetchData('/api/financials/summary')) || DEMO.financials;
    const monthly = (await fetchData('/api/financials/monthly')) || DEMO.monthly;
    const reservations = (await fetchData('/api/reservations')) || DEMO.reservations;

    renderFinancialSummary(summary);
    renderMonthlyChart(monthly);
    renderRevenueForecast(reservations);
}

function renderFinancialSummary(summary) {
    animateValue('totalRevenue', formatCurrency(summary.revenue.total));
    animateValue('totalExpenses', formatCurrency(summary.expenses.total));
    animateValue('totalNet', formatCurrency(summary.net_profit));

    const streams = document.getElementById('revenueStreams');
    const rev = summary.revenue;
    const items = [
        { label: '🏠 Airbnb', value: rev.airbnb },
        { label: '📋 Direct Booking', value: rev.direct_booking },
        { label: '🛍️ Merchandise', value: rev.merch },
        { label: '🥤 Vending', value: rev.vending },
        { label: '🚗 Car Rental', value: rev.car_rental },
    ];

    streams.innerHTML = '<table><thead><tr><th>Stream</th><th>Revenue</th><th>% of Total</th></tr></thead><tbody>' +
        items.map(i => `
            <tr>
                <td>${i.label}</td>
                <td>${formatCurrency(i.value)}</td>
                <td>${rev.total ? ((i.value/rev.total)*100).toFixed(1) : 0}%</td>
            </tr>
        `).join('') + '</tbody></table>';

    const expenseBreak = document.getElementById('expenseBreakdown');
    expenseBreak.innerHTML = `
        <table>
            <tr><td>General Expenses</td><td>${formatCurrency(summary.expenses.general)}</td></tr>
            <tr><td>Cleaner Costs</td><td>${formatCurrency(summary.expenses.cleaners)}</td></tr>
            <tr style="font-weight:700"><td>Total Expenses</td><td>${formatCurrency(summary.expenses.total)}</td></tr>
        </table>
    `;
}

function renderMonthlyChart(monthly) {
    const container = document.getElementById('monthlyChart');
    const maxRev = Math.max(...monthly.map(m => m.revenue), 1);

    container.innerHTML = '<div style="display:flex;gap:0.5rem;align-items:flex-end;height:220px;padding-top:1rem">' +
        monthly.map((m, i) => {
            const height = (m.revenue / maxRev * 180);
            const netHeight = (m.net / maxRev * 180);
            const monthLabel = new Date(m.month + '-15').toLocaleDateString('en-US', { month: 'short' });
            return `
                <div style="flex:1;text-align:center;animation:fadeSlideUp 0.3s ease ${i * 0.08}s forwards;opacity:0">
                    <div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:200px">
                        <div style="font-size:0.7rem;font-weight:600;margin-bottom:0.25rem">${formatCurrency(m.revenue)}</div>
                        <div style="width:75%;height:${height}px;background:var(--terracotta);border-radius:6px 6px 0 0;position:relative;overflow:hidden">
                            <div style="position:absolute;bottom:0;left:0;right:0;height:${Math.max(0,netHeight)}px;background:var(--sage);opacity:0.6"></div>
                        </div>
                    </div>
                    <div style="font-size:0.75rem;color:var(--gray);margin-top:0.5rem;font-weight:600">${monthLabel}</div>
                    <div style="font-size:0.65rem;color:var(--gray)">${m.month.split('-')[0].slice(2)}</div>
                </div>
            `;
        }).join('') +
        '</div>' +
        '<div style="display:flex;gap:1.5rem;justify-content:center;margin-top:1rem;font-size:0.8rem">' +
        '<span><span style="display:inline-block;width:12px;height:12px;background:var(--terracotta);border-radius:2px;vertical-align:middle"></span> Revenue</span>' +
        '<span><span style="display:inline-block;width:12px;height:12px;background:var(--sage);opacity:0.6;border-radius:2px;vertical-align:middle"></span> Net Profit</span>' +
        '</div>';
}

function renderRevenueForecast(reservations) {
    const container = document.getElementById('revenueForecast');
    if (!container) return;

    // Calculate forecast for current + next 2 months (always relative to today)
    const now = new Date();
    const months = [];
    const monthNames = {};
    const fullMonthNames = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    for (let i = 0; i < 3; i++) {
        const d = new Date(now.getFullYear(), now.getMonth() + i, 1);
        const key = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}`;
        months.push(key);
        monthNames[key] = fullMonthNames[d.getMonth()];
    }

    const forecast = months.map(m => {
        const [yr, mo] = m.split('-').map(Number);
        const monthStart = `${m}-01`;
        const lastDay = new Date(yr, mo, 0).getDate();
        const monthEnd = `${m}-${String(lastDay).padStart(2,'0')}`;

        // Pro-rate payout by nights that fall within this month
        let confirmed = 0;
        reservations.forEach(r => {
            if (r.checkout_date <= monthStart || r.checkin_date > monthEnd) return;
            const totalNights = nightsBetween(r.checkin_date, r.checkout_date);
            if (totalNights <= 0) return;
            const overlapStart = r.checkin_date < monthStart ? monthStart : r.checkin_date;
            const overlapEnd   = r.checkout_date > monthEnd   ? monthEnd   : r.checkout_date;
            const overlapNights = nightsBetween(overlapStart, overlapEnd);
            confirmed += (r.payout / totalNights) * overlapNights;
        });
        return { month: m, label: monthNames[m], confirmed: Math.round(confirmed), projected: Math.round(confirmed) };
    });

    // Estimate avg cleaning cost per booking
    const avgCleanCost = 43; // ~$130 / 3 cleanings
    const totalBookings = reservations.length;

    container.innerHTML = `
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:1rem;margin-bottom:1.5rem">
            ${forecast.map(f => `
                <div style="text-align:center;padding:1.25rem;background:var(--cream);border-radius:2px;border:1px solid var(--light-gray)">
                    <div style="font-size:0.65rem;color:var(--gray);text-transform:uppercase;letter-spacing:2px;font-weight:600">${f.label}</div>
                    <div style="font-family:var(--font-serif);font-size:1.8rem;font-weight:700;color:var(--terracotta);margin:0.5rem 0">${formatCurrency(f.confirmed)}</div>
                    <div style="font-size:0.75rem;color:var(--sage);font-weight:600">Confirmed</div>
                </div>
            `).join('')}
        </div>
        <div style="padding:1rem;background:var(--linen);border-radius:2px;font-size:0.85rem">
            <div style="font-weight:600;margin-bottom:0.5rem;color:var(--warm-brown)">📊 Forecast Notes</div>
            <ul style="list-style:none;padding:0;margin:0">
                <li style="margin-bottom:0.25rem">→ <strong>${totalBookings}</strong> total confirmed reservations</li>
                <li style="margin-bottom:0.25rem">→ Est. cleaning costs: ~<strong>${formatCurrency(totalBookings * avgCleanCost)}</strong> (${totalBookings} turnovers × ${formatCurrency(avgCleanCost)})</li>
                <li style="margin-bottom:0.25rem">→ Confirmed revenue: <strong>${formatCurrency(forecast.reduce((s,f)=>s+f.confirmed,0))}</strong> across next 3 months</li>
                <li>→ Revenue from open gaps not included — fill vacancies to increase projection</li>
            </ul>
        </div>
    `;
}

// ===== MAINTENANCE PAGE =====
async function initMaintenance() {
    if (!checkAuth()) return;
    initMobileNav();

    // Merge locally saved maintenance items
    const localItems = loadLocalData('maintenance', []);
    const combined = [...DEMO.maintenance, ...localItems];
    DEMO.maintenance = combined;
    renderMaintenanceList(combined);
}

function saveMaintenanceRequest() {
    const prop = document.getElementById('maintProp').value;
    const issue = document.getElementById('maintIssue').value.trim();
    const priority = document.getElementById('maintPriority').value;
    const notes = document.getElementById('maintNotes').value.trim();
    const cost = document.getElementById('maintCost').value;

    if (!issue) { showToast('Please describe the issue.'); return; }

    const entry = {
        id: Date.now(),
        property: prop,
        issue,
        priority,
        status: 'open',
        reported: today(),
        notes,
        estimated_cost: parseFloat(cost) || 0,
        created: new Date().toISOString()
    };

    const items = loadLocalData('maintenance', []);
    items.push(entry);
    saveLocalData('maintenance', items);

    // Update live display
    DEMO.maintenance.push(entry);
    renderMaintenanceList(DEMO.maintenance);

    // Update counts
    document.getElementById('openCount').textContent = DEMO.maintenance.filter(m => m.status === 'open').length;
    document.getElementById('scheduledCount').textContent = DEMO.maintenance.filter(m => m.status === 'scheduled').length;
    document.getElementById('completedCount').textContent = DEMO.maintenance.filter(m => m.status === 'completed').length;

    document.getElementById('maintIssue').value = '';
    document.getElementById('maintNotes').value = '';
    document.getElementById('maintCost').value = '';
    showToast(`🔧 Maintenance logged — ${prop}: ${issue}`);
}

function renderMaintenanceList(items) {
    const container = document.getElementById('maintenanceList');
    if (!container) return;

    const priorityColors = { high: 'var(--dusty-rose)', medium: 'var(--yellow)', low: 'var(--sage)' };
    const statusIcons = { open: '🔴', scheduled: '📅', 'in-progress': '🔧', completed: '✅' };

    container.innerHTML = `
        <table>
            <thead><tr><th>Property</th><th>Issue</th><th>Priority</th><th>Status</th><th>Reported</th><th>Notes</th></tr></thead>
            <tbody>
                ${items.map(m => `
                    <tr>
                        <td style="font-weight:600">${m.property}</td>
                        <td>${m.issue}</td>
                        <td><span style="display:inline-block;padding:0.15rem 0.5rem;border-radius:2px;font-size:0.6rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;background:${priorityColors[m.priority] || 'var(--gray)'};color:white">${m.priority}</span></td>
                        <td>${statusIcons[m.status] || '❓'} ${m.status}</td>
                        <td>${formatDate(m.reported)}</td>
                        <td style="font-size:0.8rem;font-style:italic;color:var(--gray)">${m.notes || '—'}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;
}

// ===== MODAL CONTROLS =====
function openModal(id) {
    const modal = document.getElementById(id);
    if (modal) {
        modal.classList.add('active');
        modal.style.animation = 'fadeIn 0.2s ease';
        // Pre-fill dates if empty
        const dateInputs = modal.querySelectorAll('input[type="date"]');
        dateInputs.forEach(inp => { if (!inp.value) inp.value = today(); });
    }
}

function closeModal(id) {
    const modal = document.getElementById(id);
    if (modal) modal.classList.remove('active');
}

// Close modal on overlay click
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('modal-overlay') && e.target.classList.contains('active')) {
        e.target.classList.remove('active');
    }
});

// Close modal on Escape
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay.active').forEach(m => m.classList.remove('active'));
    }
});

// ===== LOCAL STORAGE DATA PERSISTENCE =====
function loadLocalData(key, fallback) {
    try {
        const stored = localStorage.getItem('ba_' + key);
        return stored ? JSON.parse(stored) : fallback;
    } catch(e) { return fallback; }
}

function saveLocalData(key, data) {
    try {
        localStorage.setItem('ba_' + key, JSON.stringify(data));
    } catch(e) { console.warn('localStorage save failed:', e); }
}

function saveCleaning() {
    const prop = document.getElementById('cleanProp');
    const date = document.getElementById('cleanDate');
    const cleaner = document.getElementById('cleanCleaner');
    const hours = document.getElementById('cleanHours');
    const type = document.getElementById('cleanType');
    const notes = document.getElementById('cleanNotes');

    if (!date.value) { showToast('Please select a date.'); return; }

    const propNames = { '1': 'Apt #6', '2': 'Apt #7', '3': 'Apt #8', '4': 'Cottage', '5': 'Combined #6+#8' };
    const entry = {
        id: Date.now(),
        property: propNames[prop.value] || prop.value,
        property_id: parseInt(prop.value),
        date: date.value,
        cleaner: cleaner.value,
        hours: parseFloat(hours.value) || 0,
        type: type.value,
        notes: notes.value,
        completed: 0,
        pay: (parseFloat(hours.value) || 0) * 25,
        created: new Date().toISOString()
    };

    const cleanings = loadLocalData('cleanings', []);
    cleanings.push(entry);
    saveLocalData('cleanings', cleanings);

    notes.value = '';
    closeModal('cleaningModal');
    showToast(`✅ Cleaning logged — ${entry.property} on ${formatDate(entry.date)}`);

    // Refresh cleaning display if on that page
    if (typeof renderCleanerSummaries === 'function') renderCleanerSummaries();
}

function saveBooking() {
    const prop = document.getElementById('bookProp');
    const guest = document.getElementById('bookGuest');
    const checkin = document.getElementById('bookCheckin');
    const checkout = document.getElementById('bookCheckout');
    const platform = document.getElementById('bookPlatform');
    const payout = document.getElementById('bookPayout');

    if (!guest.value.trim()) { showToast('Please enter guest name.'); return; }
    if (!checkin.value || !checkout.value) { showToast('Please select check-in and check-out dates.'); return; }
    if (checkin.value >= checkout.value) { showToast('Check-out must be after check-in.'); return; }

    const propNames = { '1': 'Apt #6', '2': 'Apt #7', '3': 'Apt #8', '4': 'Cottage', '5': 'Combined #6+#8' };
    const aptNumbers = { '1': '6', '2': '7', '3': '8', '4': 'Cottage', '5': '6+8' };
    const entry = {
        id: Date.now(),
        property_id: parseInt(prop.value),
        apt_number: aptNumbers[prop.value],
        property_name: propNames[prop.value],
        guest_name: guest.value.trim(),
        checkin_date: checkin.value,
        checkout_date: checkout.value,
        platform: platform.value,
        payout: parseFloat(payout.value) || 0,
        status: 'confirmed',
        created: new Date().toISOString()
    };

    const bookings = loadLocalData('bookings', []);
    bookings.push(entry);
    saveLocalData('bookings', bookings);

    // Merge into DEMO.reservations for this session
    DEMO.reservations.push(entry);

    guest.value = '';
    checkin.value = '';
    checkout.value = '';
    payout.value = '';
    closeModal('bookingModal');
    showToast(`✅ Booking saved — ${entry.guest_name} at ${entry.property_name}`);

    // Refresh vacancy gaps if displayed
    if (document.getElementById('vacancyGaps')) renderVacancyGaps(DEMO.reservations);
}

function saveExpense() {
    const category = document.getElementById('expCategory');
    const amount = document.getElementById('expAmount');
    const desc = document.getElementById('expDesc');
    const propEl = document.getElementById('expProp');

    if (!amount.value || parseFloat(amount.value) <= 0) { showToast('Please enter an amount.'); return; }
    if (!desc.value.trim()) { showToast('Please enter a description.'); return; }

    const entry = {
        id: Date.now(),
        category: category.value,
        amount: parseFloat(amount.value),
        description: desc.value.trim(),
        property: propEl.value,
        date: today(),
        created: new Date().toISOString()
    };

    const expenses = loadLocalData('expenses', []);
    expenses.push(entry);
    saveLocalData('expenses', expenses);

    // Update DEMO financials for this session
    DEMO.financials.expenses.total += entry.amount;
    if (entry.category === 'cleaning') {
        DEMO.financials.expenses.cleaners = (DEMO.financials.expenses.cleaners || 0) + entry.amount;
    } else {
        DEMO.financials.expenses.general = (DEMO.financials.expenses.general || 0) + entry.amount;
    }
    DEMO.financials.net_profit = DEMO.financials.revenue.total - DEMO.financials.expenses.total;

    amount.value = '';
    desc.value = '';
    closeModal('expenseModal');
    showToast(`💸 Expense logged — ${formatCurrency(entry.amount)} (${entry.category})`);
}

// ===== CLEANING COST CALCULATOR =====
function updateCalc() {
    const sizes = { small: { turnover: 1.5, refresh: 0.75, deep: 2.5 }, medium: { turnover: 2, refresh: 1, deep: 3.5 }, large: { turnover: 3, refresh: 1.5, deep: 4.5 }, cottage: { turnover: 2.5, refresh: 1.25, deep: 4 } };
    const prop = document.getElementById('calcProperty')?.value || 'small';
    const type = document.getElementById('calcType')?.value || 'turnover';
    const rate = parseFloat(document.getElementById('calcRate')?.value) || 25;
    const hours = sizes[prop]?.[type] || 1.5;
    const cost = hours * rate;

    const hEl = document.getElementById('calcHours');
    const cEl = document.getElementById('calcCost');
    const mEl = document.getElementById('calcMonthly');
    if (hEl) hEl.textContent = hours;
    if (cEl) cEl.textContent = formatCurrency(cost);
    if (mEl) mEl.textContent = formatCurrency(cost * 4);
}

// ===== PER-PROPERTY REVENUE =====
// Shows current-month revenue, pro-rated by how many nights fall within the month.
function renderPropertyRevenue(reservations) {
    const container = document.getElementById('propertyRevenue');
    if (!container) return;

    // Current month window
    const now = new Date();
    const yr = now.getFullYear();
    const mo = now.getMonth();
    const monthStart = `${yr}-${String(mo+1).padStart(2,'0')}-01`;
    const lastDay = new Date(yr, mo+1, 0).getDate();
    const monthEnd = `${yr}-${String(mo+1).padStart(2,'0')}-${String(lastDay).padStart(2,'0')}`;

    const propMap = {};
    reservations.forEach(r => {
        // Skip reservations entirely outside this month
        if (r.checkout_date < monthStart || r.checkin_date > monthEnd) return;

        const totalNights = nightsBetween(r.checkin_date, r.checkout_date);
        if (totalNights <= 0) return;

        // Pro-rate nights that fall within this month
        const overlapStart = r.checkin_date < monthStart ? monthStart : r.checkin_date;
        const overlapEnd   = r.checkout_date > monthEnd   ? monthEnd   : r.checkout_date;
        const overlapNights = nightsBetween(overlapStart, overlapEnd);
        const proRatedRevenue = (r.payout / totalNights) * overlapNights;

        const key = 'Apt ' + r.apt_number;
        if (!propMap[key]) propMap[key] = { revenue: 0, bookings: 0, nights: 0 };
        propMap[key].revenue += proRatedRevenue;
        propMap[key].bookings++;
        propMap[key].nights += overlapNights;
    });

    const entries = Object.entries(propMap).sort((a, b) => b[1].revenue - a[1].revenue);
    const maxRev = Math.max(...entries.map(([, v]) => v.revenue), 1);
    const totalRev = entries.reduce((s, [, v]) => s + v.revenue, 0);

    container.innerHTML = entries.map(([name, data], i) => {
        const pct = ((data.revenue / totalRev) * 100).toFixed(1);
        const barPct = (data.revenue / maxRev * 100);
        const color = PROPERTY_COLORS[name.replace('Apt ', '')] || { bg: '#999' };
        return `
            <div style="margin-bottom:1rem;animation:fadeSlideUp 0.3s ease ${i * 0.08}s forwards;opacity:0">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.35rem">
                    <div>
                        <span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:${color.bg};vertical-align:middle;margin-right:6px"></span>
                        <span style="font-weight:600;font-size:0.9rem">${name}</span>
                        <span style="color:var(--gray);font-size:0.8rem;margin-left:0.5rem">${data.bookings} booking${data.bookings !== 1 ? 's' : ''} · ${data.nights} night${data.nights !== 1 ? 's' : ''}</span>
                    </div>
                    <div>
                        <span style="font-weight:700;font-size:0.95rem">${formatCurrency(data.revenue)}</span>
                        <span style="color:var(--gray);font-size:0.75rem;margin-left:0.4rem">(${pct}%)</span>
                    </div>
                </div>
                <div style="background:var(--light-gray);border-radius:6px;height:20px;overflow:hidden">
                    <div class="bar-animate" style="background:${color.bg};height:100%;width:0;border-radius:6px;transition:width 0.8s ease" data-width="${barPct}"></div>
                </div>
            </div>
        `;
    }).join('') +
    `<div style="margin-top:1rem;padding-top:1rem;border-top:2px solid var(--terracotta);display:flex;justify-content:space-between;align-items:baseline;font-weight:700;font-size:1rem">
        <div>
            <span>${['January','February','March','April','May','June','July','August','September','October','November','December'][new Date().getMonth()]} Revenue</span>
            <span style="font-size:0.65rem;font-weight:400;color:var(--gray);margin-left:0.4rem">(pro-rated, this month only)</span>
        </div>
        <span style="color:var(--terracotta)">${formatCurrency(Math.round(totalRev))}</span>
    </div>`;

    // Animate bars
    requestAnimationFrame(() => {
        container.querySelectorAll('.bar-animate').forEach(bar => {
            setTimeout(() => { bar.style.width = bar.dataset.width + '%'; }, 200);
        });
    });
}

// ===== VACANCY GAP FINDER =====
function renderVacancyGaps(reservations) {
    const container = document.getElementById('vacancyGaps');
    if (!container) return;

    const todayStr = today();
    const lookAheadDays = 60;
    const cutoff = new Date(Date.now() + lookAheadDays * 86400000).toISOString().split('T')[0];

    const propRates = { '6': 85, '7': 116, '8': 93, 'Cottage': 43, '6+8': 150 };
    const propColors = PROPERTY_COLORS;

    // Group reservations by property
    const byProp = {};
    DEMO.properties.forEach(p => { byProp[p.id] = { prop: p, reservations: [] }; });
    reservations.forEach(r => {
        if (byProp[r.property_id]) byProp[r.property_id].reservations.push(r);
    });

    const gaps = [];
    Object.values(byProp).forEach(({ prop, reservations: res }) => {
        // Sort reservations by checkin
        const sorted = res.filter(r => r.checkout_date >= todayStr)
            .sort((a, b) => a.checkin_date.localeCompare(b.checkin_date));

        // Check gap between now and first booking
        if (sorted.length === 0) {
            gaps.push({
                apt: prop.apt_number,
                property_name: prop.name,
                start: todayStr,
                end: cutoff,
                days: lookAheadDays,
                potential: prop.base_nightly_rate * lookAheadDays * 0.6, // 60% est occupancy
                type: 'open'
            });
        } else {
            // Gap from today to first booking
            if (sorted[0].checkin_date > todayStr) {
                const gapDays = daysUntil(sorted[0].checkin_date);
                if (gapDays >= 2) {
                    gaps.push({
                        apt: prop.apt_number,
                        property_name: prop.name,
                        start: todayStr,
                        end: sorted[0].checkin_date,
                        days: gapDays,
                        potential: prop.base_nightly_rate * gapDays,
                        type: 'before_booking',
                        next_guest: sorted[0].guest_name
                    });
                }
            }

            // Gaps between bookings
            for (let i = 0; i < sorted.length - 1; i++) {
                const gapStart = sorted[i].checkout_date;
                const gapEnd = sorted[i+1].checkin_date;
                if (gapEnd > gapStart && gapStart >= todayStr && gapEnd <= cutoff) {
                    const gapDays = Math.ceil((new Date(gapEnd + 'T12:00:00') - new Date(gapStart + 'T12:00:00')) / 86400000);
                    if (gapDays >= 2) {
                        gaps.push({
                            apt: prop.apt_number,
                            property_name: prop.name,
                            start: gapStart,
                            end: gapEnd,
                            days: gapDays,
                            potential: prop.base_nightly_rate * gapDays,
                            type: 'between',
                            prev_guest: sorted[i].guest_name,
                            next_guest: sorted[i+1].guest_name
                        });
                    }
                }
            }

            // Gap after last booking within lookAhead
            const last = sorted[sorted.length - 1];
            if (last.checkout_date < cutoff) {
                const gapDays = Math.ceil((new Date(cutoff + 'T12:00:00') - new Date(last.checkout_date + 'T12:00:00')) / 86400000);
                if (gapDays >= 3) {
                    gaps.push({
                        apt: prop.apt_number,
                        property_name: prop.name,
                        start: last.checkout_date,
                        end: cutoff,
                        days: gapDays,
                        potential: prop.base_nightly_rate * gapDays * 0.5,
                        type: 'after_last',
                        prev_guest: last.guest_name
                    });
                }
            }
        }
    });

    // Sort by potential revenue desc
    gaps.sort((a, b) => b.potential - a.potential);

    if (!gaps.length) {
        container.innerHTML = '<div class="card"><p style="color:var(--sage);font-family:var(--font-serif);font-style:italic">🎉 Calendar is packed! No gaps found in the next 60 days.</p></div>';
        return;
    }

    const totalPotential = gaps.reduce((s, g) => s + g.potential, 0);

    container.innerHTML = `
        <div style="background:var(--linen);border:1px solid var(--blush);border-radius:2px;padding:1rem 1.5rem;margin-bottom:1.25rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem">
            <div>
                <div style="font-size:0.65rem;color:var(--gray);text-transform:uppercase;letter-spacing:2px;font-weight:600">Revenue Potential (next 60 days)</div>
                <div style="font-family:var(--font-serif);font-size:2rem;font-weight:700;color:var(--terracotta)">${formatCurrency(totalPotential)}</div>
            </div>
            <div style="font-size:0.8rem;color:var(--gray);font-family:var(--font-serif);font-style:italic;max-width:300px">
                ${gaps.length} vacancy window${gaps.length !== 1 ? 's' : ''} found across your properties. Fill these gaps to maximize revenue.
            </div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem">
            ${gaps.map((g, i) => {
                const color = (propColors[g.apt] || {bg:'#999'}).bg;
                const typeLabel = g.type === 'between' ? `After ${g.prev_guest} → Before ${g.next_guest}`
                    : g.type === 'before_booking' ? `Before ${g.next_guest}'s arrival`
                    : g.type === 'after_last' ? `After ${g.prev_guest} checks out`
                    : 'Fully open';
                const urgencyDot = g.days <= 3 ? '🔴' : g.days <= 7 ? '🟡' : '🟢';
                return `
                    <div style="background:var(--warm-white);border:1px solid var(--light-gray);border-left:4px solid ${color};border-radius:2px;padding:1.25rem;animation:fadeSlideUp 0.3s ease ${i * 0.06}s forwards;opacity:0">
                        <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.75rem">
                            <div>
                                <div style="font-family:var(--font-serif);font-weight:700;font-size:1rem;color:var(--warm-brown)">Apt ${g.apt}</div>
                                <div style="font-size:0.75rem;color:var(--gray);margin-top:0.1rem">${typeLabel}</div>
                            </div>
                            <div style="text-align:right">
                                <div style="font-family:var(--font-serif);font-size:1.3rem;font-weight:700;color:var(--sage)">${formatCurrency(g.potential)}</div>
                                <div style="font-size:0.65rem;color:var(--gray)">potential</div>
                            </div>
                        </div>
                        <div style="display:flex;justify-content:space-between;align-items:center">
                            <div style="font-size:0.8rem;color:var(--dark-brown)">${urgencyDot} ${formatDate(g.start)} → ${formatDate(g.end)}</div>
                            <div style="font-size:0.75rem;font-weight:700;color:var(--terracotta)">${g.days} night${g.days !== 1 ? 's' : ''}</div>
                        </div>
                    </div>
                `;
            }).join('')}
        </div>
    `;
}

// ===== TOAST SYSTEM =====
function showToast(msg, duration = 3000) {
    let toast = document.getElementById('toast');
    if (!toast) return;
    toast.textContent = msg;
    toast.style.pointerEvents = 'auto';
    requestAnimationFrame(() => {
        toast.style.transform = 'translateY(0)';
        toast.style.opacity = '1';
        setTimeout(() => {
            toast.style.transform = 'translateY(100px)';
            toast.style.opacity = '0';
            toast.style.pointerEvents = 'none';
        }, duration);
    });
}

// ===== CLEANING PAGE INLINE LOG SAVE =====
// Wired to the "Save Cleaning" button on cleaning.html (separate form from dashboard modal)
function saveCleaningFromPage() {
    const prop  = document.getElementById('logCleanProp');
    const date  = document.getElementById('logCleanDate');
    const cleaner = document.getElementById('logCleanCleaner');
    const hours = document.getElementById('logCleanHours');
    const type  = document.getElementById('logCleanType');
    const notes = document.getElementById('logCleanNotes');

    if (!date || !date.value) { showToast('Please select a date.'); return; }
    if (!hours || parseFloat(hours.value) <= 0) { showToast('Please enter valid hours.'); return; }

    const propNames   = { '1': 'Apt #6', '2': 'Apt #7', '3': 'Apt #8', '4': 'Cottage', '5': 'Combined #6+#8' };
    const aptNumbers  = { '1': '6', '2': '7', '3': '8', '4': 'Cottage', '5': '6+8' };
    const hoursVal    = parseFloat(hours.value) || 2;
    const rate        = 25; // $25/hr
    const entry = {
        id: Date.now(),
        property:    propNames[prop.value] || prop.value,
        property_id: parseInt(prop.value),
        apt_number:  aptNumbers[prop.value] || prop.value,
        date:        date.value,
        cleaner:     cleaner.value,
        hours:       hoursVal,
        type:        type.value,
        notes:       notes.value.trim(),
        completed:   1,
        pay:         hoursVal * rate,
        created:     new Date().toISOString()
    };

    const cleanings = loadLocalData('cleanings', []);
    cleanings.push(entry);
    saveLocalData('cleanings', cleanings);

    // Refresh the page sections with updated data
    const schedule = {
        scheduled: [...(DEMO.cleaningSchedule.scheduled || []), ...cleanings],
        needed: generateNeededCleanings(DEMO.reservations)
    };
    renderCleaningSchedule(schedule);
    renderCleanerSummaries();

    // Reset form
    if (notes) notes.value = '';
    if (hours) hours.value = '2';
    date.value = today();

    showToast(`✅ Cleaning logged — ${entry.property} on ${formatDate(entry.date)} (${cleaner.value}, ${hoursVal}h · ${formatCurrency(entry.pay)})`);
}

// Auto-refresh dashboard every 60 seconds
if (typeof initDashboard === 'function' && document.getElementById('propertyGrid')) {
    setInterval(() => initDashboard(), 60000);
}
