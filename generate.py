#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Générateur de la maquette statique du site PACAM."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# ICONES (SVG inline, style trait, feather-like)
# ----------------------------------------------------------------------------
ICONS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,6 12,13 2,6"/>',
    "map-pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "menu": '<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>',
    "x": '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
    "check": '<polyline points="20 6 9 17 4 12"/>',
    "check-circle": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    "arrow-right": '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
    "home": '<path d="M3 9.5 12 2l9 7.5"/><path d="M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10"/>',
    "layers": '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "clipboard": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>',
    "tool": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.4-3.4a6 6 0 0 1-8 8L4.7 20.3a2.1 2.1 0 0 1-3-3L8.1 10.9a6 6 0 0 1 8-8l-3.4 3.4z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M8.21 13.89 7 23l5-3 5 3-1.21-9.12"/>',
    "compass": '<circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>',
    "ruler": '<path d="M21.3 15.3 15.3 21.3a1 1 0 0 1-1.4 0L2.7 10.1a1 1 0 0 1 0-1.4l6-6a1 1 0 0 1 1.4 0L21.3 13.9a1 1 0 0 1 0 1.4z"/><path d="m7.5 10.5 2 2"/><path d="m10.5 7.5 2 2"/><path d="m13.5 4.5 2 2"/>',
    "file-text": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="16" y2="17"/>',
    "trending-up": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    "camera": '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    "search": '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
    "send": '<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "chevron-right": '<polyline points="9 18 15 12 9 6"/>',
    "whatsapp": '<path d="M20.52 3.48A11.86 11.86 0 0 0 12.04 0C5.5 0 .16 5.34.16 11.88c0 2.1.55 4.14 1.6 5.95L0 24l6.33-1.66a11.87 11.87 0 0 0 5.7 1.45h.01c6.54 0 11.88-5.34 11.88-11.88 0-3.17-1.23-6.15-3.4-8.43zM12.04 21.6a9.7 9.7 0 0 1-4.95-1.36l-.35-.21-3.75.98 1-3.66-.23-.38a9.7 9.7 0 0 1-1.49-5.19c0-5.37 4.37-9.74 9.78-9.74 2.61 0 5.07 1.02 6.92 2.87a9.7 9.7 0 0 1 2.86 6.9c0 5.37-4.37 9.79-9.79 9.79zm5.36-7.33c-.29-.15-1.73-.85-2-.95-.27-.1-.46-.15-.66.15-.2.29-.76.95-.93 1.15-.17.19-.34.22-.63.07-.29-.15-1.23-.45-2.34-1.44-.87-.77-1.45-1.72-1.62-2.01-.17-.29-.02-.45.13-.6.13-.13.29-.34.44-.51.15-.17.19-.29.29-.49.1-.19.05-.36-.02-.51-.07-.15-.66-1.59-.9-2.17-.24-.57-.48-.5-.66-.51h-.56c-.19 0-.51.07-.78.36-.27.29-1.02 1-1.02 2.43s1.05 2.82 1.19 3.02c.15.19 2.06 3.15 5 4.42.7.3 1.24.48 1.67.62.7.22 1.34.19 1.84.12.56-.08 1.73-.71 1.98-1.39.24-.68.24-1.27.17-1.39-.07-.12-.26-.19-.55-.34z"/>',
}


def icon(name, size=22, cls=""):
    body = ICONS.get(name, "")
    fill = "currentColor" if name == "whatsapp" else "none"
    stroke_attrs = "" if name == "whatsapp" else ' stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    return (f'<svg class="icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" '
            f'fill="{fill}"{stroke_attrs} aria-hidden="true">{body}</svg>')


# ----------------------------------------------------------------------------
# DONNEES DE CONTACT (placeholders — à remplacer par les informations
# officielles de PACAM lors de la phase de contenu)
# ----------------------------------------------------------------------------
DOMAIN = "https://pacamci.com"
PHONE_DISPLAY = "+225 07 00 00 00 00"
PHONE_TEL = "+22507000000"
WHATSAPP_TEL = "22507000000"
EMAIL = "contact@pacamci.com"
ADDRESS = "Abidjan, Côte d'Ivoire"
HOURS = "Lun – Sam : 8h00 – 18h00"

NAV = [
    ("a-propos.html", "À propos"),
    ("services.html", "Nos services"),
    ("terrains-biens.html", "Terrains & Biens"),
    ("projets.html", "Projets"),
    ("realisations.html", "Nos réalisations"),
    ("accompagnement.html", "Accompagnement"),
]
# "Accueil" est retiré du menu : le logo y renvoie déjà.
# "Contact" est retiré du menu : le bouton "Nous contacter" du header suffit
# (éviter un lien + un bouton qui mènent au même endroit).

POLES = [
    ("immobilier-foncier", "Immobilier & Foncier", "home",
     ["Vente de terrains", "Vente de maisons", "Visite de terrains", "Gestion immobilière",
      "Accompagnement à l'achat", "Services ACD & documentation sur parcelles"]),
    ("amenagement-lotissement", "Aménagement & Lotissement", "layers",
     ["Lotissement", "Aménagement foncier", "Ouverture des voies",
      "Décapage de parcelles", "Reprofilage des voies"]),
    ("etudes-conception", "Études & Conception", "clipboard",
     ["Étude de projets de construction", "Conception de plans 2D",
      "Conception de plans 3D", "Élaboration de devis"]),
    ("construction-rehabilitation", "Construction & Réhabilitation", "tool",
     ["Construction de bâtiments", "Réhabilitation de bâtiments",
      "Charpentes métalliques", "Montage et suivi de permis de construire"]),
]

TERRAINS = [
    dict(ref="TR-0142", titre="Terrain résidentiel — Zone A", loc="Zone A, périphérie ville", surf="500 m²", prix="15 000 000 FCFA", grad="g1"),
    dict(ref="TR-0158", titre="Terrain viabilisé — Zone B", loc="Zone B, quartier résidentiel", surf="800 m²", prix="25 000 000 FCFA", grad="g2"),
    dict(ref="TR-0163", titre="Terrain agricole — Zone périphérique", loc="Zone périphérique", surf="2 000 m²", prix="Prix sur demande", grad="g3"),
    dict(ref="TR-0171", titre="Terrain constructible", loc="Quartier résidentiel calme", surf="600 m²", prix="18 000 000 FCFA", grad="g4"),
    dict(ref="TR-0179", titre="Terrain d'angle — Zone commerciale", loc="Zone commerciale", surf="450 m²", prix="20 000 000 FCFA", grad="g1"),
    dict(ref="TR-0185", titre="Terrain loti — Nouveau lotissement", loc="Lotissement Les Jardins", surf="700 m²", prix="22 000 000 FCFA", grad="g2"),
]

MAISONS = [
    dict(ref="MA-0210", titre="Villa moderne 4 pièces", loc="Quartier résidentiel", surf="250 m²", prix="65 000 000 FCFA", grad="g3"),
    dict(ref="MA-0224", titre="Maison familiale 3 chambres", loc="Zone calme, proche commodités", surf="180 m²", prix="45 000 000 FCFA", grad="g4"),
    dict(ref="MA-0231", titre="Duplex contemporain", loc="Quartier résidentiel", surf="220 m²", prix="58 000 000 FCFA", grad="g1"),
    dict(ref="MA-0239", titre="Maison à rénover", loc="Centre-ville", surf="150 m²", prix="Prix sur demande", grad="g2"),
]

PROJETS = [
    dict(nom="Lotissement Les Jardins", loc="Périphérie Nord", etat="En cours",
         desc="Programme de lotissement résidentiel avec voirie et viabilisation en cours de réalisation.", grad="g1", icon="layers"),
    dict(nom="Aménagement foncier — Zone Nord", loc="Zone Nord", etat="En cours",
         desc="Décapage, reprofilage et ouverture des voies pour la préparation d'un nouvel espace constructible.", grad="g2", icon="compass"),
    dict(nom="Résidence Les Palmiers", loc="Quartier résidentiel", etat="Planifié",
         desc="Projet immobilier résidentiel comprenant plusieurs unités d'habitation modernes.", grad="g3", icon="home"),
    dict(nom="Ouverture de voies — Secteur Est", loc="Secteur Est", etat="Terminé",
         desc="Travaux d'ouverture et de reprofilage des voies d'accès pour un ensemble de parcelles.", grad="g4", icon="target"),
]

REALISATIONS = [
    dict(cat="Construction", titre="Immeuble R+2", loc="Centre-ville", grad="g1", icon="home"),
    dict(cat="Construction", titre="Villa duplex", loc="Quartier résidentiel", grad="g2", icon="home"),
    dict(cat="Réhabilitation", titre="Bâtiment administratif", loc="Zone administrative", grad="g3", icon="tool"),
    dict(cat="Charpentes métalliques", titre="Hangar industriel", loc="Zone industrielle", grad="g4", icon="layers"),
    dict(cat="Lotissement & aménagement", titre="Ouverture de voies — Zone C", loc="Zone C", grad="g1", icon="compass"),
    dict(cat="Construction", titre="Résidence familiale", loc="Quartier calme", grad="g2", icon="home"),
]

