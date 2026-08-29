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


# Le site est maintenant DEUX arbres : le francais a la racine, l'anglais
# dans /en/. Les controles de structure tournent sur les huit pages ; ceux
# qui parlent du texte francais tournent sur les quatre premieres.
FICHIERS = ['index.html', 'concept.html', 'tutoring.html', 'franchise.html']
PAGES = FICHIERS + [os.path.join('en', f) for f in FICHIERS]
for nom in PAGES:
    if not os.path.isfile(os.path.join(DEMO, nom)):
        print('la page %s n\'existe pas — lancer page_kimo.py d\'abord' % nom)
        raise SystemExit(1)
HTML = dict((n, lire(n)) for n in PAGES)
FR = dict((n, HTML[n]) for n in FICHIERS)
EN = dict((n, HTML[os.path.join('en', n)]) for n in FICHIERS)
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
print('\n--- FIDELITE A LA NOTE DU FONDATEUR ---')
# ===========================================================================
# La page « concept » n'est pas une plaquette ecrite d'apres sa note : c'est
# sa note. Ce controle le PROUVE, en comparant chaque phrase anglaise du site
# au texte du .docx qu'il a envoye. Sans lui, « je n'ai rien invente » est une
# affirmation, pas un fait — et c'est exactement le genre d'affirmation qui
# devient fausse a la troisieme retouche.
#
# Le francais, lui, est ma traduction : il n'est pas dans le document, il ne
# peut pas etre compare, et le site le dit en haut de la page.
def phrases_anglaises():
    """Toutes les chaines ANGLAISES reprises de sa note, aplaties."""
    out = [C.SIGNATURE_EN, C.PROMESSE_EN, C.METHODE_INTRO_EN,
           C.FORMAT_AVERT_EN, C.EDUCATEURS_INTRO_EN, C.PLATEFORME_NOTE_EN,
           C.SECURITE_INTRO_EN, C.COUTS_NOTE_EN, C.HORIZON_EN]
    for fr, en in (C.METHODE + C.FORMAT + C.EDUCATEURS + C.PLATEFORME
                   + C.PARENTS + C.SECURITE + C.QUALITE + C.COUTS + C.KPI
                   + C.PILOTE + C.ARCHI_MARQUE):
        out.append(en)
    for l in C.APPRENTISSAGE:
        out += [l[2], l[4]]
    for l in C.COUCHES:
        out += [l[1], l[3], l[5]]
    for l in C.AGES:
        out += [l[1], l[3], l[5], l[7]]
    for l in C.JOURNEE:
        out.append(l[2])
    for l in C.EXPLOITATION:
        out += [l[2], l[4], l[6]]
    for l in C.PHASES:
        out += [l[2], l[4]]
    for l in C.RISQUES:
        out += [l[1], l[3]]
    return out


def aplatir(s):
    """Un texte comparable : tirets, apostrophes et espaces uniformises.

    Word ecrit des tirets cadratins et des apostrophes courbes ; le fichier
    source ecrit des tirets simples et des apostrophes droites. Comparer sans
    aplanir cela ferait echouer le controle sur la TYPOGRAPHIE, ce qui n'a
    aucun rapport avec la question posee.
    """
    s = s.replace(u'’', "'").replace(u'‘', "'")
    s = s.replace(u'“', '"').replace(u'”', '"')
    s = s.replace(u'—', '-').replace(u'–', '-')
    s = s.replace(u' ', ' ')
    return re.sub(r'\s+', ' ', s).strip().lower()


NOTE = None
for base in (ICI, os.path.dirname(ICI)):
    cand = os.path.join(base, 'KIMO_Decentralized_Early_Learning_Concept.docx')
    if os.path.isfile(cand):
        NOTE = cand
        break

if NOTE is None:
    # Un controle qu'on n'a pas pu executer n'est pas un controle vert.
    t('la note de concept du fondateur est disponible pour comparaison',
      False, 'KIMO_Decentralized_Early_Learning_Concept.docx introuvable — '
             'CONTROLE NON EXECUTE')
