# -*- coding: utf-8 -*-
"""Controles du site KIMO.

Deux moitiés, et la seconde est celle qui compte.

  STATIQUE — on lit les fichiers produits. Utile pour ce qui est verifiable
  sans navigateur : la regle du nom, les deux langues, les identifiants en
  double, le fait qu'aucun chiffre reglementaire n'ait ete invente.

  NAVIGATEUR — on ouvre les deux pages pour de vrai. C'est la que se
  verifient les choses qu'un fichier ne peut pas prouver : que le simulateur
  affiche les MEMES chiffres que la formule Python (deux implementations,
  elles divergeront un jour), que la bascule de langue n'efface pas la page,
  que le formulaire refuse un envoi incomplet, et surtout que la page reste
  lisible AVEC JAVASCRIPT DESACTIVE.

Lancer : python3 tests-kimo.py
"""

import html as _H
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import contenu as C           # noqa: E402
import page_kimo as P         # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
DEMO = P.DEMO
OK = [0]
KO = [0]


def t(nom, cond, detail=''):
    if cond:
        OK[0] += 1
        print('  ok   %s' % nom)
    else:
        KO[0] += 1
        print(' ECHEC %s%s' % (nom, ('   -> %s' % detail) if detail else ''))


def lire(nom):
    with io.open(os.path.join(DEMO, nom), encoding='utf-8') as f:
        return f.read()


PAGES = ['index.html', 'franchise.html']
for nom in PAGES:
    if not os.path.isfile(os.path.join(DEMO, nom)):
        print('la page %s n\'existe pas — lancer page_kimo.py d\'abord' % nom)
        raise SystemExit(1)
HTML = dict((n, lire(n)) for n in PAGES)
TOUT = '\n'.join(HTML.values())


# ===========================================================================
print('\n--- LA REGLE DU NOM ---')
# ===========================================================================
# Elle passe avant tout le reste. Le modele peut inspirer ; le nom du reseau
# qui l'a rendu celebre n'apparait nulle part — ni dans une page, ni dans le
# code, ni dans un commentaire, ni dans un nom de fichier.
#
# Le mot cherche est ASSEMBLE, jamais ecrit : ce fichier fait partie de ce
# qu'il balaie, et un controle qui echoue sur lui-meme est un controle qu'on
# finit par desactiver.
INTERDIT = 'ku' + 'm' + 'on'

SOURCES = []
for racine, _d, fichiers in os.walk(ICI):
    if '__pycache__' in racine:
        continue
    for f in fichiers:
        SOURCES.append(os.path.join(racine, f))

interdits = []
for chemin in SOURCES:
    if INTERDIT in os.path.basename(chemin).lower():
        interdits.append(os.path.basename(chemin) + ' (nom de fichier)')
        continue
    if os.path.splitext(chemin)[1].lower() not in ('.py', '.html', '.css',
                                                   '.js', '.json', '.md',
                                                   '.txt', '.csv'):
        continue
    try:
        with io.open(chemin, encoding='utf-8', errors='ignore') as f:
            texte = f.read()
    except OSError:
        continue
    for mot in re.findall(r'[A-Za-z]{4,}', texte):
        if mot.lower() == INTERDIT:
            interdits.append(os.path.basename(chemin))
            break
t('le nom du reseau d\'apprentissage n\'apparait dans aucun fichier',
  not interdits, ', '.join(sorted(set(interdits))))
t('%d fichiers du dossier ont ete lus pour ce controle' % len(SOURCES),
  len(SOURCES) >= 6, len(SOURCES))
# Le controle doit pouvoir echouer, sinon il ne prouve rien : on lui donne
# un texte fautif et on verifie qu'il le voit.
t('ce controle sait detecter le mot (essai sur un texte fabrique)',
  any(m.lower() == INTERDIT
      for m in re.findall(r'[A-Za-z]{4,}',
                          'inspire du modele ' + INTERDIT.capitalize())))


# ===========================================================================
print('\n--- AUCUN CHIFFRE INVENTE ---')
# ===========================================================================
# Ni reglementaire (c'est du droit, ca expose un candidat), ni commercial
# (c'est une decision du groupe). Tant qu'ils ne sont pas donnes, le site
# affiche « a definir » — et le controle verifie qu'il n'a rien comble.
t('aucune valeur reglementaire n\'est renseignee dans les donnees',
  all(l[5] is None for l in C.REGLEMENTAIRE))