VALEURS = [
    ("shield", "Professionnalisme", "Un accompagnement rigoureux, du premier contact à la remise des clés."),
    ("check-circle", "Confiance", "Des engagements clairs et un suivi transparent à chaque étape."),
    ("target", "Sérieux", "Des projets menés avec méthode, dans le respect des délais annoncés."),
    ("layers", "Stabilité", "Une entreprise ancrée sur son marché, aux côtés de ses clients dans la durée."),
    ("award", "Expertise", "Une maîtrise des métiers de l'immobilier, du foncier et de la construction."),
    ("users", "Proximité", "Une équipe à l'écoute, disponible par téléphone, WhatsApp ou en agence."),
]

PARCOURS = [
    ("target", "Je veux acheter un terrain",
     ["Consulter les terrains disponibles", "Consulter les informations sur un terrain",
      "Demander une visite", "Contacter PACAM pour poursuivre la démarche"],
     "terrains-biens.html", "Découvrir les terrains"),
    ("home", "Je veux acheter une maison",
     ["Consulter les maisons disponibles", "Consulter les détails du bien",
      "Demander des informations", "Organiser une visite"],
     "terrains-biens.html#maisons", "Voir les maisons"),
    ("shield", "Je veux confier la gestion de mon bien à PACAM",
     ["Présenter le bien à gérer", "Recherche et sélection de locataires",
      "Suivi locatif et encaissement des loyers", "Entretien et suivi régulier du bien"],
     "contact.html?demande=gestion-immobiliere", "Demander une gestion"),
    ("tool", "Je veux construire",
     ["Présenter mon projet", "Demander une étude", "Obtenir une conception de plans",
      "Demander un devis", "Être accompagné dans les démarches"],
     "accompagnement.html", "Présenter mon projet"),
    ("layers", "Je veux aménager un terrain",
     ["Lotissement", "Aménagement foncier", "Ouverture des voies",
      "Décapage", "Reprofilage"],
     "services.html#amenagement-lotissement", "Voir ce service"),
    ("clipboard", "J'ai besoin d'un accompagnement foncier",
     ["Services ACD", "Documentation sur parcelles", "Démarches liées à mon terrain"],
     "contact.html?demande=accompagnement-foncier", "Demander un accompagnement"),
]

ETAPES = [
    ("1", "Définition du besoin", "Le client présente son projet à l'équipe PACAM."),
    ("2", "Étude", "PACAM analyse le besoin et les caractéristiques du projet."),
    ("3", "Conception", "Lorsque nécessaire, le projet fait l'objet d'une étude et de plans 2D ou 3D."),
    ("4", "Devis", "Un devis est établi selon la nature et l'ampleur du projet."),
    ("5", "Démarches", "PACAM accompagne le client dans les démarches, notamment le permis de construire et la documentation foncière."),
    ("6", "Réalisation", "Le projet est ensuite réalisé selon les prestations convenues."),
]