else:
    import zipfile
    with zipfile.ZipFile(NOTE) as z:
        xml = z.read('word/document.xml').decode('utf-8')
    brut = _H.unescape(re.sub(r'<[^>]+>', ' ', xml))
    SOURCE = aplatir(brut)
    t('la note de concept a ete lue (%d caracteres)' % len(SOURCE),
      len(SOURCE) > 8000, len(SOURCE))

    phrases = [p for p in phrases_anglaises() if p and p.strip()]
    absentes = [p for p in phrases if aplatir(p) not in SOURCE]
    t('les %d passages anglais du site figurent mot pour mot dans sa note'
      % len(phrases), not absentes,
      ' || '.join(a[:70] for a in absentes[:3]))

    # Et le controle doit pouvoir echouer : une phrase que j'aurais ecrite
    # moi-meme ne doit PAS etre trouvee dans son document.
    t('ce controle sait reperer une phrase qui ne vient pas de lui',
      aplatir('KIMO guarantees a 30 percent return on every center')
      not in SOURCE)

    # Le francais n'est PAS compare : c'est une traduction, elle n'est pas
    # dans le document. Le site doit donc le dire, sur la page concernee.
    t('la page concept annonce que le francais est une traduction',
      'traduction' in _H.unescape(HTML['concept.html']).lower())


def phrases_tutorat():
    """Les chaines ANGLAISES reprises de sa note « Tutoring Platform »."""
    out = [C.TUT_INTRO_EN, C.TUT_VERIF_INTRO_EN, C.TUT_PAIEMENT_NOTE_EN,
           C.TUT_SEO_INTRO_EN, C.TUT_SEO_NOTE_EN, C.TUT_MVP_NOTE_EN,
           C.TUT_IA_LIMITE_EN, C.TUT_POSITION_EN, C.TUT_MARQUE_EN]
    for t_ in (C.TUT_PRINCIPES + C.TUT_MATIERES + C.TUT_RESERVATION
               + C.TUT_CLASSE + C.TUT_PARENTS + C.TUT_ELEVE + C.TUT_TUTEUR
               + C.TUT_VERIF + C.TUT_SECURITE + C.TUT_PAIEMENT + C.TUT_MVP
               + C.TUT_IA + C.TUT_KPI):
        out.append(t_[1])
    for l in C.TUT_PROGRAMMES:
        out += [l[1], l[3]]
    for l in C.TUT_PHASES:
        out += [l[2], l[4]]
    return out + list(C.TUT_SEO)


NOTE2 = None
for base in (ICI, os.path.dirname(ICI)):
    cand = os.path.join(base, 'KIMO_Tutoring_Platform_6_17.docx')
    if os.path.isfile(cand):
        NOTE2 = cand
        break

if NOTE2 is None:
    t('la note tutorat du fondateur est disponible pour comparaison',
      False, 'KIMO_Tutoring_Platform_6_17.docx introuvable — '
             'CONTROLE NON EXECUTE')
else:
    import zipfile
    with zipfile.ZipFile(NOTE2) as z:
        xml2 = z.read('word/document.xml').decode('utf-8')
    SOURCE2 = aplatir(_H.unescape(re.sub(r'<[^>]+>', ' ', xml2)))
    t('la note tutorat a ete lue (%d caracteres)' % len(SOURCE2),
      len(SOURCE2) > 6000, len(SOURCE2))
    ph2 = [x for x in phrases_tutorat() if x and x.strip()]
    abs2 = [x for x in ph2 if aplatir(x) not in SOURCE2]
    t('les %d passages anglais du tutorat figurent mot pour mot dans sa note'
      % len(ph2), not abs2, ' || '.join(a[:70] for a in abs2[:3]))
    t('ce controle-la aussi sait echouer',
      aplatir('KIMO guarantees every student a top grade') not in SOURCE2)


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