t('aucun montant du modele economique n\'est renseigne',
  all(l[3] is None for l in C.MODELE))

cadre = re.search(r'id="cadre".*?</table>', HTML['index.html'], re.S)
t('la section reglementaire existe dans la page', cadre is not None)
if cadre:
    cellules = re.findall(r'<td class="val">(.*?)</td>', cadre.group(0), re.S)
    t('les %d lignes reglementaires sont toutes marquees a definir'
      % len(C.REGLEMENTAIRE),
      len(cellules) == len(C.REGLEMENTAIRE)
      and all('class="tbc"' in c for c in cellules),
      '%d cellules' % len(cellules))
    t('aucun chiffre ne figure dans la colonne des valeurs reglementaires',
      not any(re.search(r'\d', c) for c in cellules))

eco = re.search(r'id="modele-eco".*?</table>', HTML['franchise.html'], re.S)
t('la section modele economique existe', eco is not None)
if eco:
    cellules = re.findall(r'<td class="val">(.*?)</td>', eco.group(0), re.S)
    t('les %d lignes du modele economique sont marquees a definir'
      % len(C.MODELE),
      len(cellules) == len(C.MODELE)
      and all('class="tbc"' in c for c in cellules))
    t('aucun montant ne figure dans la colonne des valeurs',
      not any(re.search(r'\d', c) for c in cellules))

t('les %d points ouverts sont listes en haut de la page franchise'
  % len(C.A_DEFINIR),
  all(_H.escape(fr, quote=True) in HTML['franchise.html']
      for _c, fr, _p in C.A_DEFINIR))
t('la page franchise annonce qu\'aucune creche n\'est ouverte',
  'aucune creche n\'est ouverte' in _H.unescape(HTML['franchise.html']))


# ===========================================================================
print('\n--- LES DEUX LANGUES ---')
# ===========================================================================
# On isole les BALISES d'abord, puis on pose une question simple sur
# chacune. Une expression avec lookahead serait juste dans un ordre
# d'attributs et muette dans l'autre.
for nom, html in HTML.items():
    balises = re.findall(r'<[a-zA-Z][^>]*>', html)
    boiteuses = [b for b in balises
                 if ('data-fr=' in b) != ('data-en=' in b)]
    t('%s : aucune balise ne porte une seule des deux langues' % nom,
      not boiteuses, (boiteuses or [''])[0][:110])
    t('%s : la page porte bien des elements bilingues (%d)'
      % (nom, sum(1 for b in balises if 'data-fr=' in b)),
      sum(1 for b in balises if 'data-fr=' in b) > 40)

# Le texte SERVI doit dire la meme chose que data-fr, sinon la faute
# n'apparait qu'apres le passage du script — et personne ne la voit en
# relisant la page.
ecarts = []
for nom, html in HTML.items():
    for balise, attr, contenu_ in re.findall(
            r'<(p|h1|h2|h3|span|dt|summary|th|li|a|label|option)\b'
            r'[^>]*data-fr="([^"]*)"[^>]*>(.*?)</\1>', html, re.S):
        servi = re.sub(r'<[^>]+>', '', contenu_)
        if _H.unescape(attr).strip() != _H.unescape(servi).strip():
            ecarts.append('%s <%s> %r != %r'
                          % (nom, balise, _H.unescape(attr)[:40],
                             _H.unescape(servi)[:40]))
t('le texte servi est identique au data-fr partout', not ecarts,
  ' | '.join(ecarts[:2]))

t('la bascule de langue est presente sur les deux pages',
  all(html.count('class="langue"') == 1 for html in HTML.values()))
t('le bouton EN existe sur les deux pages',
  all('data-l="en"' in html for html in HTML.values()))