# ----------------------------------------------------------------------------
# CSS
# ----------------------------------------------------------------------------
CSS = """
:root{
  --orange:#E8720C;
  --orange-dark:#C4590A;
  --charcoal:#26262a;
  --charcoal-2:#1a1a1d;
  --sky:#1CADE4;
  --gold:#F5A623;
  --bg:#FAFAF7;
  --gray-100:#F2F1EE;
  --gray-200:#E7E5E0;
  --gray-500:#8a8a86;
  --gray-600:#5c5c58;
  --white:#ffffff;
  --radius:14px;
  --shadow:0 10px 30px rgba(38,38,42,.08);
  --shadow-lg:0 20px 45px rgba(38,38,42,.14);
  --maxw:1180px;
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  margin:0;
  font-family:'Inter',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  color:var(--charcoal);
  background:var(--bg);
  line-height:1.6;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3,h4{
  font-family:'Poppins',system-ui,sans-serif;
  line-height:1.22;
  margin:0 0 .5em;
  font-weight:600;
  color:var(--charcoal-2);
}
p{margin:0 0 1em;color:var(--gray-600);}
a{color:inherit;text-decoration:none;}
img{max-width:100%;display:block;}
ul{margin:0;padding:0;list-style:none;}
.container{max-width:var(--maxw);margin:0 auto;padding:0 24px;}
.icon{flex-shrink:0;}

/* ---------- Bandeau maquette ---------- */
.demo-banner{
  background:var(--charcoal-2);
  color:var(--gold);
  text-align:center;
  font-size:.8rem;
  letter-spacing:.02em;
  padding:8px 16px;
}
.demo-banner strong{color:#fff;}

/* ---------- Topbar ---------- */
.topbar{
  background:var(--charcoal);
  color:#d8d8d6;
  font-size:.82rem;
}
.topbar .container{
  display:flex;justify-content:space-between;align-items:center;
  padding-top:8px;padding-bottom:8px;flex-wrap:wrap;gap:8px;
}
.topbar-links{display:flex;gap:20px;flex-wrap:wrap;}
.topbar-links a{display:flex;align-items:center;gap:6px;color:#e9e9e7;transition:color .2s;}
.topbar-links a:hover{color:var(--gold);}
.topbar-hours{display:flex;align-items:center;gap:6px;color:#b7b7b3;}

/* ---------- Header / nav ---------- */
header.site-header{
  background:#fff;
  position:sticky;top:0;z-index:50;
  box-shadow:0 2px 14px rgba(0,0,0,.06);
}
.nav-wrap{display:flex;align-items:center;justify-content:space-between;padding:10px 24px;gap:20px;}
.brand{display:flex;align-items:center;gap:10px;}
.brand img{height:52px;width:auto;}
.brand-text{display:flex;flex-direction:column;line-height:1.1;}
.brand-text .name{font-family:'Poppins',sans-serif;font-weight:700;font-size:1.15rem;color:var(--charcoal-2);letter-spacing:.02em;}
.brand-text .tag{font-size:.68rem;color:var(--gold);font-weight:600;letter-spacing:.03em;text-transform:uppercase;}
nav.main-nav{display:flex;align-items:center;gap:6px;}
nav.main-nav a{
  padding:10px 14px;border-radius:8px;font-weight:500;font-size:.92rem;color:var(--charcoal);
  transition:background .2s,color .2s;
}
nav.main-nav a:hover{background:var(--gray-100);color:var(--orange);}
nav.main-nav a.active{color:var(--orange);font-weight:600;}
.header-cta{display:flex;align-items:center;gap:12px;}
.brand.is-home .name{color:var(--orange);}
.menu-toggle{display:none;background:none;border:none;cursor:pointer;padding:8px;color:var(--charcoal-2);}

/* ---------- Buttons ---------- */
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:8px;
  padding:13px 26px;border-radius:10px;font-weight:600;font-size:.94rem;
  cursor:pointer;border:2px solid transparent;transition:transform .15s,box-shadow .15s,background .2s,color .2s;
  white-space:nowrap;
}
.btn:active{transform:translateY(1px);}
.btn-primary{background:var(--orange);color:#fff;box-shadow:0 8px 20px rgba(232,114,12,.32);}
.btn-primary:hover{background:var(--orange-dark);box-shadow:0 10px 26px rgba(232,114,12,.4);}
.btn-secondary{background:#fff;color:var(--charcoal-2);border-color:var(--gray-200);}
.btn-secondary:hover{border-color:var(--orange);color:var(--orange);}
.btn-outline-light{background:transparent;color:#fff;border-color:rgba(255,255,255,.55);}
.btn-outline-light:hover{background:rgba(255,255,255,.12);border-color:#fff;}
.btn-light{background:#fff;color:var(--charcoal-2);}
.btn-light:hover{background:var(--gold);color:#fff;}
.btn-whatsapp{background:#25D366;color:#fff;}
.btn-whatsapp:hover{background:#1eb958;}
.btn-block{width:100%;}
.btn-sm{padding:9px 16px;font-size:.85rem;}

/* ---------- Hero ---------- */
.hero{
  position:relative;color:#fff;overflow:hidden;
  background:linear-gradient(120deg,var(--charcoal-2) 0%,#3a2c1f 45%,var(--orange-dark) 100%);
}
.hero::before{
  content:"";position:absolute;inset:0;
  background:
    radial-gradient(circle at 85% 20%, rgba(28,173,228,.35), transparent 45%),
    radial-gradient(circle at 15% 85%, rgba(245,166,35,.28), transparent 50%);
}
.hero-inner{position:relative;padding:100px 24px 90px;max-width:var(--maxw);margin:0 auto;}
.hero.hero-sm .hero-inner{padding:64px 24px;}
.eyebrow{
  display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);
  border:1px solid rgba(255,255,255,.25);padding:6px 14px;border-radius:999px;
  font-size:.78rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase;margin-bottom:20px;color:var(--gold);
}
.hero h1{color:#fff;font-size:2.6rem;max-width:820px;margin-bottom:18px;}
.hero .lead{color:#e9e6df;font-size:1.12rem;max-width:640px;margin-bottom:32px;}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;}
.breadcrumb{position:relative;font-size:.85rem;color:#e9e6df;display:flex;gap:8px;align-items:center;margin-bottom:14px;}
.breadcrumb a{color:#fff;opacity:.8;}
.breadcrumb a:hover{opacity:1;}

/* ---------- Sections ---------- */
section{padding:76px 0;}
section.tight{padding:56px 0;}
.section-head{max-width:680px;margin:0 auto 44px;text-align:center;}
.section-head.left{margin:0 0 40px;text-align:left;}
.kicker{color:var(--orange);font-weight:700;font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px;display:block;}
.section-head h2{font-size:2rem;}
.bg-alt{background:var(--gray-100);}
.bg-dark{background:var(--charcoal-2);color:#eee;}
.bg-dark h2,.bg-dark h3,.bg-dark h4{color:#fff;}
.bg-dark p{color:#c9c8c3;}

/* ---------- Grids & Cards ---------- */
.grid{display:grid;gap:26px;}
.grid-2{grid-template-columns:repeat(2,1fr);}
.grid-3{grid-template-columns:repeat(3,1fr);}
.grid-4{grid-template-columns:repeat(4,1fr);}

.card{
  background:#fff;border-radius:var(--radius);box-shadow:var(--shadow);
  transition:transform .2s,box-shadow .2s;overflow:hidden;
}
.card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);}

.icon-card{padding:30px 26px;}
.icon-badge{
  width:52px;height:52px;border-radius:12px;display:flex;align-items:center;justify-content:center;
  background:linear-gradient(135deg,var(--orange),var(--gold));color:#fff;margin-bottom:18px;
}
.icon-badge.blue{background:linear-gradient(135deg,var(--sky),#2b7fb0);}
.icon-card h3{font-size:1.1rem;margin-bottom:10px;}
.icon-card ul{margin-top:14px;display:flex;flex-direction:column;gap:9px;}
.icon-card ul li{display:flex;gap:9px;font-size:.9rem;color:var(--gray-600);align-items:flex-start;}
.icon-card ul li .icon{color:var(--orange);margin-top:3px;}
.icon-card .card-link{display:inline-flex;align-items:center;gap:6px;color:var(--orange);font-weight:600;font-size:.88rem;margin-top:18px;}

/* photo placeholder (gradient) */
.photo{
  aspect-ratio:4/3;border-radius:0;position:relative;display:flex;align-items:center;justify-content:center;
  color:rgba(255,255,255,.92);overflow:hidden;
}
.photo .icon{width:38%;height:38%;opacity:.9;}
.photo .photo-tag{
  position:absolute;top:12px;left:12px;background:rgba(0,0,0,.35);backdrop-filter:blur(2px);
  padding:4px 10px;border-radius:999px;font-size:.68rem;font-weight:600;letter-spacing:.03em;text-transform:uppercase;
}
.g1{background:linear-gradient(135deg,#E8720C,#F5A623);}
.g2{background:linear-gradient(135deg,#1CADE4,#0d6c8f);}
.g3{background:linear-gradient(135deg,#2b2b2e,#5a4632);}
.g4{background:linear-gradient(135deg,#8a5a1f,#E8720C);}

/* property card */
.prop-card{display:flex;flex-direction:column;}
.prop-body{padding:20px 22px 22px;flex:1;display:flex;flex-direction:column;}
.prop-ref{font-size:.72rem;color:var(--gray-500);font-weight:600;letter-spacing:.04em;text-transform:uppercase;margin-bottom:6px;}
.prop-body h3{font-size:1.08rem;margin-bottom:8px;}
.prop-meta{display:flex;gap:14px;flex-wrap:wrap;font-size:.85rem;color:var(--gray-600);margin-bottom:14px;}
.prop-meta span{display:flex;align-items:center;gap:5px;}
.prop-meta .icon{color:var(--orange);}
.prop-price{font-family:'Poppins',sans-serif;font-weight:700;color:var(--charcoal-2);font-size:1.15rem;margin-bottom:16px;}
.prop-actions{display:flex;gap:10px;margin-top:auto;flex-wrap:wrap;}

/* project card */
.proj-card{padding:0;}
.proj-body{padding:22px;}
.badge{display:inline-block;padding:4px 12px;border-radius:999px;font-size:.72rem;font-weight:700;letter-spacing:.02em;}
.badge-cours{background:#FFF1DE;color:var(--orange-dark);}
.badge-planifie{background:#E5F5FB;color:#0d6c8f;}
.badge-termine{background:#E7F6EC;color:#1c7a3f;}

/* realisation card */
.real-card{position:relative;}
.real-card .photo{aspect-ratio:1/1;}
.real-cat{position:absolute;bottom:12px;left:12px;color:#fff;}
.real-cat .cat{font-size:.7rem;text-transform:uppercase;letter-spacing:.05em;opacity:.85;}
.real-cat h4{color:#fff;margin:2px 0 0;font-size:1.02rem;}

/* value / process */
.values-grid .icon-card{text-align:left;}
.process-steps{display:flex;flex-direction:column;gap:0;counter-reset:step;}
.step{display:flex;gap:22px;position:relative;padding-bottom:38px;}
.step:last-child{padding-bottom:0;}
.step-num{
  flex-shrink:0;width:46px;height:46px;border-radius:50%;background:var(--orange);color:#fff;
  display:flex;align-items:center;justify-content:center;font-family:'Poppins',sans-serif;font-weight:700;
  position:relative;z-index:1;
}
.step:not(:last-child)::before{
  content:"";position:absolute;left:23px;top:46px;bottom:0;width:2px;background:var(--gray-200);
}
.step-content h4{margin-bottom:6px;font-size:1.05rem;}
.step-content p{margin-bottom:0;}

/* funnel arrow line (accueil "comment PACAM vous accompagne") */
.mini-flow{display:flex;align-items:center;flex-wrap:wrap;gap:10px;justify-content:center;}
.mini-flow .pill{background:#fff;border:1px solid var(--gray-200);padding:10px 18px;border-radius:999px;font-weight:600;font-size:.9rem;box-shadow:var(--shadow);}
.mini-flow .arrow{color:var(--orange);}

/* parcours cards (home) */
.parcours-card{padding:28px 24px;display:flex;flex-direction:column;height:100%;}
.parcours-card h3{font-size:1.05rem;margin-bottom:12px;}
.parcours-card ul{display:flex;flex-direction:column;gap:8px;margin-bottom:20px;}
.parcours-card ul li{font-size:.87rem;color:var(--gray-600);display:flex;gap:8px;}
.parcours-card ul li::before{content:"→";color:var(--orange);font-weight:700;}
.parcours-card .btn{margin-top:auto;}

/* CTA band */
.cta-band{
  background:linear-gradient(120deg,var(--orange) 0%,var(--orange-dark) 100%);
  color:#fff;border-radius:20px;padding:56px 44px;text-align:center;
  position:relative;overflow:hidden;
}
.cta-band h2{color:#fff;}
.cta-band p{color:rgba(255,255,255,.9);}
.cta-band .hero-actions{justify-content:center;}

/* forms */
.form-card{background:#fff;border-radius:var(--radius);box-shadow:var(--shadow-lg);padding:36px;}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:18px;}
.form-group{margin-bottom:18px;display:flex;flex-direction:column;gap:7px;}
.form-group label{font-size:.85rem;font-weight:600;color:var(--charcoal-2);}
.form-group .req{color:var(--orange);}
input,select,textarea{
  font-family:inherit;font-size:.94rem;padding:12px 14px;border-radius:9px;border:1.5px solid var(--gray-200);
  background:#fcfcfb;color:var(--charcoal-2);transition:border-color .2s,box-shadow .2s;width:100%;
}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--orange);box-shadow:0 0 0 3px rgba(232,114,12,.14);}
textarea{resize:vertical;min-height:110px;}
.form-note{font-size:.8rem;color:var(--gray-500);margin-top:10px;}

/* contact page info cards */
.contact-info{display:flex;flex-direction:column;gap:16px;}
.contact-info .info-item{display:flex;gap:16px;align-items:flex-start;background:#fff;border-radius:var(--radius);padding:20px;box-shadow:var(--shadow);}
.contact-info .info-item .icon-badge{margin-bottom:0;flex-shrink:0;}
.info-item h4{margin-bottom:4px;font-size:.98rem;}
.info-item p{margin:0;font-size:.9rem;}
.map-box{
  border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);
  height:220px;background:linear-gradient(135deg,#dfe7ea,#c7d2d6);position:relative;
  display:flex;align-items:center;justify-content:center;color:#5a6a70;
}

/* fiche détail bien */
.detail-gallery{display:grid;grid-template-columns:2fr 1fr;gap:10px;border-radius:var(--radius);overflow:hidden;}
.detail-gallery .photo.main{aspect-ratio:auto;height:100%;min-height:340px;}
.detail-thumbs{display:grid;grid-template-rows:1fr 1fr;gap:10px;}
.detail-thumbs .photo{aspect-ratio:auto;height:100%;}
.spec-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:22px 0;}
.spec-item{background:#fff;border-radius:10px;padding:16px;box-shadow:var(--shadow);}
.spec-item .label{font-size:.72rem;color:var(--gray-500);text-transform:uppercase;letter-spacing:.03em;margin-bottom:4px;}
.spec-item .value{font-weight:700;font-family:'Poppins',sans-serif;color:var(--charcoal-2);}

/* footer */
footer.site-footer{background:var(--charcoal-2);color:#c9c8c3;padding-top:64px;}
.footer-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.2fr;gap:40px;padding-bottom:44px;border-bottom:1px solid rgba(255,255,255,.08);}
.footer-brand{display:flex;align-items:center;gap:10px;margin-bottom:16px;}
.footer-brand img{height:48px;}
.footer-brand .name{color:#fff;font-family:'Poppins',sans-serif;font-weight:700;font-size:1.1rem;}
footer h4{color:#fff;font-size:.95rem;margin-bottom:18px;}
footer ul{display:flex;flex-direction:column;gap:11px;}
footer ul li a{font-size:.88rem;color:#b7b7b3;transition:color .2s;display:flex;align-items:center;gap:8px;}
footer ul li a:hover{color:var(--gold);}
.footer-bottom{padding:22px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;font-size:.8rem;color:#8f8f8b;}
.socials{display:flex;gap:10px;}
.socials a{width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center;color:#fff;transition:background .2s;}
.socials a:hover{background:var(--orange);}

/* floating whatsapp */
.wa-float{
  position:fixed;bottom:24px;right:24px;z-index:60;
  width:60px;height:60px;border-radius:50%;background:#25D366;color:#fff;
  display:flex;align-items:center;justify-content:center;box-shadow:0 10px 26px rgba(37,211,102,.45);
  transition:transform .2s;
}
.wa-float:hover{transform:scale(1.08);}

/* filter tabs */
.filter-tabs{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:34px;}
.filter-tabs button{
  padding:10px 20px;border-radius:999px;border:1.5px solid var(--gray-200);background:#fff;
  font-weight:600;font-size:.87rem;cursor:pointer;transition:all .2s;color:var(--charcoal-2);
}
.filter-tabs button.active,.filter-tabs button:hover{background:var(--orange);border-color:var(--orange);color:#fff;}

/* reveal animation */
.reveal{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease;}
.reveal.in{opacity:1;transform:none;}

/* misc */
.divider-flow{display:flex;flex-direction:column;align-items:center;gap:4px;color:var(--orange);margin:2px 0;}
.two-col{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center;}
.two-col.rev{grid-template-columns:.9fr 1.1fr;}
.two-col.rev .two-col-media{order:2;}
.badge-pill{display:inline-flex;align-items:center;gap:8px;background:var(--gray-100);color:var(--orange-dark);padding:7px 16px;border-radius:999px;font-size:.8rem;font-weight:700;margin-bottom:16px;}
.check-list{display:flex;flex-direction:column;gap:12px;margin:18px 0;}
.check-list li{display:flex;gap:10px;align-items:flex-start;font-size:.94rem;color:var(--charcoal-2);}
.check-list li .icon{color:var(--orange);margin-top:2px;}
.stat-row{display:flex;gap:36px;margin-top:28px;flex-wrap:wrap;}
.stat{display:flex;flex-direction:column;}
.stat b{font-family:'Poppins',sans-serif;font-size:1.7rem;color:var(--charcoal-2);}
.stat span{font-size:.8rem;color:var(--gray-500);}
.toast{
  position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(20px);
  background:var(--charcoal-2);color:#fff;padding:14px 22px;border-radius:10px;font-size:.9rem;
  box-shadow:var(--shadow-lg);opacity:0;pointer-events:none;transition:all .3s;z-index:80;display:flex;align-items:center;gap:10px;
}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0);}
.toast .icon{color:#4ade80;}

/* responsive */
@media(max-width:980px){
  .grid-4{grid-template-columns:repeat(2,1fr);}
  .grid-3{grid-template-columns:repeat(2,1fr);}
  .footer-grid{grid-template-columns:1fr 1fr;}
  .two-col,.two-col.rev{grid-template-columns:1fr;}
  .two-col.rev .two-col-media{order:0;}
  .detail-gallery{grid-template-columns:1fr;}
}
@media(max-width:760px){
  .topbar .topbar-hours{display:none;}
  nav.main-nav{
    position:fixed;top:0;right:-100%;height:100vh;width:78%;max-width:320px;background:#fff;
    flex-direction:column;align-items:flex-start;padding:90px 26px 26px;box-shadow:-10px 0 30px rgba(0,0,0,.12);
    transition:right .3s ease;gap:2px;
  }
  nav.main-nav.open{right:0;}
  nav.main-nav a{width:100%;padding:13px 10px;border-bottom:1px solid var(--gray-100);border-radius:0;}
  .menu-toggle{display:block;}
  .grid-2,.grid-3,.grid-4{grid-template-columns:1fr;}
  .footer-grid{grid-template-columns:1fr;}
  .hero h1{font-size:1.9rem;}
  .form-row{grid-template-columns:1fr;}
  .spec-grid{grid-template-columns:1fr;}
  section{padding:52px 0;}
  .cta-band{padding:40px 22px;}
}
"""