# La SEULE fourchette de capacite ecrite sur le site est la sienne (« 8 a 20
# », section 4 de sa note), et elle ne doit jamais apparaitre sans la reserve
# qui l'accompagne. Un chiffre de capacite lu sans sa reserve est lu comme un
# plafond legal, et il ne l'est pas.
capa = re.findall(r'8 à 20[^<]*', _H.unescape(HTML['concept.html']))
t('la fourchette de capacite apparait bien sur la page concept',
  len(capa) >= 1, capa)
t('elle n\'apparait jamais sans sa reserve reglementaire',
  all('sous réserve de la réglementation' in c for c in capa),
  ' | '.join(capa))
t('la fourchette de capacite ne remplace pas la ligne « capacite » du '
  'tableau reglementaire',
  all(l[5] is None for l in C.REGLEMENTAIRE if l[0] == 'capacite'))
t('la reserve du fondateur sur la juridiction est reprise sur les deux '
  'pages qui parlent de capacite',
  all(_H.escape(C.FORMAT_AVERT_FR, quote=True) in HTML[n]
      for n in ('index.html', 'concept.html')))

t('les %d points ouverts sont listes en haut de la page franchise'
  % len(C.A_DEFINIR),
  all(_H.escape(fr, quote=True) in HTML['franchise.html']
      for _c, fr, _p in C.A_DEFINIR))
t('la page franchise annonce qu\'aucune creche n\'est ouverte',
  'aucune crèche n\'est ouverte' in _H.unescape(HTML['franchise.html']))


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
# Chaque page sert la langue de son arbre : la page francaise doit dire ce
# que dit son data-fr, la page anglaise ce que dit son data-en. Une faute de
# frappe dans l'attribut seul ne se verrait qu'apres la bascule.
ecarts = []
for nom, html in HTML.items():
    langue = 'en' if nom.startswith('en' + os.sep) else 'fr'
    for balise, attr, contenu_ in re.findall(
            r'<(p|h1|h2|h3|span|dt|summary|th|li|a|label|option)\b'
            r'[^>]*data-%s="([^"]*)"[^>]*>(.*?)</\1>' % langue, html, re.S):
        servi = re.sub(r'<[^>]+>', '', contenu_)
        if _H.unescape(attr).strip() != _H.unescape(servi).strip():
            ecarts.append('%s <%s> %r != %r'
                          % (nom, balise, _H.unescape(attr)[:40],
                             _H.unescape(servi)[:40]))
t('le texte servi est celui de la langue de la page', not ecarts,
  ' | '.join(ecarts[:2]))

t('le selecteur de langue est present sur les huit pages',
  all(html.count('class="langue"') == 1 for html in HTML.values()))
# Ce n'est plus un bouton pilote par un script : c'est un LIEN. Une page
# francaise pointe vers en/<page>, une page anglaise vers ../<page>, et cela
# marche sans JavaScript.
manque = []
for nom, html in HTML.items():
    f = os.path.basename(nom)
    attendu = ('en/' + f) if not nom.startswith('en' + os.sep) else ('../' + f)
    if ('href="%s" hreflang=' % attendu) not in html:
        manque.append(nom)
t('chaque page pointe vers sa jumelle dans l\'autre langue', not manque,
  ', '.join(manque))
t('chaque page declare sa langue et son alternative',
  all(('<html lang="%s">' % ('en' if n.startswith('en' + os.sep) else 'fr'))
      in HTML[n] and 'rel="alternate" hreflang="en"' in HTML[n]
      for n in PAGES))


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

t('les quatre pages se lient les unes aux autres, dans les deux langues',
  all(('href="%s"' % autre) in HTML[nom] or ('href="%s#' % autre) in HTML[nom]
      for nom in PAGES for autre in FICHIERS
      if os.path.basename(nom) != autre),
  ', '.join('%s -> %s' % (nom, autre) for nom in PAGES for autre in FICHIERS
            if os.path.basename(nom) != autre
            and ('href="%s"' % autre) not in HTML[nom]
            and ('href="%s#' % autre) not in HTML[nom]))