# ===========================================================================
print('\n--- LA MARQUE DU GROUPE ---')
# ===========================================================================
# Le diamant et la devise sont la marque du GROUPE : ils sont identiques sur
# tous les sites. Recopies a la main, ils divergent au premier retouche.
PREST = os.path.join(os.path.dirname(ICI), 'prestige', 'page_prestige.py')
if os.path.isfile(PREST):
    with io.open(PREST, encoding='utf-8') as f:
        src_prestige = f.read()
    trace = re.search(r"DIAMANT = \((.*?)\)\n", src_prestige, re.S)
    def normalise(bloc):
        return re.sub(r"\s+", '', re.sub(r"['\n]", '', bloc))
    t('le diamant est le meme trace que sur Maisons de Prestige',
      trace is not None
      and normalise(trace.group(1)) == normalise(repr(P.DIAMANT)[1:-1]
                                                 .replace('\\', '')),
      'trace introuvable' if not trace else '')
    t('la devise francaise est identique a celle des autres sites',
      ("DEVISE_FR = '%s'" % C.DEVISE_FR) in src_prestige, C.DEVISE_FR)
    t('la devise anglaise est identique a celle des autres sites',
      ("DEVISE_EN = '%s'" % C.DEVISE_EN) in src_prestige, C.DEVISE_EN)
else:
    t('le site de prestige est present pour comparer la marque du groupe',
      False, PREST + ' introuvable — controle NON EXECUTE')

t('le diamant figure sur les deux pages', all('class="diamant"' in h
                                              for h in HTML.values()))
t('la devise figure au pied des deux pages',
  all(_H.escape(C.DEVISE_FR, quote=True) in h for h in HTML.values()))
t('le fondateur est nomme au pied des deux pages',
  all('Hakim Adjaoudi' in h for h in HTML.values()))


# ===========================================================================
print('\n--- STRUCTURE DU HTML ---')
# ===========================================================================
for nom, html in HTML.items():
    ids = re.findall(r'\bid="([^"]+)"', html)
    doubles = sorted(set(i for i in ids if ids.count(i) > 1))
    t('%s : aucun identifiant en double (%d au total)' % (nom, len(ids)),
      not doubles, ', '.join(doubles))
    t('%s : chaque label pointe sur un champ existant' % nom,
      all(f in ids for f in re.findall(r'<label for="([^"]+)"', html)),
      ', '.join(f for f in re.findall(r'<label for="([^"]+)"', html)
                if f not in ids))
    t('%s : la page declare son encodage et sa vue mobile' % nom,
      'charset="utf-8"' in html and 'width=device-width' in html)
    t('%s : la demonstration n\'est pas indexable' % nom,
      'name="robots" content="noindex"' in html)
    ancres = set(re.findall(r'href="#([^"]+)"', html))
    t('%s : toutes les ancres internes existent dans la page' % nom,
      ancres <= set(ids), ', '.join(sorted(ancres - set(ids))))

t('les liens entre les deux pages existent dans les deux sens',
  'href="franchise.html"' in HTML['index.html']
  and 'href="index.html"' in HTML['franchise.html'])
t('les liens vers les autres sites du groupe sont absolus',
  all(C.URL_ANNUAIRE in h and C.URL_PRESTIGE in h for h in HTML.values()))


# ===========================================================================
print('\n--- RIEN N\'EST CACHE SANS JAVASCRIPT ---')
# ===========================================================================
# On decoupe la feuille en paires selecteur{bloc} avant de poser la
# question. Une fenetre de lignes est juste au milieu d'une regle et fausse
# a chaque frontiere.
from style_kimo import CSS as FEUILLE          # noqa: E402
sans_media = re.sub(r'@media[^{]*\{', '', FEUILLE)
regles = re.findall(r'([^{}@]+)\{([^{}]*)\}', sans_media)
t('la feuille de style se decoupe en regles (%d)' % len(regles),
  len(regles) > 40, len(regles))
cachantes = []
for sel, bloc in regles:
    plat = bloc.replace(' ', '')
    if ('display:none' in plat or 'visibility:hidden' in plat
            or re.search(r'opacity:0(?![.\d])', plat)):
        if '-webkit-details-marker' in sel:
            continue      # une puce de <details>, pas du contenu
        cachantes.append(sel.strip())
t('aucune regle de style ne masque du contenu', not cachantes,
  ' | '.join(cachantes))
