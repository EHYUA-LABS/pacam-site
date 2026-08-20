
document.addEventListener('DOMContentLoaded', function () {
  // bandeau promotionnel : fermeture mémorisée (par annonce) + clic = navigation
  var promoBar = document.getElementById('promo-bar');
  if (promoBar) {
    var promoId = promoBar.getAttribute('data-promo-id');
    var dismissedId = null;
    try { dismissedId = localStorage.getItem('pacam_promo_dismissed'); } catch (e) {}
    if (dismissedId === promoId) {
      promoBar.classList.add('hidden');
    }
    var promoClose = promoBar.querySelector('[data-close-promo]');
    if (promoClose) {
      promoClose.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        promoBar.classList.add('hidden');
        try { localStorage.setItem('pacam_promo_dismissed', promoId); } catch (err) {}
      });
    }
  }

  // menu mobile
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
      var opened = nav.classList.contains('open');
      toggle.innerHTML = opened
        ? '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
        : '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
    });
  }

  // reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { obs.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  // filter tabs (terrains-biens / realisations)
  document.querySelectorAll('.filter-tabs').forEach(function (group) {
    var buttons = group.querySelectorAll('button');
    var targetSelector = group.getAttribute('data-target');
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var filter = btn.getAttribute('data-filter');
        document.querySelectorAll(targetSelector).forEach(function (item) {
          var cat = item.getAttribute('data-cat');
          item.style.display = (filter === 'all' || cat === filter) ? '' : 'none';
        });
      });
    });
  });

  // forms: intercept submit for the demo
  document.querySelectorAll('form[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      showToast('Merci ! Votre demande a bien été enregistrée (démonstration).');
      form.reset();
    });
  });

  // pre-fill "service" field from query string on contact page
  var params = new URLSearchParams(window.location.search);
  var demandeField = document.querySelector('[name="type_demande"]');
  if (demandeField && params.get('demande')) {
    var val = params.get('demande');
    for (var i = 0; i < demandeField.options.length; i++) {
      if (demandeField.options[i].value === val) { demandeField.selectedIndex = i; }
    }
  }
  var bienField = document.querySelector('[name="bien_concerne"]');
  if (bienField && params.get('bien')) { bienField.value = params.get('bien'); }
});

function showToast(msg) {
  var toast = document.querySelector('.toast');
  if (!toast) return;
  toast.querySelector('span').textContent = msg;
  toast.classList.add('show');
  setTimeout(function () { toast.classList.remove('show'); }, 3200);
}