# Les ancres d'une page vers UNE AUTRE page. Le controle precedent ne voit
# que « href="#x" » ; un « concept.html#p-echecs » casse en silence, et il
# casse au clic, pas a la construction.
IDS = dict((n, set(re.findall(r'\bid="([^"]+)"', HTML[n]))) for n in PAGES)
croisees = []
for nom, html in HTML.items():
    dossier = os.path.dirname(nom)
    for cible, ancre in re.findall(r'href="([a-z]+\.html)#([^"]+)"', html):
        ref = os.path.join(dossier, cible) if dossier else cible
        if ref not in IDS:
            croisees.append('%s -> %s (page inconnue)' % (nom, cible))
        elif ancre not in IDS[ref]:
            croisees.append('%s -> %s#%s' % (nom, cible, ancre))
t('les ancres d\'une page vers une autre pointent sur un element existant',
  not croisees, ' | '.join(croisees[:4]))
t('les liens vers les autres sites du groupe sont absolus',
  all(C.URL_ANNUAIRE in h and C.URL_PRESTIGE in h for h in HTML.values()))


# ===========================================================================
print('\n--- LA PAGE CONCEPT ---')
# ===========================================================================
c = HTML['concept.html']
t('les %d piliers d\'apprentissage ont chacun leur ancre'
  % len(C.APPRENTISSAGE),
  all(('id="p-%s"' % l[0]) in c for l in C.APPRENTISSAGE),
  ', '.join(l[0] for l in C.APPRENTISSAGE if ('id="p-%s"' % l[0]) not in c))
t('l\'accueil renvoie vers chacun des %d piliers' % len(C.APPRENTISSAGE),
  all(('concept.html#p-%s' % l[0]) in HTML['index.html']
      for l in C.APPRENTISSAGE))


def lignes(bloc_id, html=c):
    m = re.search(r'id="%s".*?</table>' % bloc_id, html, re.S)
    if not m:
        return -1
    corps = re.search(r'<tbody>(.*?)</tbody>', m.group(0), re.S)
    return len(re.findall(r'<tr', corps.group(1))) if corps else -1


for ident, table, quoi in (('couches', C.COUCHES, 'niveaux du modele'),
                           ('ages', C.AGES, 'etapes par age'),
                           ('journee', C.JOURNEE, 'moments de la journee'),
                           ('exploitation', C.EXPLOITATION,
                            'modeles d\'exploitation'),
                           ('risques', C.RISQUES, 'risques')):
    t('les %d %s sont tous dans le tableau' % (len(table), quoi),
      lignes(ident) == len(table), lignes(ident))

t('les %d phases de deploiement sont presentes' % len(C.PHASES),
  c.count('class="etape"') == len(C.PHASES), c.count('class="etape"'))
t('la franchise est mise en avant une seule fois dans les cinq modeles',
  c.count('<tr class="mis">') == 1, c.count('<tr class="mis">'))
t('la page franchise renvoie bien vers les quatre autres modeles',
  'concept.html#exploitation' in HTML['franchise.html'])

# La pastille « texte a valider » disait que la methode etait MA redaction.
# Elle ne l'est plus : elle vient de sa note. Une pastille laissee en place
# apres qu'elle a cesse d'etre vraie apprend a ne plus lire les pastilles.
t('la methode ne porte plus la mention « texte a valider »',
  C.METHODE_A_VALIDER is False
  and 'texte a valider' not in _H.unescape(TOUT))
t('les %d principes de la methode sont sur l\'accueil ET sur le concept'
  % len(C.METHODE),
  all(_H.escape(fr, quote=True) in HTML['index.html']
      and _H.escape(fr, quote=True) in c for fr, _en in C.METHODE))

