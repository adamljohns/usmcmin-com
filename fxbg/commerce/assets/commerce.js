/** Christ-Centered Commerce — profile factor expand (v0.4) */
(function () {
  document.querySelectorAll('.factor-row').forEach(function (row) {
    row.addEventListener('toggle', function () {
      if (row.open) {
        document.querySelectorAll('.factor-row[open]').forEach(function (other) {
          if (other !== row) other.open = false;
        });
      }
    });
  });
})();