JS = """
document.addEventListener('DOMContentLoaded', function () {
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
"""


def page_shell(title, description, active, hero, body, extra_head=""):
    nav_parts = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        nav_parts.append(f'<a href="{href}"{cls}>{label}</a>')
    nav_html = "\n".join(nav_parts)
    brand_cls = ' class="brand is-home"' if active == "index.html" else ' class="brand"'
    canonical = f"{DOMAIN}/{active}" if active != "index.html" else f"{DOMAIN}/"
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | PACAM — Services Immobilier &amp; Foncier</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="PACAM">
<meta property="og:title" content="{title} | PACAM">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#E8720C">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
{extra_head}
</head>
<body>

<div class="demo-banner">🏗️ <strong>Aperçu exclusif</strong> — Maquette du futur site PACAM, réalisée sur la base de votre cahier des charges. Contenus &amp; coordonnées à titre d'exemple.</div>

<div class="topbar">
  <div class="container">
    <div class="topbar-links">
      <a href="tel:{PHONE_TEL}">{icon('phone',15)} {PHONE_DISPLAY}</a>
      <a href="https://wa.me/{WHATSAPP_TEL}" target="_blank" rel="noopener">{icon('whatsapp',15)} WhatsApp</a>
      <a href="mailto:{EMAIL}">{icon('mail',15)} {EMAIL}</a>
    </div>
    <div class="topbar-hours">{icon('clock',15)} {HOURS}</div>
  </div>
</div>

<header class="site-header">
  <div class="nav-wrap">
    <a{brand_cls} href="index.html">
      <img src="images/logo-light.jpg" alt="Logo PACAM">
      <span class="brand-text"><span class="name">PACAM</span><span class="tag">Services Immobilier &amp; Foncier</span></span>
    </a>
    <nav class="main-nav">
      {nav_html}
    </nav>
    <div class="header-cta">
      <a class="btn btn-primary btn-sm" href="contact.html">Nous contacter</a>
      <button class="menu-toggle" aria-label="Ouvrir le menu">{icon('menu',26)}</button>
    </div>
  </div>
</header>

{hero}

<main>
{body}
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="images/logo-dark.jpg" alt="Logo PACAM">
          <span class="name">PACAM</span>
        </div>
        <p>PACAM accompagne ses clients de leur besoin à la réalisation de leur projet : immobilier, foncier, aménagement, études, conception et construction.</p>
        <div class="socials">
          <a href="#" aria-label="Facebook">f</a>
          <a href="#" aria-label="Instagram">in</a>
          <a href="#" aria-label="LinkedIn">li</a>
        </div>
      </div>
      <div>
        <h4>Navigation</h4>
        <ul>
          <li><a href="index.html">Accueil</a></li>
          <li><a href="a-propos.html">À propos</a></li>
          <li><a href="services.html">Nos services</a></li>
          <li><a href="terrains-biens.html">Terrains &amp; Biens</a></li>
          <li><a href="projets.html">Projets</a></li>
          <li><a href="realisations.html">Nos réalisations</a></li>
        </ul>
      </div>
      <div>
        <h4>Nos pôles</h4>
        <ul>
          <li><a href="services.html#immobilier-foncier">Immobilier &amp; Foncier</a></li>
          <li><a href="services.html#amenagement-lotissement">Aménagement &amp; Lotissement</a></li>
          <li><a href="services.html#etudes-conception">Études &amp; Conception</a></li>
          <li><a href="services.html#construction-rehabilitation">Construction &amp; Réhabilitation</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{icon('phone',16)} {PHONE_DISPLAY}</a></li>
          <li><a href="https://wa.me/{WHATSAPP_TEL}" target="_blank" rel="noopener">{icon('whatsapp',16)} WhatsApp</a></li>
          <li><a href="mailto:{EMAIL}">{icon('mail',16)} {EMAIL}</a></li>
          <li><a href="contact.html">{icon('map-pin',16)} {ADDRESS}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 PACAM — Services Immobilier &amp; Foncier. Tous droits réservés. <a href="{DOMAIN}/" style="color:#c9c8c3;">www.pacamci.com</a></span>
      <span>Maquette réalisée pour PACAM — contenus à personnaliser.</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="https://wa.me/{WHATSAPP_TEL}" target="_blank" rel="noopener" aria-label="Contacter PACAM sur WhatsApp">{icon('whatsapp',30)}</a>