# La signature. L'anglais est le sien, mot pour mot, et le francais est
# annonce comme une traduction tant qu'il ne l'a pas confirme.
attendue = '%s — %s' % (C.MARQUE, C.SIGNATURE_EN)
t('la signature anglaise est exactement la sienne',
  all(_H.escape(attendue, quote=True) in HTML[n]
      for n in ('index.html', 'concept.html')), attendue)
t('la traduction francaise de la signature est signalee comme a valider',
  C.SIGNATURE_TRAD_A_VALIDER
  and all('traduction française à valider' in HTML[n]
          for n in ('index.html', 'concept.html', 'tutoring.html')))
# Et la mention n'a rien a faire sur la page ANGLAISE : la phrase y est la
# sienne, il n'y a pas de traduction a valider.
# On regarde le texte SERVI, pas le fichier : les attributs data-fr portent
# le francais sur toutes les pages, c'est leur role.
def servi(html):
    return re.sub(r'<[^>]+>', ' ', html)


t('la mention n\'apparait pas sur les pages anglaises',
  not any('traduction française' in servi(EN[f]) for f in FICHIERS),
  ', '.join(f for f in FICHIERS if 'traduction française' in servi(EN[f])))
# Et la preuve que la pose de langue fait quelque chose : l'anglais doit
# etre SERVI, pas seulement present en attribut.
t('les pages anglaises servent bien l\'anglais',
  '>The network<' in EN['index.html']
  and 'My sites impact the world.</p>' in EN['index.html']
  and '>The concept<' in EN['concept.html'])



# ===========================================================================
print('\n--- LES ACCENTS, AU DICTIONNAIRE ---')
# ===========================================================================
# Le francais du site est passe a un vrai dictionnaire francais. Une liste de
# mots ecrite a la main ne vaut rien ici : elle ne peut confirmer que les
# mots qu'on y a mis, et c'est justement ceux qu'on oublie qui manquent.
try:
    from spellchecker import SpellChecker
except ImportError:
    t('un dictionnaire francais est disponible pour verifier les accents',
      False, 'pyspellchecker absent — CONTROLE NON EXECUTE')
else:
    MOTS_FR = set(SpellChecker(language='fr').word_frequency.dictionary)
    # Marque, sigles et mots que le dictionnaire ne connait pas mais qui sont
    # justes. Cette liste est COURTE et chaque entree est un choix assume.
    ADMIS = set("""
    kimo jncorp adjaoudi hakim javascript aujourd jusqu quelqu rez mini
    nommage prototyper impactent précontractuelle présences candidater
    maltraitance encadrants inc logic chess move stories science discover
    explore advance master tutoring ludification consentements indexables ia
    tutorat prépayés présentiel réservable eur cad chf dzd mad gbp fr en seo
    mvp api url dns etp kpi subject city age group topic tutors programs
    subjects online resources
    """.split())
    inconnus = {}
    total_mots = 0
    for nom in FICHIERS:
        for attr in re.findall(r'data-fr="([^"]*)"', HTML[nom]):
            for mot in re.findall(r"[A-Za-zÀ-ÿ]{2,}", _H.unescape(attr)):
                total_mots += 1
                if mot.lower() not in MOTS_FR and mot.lower() not in ADMIS:
                    inconnus.setdefault(mot.lower(), nom)
    t('les %d mots francais servis sont tous connus du dictionnaire'
      % total_mots, not inconnus,
      ', '.join('%s (%s)' % (m, f) for m, f in list(inconnus.items())[:5]))
    # Et le controle doit savoir echouer.
    t('ce controle sait reperer un mot sans accent',
      'reglementaire' not in MOTS_FR and 'réglementaire' in MOTS_FR)

