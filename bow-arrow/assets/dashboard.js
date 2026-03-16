/* Bow & Arrow Studio OS — Dashboard JavaScript */

const API_BASE = ''; // Empty = use demo data (no backend running on GitHub Pages)

// Demo data (seeded from real B&A data — used when backend is offline)
const DEMO = {
    properties: [
        { id: 1, name: 'Spacious Apartment', apt_number: '6', beds: 2, baths: 1, base_nightly_rate: 85, status: 'active', current_guest: 'Jess', current_checkout: '2026-03-20', next_guest: 'Cleve', next_checkin: '2026-03-20' },
        { id: 2, name: 'Boho-Modern Apartment', apt_number: '7', beds: 2, baths: 1, base_nightly_rate: 116, status: 'active', current_guest: null, current_checkout: null, next_guest: 'Diane', next_checkin: '2026-03-19' },
        { id: 3, name: 'Orange Apartment', apt_number: '8', beds: 1, baths: 1, base_nightly_rate: 93, status: 'active', current_guest: 'Brandi', current_checkout: '2026-03-21', next_guest: null, next_checkin: null },
        { id: 4, name: 'Prof Row Cottage', apt_number: 'Cottage', beds: 1, baths: 1, base_nightly_rate: 43, min_nights: 30, status: 'active', current_guest: null, current_checkout: null, next_guest: 'Virginia Van Alstine', next_checkin: '2026-04-06' },
        { id: 5, name: 'Hanover Combined', apt_number: '6+8', beds: 3, baths: 2, base_nightly_rate: 150, status: 'active', current_guest: null, current_checkout: null, next_guest: null, next_checkin: null },
    ],
    reservations: [
        { id: 1, property_id: 3, guest_name: 'Brandi', checkin_date: '2026-03-15', checkout_date: '2026-03-21', platform: 'airbnb', payout: 465, status: 'checked_in', apt_number: '8', property_name: 'Orange Apartment' },
        { id: 2, property_id: 1, guest_name: 'Jess', checkin_date: '2026-03-15', checkout_date: '2026-03-20', platform: 'airbnb', payout: 340, status: 'checked_in', apt_number: '6', property_name: 'Spacious Apartment' },
        { id: 3, property_id: 2, guest_name: 'Diane', checkin_date: '2026-03-19', checkout_date: '2026-03-26', platform: 'airbnb', payout: 650, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment' },
        { id: 4, property_id: 1, guest_name: 'Cleve', checkin_date: '2026-03-20', checkout_date: '2026-03-21', platform: 'airbnb', payout: 85, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment' },
        { id: 5, property_id: 1, guest_name: 'Amy', checkin_date: '2026-03-23', checkout_date: '2026-03-28', platform: 'airbnb', payout: 340, status: 'confirmed', apt_number: '6', property_name: 'Spacious Apartment' },
        { id: 6, property_id: 2, guest_name: 'Brittany', checkin_date: '2026-03-26', checkout_date: '2026-03-30', platform: 'airbnb', payout: 370, status: 'confirmed', apt_number: '7', property_name: 'Boho-Modern Apartment' },
        { id: 7, property_id: 4, guest_name: 'Virginia Van Alstine', checkin_date: '2026-04-06', checkout_date: '2026-05-06', platform: 'airbnb', payout: 1290, status: 'confirmed', apt_number: 'Cottage', property_name: 'Prof Row Cottage' },
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
        { type: 'checkout', priority: 'medium', message: 'Jess checks out of Apt 6 on 2026-03-20' },
        { type: 'checkout', priority: 'medium', message: 'Brandi checks out of Apt 8 on 2026-03-21' },
        { type: 'cleaning', priority: 'high', message: 'Apt 6 needs cleaning after Jess (checkout Mar 20). Suggest: tiffany' },
        { type: 'cleaning', priority: 'high', message: 'Apt 8 needs cleaning after Brandi (checkout Mar 21). Suggest: tiffany' },
    ],
    cleaningSchedule: {
        scheduled: [
            { property_name: 'Spacious Apartment', apt_number: '6', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1 },
            { property_name: 'Boho-Modern Apartment', apt_number: '7', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1 },
            { property_name: 'Orange Apartment', apt_number: '8', date: '2026-03-15', cleaner: 'tiffany', type: 'turnover', completed: 1 },
        ],
        needed: [
            { apt_number: '6', guest_name: 'Jess', checkout_date: '2026-03-20', suggested_cleaner: 'tiffany' },
            { apt_number: '8', guest_name: 'Brandi', checkout_date: '2026-03-21', suggested_cleaner: 'tiffany' },
        ]
    },
    occupancy: [
        { apt_number: '6', property_name: 'Spacious Apartment', occupancy_30d: 46.7, adr: 85.0, revpar: 39.7 },
        { apt_number: '7', property_name: 'Boho-Modern Apartment', occupancy_30d: 23.3, adr: 116.0, revpar: 27.1 },
        { apt_number: '8', property_name: 'Orange Apartment', occupancy_30d: 20.0, adr: 93.0, revpar: 18.6 },
        { apt_number: 'Cottage', property_name: 'Prof Row Cottage', occupancy_30d: 0, adr: 0, revpar: 0 },
        { apt_number: '6+8', property_name: 'Hanover Combined', occupancy_30d: 0, adr: 0, revpar: 0 },
        { apt_number: 'ALL', property_name: 'Overall', occupancy_30d: 18.0, adr: 88.5, revpar: 15.9 },
    ]
};

// Auth check
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

// Data fetching (falls back to demo)
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

// Format helpers
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

// Dashboard page
async function initDashboard() {
    if (!checkAuth()) return;

    document.getElementById('dateInfo').textContent = todayNice();

    const properties = (await fetchData('/api/properties')) || DEMO.properties;
    const alerts = (await fetchData('/api/alerts')) || DEMO.alerts;
    const financials = (await fetchData('/api/financials/summary')) || DEMO.financials;
    const reservations = (await fetchData('/api/reservations')) || DEMO.reservations;

    renderPropertyGrid(properties);
    renderAlerts(alerts);
    renderRevenueSnapshot(financials);
    renderUpcomingEvents(reservations);
    renderSummaryCards(properties, financials);
}

function renderSummaryCards(properties, financials) {
    const occupied = properties.filter(p => p.current_guest).length;
    document.getElementById('occupiedCount').textContent = `${occupied}/${properties.length}`;
    document.getElementById('occupiedLabel').textContent = 'Properties Occupied';
    document.getElementById('revenueTotal').textContent = formatCurrency(financials.revenue.total);
    document.getElementById('revenueLabel').textContent = `March Revenue`;
    document.getElementById('netProfit').textContent = formatCurrency(financials.net_profit);
    document.getElementById('netLabel').textContent = 'Net Profit (March)';
}

function renderPropertyGrid(properties) {
    const container = document.getElementById('propertyGrid');
    container.innerHTML = properties.map(p => {
        const isOccupied = !!p.current_guest;
        const statusClass = isOccupied ? 'occupied' : 'vacant';
        const badgeClass = isOccupied ? 'badge-occupied' : 'badge-vacant';
        const badgeText = isOccupied ? 'OCCUPIED' : 'VACANT';

        return `
            <div class="property-card ${statusClass}">
                <div style="display:flex;justify-content:space-between;align-items:center">
                    <div class="apt-name">Apt ${p.apt_number}</div>
                    <span class="status-badge ${badgeClass}">${badgeText}</span>
                </div>
                <div class="rate">${formatCurrency(p.base_nightly_rate)}/night</div>
                <div class="guest-info">
                    <div class="label">Current Guest</div>
                    <div class="name">${p.current_guest || '—'} ${p.current_checkout ? '→ ' + formatDate(p.current_checkout) : ''}</div>
                </div>
                <div class="guest-info">
                    <div class="label">Next Guest</div>
                    <div class="name">${p.next_guest || '—'} ${p.next_checkin ? '← ' + formatDate(p.next_checkin) : ''}</div>
                </div>
            </div>
        `;
    }).join('');
}

function renderAlerts(alerts) {
    const container = document.getElementById('alertFeed');
    if (!alerts.length) {
        container.innerHTML = '<p style="color:var(--gray);padding:1rem">No alerts right now 👍</p>';
        return;
    }
    const icons = { checkout: '🚪', cleaning: '🧹', low_stock: '📦' };
    container.innerHTML = '<ul class="alert-list">' + alerts.map(a => `
        <li class="alert-item">
            <div class="alert-icon alert-${a.priority}">${icons[a.type] || '⚠️'}</div>
            <div>${a.message}</div>
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
        container.innerHTML = '<p style="color:var(--gray)">No revenue data yet</p>';
        return;
    }

    // Simple horizontal bar chart
    const maxVal = Math.max(...streams.map(s => s.value));
    container.innerHTML = streams.map(s => `
        <div style="margin-bottom:0.75rem">
            <div style="display:flex;justify-content:space-between;margin-bottom:0.25rem">
                <span style="font-weight:600;font-size:0.85rem">${s.label}</span>
                <span style="font-weight:700">${formatCurrency(s.value)}</span>
            </div>
            <div style="background:var(--light-gray);border-radius:6px;height:24px;overflow:hidden">
                <div style="background:${s.color};height:100%;width:${(s.value/maxVal*100)}%;border-radius:6px;transition:width 0.5s"></div>
            </div>
        </div>
    `).join('');
}

function renderUpcomingEvents(reservations) {
    const container = document.getElementById('upcomingEvents');
    const todayStr = today();
    const weekEnd = new Date(Date.now() + 7 * 86400000).toISOString().split('T')[0];

    const events = [];
    reservations.forEach(r => {
        if (r.checkout_date >= todayStr && r.checkout_date <= weekEnd) {
            events.push({ date: r.checkout_date, type: '🚪 Checkout', name: r.guest_name, apt: r.apt_number });
        }
        if (r.checkin_date >= todayStr && r.checkin_date <= weekEnd) {
            events.push({ date: r.checkin_date, type: '🔑 Checkin', name: r.guest_name, apt: r.apt_number });
        }
    });

    events.sort((a, b) => a.date.localeCompare(b.date));

    if (!events.length) {
        container.innerHTML = '<p style="color:var(--gray);padding:0.5rem">No events this week</p>';
        return;
    }

    container.innerHTML = '<table><thead><tr><th>Date</th><th>Event</th><th>Guest</th><th>Apt</th></tr></thead><tbody>' +
        events.map(e => `<tr><td>${formatDate(e.date)}</td><td>${e.type}</td><td>${e.name}</td><td>${e.apt}</td></tr>`).join('') +
        '</tbody></table>';
}

// Calendar page
async function initCalendar() {
    if (!checkAuth()) return;

    const properties = (await fetchData('/api/properties')) || DEMO.properties;
    const reservations = (await fetchData('/api/reservations')) || DEMO.reservations;

    renderCalendar(properties, reservations, new Date().getFullYear(), new Date().getMonth());
}

let calYear, calMonth;

function renderCalendar(properties, reservations, year, month) {
    calYear = year;
    calMonth = month;
    const container = document.getElementById('calendarGrid');
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const monthNames = ['January','February','March','April','May','June','July','August','September','October','November','December'];

    document.getElementById('calMonthLabel').textContent = `${monthNames[month]} ${year}`;

    // Set grid columns
    container.style.gridTemplateColumns = `120px repeat(${daysInMonth}, 1fr)`;

    let html = '<div class="cal-header" style="grid-column:1">Property</div>';
    for (let d = 1; d <= daysInMonth; d++) {
        const isToday = (year === new Date().getFullYear() && month === new Date().getMonth() && d === new Date().getDate());
        html += `<div class="cal-header${isToday ? ' today' : ''}">${d}</div>`;
    }

    properties.forEach(p => {
        html += `<div class="cal-property">Apt ${p.apt_number}</div>`;
        for (let d = 1; d <= daysInMonth; d++) {
            const dateStr = `${year}-${String(month+1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
            const isToday = dateStr === today();
            let cls = 'vacant';
            let guest = '';

            for (const r of reservations) {
                if (r.property_id === p.id && dateStr >= r.checkin_date && dateStr < r.checkout_date) {
                    cls = 'occupied';
                    guest = r.guest_name;
                    break;
                }
            }

            html += `<div class="cal-day ${cls}${isToday ? ' today' : ''}">${guest ? `<span class="tooltip">${guest}</span>` : ''}</div>`;
        }
    });

    container.innerHTML = html;
}

function calPrev() {
    const properties = DEMO.properties;
    const reservations = DEMO.reservations;
    calMonth--;
    if (calMonth < 0) { calMonth = 11; calYear--; }
    renderCalendar(properties, reservations, calYear, calMonth);
}

function calNext() {
    const properties = DEMO.properties;
    const reservations = DEMO.reservations;
    calMonth++;
    if (calMonth > 11) { calMonth = 0; calYear++; }
    renderCalendar(properties, reservations, calYear, calMonth);
}

// Cleaning page
async function initCleaning() {
    if (!checkAuth()) return;

    const schedule = (await fetchData('/api/cleaning-schedule')) || DEMO.cleaningSchedule;
    renderCleaningSchedule(schedule);
    renderCleanerSummaries();
}

function renderCleaningSchedule(schedule) {
    const scheduled = document.getElementById('scheduledCleanings');
    const needed = document.getElementById('neededCleanings');

    if (schedule.scheduled.length) {
        scheduled.innerHTML = '<table><thead><tr><th>Date</th><th>Property</th><th>Cleaner</th><th>Type</th><th>Status</th></tr></thead><tbody>' +
            schedule.scheduled.map(c => `
                <tr>
                    <td>${formatDate(c.date)}</td>
                    <td>Apt ${c.apt_number}</td>
                    <td>${c.cleaner.charAt(0).toUpperCase() + c.cleaner.slice(1)}</td>
                    <td>${c.type}</td>
                    <td>${c.completed ? '✅ Done' : '⏳ Pending'}</td>
                </tr>
            `).join('') + '</tbody></table>';
    } else {
        scheduled.innerHTML = '<p style="color:var(--gray)">No cleanings scheduled this week</p>';
    }

    if (schedule.needed.length) {
        needed.innerHTML = '<table><thead><tr><th>Property</th><th>After Guest</th><th>Checkout</th><th>Suggested</th></tr></thead><tbody>' +
            schedule.needed.map(n => `
                <tr>
                    <td>Apt ${n.apt_number}</td>
                    <td>${n.guest_name}</td>
                    <td>${formatDate(n.checkout_date)}</td>
                    <td>${n.suggested_cleaner.charAt(0).toUpperCase() + n.suggested_cleaner.slice(1)}</td>
                </tr>
            `).join('') + '</tbody></table>';
    } else {
        needed.innerHTML = '<p style="color:var(--gray)">All cleanings covered 👍</p>';
    }
}

function renderCleanerSummaries() {
    // Amanda
    document.getElementById('amandaHours').textContent = '0';
    document.getElementById('amandaPay').textContent = '$0';
    document.getElementById('amandaCleanings').textContent = '0';

    // Tiffany
    document.getElementById('tiffanyHours').textContent = '5';
    document.getElementById('tiffanyPay').textContent = '$130';
    document.getElementById('tiffanyCleanings').textContent = '3';
}

// Financials page
async function initFinancials() {
    if (!checkAuth()) return;

    const summary = (await fetchData('/api/financials/summary')) || DEMO.financials;
    const monthly = (await fetchData('/api/financials/monthly')) || DEMO.monthly;

    renderFinancialSummary(summary);
    renderMonthlyChart(monthly);
}

function renderFinancialSummary(summary) {
    document.getElementById('totalRevenue').textContent = formatCurrency(summary.revenue.total);
    document.getElementById('totalExpenses').textContent = formatCurrency(summary.expenses.total);
    document.getElementById('totalNet').textContent = formatCurrency(summary.net_profit);

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

    container.innerHTML = '<div style="display:flex;gap:0.5rem;align-items:flex-end;height:200px;padding-top:1rem">' +
        monthly.map(m => {
            const height = (m.revenue / maxRev * 160);
            const netHeight = (m.net / maxRev * 160);
            return `
                <div style="flex:1;text-align:center">
                    <div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:180px">
                        <div style="font-size:0.7rem;font-weight:600;margin-bottom:0.25rem">${formatCurrency(m.revenue)}</div>
                        <div style="width:70%;height:${height}px;background:var(--saddle);border-radius:6px 6px 0 0;position:relative">
                            <div style="position:absolute;bottom:0;left:0;right:0;height:${Math.max(0,netHeight)}px;background:var(--green);border-radius:0 0 0 0;opacity:0.6"></div>
                        </div>
                    </div>
                    <div style="font-size:0.75rem;color:var(--gray);margin-top:0.25rem">${m.month.split('-')[1]}/${m.month.split('-')[0].slice(2)}</div>
                </div>
            `;
        }).join('') +
        '</div>' +
        '<div style="display:flex;gap:1rem;justify-content:center;margin-top:0.75rem;font-size:0.8rem">' +
        '<span><span style="display:inline-block;width:12px;height:12px;background:var(--saddle);border-radius:2px;vertical-align:middle"></span> Revenue</span>' +
        '<span><span style="display:inline-block;width:12px;height:12px;background:var(--green);opacity:0.6;border-radius:2px;vertical-align:middle"></span> Net Profit</span>' +
        '</div>';
}

// Modal controls
function openModal(id) {
    document.getElementById(id).classList.add('active');
}

function closeModal(id) {
    document.getElementById(id).classList.remove('active');
}

// Auto-refresh
if (typeof initDashboard === 'function' && document.getElementById('propertyGrid')) {
    setInterval(() => initDashboard(), 60000);
}