<div class="toast">{icon('check-circle',18)}<span></span></div>

<script src="js/script.js"></script>
</body>
</html>
"""


def hero_block(eyebrow, title, lead, actions, breadcrumb=None, small=False):
    crumb = ""
    if breadcrumb:
        crumb = f'<div class="breadcrumb"><a href="index.html">Accueil</a> {icon("chevron-right",14)} <span>{breadcrumb}</span></div>'
    cls = "hero hero-sm" if small else "hero"
    return f"""<section class="{cls}">
  <div class="hero-inner">
    {crumb}
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    <div class="hero-actions">{actions}</div>
  </div>
</section>"""


def photo_block(gradient, icon_name, label, tag=None):
    tag_html = f'<span class="photo-tag">{tag}</span>' if tag else ""
    return f'<div class="photo {gradient}">{tag_html}{icon(icon_name, 64)}</div>'


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("écrit:", path)


# écriture CSS / JS
write("css/style.css", CSS)
write("js/script.js", JS)

print("Assets de base générés. Génération des pages...")


# ----------------------------------------------------------------------------
# COMPOSANTS REUTILISABLES
# ----------------------------------------------------------------------------
def prop_card(p, kind="terrain"):
    action_visite = f"contact.html?demande=demander-une-visite&bien={p['ref']}"
    detail = f"bien-detail.html?ref={p['ref']}" if p["ref"] == "TR-0142" else f"bien-detail.html?ref={p['ref']}"
    return f"""<div class="card prop-card reveal" data-cat="{kind}">
  {photo_block(p['grad'], 'home' if kind=='maison' else 'map-pin', p['titre'], tag='Maison' if kind=='maison' else 'Terrain')}
  <div class="prop-body">
    <div class="prop-ref">Réf. {p['ref']}</div>
    <h3>{p['titre']}</h3>
    <div class="prop-meta">
      <span>{icon('map-pin',15)} {p['loc']}</span>
      <span>{icon('ruler',15)} {p['surf']}</span>
    </div>
    <div class="prop-price">{p['prix']}</div>
    <div class="prop-actions">
      <a class="btn btn-secondary btn-sm" href="{detail}">Voir les détails</a>
      <a class="btn btn-primary btn-sm" href="{action_visite}">Demander une visite</a>
    </div>
  </div>
</div>"""


def project_card(p):
    badge_cls = {"En cours": "badge-cours", "Planifié": "badge-planifie", "Terminé": "badge-termine"}[p["etat"]]
    return f"""<div class="card proj-card reveal">
  {photo_block(p['grad'], p['icon'], p['nom'])}
  <div class="proj-body">
    <span class="badge {badge_cls}">{p['etat']}</span>
    <h3 style="margin-top:12px;">{p['nom']}</h3>
    <div class="prop-meta" style="margin-bottom:12px;"><span>{icon('map-pin',15)} {p['loc']}</span></div>
    <p>{p['desc']}</p>
    <a class="btn btn-secondary btn-sm" href="contact.html?demande=projet">En savoir plus</a>
  </div>
</div>"""


def real_card(r):
    slug = r["cat"].lower().replace(" & ", "-").replace(" ", "-").replace("é", "e")
    return f"""<div class="card real-card reveal" data-cat="{slug}">
  <div class="photo {r['grad']}">
    {icon(r['icon'], 64)}
    <div class="real-cat"><span class="cat">{r['cat']}</span><h4>{r['titre']}</h4></div>
  </div>
</div>"""


def pole_card(anchor, title, icon_name, items):
    lis = "\n".join(f'<li>{icon("check",15)} {i}</li>' for i in items)
    return f"""<div class="card icon-card reveal" id="{anchor}">
  <div class="icon-badge">{icon(icon_name, 26)}</div>
  <h3>{title}</h3>
  <ul>{lis}</ul>
  <a class="card-link" href="contact.html?demande={anchor}">Demander ce service {icon('arrow-right',15)}</a>
</div>"""


def value_card(icon_name, title, text):
    return f"""<div class="card icon-card reveal">
  <div class="icon-badge blue">{icon(icon_name, 24)}</div>
  <h3>{title}</h3>
  <p>{text}</p>
</div>"""


def parcours_card(icon_name, title, items, link, cta):
    lis = "\n".join(f"<li>{i}</li>" for i in items)
    return f"""<div class="card parcours-card reveal">
  <div class="icon-badge">{icon(icon_name, 24)}</div>
  <h3>{title}</h3>
  <ul>{lis}</ul>
  <a class="btn btn-secondary btn-block" href="{link}">{cta} {icon('arrow-right',15)}</a>
</div>"""


TOAST_FORM_HEAD = ""  # (kept for clarity; toast markup lives in page_shell)


# ----------------------------------------------------------------------------
# PAGE : ACCUEIL
# ----------------------------------------------------------------------------
def page_index():
    hero = f"""<section class="hero">
  <div class="hero-inner">
    <span class="eyebrow">{icon('shield',15)} Immobilier · Foncier · Construction</span>
    <h1>Votre partenaire de confiance pour l'immobilier, le foncier et la construction</h1>
    <p class="lead">De l'achat d'un terrain à la réalisation de votre bâtiment, PACAM vous accompagne à chaque étape de votre projet, avec sérieux et professionnalisme.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="terrains-biens.html">{icon('map-pin',18)} Découvrir nos terrains</a>
      <a class="btn btn-outline-light" href="accompagnement.html">Présenter mon projet</a>
      <a class="btn btn-outline-light" href="contact.html">Nous contacter</a>
    </div>
    <div class="stat-row">
      <div class="stat"><b>4</b><span>pôles de compétences</span></div>
      <div class="stat"><b>100%</b><span>accompagnement du besoin à la livraison</span></div>
      <div class="stat"><b>24/7</b><span>contact WhatsApp &amp; téléphone</span></div>
    </div>
  </div>
</section>"""

    parcours_html = "\n".join(parcours_card(*p) for p in PARCOURS)
    poles_html = "\n".join(pole_card(*p) for p in POLES)
    terrains_preview = "\n".join(prop_card(p, "terrain") for p in TERRAINS[:3])
    real_preview = "\n".join(real_card(r) for r in REALISATIONS[:4])

    body = f"""
<section class="tight">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Que souhaitez-vous faire ?</span>
      <h2>Dites-nous votre besoin, nous vous montrons le chemin</h2>
      <p>Choisissez le parcours qui correspond à votre projet : PACAM vous guide, étape par étape, jusqu'à la réalisation.</p>
    </div>
    <div class="grid grid-3">{parcours_html}</div>
  </div>
</section>

<section class="bg-alt">
  <div class="container two-col">
    <div class="reveal">
      <span class="badge-pill">{icon('award',15)} Qui sommes-nous</span>
      <h2>PACAM, l'expertise immobilière, foncière et de construction à votre service</h2>
      <p>PACAM accompagne particuliers et porteurs de projets dans l'acquisition de terrains et de maisons, l'aménagement de parcelles, les études et la conception de plans, ainsi que la construction et la réhabilitation de bâtiments.</p>
      <ul class="check-list">
        <li>{icon('check-circle',18)} Une équipe qui vous accompagne du besoin à la réalisation</li>
        <li>{icon('check-circle',18)} Des opportunités foncières et immobilières régulièrement mises à jour</li>
        <li>{icon('check-circle',18)} Un savoir-faire reconnu en études, conception et construction</li>
      </ul>
      <a class="btn btn-primary" href="a-propos.html">En savoir plus sur PACAM {icon('arrow-right',18)}</a>
    </div>
    <div class="reveal">{photo_block('g3', 'shield', 'PACAM')}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Nos domaines d'expertise</span>
      <h2>Quatre pôles pour vous accompagner à chaque étape</h2>
      <p>Immobilier, aménagement, études et construction : PACAM réunit toutes les compétences nécessaires à la réussite de votre projet.</p>
    </div>
    <div class="grid grid-4">{poles_html}</div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head left reveal" style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:16px;">
      <div>
        <span class="kicker">Opportunités immobilières</span>
        <h2 style="margin-bottom:0;">Une sélection de terrains et biens disponibles</h2>
      </div>
      <a class="btn btn-secondary" href="terrains-biens.html">Voir tout le catalogue {icon('arrow-right',16)}</a>
    </div>
    <div class="grid grid-3">{terrains_preview}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head left reveal" style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:16px;">
      <div>
        <span class="kicker">Nos réalisations</span>
        <h2 style="margin-bottom:0;">Un savoir-faire qui parle de lui-même</h2>
      </div>
      <a class="btn btn-secondary" href="realisations.html">Voir toutes nos réalisations {icon('arrow-right',16)}</a>
    </div>
    <div class="grid grid-4">{real_preview}</div>
  </div>