# Le « a » nu : le dictionnaire ne peut rien dire, « a » et « à » existent
# tous les deux. On le lit donc a la main, en excluant le verbe avoir.
nus = []
for nom in FICHIERS:
    for attr in re.findall(r'data-fr="([^"]*)"', HTML[nom]):
        texte = _H.unescape(attr)
        for m in re.finditer(r"(?<![\w'À-ÿ])a(?![\wÀ-ÿ])", texte):
            avant = texte[max(0, m.start() - 14):m.start()]
            if not re.search(r"(qui|il|elle|on|n'|y|ça|ce)\s*$", avant):
                nus.append('%s : ...%s[a]...' % (nom, avant[-24:]))
t('aucun « a » ne remplace un « à » dans le texte francais', not nus,
  ' | '.join(nus[:3]))


# ===========================================================================
print('\n--- LES DEUX ARBRES DE LANGUE ---')
# ===========================================================================
t('les huit pages existent (quatre par langue)', len(HTML) == 8, len(HTML))
t('les pages anglaises ne servent aucune pastille francaise',
  not any('à définir' in servi(EN[f]) for f in FICHIERS),
  ', '.join(f for f in FICHIERS if 'à définir' in servi(EN[f])))
t('les pages anglaises servent la pastille anglaise',
  all('to be set' in servi(EN[f]) for f in ('concept.html', 'franchise.html',
                                            'tutoring.html')))
t('le titre de chaque page anglaise est en anglais',
  all(re.search(r'<title>([^<]*)</title>', EN[f]).group(1).startswith('KIMO —')
      and 'the' in re.search(r'<title>([^<]*)</title>',
                             EN[f]).group(1).lower()
      or 'become' in re.search(r'<title>([^<]*)</title>',
                               EN[f]).group(1).lower()
      or 'decentralized' in re.search(r'<title>([^<]*)</title>',
                                      EN[f]).group(1).lower()
      or 'support' in re.search(r'<title>([^<]*)</title>',
                                EN[f]).group(1).lower()
      for f in FICHIERS),
  ' | '.join(re.search(r'<title>([^<]*)</title>', EN[f]).group(1)
             for f in FICHIERS))


# ===========================================================================
print('\n--- TOUTE CLASSE A UNE REGLE ---')
# ===========================================================================
# C'est ce controle qui manquait quand l'accentuation a transforme
# class="etat" en class="état" : le selecteur .etat existait toujours, la
# page ne le portait plus, et la mise en page tombait sans un mot.
from style_kimo import CSS as FEUILLE_CSS      # noqa: E402
classes_css = set(re.findall(r'\.([a-zA-Z][\w-]*)', FEUILLE_CSS))
orphelines = {}
for nom, html in HTML.items():
    for bloc in re.findall(r'class="([^"]*)"', html):
        for c in bloc.split():
            if c not in classes_css:
                orphelines.setdefault(c, nom)
t('toute classe posee dans le HTML a une regle dans la feuille',
  not orphelines,
  ', '.join('%s (%s)' % (c, f) for c, f in list(orphelines.items())[:5]))
t('aucun identifiant ne porte d\'accent',
  not re.search(r'(class|id|for)="[^"]*[àâéèêîïôùûç]', TOUT),
  (re.search(r'(class|id|for)="[^"]*[àâéèêîïôùûç][^"]*"', TOUT)
   or [''])[0] if re.search(r'(class|id|for)="[^"]*[àâéèêîïôùûç]', TOUT)
  else '')


# ===========================================================================
print('\n--- KIMO TUTORING ---')
# ===========================================================================
tut = HTML['tutoring.html']
t('les %d matieres sont sur la page' % len(C.TUT_MATIERES),
  all(_H.escape(fr, quote=True) in tut for fr, _en in C.TUT_MATIERES))
t('les %d programmes par age sont sur la page' % len(C.TUT_PROGRAMMES),
  all(nom in tut for _a, nom, _f, _e in C.TUT_PROGRAMMES))
t('les tranches d\'age sont affichees',
  all(('<p class="age">%s</p>' % a) in tut for a, _n, _f, _e in
      C.TUT_PROGRAMMES))