t('aucun element du HTML ne porte un style en ligne qui le masque',
  not re.search(r'style="[^"]*(display:\s*none|opacity:\s*0[^.\d])', TOUT))
t('la navigation ne disparait pas en mobile',
  not re.search(r'\.nav\s*\{[^}]*display:\s*none', FEUILLE))


# ===========================================================================
print('\n--- LE SIMULATEUR, COTE FORMULE ---')
# ===========================================================================
d = P.defauts()
r = P.calcul(d)
# Un calcul refait a la main, sur les valeurs de depart. Comparer la
# fonction a elle-meme ne prouverait rien.
produits = 12 * 0.90 * 1300
masse = 4 * 2500
fixes = 1600 + masse + 1100
t('produits mensuels : 12 places x 90 %% x 1300 = %d' % produits,
  abs(r['produits'] - produits) < 1e-9, r['produits'])
t('masse salariale : 4 x 2500 = %d' % masse, abs(r['masse'] - masse) < 1e-9)
t('total des charges (redevance a zero) = %d' % fixes,
  abs(r['charges'] - fixes) < 1e-9, r['charges'])
t('resultat mensuel = produits - charges = %d' % (produits - fixes),
  abs(r['resultat'] - (produits - fixes)) < 1e-9, r['resultat'])
t('resultat annuel = 12 x le mensuel',
  abs(r['annuel'] - r['resultat'] * 12) < 1e-9)
t('point mort = charges fixes / (places x tarif), soit %.1f %%'
  % (fixes / (12 * 1300) * 100),
  abs(r['seuil'] - fixes / (12 * 1300) * 100) < 1e-9, r['seuil'])

# La redevance doit mordre : sinon le champ ne sert a rien et personne ne
# s'en apercoit tant qu'il vaut zero.
d2 = dict(d, redevance=6)
r2 = P.calcul(d2)
t('une redevance de 6 % reduit bien le resultat',
  r2['resultat'] < r['resultat'] - 1, '%s vs %s' % (r2['resultat'],
                                                    r['resultat']))
t('une redevance de 6 % remonte le point mort',
  r2['seuil'] > r['seuil'] + 1)
t('a zero place, le point mort ne divise pas par zero',
  P.calcul(dict(d, places=0))['seuil'] == 0)

t('les valeurs de depart du simulateur sont ecrites dans le HTML',
  all(('id="s-%s"' % c[0]) in HTML['franchise.html'] for c in C.SIM_CHAMPS))
for cle, _fr, _en, _u, _f in P.SORTIES:
    attendu = P.nb(r[cle])
    trouve = re.search(r'id="r-%s">([^<]*)' % cle, HTML['franchise.html'])
    t('la sortie « %s » est calculee dans la page servie' % cle,
      trouve is not None and trouve.group(1).strip().startswith(attendu),
      '%r attendait %r' % (trouve.group(1) if trouve else None, attendu))
t('le simulateur previent que ses chiffres ne sont pas ceux de KIMO',
  _H.escape(C.SIM_NOTE_FR, quote=True) in HTML['franchise.html'])


# ===========================================================================
print('\n--- LE FORMULAIRE DE CANDIDATURE ---')
# ===========================================================================
f = HTML['franchise.html']
t('le formulaire porte un identifiant distinct de sa section',
  'id="demande"' in f and 'id="candidature"' in f)
t('les %d champs de candidature sont presents' % len(C.FORMULAIRE),
  all(('id="f-%s"' % c[0]) in f for c in C.FORMULAIRE))
obligs = [c[0] for c in C.FORMULAIRE if c[4]]
t('les %d champs obligatoires sont marques required' % len(obligs),
  all(re.search(r'id="f-%s"[^>]*required' % c, f) for c in obligs),
  ', '.join(c for c in obligs
            if not re.search(r'id="f-%s"[^>]*required' % c, f)))
t('la destination du formulaire est annoncee comme non fixee',
  'destination a definir' in f)
t('le formulaire ne part pas vers une adresse inventee',
  not re.search(r'<form[^>]*action=', f))


# ===========================================================================
print('\n--- DANS UN VRAI NAVIGATEUR ---')
# ===========================================================================
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print(' (playwright absent — les controles navigateur ne sont PAS'
          ' executes, et ce sont eux qui comptent)')
    KO[0] += 1