</section>

<section class="bg-dark">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker" style="color:var(--gold);">Notre méthode</span>
      <h2>Comment PACAM vous accompagne</h2>
      <p>Un parcours clair, du premier échange jusqu'à la réalisation de votre projet.</p>
    </div>
    <div class="mini-flow reveal">
      <span class="pill">Votre besoin</span><span class="arrow">{icon('arrow-right',20)}</span>
      <span class="pill">Étude</span><span class="arrow">{icon('arrow-right',20)}</span>
      <span class="pill">Accompagnement</span><span class="arrow">{icon('arrow-right',20)}</span>
      <span class="pill">Réalisation</span>
    </div>
    <div style="text-align:center;margin-top:32px;">
      <a class="btn btn-primary" href="accompagnement.html">Découvrir notre accompagnement {icon('arrow-right',18)}</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band reveal">
      <h2>Un projet en tête ? Parlons-en dès aujourd'hui.</h2>
      <p>Achat de terrain, construction, aménagement ou accompagnement foncier : notre équipe est à votre écoute.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="contact.html">{icon('send',18)} Présenter mon projet</a>
        <a class="btn btn-outline-light" href="tel:{PHONE_TEL}">{icon('phone',18)} Appeler PACAM</a>
      </div>
    </div>
  </div>
</section>
"""
    return page_shell(
        "Accueil", "Site vitrine et commercial de PACAM — immobilier, foncier, aménagement et construction.",
        "index.html", hero, body,
    )


# ----------------------------------------------------------------------------
# PAGE : A PROPOS
# ----------------------------------------------------------------------------
def page_a_propos():
    hero = hero_block(
        "À propos de PACAM", "Un partenaire de confiance pour vos projets immobiliers et fonciers",
        "Découvrez qui nous sommes, notre vision, nos valeurs et notre savoir-faire au service de vos projets.",
        f'<a class="btn btn-primary" href="services.html">Découvrir nos services {icon("arrow-right",18)}</a>'
        f'<a class="btn btn-outline-light" href="contact.html">Nous contacter</a>',
        breadcrumb="À propos", small=True,
    )
    valeurs_html = "\n".join(value_card(*v) for v in VALEURS)
    body = f"""
<section>
  <div class="container two-col">
    <div class="reveal">
      <span class="badge-pill">{icon('target',15)} Notre identité</span>
      <h2>PACAM, une entreprise dédiée à l'immobilier, au foncier et à la construction</h2>
      <p>PACAM accompagne ses clients dans l'ensemble de leurs démarches immobilières et foncières : achat de terrains et de maisons, aménagement et lotissement, études et conception de projets, construction et réhabilitation de bâtiments.</p>
      <p>Notre mission est simple : permettre à chaque client de passer de son besoin à la réalisation concrète de son projet, avec un accompagnement clair à chaque étape.</p>
    </div>
    <div class="reveal">{photo_block('g1', 'target', 'Notre identité')}</div>
  </div>
</section>

<section class="bg-alt">
  <div class="container two-col rev">
    <div class="two-col-media reveal">{photo_block('g2', 'compass', 'Notre vision')}</div>
    <div class="reveal">
      <span class="badge-pill">{icon('compass',15)} Notre vision</span>
      <h2>Devenir un acteur de référence de l'immobilier et du foncier</h2>
      <p>Nous voulons offrir à nos clients une expérience simple et rassurante, où chaque étape — de la découverte d'un terrain jusqu'à la remise des clés — est accompagnée avec sérieux, transparence et expertise.</p>
      <ul class="check-list">
        <li>{icon('check-circle',18)} Une présence durable auprès de nos clients</li>
        <li>{icon('check-circle',18)} Un catalogue d'opportunités foncières et immobilières évolutif</li>
        <li>{icon('check-circle',18)} Une capacité à intervenir sur l'ensemble de la chaîne de valeur du projet</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Nos valeurs</span>
      <h2>Ce qui guide chacune de nos interventions</h2>
    </div>
    <div class="grid grid-3 values-grid">{valeurs_html}</div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Nos domaines d'intervention</span>
      <h2>Quatre pôles de compétences complémentaires</h2>
    </div>
    <div class="grid grid-4">
      {"".join(f'<div class="card icon-card reveal"><div class="icon-badge">{icon(i,26)}</div><h3>{t}</h3><a class="card-link" href="services.html#{a}">Découvrir {icon("arrow-right",15)}</a></div>' for a,t,i,_ in POLES)}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band reveal">
      <h2>Faisons connaissance autour de votre projet</h2>
      <p>Parlez-nous de votre besoin : notre équipe vous propose l'accompagnement le plus adapté.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="contact.html">Nous contacter {icon('arrow-right',18)}</a>
      </div>
    </div>
  </div>
</section>
"""
    return page_shell(
        "À propos", "Identité, vision, valeurs et savoir-faire de PACAM, votre partenaire immobilier et foncier.",
        "a-propos.html", hero, body,
    )


# ----------------------------------------------------------------------------
# PAGE : SERVICES
# ----------------------------------------------------------------------------
def page_services():
    hero = hero_block(
        "Nos services", "Une offre complète, de l'idée à la réalisation",
        "Immobilier &amp; foncier, aménagement &amp; lotissement, études &amp; conception, construction &amp; réhabilitation : découvrez l'ensemble de nos prestations.",
        f'<a class="btn btn-primary" href="contact.html">Demander un devis {icon("send",18)}</a>',
        breadcrumb="Nos services", small=True,
    )
    sections = []
    for anchor, title, icon_name, items in POLES:
        rows = "\n".join(
            f"""<li class="reveal">
        <div class="icon-badge" style="width:40px;height:40px;">{icon('check',18)}</div>
        <div>
          <h4 style="margin-bottom:4px;">{item}</h4>
        </div>
      </li>"""
            for item in items
        )
        sections.append(f"""
<section id="{anchor}">
  <div class="container two-col">
    <div class="reveal">
      <span class="badge-pill">{icon(icon_name,15)} Pôle de compétence</span>
      <h2>{title}</h2>
      <ul class="check-list">
        {''.join(f'<li>{icon("check-circle",18)} {i}</li>' for i in items)}
      </ul>
      <a class="btn btn-primary" href="contact.html?demande={anchor}">Demander ce service {icon('send',18)}</a>
    </div>
    <div class="reveal">{photo_block('g' + str((POLES.index((anchor,title,icon_name,items))%4)+1), icon_name, title)}</div>
  </div>
</section>""")
    body = "\n".join(sections) + f"""
<section class="bg-dark">
  <div class="container">
    <div class="cta-band reveal" style="background:linear-gradient(120deg,var(--sky),#0d6c8f);">
      <h2>Un besoin qui combine plusieurs services ?</h2>
      <p>PACAM coordonne l'ensemble de vos prestations, de l'étude jusqu'à la réalisation.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="accompagnement.html">Découvrir notre accompagnement {icon('arrow-right',18)}</a>
      </div>
    </div>
  </div>
</section>
"""
    return page_shell(
        "Nos services", "Immobilier, aménagement, études et construction : découvrez l'ensemble des services PACAM.",
        "services.html", hero, body,
    )


# ----------------------------------------------------------------------------
# PAGE : TERRAINS & BIENS
# ----------------------------------------------------------------------------
def page_terrains_biens():
    hero = hero_block(
        "Terrains & Biens", "Découvrez les opportunités foncières et immobilières de PACAM",
        "Terrains constructibles, viabilisés ou agricoles, maisons à vendre : consultez nos biens disponibles et demandez une visite en quelques clics.",
        f'<a class="btn btn-primary" href="#catalogue">Voir le catalogue {icon("arrow-right",18)}</a>'
        f'<a class="btn btn-outline-light" href="contact.html">Demander une visite</a>',
        breadcrumb="Terrains & Biens", small=True,
    )
    all_props = "\n".join(prop_card(p, "terrain") for p in TERRAINS) + "\n" + "\n".join(prop_card(p, "maison") for p in MAISONS)
    body = f"""