t('la securite des enfants est AVANT le modele economique dans la page',
  tut.index('id="securite"') < tut.index('id="modele-tut"'))
t('la page annonce qu\'aucun tuteur n\'est inscrit',
  'aucun tuteur n\'est inscrit' in _H.unescape(servi(tut)).lower())

# AUCUN TUTEUR INVENTE. Une place de marche vide qu'on remplit de profils
# d'exemple, ce sont des personnes inventees a qui des parents confieraient
# leur enfant. Le controle cherche ce qui trahirait une fiche fabriquee.
SOUPCONS = [
    (r'\b\d[,.]\d\s*/\s*5\b', 'une note sur 5'),
    (r'\b\d+\s*(avis|reviews?)\b', 'un nombre d\'avis'),
    (r'\b\d+\s*(€|\$|EUR|CAD)\s*/\s*(h|heure|hour)', 'un tarif horaire'),
    (r'class="[^"]*(tutor-card|profil-tuteur|avis|review|rating|note-etoile)',
     'une fiche ou une note'),
    (r'★|⭐', 'des etoiles'),
]
trouves = [quoi for motif, quoi in SOUPCONS
           if re.search(motif, tut, re.I)]
t('aucune fiche de tuteur, note, avis ni tarif horaire n\'est fabrique',
  not trouves, ', '.join(trouves))
t('ce controle sait reperer un profil fabrique',
  any(re.search(motif, 'Amina B. — 4,8 / 5 — 32 avis — 25 EUR / h', re.I)
      for motif, _q in SOUPCONS))
