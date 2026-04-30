/* USMC Ministries — newsletter signup
 *
 * Default behavior: opens user's mail client with a pre-filled subscribe email
 * (works without any server). To upgrade to an API endpoint later, set
 * window.USMC_NEWSLETTER_ENDPOINT = "https://api.example.com/subscribe"
 * before this script runs (e.g., in a <script> tag in <head>).
 *
 * Forms must have:
 *   <form data-newsletter [data-source="page-name"]>
 *     <input type="email" name="email" required>
 *     <button type="submit">Join</button>
 *   </form>
 */
(function () {
  'use strict';

  var TO    = 'info@usmcmin.com';
  var SUBJ  = 'Subscribe me to the Field Brief';

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
        // API mode — POST JSON
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
        // Mailto fallback — opens the user's mail client
        var body = 'Please subscribe me to the Field Brief.\n\nEmail: ' + email +
                   '\nSource: ' + source + '\n';
        var href = 'mailto:' + TO +
                   '?subject=' + encodeURIComponent(SUBJ) +
                   '&body=' + encodeURIComponent(body);
        window.location.href = href;
        showStatus('Opening your mail app — just hit send.', true);
      }
    });
  });
})();
