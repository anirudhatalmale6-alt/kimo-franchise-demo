# -*- coding: utf-8 -*-
"""La feuille de style de KIMO.

Ce n'est pas le site noir. Le site de prestige vend une adresse a un
proprietaire d'hotel ; celui-ci s'adresse a quelqu'un qui va confier son
enfant, et a quelqu'un qui va y engager ses economies. Fond creme, vert
profond, un abricot pour les appels a l'action, des angles arrondis et de
grandes tailles de texte.

RIEN N'EST CACHE SANS JAVASCRIPT. Il n'y a volontairement aucune animation
d'apparition ici : pas de `opacity:0` pose a l'aveugle, donc pas de page
blanche si le script tombe. Les seuls elements qui bougent sont les blocs
de reponse de la FAQ, et ils utilisent <details>, qui s'ouvre sans script.
"""

CSS = """
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:#fbf7f0;color:#16211d;
  font:400 17px/1.65 ui-sans-serif,system-ui,"Segoe UI",Roboto,Helvetica,Arial,
  sans-serif;-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}
a{color:#2f6b52}
h1,h2,h3{line-height:1.15;margin:0;font-weight:650;letter-spacing:-.015em}
h1{font-size:clamp(32px,5.2vw,58px)}
h2{font-size:clamp(25px,3.4vw,38px)}
h3{font-size:19px}
p{margin:0}
.enveloppe{max-width:1120px;margin:0 auto;padding:0 22px}

/* ------------------------------------------------------------- en-tete --- */
.haut{position:sticky;top:0;z-index:40;background:rgba(251,247,240,.94);
  backdrop-filter:blur(9px);border-bottom:1px solid #e6ddcd}
.haut-in{max-width:1120px;margin:0 auto;padding:12px 22px;display:flex;
  align-items:center;gap:20px}
.marque{display:flex;align-items:center;gap:9px;text-decoration:none;
  color:#16211d;font-weight:700;font-size:21px;letter-spacing:.02em}
.marque .mot{white-space:nowrap}
.diamant{width:20px;height:20px;flex:none;fill:none;stroke:#2f6b52;
  stroke-width:1.35;stroke-linejoin:round}
.nav{display:flex;gap:20px;margin-left:auto;flex-wrap:wrap}
.nav a{text-decoration:none;color:#4b5a53;font-size:15px;padding:5px 0;
  border-bottom:2px solid transparent}
.nav a:hover{color:#16211d}
.nav a[aria-current="page"]{color:#16211d;border-bottom-color:#e08a5b}
/* Le selecteur de langue est fait de deux LIENS : la langue est celle de la
   page (/ et /en/), pas un etat que garde un script. La langue courante est
   un <span>, pas un lien mort vers soi-meme. */
.langue{display:flex;border:1px solid #d9cfbc;border-radius:999px;
  overflow:hidden;flex:none}
.langue a,.langue span{font-size:13px;font-weight:600;padding:5px 12px;
  text-decoration:none;color:#6b7a72;line-height:1.6}
.langue a:hover{background:#efe6d6;color:#16211d}
.langue span[aria-current]{background:#2f6b52;color:#fff}

/* ---------------------------------------------------------------- hero --- */
.hero{padding:74px 0 58px;background:
  radial-gradient(120% 90% at 88% 0%,#efe6d6 0%,rgba(239,230,214,0) 62%)}
.hero-in{display:grid;grid-template-columns:1.25fr .75fr;gap:46px;
  align-items:center}
.surtitre{font-size:13px;letter-spacing:.16em;text-transform:uppercase;
  color:#2f6b52;font-weight:700;margin-bottom:16px}
.hero h1{max-width:15ch}
.chapo{margin-top:20px;font-size:19px;color:#41504a;max-width:52ch}
.actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.bouton{display:inline-block;text-decoration:none;font-weight:650;
  font-size:16px;padding:13px 24px;border-radius:999px;border:1px solid
  transparent}
.bouton.plein{background:#e08a5b;color:#231007}
.bouton.plein:hover{background:#d67d4c}
.bouton.vide{border-color:#c9bda6;color:#16211d}
.bouton.vide:hover{border-color:#2f6b52}

/* l'etat du reseau : un encart, pas un compteur. Il n'y a rien a compter. */
.etat{background:#fff;border:1px solid #e6ddcd;border-radius:18px;
  padding:24px}
.etat h3{font-size:15px;letter-spacing:.1em;text-transform:uppercase;
  color:#6b7a72}
.etat ul{list-style:none;margin:14px 0 0;padding:0;display:grid;gap:11px}
.etat li{display:flex;gap:10px;align-items:flex-start;font-size:15px;
  color:#41504a}
.etat li::before{content:"";width:7px;height:7px;border-radius:50%;
  background:#e08a5b;margin-top:8px;flex:none}

/* -------------------------------------------------------------- blocs --- */
section{padding:66px 0}
section.pale{background:#f5eee2}
.titre-bloc{max-width:60ch;margin-bottom:38px}
.titre-bloc p{margin-top:14px;color:#4b5a53;font-size:18px}
.grille{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.carte{background:#fff;border:1px solid #e6ddcd;border-radius:18px;
  padding:26px}
.carte h3{margin-bottom:10px}
.carte p{color:#4b5a53;font-size:16px}
.pale .carte{background:#fbf7f0}

/* la pastille « a definir » — elle doit se voir, c'est tout son interet */
.tbc{display:inline-flex;align-items:center;gap:6px;background:#fdf0e6;
  border:1px dashed #e08a5b;color:#a2512a;border-radius:999px;
  padding:2px 11px;font-size:13px;font-weight:650;letter-spacing:.01em;
  white-space:nowrap}
.tbc::before{content:"";width:6px;height:6px;border-radius:50%;
  background:#e08a5b;flex:none}
.note{margin-top:12px;font-size:15px;color:#6b7a72}

/* ----------------------------------------------------------- tableaux --- */
.tab{width:100%;border-collapse:collapse;background:#fff;
  border:1px solid #e6ddcd;border-radius:18px;overflow:hidden}
.enrouleur{overflow-x:auto;-webkit-overflow-scrolling:touch}
.tab th,.tab td{text-align:left;padding:16px 18px;border-bottom:1px solid
  #efe7d9;vertical-align:top;font-size:16px}
.tab tr:last-child td{border-bottom:0}
.tab th{width:32%;font-weight:650;color:#16211d}
.tab td.val{width:20%;white-space:nowrap}
.tab td.exp{color:#4b5a53;font-size:15px}

/* ----------------------------------------------------------- parcours --- */
.etapes{counter-reset:e;display:grid;gap:2px}
.etape{display:grid;grid-template-columns:64px 1fr;gap:20px;
  background:#fff;border:1px solid #e6ddcd;padding:24px}
.etape:first-child{border-radius:18px 18px 0 0}
.etape:last-child{border-radius:0 0 18px 18px}
.etape .num{font-size:26px;font-weight:700;color:#c9bda6;line-height:1.1}
.etape h3{margin-bottom:8px}
.etape p{color:#4b5a53;font-size:16px}

/* --------------------------------------------------------- deux listes --- */
.listes{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.liste{background:#fff;border:1px solid #e6ddcd;border-radius:18px;
  padding:26px}
.liste.accent{background:#2f6b52;border-color:#2f6b52;color:#fff}
.liste.accent h3{color:#fff}
.liste.accent li{color:#dbe8e1}
.liste.accent li::before{background:#e08a5b}
.liste ul{list-style:none;margin:16px 0 0;padding:0;display:grid;gap:12px}
.liste li{display:flex;gap:11px;align-items:flex-start;font-size:16px;
  color:#41504a}
.liste li::before{content:"";width:7px;height:7px;border-radius:50%;
  background:#2f6b52;margin-top:9px;flex:none}

/* --------------------------------------------------------- simulateur --- */
.simu{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:start}
.champs{background:#fff;border:1px solid #e6ddcd;border-radius:18px;
  padding:26px;display:grid;gap:16px}
.champ{display:grid;gap:6px}
.champ label{font-size:15px;font-weight:600;color:#41504a}
.champ input,.champ select,.form select,.form input,.form textarea{
  font:inherit;font-size:16px;padding:11px 13px;border:1px solid #d9cfbc;
  border-radius:11px;background:#fbf7f0;color:#16211d;width:100%}
.champ input:focus,.champ select:focus,.form input:focus,.form select:focus,
.form textarea:focus{outline:2px solid #2f6b52;outline-offset:1px}
.sortie{background:#16211d;color:#fff;border-radius:18px;padding:26px}
.sortie h3{color:#fff;font-size:15px;letter-spacing:.1em;
  text-transform:uppercase}
.sortie dl{margin:18px 0 0;display:grid;gap:0}
.sortie .ligne{display:flex;justify-content:space-between;gap:16px;
  padding:12px 0;border-bottom:1px solid #2c3a34;font-size:16px}
.sortie .ligne:last-child{border-bottom:0}
.sortie dt{color:#a9bab2}
.sortie dd{margin:0;font-variant-numeric:tabular-nums;font-weight:650}
.sortie .fort{font-size:20px}
.sortie .fort dd{color:#8fd6b0}
.sortie .neg dd{color:#ffab8f}
.sortie .rappel{margin-top:18px;font-size:14px;color:#a9bab2}

/* ------------------------------------------------------------ methode --- */
.pastille-titre{display:flex;align-items:center;gap:12px;flex-wrap:wrap}

/* ----------------------------------------------------------- signature --- */
/* « KIMO — Learn to Think. » La mention de traduction est posee A COTE, pas
   dessous : dessous, elle se lit comme une partie de la signature. */
.signature{display:flex;align-items:center;gap:14px;flex-wrap:wrap;
  margin-top:18px;font-size:19px;font-weight:650;color:#2f6b52;
  letter-spacing:.01em}

/* ------------------------------------------------- listes autonomes --- */
/* Les listes de sa note restent des listes. Sur une pleine largeur elles
   passent en deux colonnes, mais chaque puce reste insecable : une puce
   coupee en deux colonnes se lit comme deux puces. */
.liste.large{background:#fff;border:1px solid #e6ddcd;border-radius:18px;
  padding:26px 30px;max-width:none}
/* display:block est OBLIGATOIRE ici : la regle generale .liste ul pose
   display:grid, et un conteneur en grille ignore purement et simplement
   `columns`. La feuille disait deux colonnes, la page en montrait une. */
.liste.large ul{margin:0;display:block;columns:2;column-gap:44px}
.liste.large li{break-inside:avoid;margin-bottom:12px}
.pale .liste.large{background:#fbf7f0}

/* Une reserve du fondateur : encadree, pas en petit gris. */
.reserve{margin-top:24px;background:#fdf0e6;border:1px solid #f0cdb2;
  border-left:4px solid #e08a5b;border-radius:14px;padding:18px 22px;
  color:#7d3f1e;font-size:16px;max-width:86ch}

.apres{margin-top:28px}
.apres-liste{margin-top:34px}
.apres-liste h3{margin-bottom:16px}
section.mince{padding:22px 0}
.rappel-modele{display:flex;gap:18px;align-items:baseline;flex-wrap:wrap;
  border-left:3px solid #e08a5b;padding:2px 0 2px 18px;color:#4b5a53;
  font-size:16px}
.rappel-modele p{max-width:74ch}

/* Les sept piliers en resume sur l'accueil : des liens, pas des cartes
   mortes — chacun mene a son paragraphe sur la page concept. */
.grille.serree{gap:14px}
.carte.mini{display:block;padding:18px 20px;text-decoration:none;
  color:#16211d}
.carte.mini h3{font-size:16px;margin:0}
.carte.mini:hover{border-color:#2f6b52}

/* ------------------------------------------------------- KIMO Tutoring --- */
/* Les quatre programmes par age. La tranche d'age est ce qu'un parent
   cherche en premier : elle passe AVANT le nom du programme. */
.carte.prog .age{font-size:13px;font-weight:700;letter-spacing:.12em;
  color:#e08a5b;margin-bottom:8px}
.carte.prog h3{margin-bottom:10px}
.carte.prog p{color:#4b5a53;font-size:15px}
.liste.large code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:14px;background:#f5eee2;border:1px solid #e6ddcd;
  border-radius:7px;padding:2px 7px;color:#2f6b52}
.liste code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:14px;background:#f5eee2;border:1px solid #e6ddcd;
  border-radius:7px;padding:2px 7px;color:#2f6b52}
/* le code de monnaie, dans le bloc sombre du simulateur */
.sortie .dev{color:#a9bab2;font-weight:600}

/* ------------------------------------------------- tableaux du concept --- */
.tab.large th{width:auto}
.tab.large thead th{background:#f5eee2;font-size:14px;letter-spacing:.06em;
  text-transform:uppercase;color:#4b5a53;font-weight:700}
.pale .tab.large thead th{background:#efe6d6}
.tab.large tbody th{width:22%;color:#16211d}
.tab.large td{color:#41504a}
.tab tr.mis td,.tab tr.mis th{background:#f3f8f5}
.tab tr.mis th{box-shadow:inset 3px 0 0 #2f6b52}
.tab.horaire tbody th.h{width:130px;white-space:nowrap;
  font-variant-numeric:tabular-nums;color:#2f6b52}

/* ---------------------------------------------------------------- faq --- */
.faq{display:grid;gap:2px;max-width:860px}
details{background:#fff;border:1px solid #e6ddcd;padding:20px 24px}
details:first-of-type{border-radius:18px 18px 0 0}
details:last-of-type{border-radius:0 0 18px 18px}
summary{cursor:pointer;font-weight:650;font-size:17px;list-style:none}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";float:right;color:#e08a5b;font-weight:700}
details[open] summary::after{content:"\\2013"}
details p{margin-top:12px;color:#4b5a53;font-size:16px;max-width:70ch}

/* ------------------------------------------------------------ formulaire */
.form{background:#fff;border:1px solid #e6ddcd;border-radius:18px;
  padding:30px;display:grid;gap:18px;max-width:760px}
.form .paire{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.form label{font-size:15px;font-weight:600;color:#41504a;display:block;
  margin-bottom:6px}
.form textarea{min-height:120px;resize:vertical}
.oblig{color:#a2512a}
.form .env{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.form button{font:inherit;font-weight:650;font-size:16px;padding:13px 26px;
  border-radius:999px;border:0;background:#e08a5b;color:#231007;cursor:pointer}
.form button:hover{background:#d67d4c}
.recu{background:#eaf3ee;border:1px solid #b9d6c7;border-radius:14px;
  padding:16px 18px;font-size:15px;color:#1f4a39}

/* ------------------------------------------------------------- bandeau --- */
.bandeau{background:#2f6b52;color:#fff;border-radius:22px;padding:44px;
  display:flex;gap:28px;align-items:center;justify-content:space-between;
  flex-wrap:wrap}
.bandeau h2{color:#fff;max-width:20ch}
.bandeau p{color:#cfe3d9;margin-top:10px;max-width:46ch}

/* ---------------------------------------------------------------- pied --- */
footer{background:#16211d;color:#a9bab2;padding:48px 0;margin-top:6px;
  font-size:15px}
footer .devise{color:#fff;font-size:19px;font-weight:600;
  display:flex;align-items:center;gap:10px;margin-bottom:8px}
footer .devise .diamant{stroke:#e08a5b;width:18px;height:18px}
footer .fond{color:#8ea79a;margin-bottom:22px}
footer .avert{border:1px solid #2c3a34;border-radius:14px;padding:16px 18px;
  margin-bottom:20px;color:#c3d2ca;font-size:14px;max-width:82ch}
footer .liens-sites{display:flex;gap:22px;flex-wrap:wrap;margin-top:16px}
footer a{color:#8fd6b0}

/* -------------------------------------------------------------- mobile --- */
@media(max-width:900px){
  .hero-in{grid-template-columns:1fr;gap:32px}
  .g3,.g4{grid-template-columns:repeat(2,1fr)}
  .simu,.listes,.form .paire{grid-template-columns:1fr}
  /* La navigation ne DISPARAIT pas en mobile : elle passe a la ligne. Un
     menu cache derriere un bouton qu'on n'a pas construit, c'est un site a
     deux pages dont la seconde n'est atteignable que par le logo.
     En revanche l'en-tete cesse d'etre COLLE : sur deux lignes il ferait
     160 px, et il mangerait un cinquieme de l'ecran pendant toute la
     lecture. Il coute sa hauteur une fois, en haut de page. */
  .haut{position:static}
  .haut-in{gap:12px;flex-wrap:wrap}
  .marque{order:1}
  .langue{order:2;margin-left:auto}
  .nav{order:3;width:100%;margin-left:0;gap:16px;font-size:14px;
    border-top:1px solid #e6ddcd;padding-top:9px}
  .nav a{font-size:14px}
  section{padding:48px 0}
  .hero{padding:48px 0 40px}
  .bandeau{padding:30px}
}
@media(max-width:620px){
  .g2,.g3,.g4{grid-template-columns:1fr}
  .etape{grid-template-columns:44px 1fr;gap:14px;padding:20px}
  .tab th{width:auto}
  /* Deux colonnes de puces sur 390 px de large, ce sont deux colonnes de
     trois mots. Une seule. */
  .liste.large ul{columns:1}
  .liste.large{padding:22px}
  .signature{font-size:17px}
}
@media(prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important}
}
"""
