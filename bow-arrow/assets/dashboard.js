/* Bow & Arrow Studio OS — Dashboard JavaScript
   v2.0 — March 2026 Refinement */

const API_BASE = ''; // Empty = use demo data (no backend running on GitHub Pages)

// Demo data (seeded from real B&A data — used when backend is offline)
const DEMO = {
    properties: [
        { id: 1, name: 'Spacious Apartment', apt_number: '6', beds: 1, baths: 1, base_nightly_rate: 85, status: 'active', current_guest: 'Jess', current_checkout: '2026-03-20', next_guest: 'Cleve', next_checkin: '2026-03-20', review_avg: 5.0, review_count: 24 },
        { id: 2, name: 'Boho-Modern Apartment', apt_number: '7', beds: 2, baths: 2, base_nightly_rate: 116, status: 'active', current_guest: null, current_checkout: null, next_guest: 'Diane', next_checkin: '2026-03-19', review_avg: 5.0, review_count: 18 },
        { id: 3, name: 'Orange Apartment', apt_number: '8', beds: 1, baths: 1, base_nightly_rate: 93, status: 'active', current_guest: 'Brandi', current_checkout: '2026-03-21', next_guest: null, next_checkin: null, review_avg: 5.0, review_count: 21 },
        { id: 4, name: 'Prof Row Cottage', apt_number: 'Cottage', beds: 3, baths: 1, base_nightly_rate: 43, min_nights: 30, status: 'active', current_guest: null, current_checkout: null, next_guest: 'Virginia Van Alstine', next_checkin: '2026-04-06', review_avg: 4.9, review_count: 8 },
        { id: 5, name: 'Hanover Combined', apt_number: '6+8', beds: 2, baths: 2, base_nightly_rate: 150, status: 'active', current_guest: null, current_checkout: null, next_guest: null, next_checkin: null, review_avg: 5.0, review_count: 6 },
    ],
    reservations: [
        { id: 1, property_id: 3, guest_name: 'Brandi', checkin_date: '2026-03-15', checkout_date: '2026-03-21', platform: 'airbnb', payout: 465, status: 'checked_in', apt_number: '8', property_name: 'Orange Apartment', guests: 1 },
        { id: 2, property_id: 1, guest_name: 'Jess', checkin_date: '2026-03-15', checkout_date: '2026-03-20', platform: 'airbnb', payout: 340, status: 'checked_in', apt_number: '6', property_name: 'Spacious Apartment', guests: 2 },
        { id: 3, property_id: 2, guest_name: 'Diane', checkin_date: '2026-03-19', checkout_date: '2026-03-26', platform: 'airbnb', payout: 650, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 3 },
        { id: 4, property_id: 1, guest_name: 'Cleve', checkin_date: '2026-03-20', checkout_date: '2026-03-21', platform: 'airbnb', payout: 85, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 1 },
        { id: 5, property_id: 1, guest_name: 'Amy', checkin_date: '2026-03-23', checkout_date: '2026-03-28', platform: 'airbnb', payout: 340, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment', guests: 2 },
        { id: 6, property_id: 2, guest_name: 'Brittany', checkin_date: '2026-03-26', checkout_date: '2026-03-30', platform: 'airbnb', payout: 370, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment', guests: 2 },
        { id: 7, property_id: 4, guest_name: 'Virginia Van Alstine', checkin_date: '2026-04-06', checkout_date: '2026-05-06', platform: 'airbnb', payout: 1290, status: 'confirmed', apt_number: 'Cottage', property_name: 'Prof Row Cottage', guests: 2 },
    ],
    financials: {
        month: '2026-03',
        revenue: { airbnb: 2250, direct_booking: 0, merch: 0, vending: 0, car_rental: 0, total: 2250 },
        expenses: { general: 0, cleaners: 130, total: 130 },
        net_profit: 2120
    },
    monthly: [
        { month: '2025-10', revenue: 1800, expenses: 380, net: 1420 },
        { month: '2025-11', revenue: 2100, expenses: 410, net: 1690 },
        { month: '2025-12', revenue: 2600, expenses: 520, net: 2080 },
        { month: '2026-01', revenue: 1950, expenses: 350, net: 1600 },
        { month: '2026-02', revenue: 2300, expenses: 400, net: 1900 },
        { month: '2026-03', revenue: 2250, expenses: 130, net: 2120 },
    ],
    alerts: [
        { type: 'checkin', priority: 'high', message: 'Diane checks in to Apt 7 on Mar 19 (tomorrow!)', time: '2026-03-17T03:00:00' },
        { type: 'checkout', priority: 'medium', message: 'Jess checks out of Apt 6 on Mar 20 (Thu)', time: '2026-03-17T03:00:00' },
        { type: 'checkout', priority: 'medium', message: 'Brandi checks out of Apt 8 on Mar 21 (Fri)', time: '2026-03-17T03:00:00' },
        { type: 'cleaning', priority: 'high', message: 'Apt 6 needs turnover after Jess (Mar 20) — Cleve arrives same day!', time: '2026-03-17T03:00:00' },
        { type: 'cleaning', priority: 'medium', message: 'Apt 8 needs cleaning after Brandi (Mar 21). Suggest: Tiffany', time: '2026-03-17T03:00:00' },
        { type: 'review', priority: 'low', message: '⭐ 5.00 perfect streak — 77 reviews! Keep it going!', time: '2026-03-17T03:00:00' },
    ],
    cleaningSchedule: {
        scheduled: [
            { property_name: 'Spacious Apartment', apt_number: '6', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1, hours: 1.5, pay: 37.50 },
            { property_name: 'Boho-Modern Apartment', apt_number: '7', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1, hours: 2, pay: 50 },
            { property_name: 'Orange Apartment', apt_number: '8', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1, hours: 1.5, pay: 42.50 },
        ],
        needed: [
            { apt_number: '6', guest_name: 'Jess', checkout_date: '2026-03-20', suggested_cleaner: 'tiffany', urgency: 'critical', note: 'Same-day turnover — Cleve arriving!' },
            { apt_number: '8', guest_name: 'Brandi', checkout_date: '2026-03-21', suggested_cleaner: 'tiffany', urgency: 'normal', note: '' },
            { apt_number: '7', guest_name: 'Diane', checkout_date: '2026-03-26', suggested_cleaner: 'amanda', urgency: 'upcoming', note: 'Brittany arrives same day' },
        ]
    },
    occupancy: [
        { apt_number: '6', property_name: 'Spacious Apartment', occupancy_30d: 46.7, adr: 85.0, revpar: 39.7 },
        { apt_number: '7', property_name: 'Boho-Modern Apartment', occupancy_30d: 23.3, adr: 116.0, revpar: 27.1 },
        { apt_number: '8', property_name: 'Orange Apartment', occupancy_30d: 20.0, adr: 93.0, revpar: 18.6 },
        { apt_number: 'Cottage', property_name: 'Prof Row Cottage', occupancy_30d: 0, adr: 0, revpar: 0 },
        { apt_number: '6+8', property_name: 'Hanover Combined', occupancy_30d: 0, adr: 0, revpar: 0 },
        { apt_number: 'ALL', property_name: 'Overall', occupancy_30d: 18.0, adr: 88.5, revpar: 15.9 },
    ],
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

    // Show loading skeletons
    showSkeleton('propertyGrid', 5);

    const properties = (await fetchData('/api/properties')) || DEMO.properties;
    const alerts = (await fetchData('/api/alerts')) || DEMO.alerts;
    const financials = (await fetchData('/api/financials/summary')) || DEMO.financials;
    const reservations = (await fetchData('/api/reservations')) || DEMO.reservations;
    const reviews = DEMO.reviews;

    renderSummaryCards(properties, financials, reviews);
    renderPropertyGrid(properties);
    renderReviewTracker(reviews);
    renderAlerts(alerts);
    renderRevenueSnapshot(financials);
    renderUpcomingEvents(reservations);
}

function renderSummaryCards(properties, financials, reviews) {
    const occupied = properties.filter(p => p.current_guest).length;

    animateValue('occupiedCount', `${occupied}/${properties.length}`);
    document.getElementById('occupiedLabel').textContent = occupied > 0 ? `${occupied} occupied tonight` : 'All vacant';

    animateValue('revenueTotal', formatCurrency(financials.revenue.total));
    document.getElementById('revenueLabel').textContent = 'March Revenue';

    animateValue('netProfit', formatCurrency(financials.net_profit));
    document.getElementById('netLabel').textContent = `${((financials.net_profit / financials.revenue.total) * 100).toFixed(0)}% margin`;

    // Review card
    const reviewCard = document.getElementById('reviewCard');
    if (reviewCard) {
        animateValue('reviewScore', reviews.overall_avg.toFixed(2));
        document.getElementById('reviewLabel').textContent = `${reviews.total_count} reviews · ${reviews.perfect_streak} perfect streak`;
    }
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

    const properties = (await fetchData('/api/properties')) || DEMO.properties;
    const reservations = (await fetchData('/api/reservations')) || DEMO.reservations;

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

    const schedule = (await fetchData('/api/cleaning-schedule')) || DEMO.cleaningSchedule;
    renderCleaningSchedule(schedule);
    renderCleanerSummaries();
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
    document.getElementById('amandaHours').textContent = '0';
    document.getElementById('amandaPay').textContent = '$0';
    document.getElementById('amandaCleanings').textContent = '0';
    document.getElementById('tiffanyHours').textContent = '5';
    document.getElementById('tiffanyPay').textContent = '$130';
    document.getElementById('tiffanyCleanings').textContent = '3';
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

    // Calculate forecast for next 3 months
    const months = ['2026-03', '2026-04', '2026-05'];
    const monthNames = { '2026-03': 'March', '2026-04': 'April', '2026-05': 'May' };

    const forecast = months.map(m => {
        const monthRes = reservations.filter(r => r.checkin_date.startsWith(m) || (r.checkin_date < m + '-01' && r.checkout_date > m + '-01'));
        const confirmed = monthRes.reduce((sum, r) => sum + (r.payout || 0), 0);
        return { month: m, label: monthNames[m], confirmed, projected: confirmed };
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
                <li style="margin-bottom:0.25rem">→ Prof Row Cottage booked Apr 6 – May 6 (<strong>${formatCurrency(1290)}</strong> payout)</li>
                <li>→ Vacancy opportunity: Apt #8 open after Mar 21, Cottage open until Apr 6</li>
            </ul>
        </div>
    `;
}

// ===== MAINTENANCE PAGE =====
async function initMaintenance() {
    if (!checkAuth()) return;
    initMobileNav();

    const maintenance = DEMO.maintenance;
    renderMaintenanceList(maintenance);
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

// Auto-refresh dashboard every 60 seconds
if (typeof initDashboard === 'function' && document.getElementById('propertyGrid')) {
    setInterval(() => initDashboard(), 60000);
}