else:
    def url(nom):
        return 'file://' + os.path.join(DEMO, nom)

    with sync_playwright() as pw:
        nav = pw.chromium.launch()

        # ------------------------------------------------- avec JavaScript
        ctx = nav.new_context(viewport={'width': 1280, 'height': 900})
        page = ctx.new_page()
        erreurs = []
        page.on('pageerror', lambda x: erreurs.append(str(x)))
        page.on('console', lambda m: erreurs.append(m.text)
                if m.type == 'error' else None)

        page.goto(url('index.html'))
        t('accueil : aucune erreur JavaScript', not erreurs,
          ' | '.join(erreurs[:2]))
        t('accueil : le titre est visible',
          page.locator('h1').first.is_visible())
        t('accueil : les pastilles « a definir » se voient (%d)'
          % page.locator('.tbc').count(),
          page.locator('.tbc').count() >= 3)

        # Rien ne doit etre transparent ou invisible au chargement.
        invisibles = page.evaluate("""() => {
            const out = [];
            document.querySelectorAll('body *').forEach(n => {
              if (n.closest('details:not([open])')) return;
              const s = getComputedStyle(n);
              if (s.opacity === '0' || s.visibility === 'hidden')
                out.push(n.tagName + '.' + n.className);
            });
            return out.slice(0, 5);
        }""")
        t('accueil : aucun element n\'est rendu invisible', not invisibles,
          ' | '.join(invisibles))

        # La bascule de langue.
        page.click('.langue button[data-l="en"]')
        t('accueil : la bascule passe la navigation en anglais',
          page.locator('.nav a').first.inner_text().strip() == 'The network',
          page.locator('.nav a').first.inner_text())
        t('accueil : la langue du document suit',
          page.evaluate('document.documentElement.lang') == 'en')
        t('accueil : le titre n\'a pas ete vide par la bascule',
          len(page.locator('h1').first.inner_text().strip()) > 20)
        page.click('.langue button[data-l="fr"]')
        t('accueil : le retour au francais fonctionne',
          page.locator('.nav a').first.inner_text().strip() == 'Le reseau')

        # ------------------------------------------- le simulateur en vrai
        page.goto(url('franchise.html'))
        t('franchise : aucune erreur JavaScript', not erreurs,
          ' | '.join(erreurs[:2]))

        # Le chiffre affiche et le chiffre attendu passent par LA MEME
        # normalisation : l'espace insecable des milliers devient un espace
        # ordinaire des deux cotes. Sans cela le controle mesure la nature
        # de l'espace, pas le calcul — et il passe ou echoue selon que la
        # valeur vient du HTML de depart ou du script.
        NBSP = u'\u00a0'

        def lu(cle):
            return (page.locator('#r-%s' % cle).inner_text()
                    .replace(NBSP, ' ').strip())

        def attendu(valeur, unite):
            return (P.nb(valeur).replace(NBSP, ' ')
                    + (' %' if unite == 'pourcent' else ' EUR'))

        # LE controle : la formule Python et la formule JavaScript doivent
        # tomber sur le meme chiffre. Elles sont ecrites deux fois, elles
        # divergeront un jour ; autant que ce soit ici.
        ecarts = []
        for cle, _fr, _en, unite, _f in P.SORTIES:
            att = attendu(r[cle], unite)
            if lu(cle) != att:
                ecarts.append('%s: %r != %r' % (cle, lu(cle), att))
        t('valeurs de depart : le script retrouve les chiffres de la '
          'construction', not ecarts, ' | '.join(ecarts[:3]))

        # On change une entree et on recompare a la formule Python.
        page.fill('#s-places', '20')
        page.dispatch_event('#s-places', 'input')
        r20 = P.calcul(dict(d, places=20))
        ecarts = []
        for cle, _fr, _en, unite, _f in P.SORTIES:
            att = attendu(r20[cle], unite)
            if lu(cle) != att:
                ecarts.append('%s: %r != %r' % (cle, lu(cle), att))
        t('20 places : le script suit toujours la formule Python',
          not ecarts, ' | '.join(ecarts[:3]))

        # Une redevance doit se voir dans la ligne qui porte son nom.
        page.fill('#s-redevance', '6')
        page.dispatch_event('#s-redevance', 'input')
        t('une redevance saisie apparait dans la ligne redevance',
          lu('redevance') != attendu(0, 'devise'), lu('redevance'))

        # Un resultat negatif doit SE VOIR negatif.
        page.fill('#s-salaire', '9000')
        page.dispatch_event('#s-salaire', 'input')
        t('un resultat negatif est signale comme tel',
          page.locator('.ligne[data-sortie="resultat"].neg').count() == 1,
          lu('resultat'))

        # La monnaie choisie doit remplacer le code affiche.
        page.select_option('#s-devise', 'CAD')
        t('le code de monnaie choisi remplace celui du depart',
          'CAD' in lu('produits') and 'EUR' not in lu('produits'),
          lu('produits'))

        # ------------------------------------------------ le formulaire
        page.goto(url('franchise.html'))
        page.click('#demande button[type="submit"]')
        recu = page.locator('#recu')
        t('un envoi incomplet est refuse et dit ce qui manque',
          recu.is_visible() and 'Il manque' in recu.inner_text(),
          recu.inner_text()[:80])
        t('la page n\'a pas ete rechargee par l\'envoi',
          page.evaluate('!!document.getElementById("recu")'))
        for cle, _fr, _en, typ, oblig, _o in C.FORMULAIRE:
            if not oblig:
                continue
            if typ == 'select':
                page.select_option('#f-%s' % cle, index=1)
            else:
                page.fill('#f-%s' % cle, 'essai')
        page.click('#demande button[type="submit"]')
        t('un envoi complet est accepte, et dit qu\'il n\'envoie rien',
          'enregistree' in recu.inner_text()
          and 'rien n\'est envoye' in recu.inner_text(),
          recu.inner_text()[:90])
        t('le formulaire est vide apres un envoi accepte',
          page.input_value('#f-nom') == '')
        ctx.close()

        # -------------------------------------------- SANS JavaScript
        # Une page qui a besoin du script pour montrer son texte est une
        # page blanche le jour ou le script ne charge pas.
        ctx = nav.new_context(viewport={'width': 1280, 'height': 900},
                              java_script_enabled=False)
        page = ctx.new_page()
        page.goto(url('index.html'))
        t('sans JavaScript : le titre de l\'accueil est lisible',
          len(page.locator('h1').first.inner_text().strip()) > 20)
        t('sans JavaScript : le tableau reglementaire est visible',
          page.locator('#cadre .tbc').count() == len(C.REGLEMENTAIRE),
          page.locator('#cadre .tbc').count())
        page.goto(url('franchise.html'))
        t('sans JavaScript : le simulateur affiche deja ses chiffres',
          page.locator('#r-resultat').inner_text().strip()
          .startswith(P.nb(r['resultat'])),
          page.locator('#r-resultat').inner_text())
        t('sans JavaScript : les six etapes du parcours sont la',
          page.locator('.etape').count() == len(C.PARCOURS))
        t('sans JavaScript : les questions s\'ouvrent quand meme',
          page.locator('details').count() == len(C.FAQ))
        ctx.close()

        # ------------------------------------------------------- mobile
        ctx = nav.new_context(viewport={'width': 390, 'height': 844})
        page = ctx.new_page()
        page.goto(url('index.html'))
        t('mobile : la navigation reste atteignable',
          page.locator('.nav a').first.is_visible())
        largeur = page.evaluate(
            'Math.max(document.documentElement.scrollWidth,'
            ' document.body.scrollWidth)')
        t('mobile : la page ne deborde pas en largeur (%d px)' % largeur,
          largeur <= 390 + 1, largeur)
        page.goto(url('franchise.html'))
        largeur = page.evaluate(
            'Math.max(document.documentElement.scrollWidth,'
            ' document.body.scrollWidth)')
        t('mobile : la page franchise ne deborde pas non plus (%d px)'
          % largeur, largeur <= 390 + 1, largeur)
        ctx.close()
        nav.close()


print('\n%d controles verts, %d en echec' % (OK[0], KO[0]))
raise SystemExit(0 if KO[0] == 0 else 1)