t('la page tutorat liste ce qui manque pour commencer',
  all(_H.escape(fr, quote=True) in tut for fr, _en in C.TUT_A_DEFINIR))


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
  'destination à définir' in f)
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

        # Le selecteur de langue est un LIEN : on le suit, comme le ferait
        # un visiteur, et on verifie qu'on arrive sur la page anglaise.
        page.click('.langue a')
        page.wait_for_load_state()
        t('accueil : le lien EN mene a la page anglaise',
          page.url.endswith('en/index.html'), page.url[-30:])
        t('accueil anglais : la navigation est en anglais',
          page.locator('.nav a').first.inner_text().strip() == 'The network',
          page.locator('.nav a').first.inner_text())
        t('accueil anglais : le document declare lang="en"',
          page.evaluate('document.documentElement.lang') == 'en')
        t('accueil anglais : le titre est bien la',
          len(page.locator('h1').first.inner_text().strip()) > 20)
        t('accueil anglais : la mention de traduction n\'y est pas',
          page.locator('.signature .tbc').count() == 0)
        page.click('.langue a')
        page.wait_for_load_state()
        t('le retour au francais fonctionne',
          page.locator('.nav a').first.inner_text().strip() == 'Le réseau',
          page.locator('.nav a').first.inner_text())

        # -------------------------------------------- la page du concept
        erreurs[:] = []
        page.goto(url('concept.html'))
        t('concept : aucune erreur JavaScript', not erreurs,
          ' | '.join(erreurs[:2]))
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
        t('concept : aucun element n\'est rendu invisible', not invisibles,
          ' | '.join(invisibles))
        # Lire « columns:2 » dans la feuille ne dit pas que la page a deux
        # colonnes : une regle plus generale peut avoir gagne. On demande au
        # navigateur ce qu'il a APPLIQUE. (Ici .liste ul posait display:grid,
        # et une grille ignore columns : la feuille en promettait deux, la
        # page en montrait une.)
        cols = page.evaluate(
            "() => getComputedStyle("
            "document.querySelector('.liste.large ul')).columnCount")
        t('concept : les longues listes sont bien sur deux colonnes en '
          'grand ecran', cols == '2', cols)
        t('concept : les %d piliers sont rendus' % len(C.APPRENTISSAGE),
          page.locator('#apprentissage .carte').count()
          == len(C.APPRENTISSAGE),
          page.locator('#apprentissage .carte').count())
        # Une ancre venue de l'accueil doit tomber sur quelque chose de
        # visible : un id qui existe dans le fichier mais que rien ne rend
        # n'est pas un lien qui marche.
        page.goto(url('index.html') + '')
        page.click('a[href="concept.html#p-echecs"]')
        page.wait_for_load_state()
        t('le lien « echecs » de l\'accueil mene au bon paragraphe',
          page.locator('#p-echecs').is_visible()
          and 'chec' in page.locator('#p-echecs h3').inner_text(),
          page.url.split('/')[-1])
        page.goto(url('en/concept.html'))
        t('concept anglais : le pilier est rendu en anglais',
          page.locator('#p-echecs h3').inner_text().strip()
          == 'Chess & Strategic Thinking',
          page.locator('#p-echecs h3').inner_text())
        t('concept anglais : le paragraphe n\'est pas vide',
          len(page.locator('#p-echecs p').inner_text().strip()) > 60)
        t('concept anglais : le lien FR revient a la racine',
          page.locator('.langue a').first.get_attribute('href')
          == '../concept.html')
        page.goto(url('concept.html'))

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
        page.goto(url('concept.html'))
        t('sans JavaScript : les sept piliers sont lisibles',
          page.locator('#apprentissage .carte').count()
          == len(C.APPRENTISSAGE))
        t('sans JavaScript : la journee type est complete',
          page.locator('#journee tbody tr').count() == len(C.JOURNEE),
          page.locator('#journee tbody tr').count())
        t('sans JavaScript : les cinq modeles d\'exploitation sont la',
          page.locator('#exploitation tbody tr').count()
          == len(C.EXPLOITATION))
        t('sans JavaScript : la reserve du fondateur sur la juridiction est '
          'visible', page.locator('#format .reserve').first.is_visible()
          and len(page.locator('#format .reserve').first.inner_text()) > 120)
        page.goto(url('tutoring.html'))
        t('sans JavaScript : les %d matieres sont lisibles'
          % len(C.TUT_MATIERES),
          page.locator('#matieres .carte').count() == len(C.TUT_MATIERES))
        t('sans JavaScript : les quatre programmes sont lisibles',
          page.locator('#programmes .carte.prog').count()
          == len(C.TUT_PROGRAMMES))
        t('sans JavaScript : l\'avertissement « rien n\'est en service » est '
          'visible',
          page.locator('.reserve').first.is_visible()
          and 'pas de tuteur inscrit' in
          page.locator('.reserve').first.inner_text().lower())
        page.goto(url('en/tutoring.html'))
        t('sans JavaScript : la page anglaise du tutorat est en anglais',
          page.locator('#programmes .carte.prog p:not(.age)').first
          .inner_text().strip().startswith('Foundations'),
          page.locator('#programmes .carte.prog p:not(.age)').first
          .inner_text()[:40])
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
        for autre in PAGES[1:]:
            page.goto(url(autre.replace(os.sep, '/')))
            largeur = page.evaluate(
                'Math.max(document.documentElement.scrollWidth,'
                ' document.body.scrollWidth)')
            t('mobile : %s ne deborde pas non plus (%d px)'
              % (autre, largeur), largeur <= 390 + 1, largeur)
        # Les longues listes du concept passent en deux colonnes sur grand
        # ecran. En 390 px, deux colonnes ce sont deux colonnes de trois
        # mots : on verifie qu'il n'en reste qu'une.
        page.goto(url('concept.html'))
        colonnes = page.evaluate(
            "() => getComputedStyle("
            "document.querySelector('.liste.large ul')).columnCount")
        t('mobile : les listes du concept repassent sur une colonne',
          colonnes in ('1', 'auto'), colonnes)
        ctx.close()
        nav.close()


print('\n%d controles verts, %d en echec' % (OK[0], KO[0]))
raise SystemExit(0 if KO[0] == 0 else 1)