<section id="catalogue">
  <div class="container">
    <div class="section-head left reveal">
      <span class="kicker">Catalogue</span>
      <h2>Nos terrains et biens disponibles</h2>
      <p>Ce catalogue est amené à évoluer régulièrement. Contactez-nous pour connaître les dernières disponibilités et opportunités non encore publiées.</p>
    </div>
    <div class="filter-tabs" data-target="#catalogue .prop-card">
      <button class="active" data-filter="all">Tous les biens</button>
      <button data-filter="terrain">Terrains</button>
      <button data-filter="maison" id="maisons">Maisons</button>
    </div>
    <div class="grid grid-3">{all_props}</div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-band reveal">
      <h2>Vous ne trouvez pas le bien qui correspond à votre besoin ?</h2>
      <p>Décrivez-nous votre recherche : nous vous accompagnons pour trouver le terrain ou la maison adaptée à votre projet.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="contact.html?demande=recherche-bien">Décrire ma recherche {icon('send',18)}</a>
      </div>
    </div>
  </div>
</section>
"""
    return page_shell(
        "Terrains & Biens", "Consultez les terrains et maisons disponibles à la vente chez PACAM.",
        "terrains-biens.html", hero, body,
    )


# ----------------------------------------------------------------------------
# PAGE : FICHE DETAIL D'UN BIEN (exemple)
# ----------------------------------------------------------------------------
def page_bien_detail():
    p = TERRAINS[0]
    import json as _json
    all_biens = {}
    for item in TERRAINS:
        all_biens[item["ref"]] = dict(item, kind="Terrain", tag="Terrain")
    for item in MAISONS:
        all_biens[item["ref"]] = dict(item, kind="Maison", tag="Maison")
    biens_json = _json.dumps(all_biens, ensure_ascii=False)

    hero = f"""<section class="hero hero-sm">
  <div class="hero-inner">
    <div class="breadcrumb"><a href="index.html">Accueil</a> {icon("chevron-right",14)} <a href="terrains-biens.html">Terrains &amp; Biens</a> {icon("chevron-right",14)} <span id="bd-crumb">{p['titre']}</span></div>
    <span class="eyebrow" id="bd-eyebrow">{icon('map-pin',15)} Terrain à vendre</span>
    <h1 id="bd-title">{p['titre']}</h1>
    <p class="lead" id="bd-sub">Référence {p['ref']} — {p['loc']}</p>
  </div>
</section>"""

    body = f"""
<section>
  <div class="container">
    <a href="terrains-biens.html" style="display:inline-flex;align-items:center;gap:6px;color:var(--orange);font-weight:600;margin-bottom:24px;"><span style="display:inline-block;transform:scaleX(-1);">{icon('arrow-right',16)}</span> Retour au catalogue</a>
    <div class="two-col" style="align-items:flex-start;">
      <div class="reveal">
        <div class="detail-gallery">
          <div class="photo main {p['grad']}" id="bd-photo-main"><span class="photo-tag" id="bd-photo-tag">Photo principale</span>{icon('map-pin', 64)}</div>
          <div class="detail-thumbs">
            {photo_block('g2', 'camera', 'Vue 2')}
            {photo_block('g3', 'camera', 'Vue 3')}
          </div>
        </div>
        <div class="spec-grid">
          <div class="spec-item"><div class="label">Superficie</div><div class="value" id="bd-surf">{p['surf']}</div></div>
          <div class="spec-item"><div class="label">Prix</div><div class="value" id="bd-prix">{p['prix']}</div></div>
          <div class="spec-item"><div class="label">Référence</div><div class="value" id="bd-ref">{p['ref']}</div></div>
          <div class="spec-item"><div class="label">Localisation</div><div class="value" id="bd-loc">{p['loc']}</div></div>
        </div>
        <h3>Description</h3>
        <p id="bd-desc">Terrain bien situé, idéal pour un projet résidentiel. Accès facile, environnement calme et en développement. Documents et informations complémentaires disponibles sur demande auprès de notre équipe.</p>
        <h3>Caractéristiques</h3>
        <ul class="check-list">
          <li>{icon('check-circle',18)} Bien prêt pour votre projet</li>
          <li>{icon('check-circle',18)} Accès direct à une voie praticable</li>
          <li>{icon('check-circle',18)} Proche des commodités essentielles</li>
          <li>{icon('check-circle',18)} Documentation foncière disponible sur demande</li>
        </ul>
      </div>
      <div class="reveal">
        <div class="form-card">
          <h3>Demander une visite</h3>
          <p style="font-size:.88rem;">Bien concerné : <strong id="bd-form-label">{p['titre']} ({p['ref']})</strong></p>
          <form data-demo-form>
            <div class="form-group"><label>Nom &amp; prénom <span class="req">*</span></label><input type="text" name="nom" required></div>
            <div class="form-group"><label>Téléphone <span class="req">*</span></label><input type="tel" name="telephone" required></div>
            <input type="hidden" name="bien_concerne" id="bd-form-ref" value="{p['ref']}">
            <div class="form-group"><label>Disponibilités</label><input type="text" name="disponibilites" placeholder="Ex : semaine prochaine, matin"></div>
            <div class="form-group"><label>Message</label><textarea name="message" placeholder="Précisez votre demande..."></textarea></div>
            <button class="btn btn-primary btn-block" type="submit">{icon('send',18)} Envoyer ma demande de visite</button>
          </form>
          <p class="form-note">Ou contactez-nous directement au {PHONE_DISPLAY} / WhatsApp.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<script>
  var PACAM_BIENS = {biens_json};
  (function () {{
    var ref = new URLSearchParams(window.location.search).get('ref');
    var b = ref && PACAM_BIENS[ref];
    if (!b) return;
    document.title = b.titre + " | PACAM — Services Immobilier & Foncier";
    document.getElementById('bd-crumb').textContent = b.titre;
    document.getElementById('bd-eyebrow').innerHTML = document.getElementById('bd-eyebrow').innerHTML.replace(/Terrain à vendre|Maison à vendre/, b.kind + ' à vendre');
    document.getElementById('bd-title').textContent = b.titre;
    document.getElementById('bd-sub').textContent = 'Référence ' + b.ref + ' — ' + b.loc;
    document.getElementById('bd-photo-tag').textContent = b.tag;
    document.getElementById('bd-surf').textContent = b.surf;
    document.getElementById('bd-prix').textContent = b.prix;
    document.getElementById('bd-ref').textContent = b.ref;
    document.getElementById('bd-loc').textContent = b.loc;
    document.getElementById('bd-form-label').textContent = b.titre + ' (' + b.ref + ')';
    document.getElementById('bd-form-ref').value = b.ref;
    var photo = document.getElementById('bd-photo-main');
    photo.classList.remove('g1','g2','g3','g4');
    photo.classList.add(b.grad);
  }})();
</script>
"""
    return page_shell(
        f"{p['titre']}", f"Fiche détaillée du terrain {p['ref']} proposé par PACAM.",
        "terrains-biens.html", hero, body,
    )


# ----------------------------------------------------------------------------
# PAGE : PROJETS
# ----------------------------------------------------------------------------
def page_projets():
    hero = hero_block(
        "Projets", "Les projets développés ou accompagnés par PACAM",
        "Lotissements, aménagements fonciers, projets immobiliers : découvrez les initiatives portées par PACAM sur son territoire d'intervention.",
        f'<a class="btn btn-primary" href="contact.html?demande=projet">Contacter PACAM {icon("arrow-right",18)}</a>',
        breadcrumb="Projets", small=True,
    )
    projets_html = "\n".join(project_card(p) for p in PROJETS)
    body = f"""
<section>
  <div class="container">
    <div class="section-head left reveal">
      <span class="kicker">Nos projets</span>
      <h2>Des initiatives concrètes, au service du territoire</h2>
    </div>
    <div class="grid grid-2">{projets_html}</div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-band reveal">
      <h2>Un projet à nous présenter ?</h2>
      <p>Lotissement, aménagement foncier, projet immobilier : partagez-nous les grandes lignes de votre projet.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="accompagnement.html">Présenter mon projet {icon('arrow-right',18)}</a>
      </div>
    </div>
  </div>
</section>
"""
    return page_shell(
        "Projets", "Découvrez les projets de lotissement, aménagement foncier et immobilier portés par PACAM.",
        "projets.html", hero, body,
    )


# ----------------------------------------------------------------------------
# PAGE : NOS REALISATIONS
# ----------------------------------------------------------------------------
def page_realisations():
    hero = hero_block(
        "Nos réalisations", "Notre savoir-faire, démontré par nos réalisations",
        "Construction, réhabilitation, charpentes métalliques, lotissement et aménagement : un aperçu concret des travaux réalisés par PACAM.",
        "", breadcrumb="Nos réalisations", small=True,
    )
    cats = ["Construction", "Réhabilitation", "Charpentes métalliques", "Lotissement & aménagement"]
    tabs = '<button class="active" data-filter="all">Tout</button>' + "".join(
        f'<button data-filter="{c.lower().replace(" & ","-").replace(" ","-").replace("é","e")}">{c}</button>' for c in cats
    )
    cards = "\n".join(real_card(r) for r in REALISATIONS)
    body = f"""
<section>
  <div class="container">
    <div class="filter-tabs" data-target="#gallery .real-card">{tabs}</div>
    <div class="grid grid-4" id="gallery">{cards}</div>
  </div>
</section>

<section class="bg-alt">
  <div class="container">
    <div class="cta-band reveal">
      <h2>Envie d'un résultat similaire pour votre projet ?</h2>
      <p>Parlons de votre besoin : construction, réhabilitation, charpente ou aménagement.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="contact.html">Discuter de mon projet {icon('arrow-right',18)}</a>
      </div>
    </div>
  </div>
</section>
"""
    return page_shell(
        "Nos réalisations", "Découvrez les réalisations de PACAM en construction, réhabilitation et aménagement.",
        "realisations.html", hero, body,
    )


# ----------------------------------------------------------------------------
# PAGE : ACCOMPAGNEMENT
# ----------------------------------------------------------------------------
def page_accompagnement():
    hero = hero_block(
        "Accompagnement", "PACAM vous accompagne à chaque étape de votre projet",
        "Du besoin exprimé jusqu'à la réalisation, découvrez notre méthode de travail et présentez-nous votre projet.",
        f'<a class="btn btn-primary" href="#presenter">Présenter mon projet {icon("arrow-right",18)}</a>',
        breadcrumb="Accompagnement", small=True,
    )
    steps_html = "\n".join(
        f"""<div class="step reveal">
      <div class="step-num">{n}</div>
      <div class="step-content"><h4>{t}</h4><p>{d}</p></div>
    </div>""" for n, t, d in ETAPES
    )
    body = f"""
<section>
  <div class="container two-col">
    <div class="reveal">
      <span class="badge-pill">{icon('compass',15)} Notre méthode</span>
      <h2>Un parcours structuré, de votre besoin à la réalisation</h2>
      <p>Quelle que soit l'ampleur de votre projet, PACAM vous accompagne étape par étape, avec la possibilité d'intervenir dès la définition du besoin ou plus tard dans le parcours.</p>
    </div>
    <div class="reveal process-steps">{steps_html}</div>
  </div>
</section>

<section class="bg-dark" id="presenter">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker" style="color:var(--gold);">Étape 1</span>
      <h2>Présentez-nous votre projet</h2>
      <p>Renseignez ce formulaire : notre équipe reviendra vers vous rapidement pour échanger sur votre besoin.</p>
    </div>
    <div class="form-card reveal" style="max-width:720px;margin:0 auto;">
      <form data-demo-form>
        <div class="form-row">
          <div class="form-group"><label>Nom &amp; prénom <span class="req">*</span></label><input type="text" name="nom" required></div>
          <div class="form-group"><label>Téléphone <span class="req">*</span></label><input type="tel" name="telephone" required></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label>Type de projet <span class="req">*</span></label>
            <select name="type_projet" required>
              <option value="">Sélectionnez...</option>
              <option>Construction</option>
              <option>Réhabilitation</option>
              <option>Lotissement / aménagement</option>
              <option>Étude &amp; conception</option>
              <option>Autre</option>
            </select>
          </div>
          <div class="form-group"><label>Localisation</label><input type="text" name="localisation" placeholder="Ville, quartier..."></div>
        </div>
        <div class="form-group"><label>Description du projet <span class="req">*</span></label><textarea name="description" required placeholder="Décrivez votre projet en quelques lignes..."></textarea></div>
        <div class="form-row">
          <div class="form-group"><label>Budget indicatif</label><input type="text" name="budget" placeholder="Facultatif"></div>
          <div class="form-group"><label>Document à joindre</label><input type="file" name="document"></div>
        </div>
        <button class="btn btn-primary btn-block" type="submit">{icon('send',18)} Envoyer mon projet</button>
        <p class="form-note" style="color:#c9c8c3;">Vos informations sont utilisées uniquement pour le traitement de votre demande par PACAM.</p>
      </form>
    </div>
  </div>
</section>
"""
    return page_shell(
        "Accompagnement", "Découvrez comment PACAM accompagne ses clients du besoin à la réalisation du projet.",
        "accompagnement.html", hero, body,
    )


# ----------------------------------------------------------------------------
# PAGE : CONTACT
# ----------------------------------------------------------------------------
def page_contact():
    hero = hero_block(
        "Contact", "Parlons de votre projet",
        "Par téléphone, WhatsApp, email ou via le formulaire ci-dessous : PACAM vous répond rapidement.",
        "", breadcrumb="Contact", small=True,
    )
    body = f"""
<section>
  <div class="container two-col" style="align-items:flex-start;">
    <div class="reveal">
      <span class="badge-pill">{icon('phone',15)} Nous joindre</span>
      <h2>Toutes les façons de contacter PACAM</h2>
      <div class="contact-info" style="margin-top:24px;">
        <div class="info-item">
          <div class="icon-badge">{icon('phone',22)}</div>
          <div><h4>Téléphone</h4><p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p></div>
        </div>
        <div class="info-item">
          <div class="icon-badge" style="background:linear-gradient(135deg,#25D366,#128C7E);">{icon('whatsapp',22)}</div>
          <div><h4>WhatsApp</h4><p><a href="https://wa.me/{WHATSAPP_TEL}" target="_blank" rel="noopener">Discuter sur WhatsApp</a></p></div>
        </div>
        <div class="info-item">
          <div class="icon-badge blue">{icon('mail',22)}</div>
          <div><h4>Email</h4><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
        </div>
        <div class="info-item">
          <div class="icon-badge">{icon('map-pin',22)}</div>
          <div><h4>Adresse</h4><p>{ADDRESS}</p></div>
        </div>
        <div class="info-item">
          <div class="icon-badge blue">{icon('clock',22)}</div>
          <div><h4>Horaires d'ouverture</h4><p>{HOURS}</p></div>
        </div>
      </div>
      <div class="map-box" style="margin-top:24px;">{icon('map-pin',40)}<span style="margin-left:10px;">Carte de localisation — à intégrer</span></div>
    </div>

    <div class="reveal">
      <div class="form-card">
        <h3>Formulaire de contact</h3>
        <form data-demo-form>
          <div class="form-row">
            <div class="form-group"><label>Nom &amp; prénom <span class="req">*</span></label><input type="text" name="nom" required></div>
            <div class="form-group"><label>Téléphone <span class="req">*</span></label><input type="tel" name="telephone" required></div>
          </div>
          <div class="form-row">
            <div class="form-group"><label>Email</label><input type="email" name="email"></div>
            <div class="form-group"><label>Localité</label><input type="text" name="localite"></div>
          </div>
          <div class="form-group">
            <label>Type de demande <span class="req">*</span></label>
            <select name="type_demande" required>
              <option value="">Sélectionnez...</option>
              <option value="acheter-terrain">Acheter un terrain</option>
              <option value="acheter-maison">Acheter une maison</option>
              <option value="gestion-immobiliere">Confier la gestion de mon bien</option>
              <option value="demander-une-visite">Demander une visite</option>
              <option value="projet">Réaliser un projet de construction</option>
              <option value="etude">Demander une étude</option>
              <option value="plans">Obtenir un plan 2D ou 3D</option>
              <option value="devis">Demander un devis</option>
              <option value="amenagement-lotissement">Lotissement / aménagement foncier</option>
              <option value="permis">Accompagnement permis de construire</option>
              <option value="accompagnement-foncier">Accompagnement ACD / documentation foncière</option>
              <option value="autre">Autre demande</option>
            </select>
          </div>
          <input type="hidden" name="bien_concerne">
          <div class="form-group"><label>Message <span class="req">*</span></label><textarea name="message" required placeholder="Décrivez votre demande..."></textarea></div>
          <button class="btn btn-primary btn-block" type="submit">{icon('send',18)} Envoyer ma demande</button>
        </form>
      </div>
    </div>
  </div>
</section>
"""
    return page_shell(
        "Contact", "Contactez PACAM par téléphone, WhatsApp, email ou via le formulaire de contact en ligne.",
        "contact.html", hero, body,
    )


# ----------------------------------------------------------------------------
# GENERATION
# ----------------------------------------------------------------------------
PAGES = {
    "index.html": page_index,
    "a-propos.html": page_a_propos,
    "services.html": page_services,
    "terrains-biens.html": page_terrains_biens,
    "bien-detail.html": page_bien_detail,
    "projets.html": page_projets,
    "realisations.html": page_realisations,
    "accompagnement.html": page_accompagnement,
    "contact.html": page_contact,
}

for fname, fn in PAGES.items():
    write(fname, fn())

print("\\nTerminé :", len(PAGES), "pages générées.")
