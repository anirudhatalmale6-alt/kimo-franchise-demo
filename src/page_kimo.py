# -*- coding: utf-8 -*-
"""Construit les deux pages de KIMO : l'accueil et la page franchise.

Deux pages, parce qu'il y a deux lecteurs. Un parent veut savoir a quoi
ressemble la creche ; un candidat franchise veut savoir ce que ca coute et
ce qu'il signe. Melanges, on perd les deux.

CE QUI EST CALCULE ICI, ET POURQUOI :

  - le nombre de points « a definir » affiche sur l'accueil est COMPTE dans
    contenu.py. Ecrit a la main, il se serait mis a mentir des la premiere
    valeur remplie ;
  - les resultats de depart du simulateur sont calcules a la construction et
    ecrits dans le HTML. Un visiteur sans JavaScript voit donc un tableau
    rempli, pas des tirets ; et le script, quand il tourne, recalcule les
    memes chiffres. Un controle Playwright verifie que les deux sont
    d'accord — deux implementations de la meme formule, ca finit toujours
    par diverger, autant le savoir tout de suite.
"""

import html as _H
import os
import re

from chemins import dossier_pages
from style_kimo import CSS
import contenu as C

ICI = os.path.dirname(os.path.abspath(__file__))
DEMO = dossier_pages(ICI)


def e(x):
    return _H.escape(str(x), quote=True)


# Le diamant du groupe. COPIE MOT POUR MOT depuis prestige/page_prestige.py,
# jamais redessine : c'est la marque du groupe, elle est la meme partout. Un
# controle compare les deux fichiers et echoue si l'un des deux bouge.
DIAMANT = (
    '<svg class="diamant" viewBox="0 0 24 24" aria-hidden="true" '
    'focusable="false">'
    '<path d="M6 3h12l4 6-10 12L2 9z"/>'
    '<path d="M2 9h20M6 3l3 6M18 3l-3 6M12 3l-3 6M12 3l3 6'
    'M9 9l3 12M15 9l-3 12"/>'
    '</svg>')

TBC_FR = 'a definir'
TBC_EN = 'to be set'


def bi(fr, en, balise='p', classe=''):
    """Un element qui porte SES DEUX langues.

    Les deux attributs vont toujours ensemble : un element qui n'aurait que
    data-fr resterait en francais apres la bascule, sans rien signaler. Un
    controle du fichier verifie qu'aucun n'est seul.
    """
    cl = ' class="%s"' % classe if classe else ''
    return ('<%s%s data-fr="%s" data-en="%s">%s</%s>'
            % (balise, cl, e(fr), e(en), fr, balise))


def tbc():
    """La pastille « a definir ». Visible, pas discrete."""
    return ('<span class="tbc" data-fr="%s" data-en="%s">%s</span>'
            % (e(TBC_FR), e(TBC_EN), TBC_FR))


def nb(n):
    """Un nombre, separateurs par espace INSECABLE.

    Le meme format des deux cotes : le simulateur ecrit ses chiffres a la
    construction (Python) et les recalcule ensuite (JavaScript). Deux
    formats differents et le controle qui les compare devient illisible.
    """
    neg = n < 0
    s = '%d' % abs(int(round(n)))
    out = ''
    while len(s) > 3:
        out = ' ' + s[-3:] + out
        s = s[:-3]
    return ('-' if neg else '') + s + out


def signature():
    """« KIMO — Learn to Think. »

    L'anglais est sa phrase, mot pour mot. Le francais est ma traduction, et
    tant qu'il ne l'a pas confirmee elle porte une mention visible : une
    signature de marque se traduit avec son fondateur, pas a sa place.
    """
    o = ['<p class="signature">']
    o.append('<span data-fr="%s" data-en="%s">%s</span>'
             % (e('%s — %s' % (C.MARQUE, C.SIGNATURE_FR)),
                e('%s — %s' % (C.MARQUE, C.SIGNATURE_EN)),
                e('%s — %s' % (C.MARQUE, C.SIGNATURE_FR))))
    if C.SIGNATURE_TRAD_A_VALIDER:
        o.append('<span class="tbc" data-fr="traduction francaise a valider" '
                 'data-en="English wording is yours, as written">'
                 'traduction francaise a valider</span>')
    o.append('</p>')
    return '\n'.join(o)


def puces(paires, classe='liste'):
    """Une liste a puces bilingue, a partir d'une table de couples (fr, en).

    Les listes de sa note sont des listes : elles restent des listes. Les
    transformer en cartes avec un paragraphe chacune obligerait a inventer le
    paragraphe, et c'est precisement ce que ce site ne fait pas.
    """
    o = ['<div class="%s"><ul>' % classe]
    for fr, en in paires:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    return '\n'.join(o)


def encadre(fr, en, classe='reserve'):
    """Une reserve du fondateur, encadree au lieu d'etre noyee.

    Sa note dit deux fois, noir sur blanc, que la capacite, les taux
    d'encadrement et le modele financier dependent de la juridiction. Ces
    deux phrases-la sont la justification de tous les blancs du site : elles
    ne partent pas en petit gris au bas d'un bloc.
    """
    return ('<div class="%s" data-fr="%s" data-en="%s">%s</div>'
            % (classe, e(fr), e(en), e(fr)))


def titre_bloc(fr, en, dfr=None, den=None):
    o = ['<div class="titre-bloc">', bi(fr, en, 'h2')]
    if dfr is not None:
        o.append(bi(dfr, den))
    o.append('</div>')
    return '\n'.join(o)


# ===========================================================================
#                          EN-TETE, PIED, SQUELETTE
# ===========================================================================
def entete(page):
    def lien(href, cle, fr, en):
        a = ' aria-current="page"' if cle == page else ''
        return ('<a href="%s"%s data-fr="%s" data-en="%s">%s</a>'
                % (href, a, e(fr), e(en), fr))
    return """<header class="haut"><div class="haut-in">
  <a class="marque" href="index.html">__D__<span class="mot">__M__</span></a>
  <nav class="nav">__L1____L2____L3____L4__</nav>
  <div class="langue">
    <button type="button" data-l="fr" aria-pressed="true">FR</button>
    <button type="button" data-l="en" aria-pressed="false">EN</button>
  </div>
</div></header>""" \
        .replace('__D__', DIAMANT).replace('__M__', e(C.MARQUE)) \
        .replace('__L1__', lien('index.html', 'accueil', 'Le reseau',
                                'The network')) \
        .replace('__L2__', lien('concept.html', 'concept', 'Le concept',
                                'The concept')) \
        .replace('__L3__', lien('franchise.html', 'franchise',
                                'Devenir franchise', 'Become a franchisee')) \
        .replace('__L4__', lien('franchise.html#candidature', '',
                                'Candidater', 'Apply'))


def pied():
    o = []
    o.append('<footer><div class="enveloppe">')
    o.append('<p class="devise" data-fr="%s" data-en="%s">%s</p>'
             % (e(C.DEVISE_FR), e(C.DEVISE_EN), e(C.DEVISE_FR)))
    o.append(bi('Hakim Adjaoudi, fondateur — JNCORP INC.',
                'Hakim Adjaoudi, founder — JNCORP INC.', 'p', 'fond'))
    o.append('<div class="avert" data-fr="%s" data-en="%s">%s</div>'
             % (e(C.AVERT_FR), e(C.AVERT_EN), e(C.AVERT_FR)))
    o.append('<div class="liens-sites">'
             '<a href="%s" data-fr="Annuaire des franchises" '
             'data-en="Franchise directory">Annuaire des franchises</a>'
             '<a href="%s" data-fr="Maisons de Prestige" '
             'data-en="Maisons de Prestige">Maisons de Prestige</a>'
             '</div>' % (C.URL_ANNUAIRE, C.URL_PRESTIGE))
    o.append('</div></footer>')
    return '\n'.join(o)


# La bascule de langue. Elle ne connait rien au contenu : elle echange le
# texte de tout element qui porte les deux versions, et previent le reste de
# la page (le simulateur en a besoin pour ses libelles).
JS_LANGUE = """
(function(){
  var L='fr';
  function pose(l){
    L=l;
    document.documentElement.lang=l;
    var n=document.querySelectorAll('[data-fr][data-en]');
    for(var i=0;i<n.length;i++) n[i].innerHTML=n[i].getAttribute('data-'+l);
    var b=document.querySelectorAll('.langue button');
    for(var j=0;j<b.length;j++)
      b[j].setAttribute('aria-pressed',
        b[j].getAttribute('data-l')===l?'true':'false');
    try{localStorage.setItem('kimo-langue',l);}catch(e){}
    if(window.surLangue) window.surLangue(l);
  }
  window.langue=function(){return L;};
  window.poseLangue=pose;
  document.addEventListener('click',function(ev){
    var b=ev.target.closest&&ev.target.closest('.langue button');
    if(b) pose(b.getAttribute('data-l'));
  });
  var m=null; try{m=localStorage.getItem('kimo-langue');}catch(e){}
  pose(m==='en'?'en':'fr');
})();
"""

SQUELETTE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITRE__</title>
<meta name="description" content="__DESC__">
<meta name="robots" content="noindex">
<style>
__CSS__
</style>
</head>
<body>
__CORPS__
<script>
__JS__
</script>
</body>
</html>
"""


def squelette(titre, desc, corps, js):
    return (SQUELETTE.replace('__TITRE__', e(titre))
                     .replace('__DESC__', e(desc))
                     .replace('__CSS__', CSS.strip())
                     .replace('__CORPS__', corps)
                     .replace('__JS__', js.strip()))


# ===========================================================================
#                                 L'ACCUEIL
# ===========================================================================
def page_accueil():
    o = [entete('accueil')]

    # ------------------------------------------------------------------ hero
    o.append('<div class="hero"><div class="enveloppe"><div class="hero-in">')
    o.append('<div>')
    o.append(bi('Reseau decentralise d\'eveil et d\'apprentissage',
                'Decentralized early-learning network', 'p', 'surtitre'))
    o.append(bi('Une creche a taille humaine, la ou les familles habitent.',
                'A nursery on a human scale, where families actually live.',
                'h1'))
    o.append(signature())
    o.append(bi('KIMO ouvre de petites unites de quartier, tenues par des '
                'equipes locales, avec un meme programme, une meme plateforme '
                'et un meme systeme qualite. On y travaille la logique, les '
                'echecs, les mathematiques, les sciences, l\'histoire, le '
                'mouvement et la creation — par le jeu, jamais par la lecon.',
                'KIMO opens small neighbourhood units, run by local teams, '
                'sharing one educational program, one platform and one '
                'quality system. Logic, chess, mathematics, science, history, '
                'movement and creativity — through play, never through '
                'lessons.',
                'p', 'chapo'))
    o.append('<div class="actions">'
             '<a class="bouton plein" href="concept.html" '
             'data-fr="Lire le concept" data-en="Read the concept">'
             'Lire le concept</a>'
             '<a class="bouton vide" href="franchise.html" '
             'data-fr="Ouvrir une KIMO" data-en="Open a KIMO">'
             'Ouvrir une KIMO</a></div>')
    o.append('</div>')

    # L'etat du reseau. Pas de compteur : il n'y a rien a compter, et un
    # « 0 creche » en gros chiffre serait la seule statistique du site.
    o.append('<div class="etat">')
    o.append(bi('Etat du reseau', 'Network status', 'h3'))
    o.append('<ul>')
    o.append('<li>' + bi('Reseau en cours de constitution : la premiere '
                         'creche n\'est pas encore ouverte.',
                         'Network being set up: the first nursery has not '
                         'opened yet.', 'span') + '</li>')
    o.append('<li><span>' + bi('Pays et ville de la premiere ouverture',
                               'Country and city of the first opening',
                               'span') + ' — ' + tbc() + '</span></li>')
    o.append('<li><span>' + bi('Cadre reglementaire applicable',
                               'Applicable regulatory framework', 'span')
             + ' — ' + tbc() + '</span></li>')
    o.append('<li>' + bi('Les candidatures de franchises sont ouvertes des '
                         'maintenant.',
                         'Franchise applications are open now.', 'span')
             + '</li>')
    o.append('</ul></div>')
    o.append('</div></div></div>')

    # ---------------------------------------------------------- le modele
    o.append('<section id="modele"><div class="enveloppe">')
    o.append('<div class="titre-bloc">')
    o.append(bi('Pourquoi decentralise', 'Why decentralised', 'h2'))
    o.append(bi('Le modele n\'est pas une creche plus petite par manque de '
                'moyens. C\'est un choix : beaucoup de petites unites '
                'valent mieux qu\'une grande, a condition que le reseau '
                'porte tout ce qu\'une petite unite ne sait pas porter '
                'seule.',
                'The model is not a smaller nursery for lack of means. It is '
                'a choice: many small units beat one large one — provided '
                'the network carries everything a small unit cannot carry '
                'alone.'))
    o.append('</div><div class="grille g2">')
    for _cle, fr, en, dfr, den in C.PILIERS:
        o.append('<div class="carte">' + bi(fr, en, 'h3') + bi(dfr, den)
                 + '</div>')
    o.append('</div></div></section>')

    # --------------------------------------------------------- la methode
    # Le texte de ce bloc vient de sa note. Il n'y a donc plus de pastille
    # « a valider » ici : elle disait que la redaction etait de moi, ce qui
    # n'est plus vrai. Une pastille qu'on laisse quand elle a cesse d'etre
    # exacte apprend au lecteur a ne plus les lire.
    o.append('<section id="methode" class="pale"><div class="enveloppe">')
    o.append(titre_bloc('La methode', 'The method',
                        C.METHODE_INTRO_FR, C.METHODE_INTRO_EN))
    o.append(puces(C.METHODE, 'liste large'))
    o.append('<div class="apres">')
    o.append('<a class="bouton vide" href="concept.html#apprentissage" '
             'data-fr="Les sept piliers d\'apprentissage" '
             'data-en="The seven learning pillars">'
             'Les sept piliers d\'apprentissage</a>')
    o.append('</div>')
    o.append('</div></section>')

    # -------------------------------------------------- piliers, en resume
    o.append('<section id="piliers"><div class="enveloppe">')
    o.append(titre_bloc(
        'Ce qu\'on y travaille', 'What is worked on',
        'Sept domaines, tous abordes par le jeu. Le detail de chacun est sur '
        'la page du concept.',
        'Seven areas, all approached through play. Each one is detailed on '
        'the concept page.'))
    o.append('<div class="grille g4 serree">')
    for cle, fr, en, _dfr, _den in C.APPRENTISSAGE:
        o.append('<a class="carte mini" href="concept.html#p-%s">%s</a>'
                 % (e(cle), bi(fr, en, 'h3')))
    o.append('</div></div></section>')

    # ---------------------------------------------------- reglementaire
    o.append('<section id="cadre"><div class="enveloppe">')
    o.append('<div class="titre-bloc">')
    o.append(bi('Le cadre reglementaire', 'The regulatory framework', 'h2'))
    o.append(bi('Une micro-creche est un etablissement autorise. Le nombre '
                'de places, le taux d\'encadrement, la qualification du '
                'responsable et la surface par enfant sont fixes par le '
                'droit du pays, et parfois de la region. Rien n\'est ecrit '
                'ici tant que ce n\'est pas verifie dans le pays retenu : '
                'un candidat construit son local et son financement sur ces '
                'lignes.',
                'A micro-nursery is a licensed facility. The number of '
                'places, the staff ratio, the manager\'s qualification and '
                'the floor area per child are set by national — sometimes '
                'regional — law. Nothing is written here until it has been '
                'checked in the chosen country: a candidate builds their '
                'premises and their financing on these lines.'))
    o.append('</div><div class="enrouleur"><table class="tab"><tbody>')
    for _cle, fr, en, dfr, den, valeur in C.REGLEMENTAIRE:
        val = e(valeur) if valeur else tbc()
        o.append('<tr>' + bi(fr, en, 'th') + '<td class="val">' + val
                 + '</td><td class="exp">'
                 + bi(dfr, den, 'span') + '</td></tr>')
    o.append('</tbody></table></div>')
    # Sa propre reserve, citee ici : c'est lui qui ecrit que la capacite
    # definitive et les taux d'encadrement doivent etre adaptes a la
    # juridiction. Les blancs de ce tableau ne sont pas une prudence de
    # developpeur, ils appliquent ce qu'il a ecrit.
    o.append(encadre(C.FORMAT_AVERT_FR, C.FORMAT_AVERT_EN))
    o.append('</div></section>')

    # ------------------------------------------------------------ bandeau
    o.append('<section class="pale"><div class="enveloppe">'
             '<div class="bandeau"><div>')
    o.append(bi('Ouvrir une KIMO dans votre ville', 'Open a KIMO in your city',
                'h2'))
    o.append(bi('Le parcours, ce que le reseau apporte, un simulateur de '
                'compte d\'exploitation et le formulaire de candidature.',
                'The journey, what the network provides, a P&L simulator and '
                'the application form.'))
    o.append('</div><a class="bouton plein" href="franchise.html" '
             'data-fr="Voir la page franchise" data-en="See the franchise page"'
             '>Voir la page franchise</a>')
    o.append('</div></div></section>')

    o.append(pied())
    return squelette('KIMO — reseau de micro-creches decentralisees',
                     'KIMO ouvre de petites creches de quartier tenues par '
                     'des responsables independants, avec une methode '
                     'commune.',
                     '\n'.join(o), JS_LANGUE)


# ===========================================================================
#                               LE CONCEPT
#
# Cette page est sa note mise en page. Elle ne resume pas et n'arrondit pas :
# un candidat, un partenaire immobilier ou une mairie qui demande « c'est
# quoi KIMO » doit trouver le document, pas une plaquette qui en donne
# l'impression.
#
# Deux choses y sont dites une bonne fois, en haut, et pas au detour d'une
# ligne : d'ou vient le texte, et que le francais est une traduction.
# ===========================================================================
def page_concept():
    o = [entete('concept')]

    # ------------------------------------------------------------------ hero
    o.append('<div class="hero"><div class="enveloppe"><div class="hero-in">')
    o.append('<div>')
    o.append(bi('Le concept', 'The concept', 'p', 'surtitre'))
    o.append(bi('Un seul ecosysteme educatif, beaucoup de centres locaux.',
                'One educational ecosystem, many local centers.', 'h1'))
    o.append(signature())
    o.append(bi('Un enfant ne devrait pas seulement retenir des reponses : il '
                'devrait apprendre peu a peu a observer, raisonner, '
                'experimenter, expliquer et chercher une solution. Les '
                'matieres sont introduites par le jeu adapte a son age, pas '
                'par l\'ecole avant l\'ecole.',
                'Children should not only memorize answers; they should '
                'gradually learn how to observe, reason, experiment, '
                'communicate and find solutions. Academic subjects are '
                'introduced through age-appropriate play rather than formal '
                'schooling.', 'p', 'chapo'))
    o.append('</div>')

    # D'ou vient ce texte. Une page de concept sans provenance se lit comme
    # une redaction d'agence ; celle-ci n'en est pas une.
    o.append('<div class="etat">')
    o.append(bi('D\'ou vient cette page', 'Where this page comes from', 'h3'))
    o.append('<ul>')
    o.append('<li>' + bi('Le texte est celui de la note de concept du '
                         'fondateur. Il n\'a pas ete resume.',
                         'The text is the founder\'s concept note. It has not '
                         'been summarised.', 'span') + '</li>')
    o.append('<li>' + bi('La version anglaise est la sienne, mot pour mot.',
                         'The English version is his, word for word.',
                         'span') + '</li>')
    o.append('<li><span>' + bi('La version francaise est une traduction',
                               'The French version is a translation', 'span')
             + ' — ' + tbc() + '</span></li>')
    o.append('<li>' + bi('Les chiffres reglementaires et commerciaux restent '
                         'vides : voir le cadre reglementaire.',
                         'Regulatory and commercial figures remain blank: see '
                         'the regulatory framework.', 'span') + '</li>')
    o.append('</ul></div>')
    o.append('</div></div></div>')

    # ------------------------------------------------- 3. modele decentralise
    o.append('<section id="couches"><div class="enveloppe">')
    o.append(titre_bloc(
        'Qui fait quoi', 'Who does what',
        'Le reseau ne se contente pas de preter une marque : il tient le '
        'programme, la technologie, la formation et le controle. L\'unite '
        'locale tient l\'enfant et la famille.',
        'The network does more than lend a brand: it holds the program, the '
        'technology, the training and the audit. The local unit holds the '
        'child and the family.'))
    o.append('<div class="enrouleur"><table class="tab large"><thead><tr>'
             + bi('Niveau', 'Layer', 'th')
             + bi('Responsabilite', 'Responsibility', 'th')
             + bi('Exemples', 'Examples', 'th')
             + '</tr></thead><tbody>')
    for nfr, nen, rfr, ren, efr, een in C.COUCHES:
        o.append('<tr>' + bi(nfr, nen, 'th') + '<td>' + bi(rfr, ren, 'span')
                 + '</td><td class="exp">' + bi(efr, een, 'span')
                 + '</td></tr>')
    o.append('</tbody></table></div></div></section>')

    # -------------------------------------------------------- 4. le format
    o.append('<section id="format" class="pale"><div class="enveloppe">')
    o.append(titre_bloc(
        'Le format d\'une unite', 'Center format',
        'Petit, proche, et concu pour cela — pas une grande structure '
        'retrecie.',
        'Small, close by, and designed that way — not a large facility '
        'shrunk down.'))
    o.append(puces(C.FORMAT, 'liste large'))
    o.append(encadre(C.FORMAT_AVERT_FR, C.FORMAT_AVERT_EN))
    o.append('</div></section>')

    # ------------------------------------------------------- 5. la methode
    o.append('<section id="philosophie"><div class="enveloppe">')
    o.append(titre_bloc('La philosophie pedagogique',
                        'Educational philosophy',
                        C.METHODE_INTRO_FR, C.METHODE_INTRO_EN))
    o.append(puces(C.METHODE, 'liste large'))
    o.append('</div></section>')

    # ------------------------------------------------------- 6. les piliers
    o.append('<section id="apprentissage" class="pale">'
             '<div class="enveloppe">')
    o.append(titre_bloc(
        'Les sept piliers d\'apprentissage', 'The seven learning pillars',
        'Chacun est un support de jeu, pas une matiere a evaluer.',
        'Each one is a support for play, not a subject to be graded.'))
    o.append('<div class="grille g2">')
    for cle, fr, en, dfr, den in C.APPRENTISSAGE:
        o.append('<div class="carte" id="p-%s">' % e(cle)
                 + bi(fr, en, 'h3') + bi(dfr, den) + '</div>')
    o.append('</div></div></section>')

    # -------------------------------------------------- 7. le parcours d'age
    o.append('<section id="ages"><div class="enveloppe">')
    o.append(titre_bloc(
        'Un exemple de progression par age',
        'Example learning journey by age',
        'Un exemple, pas un calendrier : la difficulte se regle sur la '
        'maturite de l\'enfant, c\'est le sixieme principe de la methode.',
        'An example, not a schedule: complexity follows the child\'s '
        'readiness — that is the sixth principle of the method.'))
    o.append('<div class="enrouleur"><table class="tab large"><thead><tr>'
             + bi('Etape', 'Stage', 'th')
             + bi('Ce qu\'on travaille', 'Learning focus', 'th')
             + bi('Activites types', 'Typical activities', 'th')
             + bi('Facon de faire', 'Approach', 'th')
             + '</tr></thead><tbody>')
    for sfr, sen, ffr, fen, afr, aen, mfr, men in C.AGES:
        o.append('<tr>' + bi(sfr, sen, 'th')
                 + '<td>' + bi(ffr, fen, 'span') + '</td>'
                 + '<td class="exp">' + bi(afr, aen, 'span') + '</td>'
                 + '<td class="exp">' + bi(mfr, men, 'span') + '</td></tr>')
    o.append('</tbody></table></div></div></section>')

    # ------------------------------------------------------ 8. journee type
    o.append('<section id="journee" class="pale"><div class="enveloppe">')
    o.append(titre_bloc(
        'Une journee type', 'Example daily schedule',
        'Les activites dirigees occupent moins de deux heures. Le reste est '
        'du jeu, du mouvement, des repas et du repos.',
        'Structured activities take under two hours. The rest is play, '
        'movement, meals and rest.'))
    o.append('<div class="enrouleur"><table class="tab horaire"><tbody>')
    for heure, afr, aen in C.JOURNEE:
        o.append('<tr><th class="h">%s</th><td>%s</td></tr>'
                 % (e(heure), bi(afr, aen, 'span')))
    o.append('</tbody></table></div></div></section>')

    # ------------------------------------------ 9 + 11. educateurs, parents
    o.append('<section id="equipe"><div class="enveloppe">')
    o.append(titre_bloc('Les educateurs, les parents',
                        'Educators, parents',
                        C.EDUCATEURS_INTRO_FR, C.EDUCATEURS_INTRO_EN))
    o.append('<div class="listes">')
    o.append('<div class="liste accent">'
             + bi('Ce que le reseau demande a ses educateurs',
                  'What the network asks of its educators', 'h3') + '<ul>')
    for fr, en in C.EDUCATEURS:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('<div class="liste">'
             + bi('Ce que voit un parent', 'What a parent gets', 'h3')
             + '<ul>')
    for fr, en in C.PARENTS:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('</div></div></section>')

    # ---------------------------------------------------- 10. la plateforme
    o.append('<section id="plateforme" class="pale"><div class="enveloppe">')
    o.append(titre_bloc(
        'La plateforme', 'The digital platform',
        'Un compte pour la famille, un outil de travail pour l\'educateur, '
        'un tableau de bord pour le reseau. Ce sont trois lecteurs, pas un.',
        'One account for the family, one working tool for the educator, one '
        'dashboard for the network. Three readers, not one.'))
    o.append(puces(C.PLATEFORME, 'liste large'))
    o.append(encadre(C.PLATEFORME_NOTE_FR, C.PLATEFORME_NOTE_EN))
    o.append('</div></section>')

    # ------------------------------------------- 12 + 13. securite, qualite
    o.append('<section id="securite"><div class="enveloppe">')
    o.append(titre_bloc('Securite, protection de l\'enfance, qualite',
                        'Safety, safeguarding, quality',
                        C.SECURITE_INTRO_FR, C.SECURITE_INTRO_EN))
    o.append('<div class="listes">')
    o.append('<div class="liste">'
             + bi('Ce qui doit etre en place dans chaque unite',
                  'What must be in place in every unit', 'h3') + '<ul>')
    for fr, en in C.SECURITE:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('<div class="liste">'
             + bi('Ce que le reseau controle', 'What the network audits', 'h3')
             + '<ul>')
    for fr, en in C.QUALITE:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('</div></div></section>')

    # ------------------------------------------------- 14. les cinq modeles
    o.append('<section id="exploitation" class="pale">'
             '<div class="enveloppe">')
    o.append(titre_bloc(
        'Cinq facons d\'ouvrir un centre', 'Five ways to open a center',
        'La franchise est l\'une des cinq. C\'est la seule qui se candidate : '
        'les quatre autres se negocient.',
        'Franchise is one of the five. It is the only one you apply for: the '
        'other four are negotiated.'))
    o.append('<div class="enrouleur"><table class="tab large"><thead><tr>'
             + bi('Modele', 'Model', 'th')
             + bi('Description', 'Description', 'th')
             + bi('Recettes', 'Revenue', 'th')
             + '</tr></thead><tbody>')
    for _cle, nfr, nen, dfr, den, rfr, ren, mis in C.EXPLOITATION:
        cl = ' class="mis"' if mis else ''
        o.append('<tr%s>' % cl + bi(nfr, nen, 'th')
                 + '<td>' + bi(dfr, den, 'span') + '</td>'
                 + '<td class="exp">' + bi(rfr, ren, 'span')
                 + '</td></tr>')
    o.append('</tbody></table></div>')
    o.append('<div class="apres"><a class="bouton plein" href="franchise.html"'
             ' data-fr="La franchise en detail" '
             'data-en="The franchise in detail">La franchise en detail</a>'
             '</div>')
    o.append('</div></section>')

    # ----------------------------------------------- 15 + 16. couts et KPI
    o.append('<section id="economie"><div class="enveloppe">')
    o.append(titre_bloc(
        'Ce que coute un centre, ce qu\'on y mesure',
        'What a center costs, what gets measured',
        'Aucun montant n\'est avance ici, et ce n\'est pas un oubli : c\'est '
        'sa propre consigne, rappelee sous le tableau.',
        'No amount is stated here, and that is not an omission: it is his own '
        'instruction, repeated below the table.'))
    o.append('<div class="listes">')
    o.append('<div class="liste">'
             + bi('Les postes de cout', 'Cost structure', 'h3') + '<ul>')
    for fr, en in C.COUTS:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('<div class="liste">'
             + bi('Les indicateurs du reseau', 'Network KPIs', 'h3') + '<ul>')
    for fr, en in C.KPI:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('</div>')
    o.append(encadre(C.COUTS_NOTE_FR, C.COUTS_NOTE_EN))
    o.append('</div></section>')

    # ------------------------------------------- 17 + 18. phases et pilote
    o.append('<section id="phases" class="pale"><div class="enveloppe">')
    o.append(titre_bloc(
        'Le deploiement, en cinq phases', 'Deployment, in five phases',
        'Aucune duree n\'est portee sur ces phases : la duree de la phase 1 '
        'depend de l\'autorite d\'agrement du pays retenu, et le pays n\'est '
        'pas arrete.',
        'No durations are attached to these phases: phase 1 depends on the '
        'licensing authority of the chosen country, and the country is not '
        'settled.'))
    o.append('<div class="etapes">')
    for num, fr, en, dfr, den in C.PHASES:
        o.append('<div class="etape"><div class="num">%s</div><div>'
                 % e(num))
        o.append(bi(fr, en, 'h3'))
        o.append(bi(dfr, den))
        o.append('</div></div>')
    o.append('</div>')
    o.append('<div class="apres-liste">')
    o.append(bi('Ce que le pilote doit prouver avant la phase 3',
                'What the pilot must prove before phase 3', 'h3'))
    o.append(puces(C.PILOTE, 'liste large'))
    o.append('</div>')
    o.append('</div></section>')

    # ---------------------------------------------------------- 19. risques
    o.append('<section id="risques"><div class="enveloppe">')
    o.append(titre_bloc(
        'Les risques, et ce qu\'on leur oppose', 'Risks and mitigation',
        'Un reseau decentralise a des faiblesses propres, et elles sont '
        'connues. Les nommer vaut mieux que de les decouvrir au troisieme '
        'centre.',
        'A decentralised network has its own weaknesses, and they are known. '
        'Naming them beats discovering them at the third center.'))
    o.append('<div class="enrouleur"><table class="tab large"><thead><tr>'
             + bi('Risque', 'Risk', 'th')
             + bi('Ce qu\'on lui oppose', 'Mitigation', 'th')
             + '</tr></thead><tbody>')
    for rfr, ren, mfr, men in C.RISQUES:
        o.append('<tr>' + bi(rfr, ren, 'th') + '<td>'
                 + bi(mfr, men, 'span') + '</td></tr>')
    o.append('</tbody></table></div></div></section>')

    # -------------------------------------------------- 20 + 21. marque, suite
    o.append('<section id="marque" class="pale"><div class="enveloppe">')
    o.append(titre_bloc(
        'L\'architecture de marque, et ce qui vient apres',
        'Brand architecture, and what comes next'))
    o.append('<div class="listes">')
    o.append('<div class="liste">'
             + bi('La marque', 'The brand', 'h3') + '<ul>')
    for fr, en in C.ARCHI_MARQUE:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('<div class="liste">'
             + bi('Apres le reseau de centres', 'Beyond the center network',
                  'h3')
             + bi(C.HORIZON_FR, C.HORIZON_EN) + '</div>')
    o.append('</div></div></section>')

    # ------------------------------------------------------------ bandeau
    o.append('<section><div class="enveloppe"><div class="bandeau"><div>')
    o.append(bi('Ouvrir une KIMO dans votre ville',
                'Open a KIMO in your city', 'h2'))
    o.append(bi('Le parcours d\'un candidat, ce que le reseau apporte, un '
                'simulateur de compte d\'exploitation et le formulaire.',
                'The candidate journey, what the network provides, a P&L '
                'simulator and the form.'))
    o.append('</div><a class="bouton plein" href="franchise.html" '
             'data-fr="Voir la page franchise" '
             'data-en="See the franchise page">Voir la page franchise</a>')
    o.append('</div></div></section>')

    o.append(pied())
    return squelette(
        'KIMO — le concept',
        'Le modele decentralise KIMO : format des unites, philosophie '
        'pedagogique, sept piliers d\'apprentissage, journee type, '
        'plateforme, securite, deploiement.',
        '\n'.join(o), JS_LANGUE)


# ===========================================================================
#                            LE SIMULATEUR (formule)
# ===========================================================================
def defauts():
    return dict((c[0], c[3]) for c in C.SIM_CHAMPS)


def calcul(v):
    """LA formule, une seule fois en Python.

    Elle est reecrite en JavaScript plus bas — c'est inevitable, la page doit
    recalculer sans rechargement. Ce qui n'est pas inevitable, c'est que
    personne ne s'apercoive qu'elles ont diverge : un controle Playwright
    ouvre la page et compare les valeurs affichees a celles-ci.
    """
    produits = v['places'] * v['occupation'] / 100.0 * v['tarif']
    redevance = produits * v['redevance'] / 100.0
    masse = v['etp'] * v['salaire']
    fixes = v['loyer'] + masse + v['autres']
    charges = fixes + redevance
    resultat = produits - charges
    denom = v['places'] * v['tarif'] * (1 - v['redevance'] / 100.0)
    seuil = (fixes / denom * 100.0) if denom > 0 else 0.0
    return {'produits': produits, 'redevance': redevance, 'masse': masse,
            'charges': charges, 'resultat': resultat,
            'annuel': resultat * 12, 'seuil': seuil}


SORTIES = [
    ('produits', 'Produits mensuels', 'Monthly revenue', 'devise', False),
    ('masse', 'Dont masse salariale', 'Of which payroll', 'devise', False),
    ('redevance', 'Dont redevance reseau', 'Of which network royalty',
     'devise', False),
    ('charges', 'Total des charges', 'Total costs', 'devise', False),
    ('resultat', 'Resultat mensuel', 'Monthly result', 'devise', True),
    ('annuel', 'Resultat annuel', 'Annual result', 'devise', True),
    ('seuil', 'Occupation au point mort', 'Break-even occupancy', 'pourcent',
     False),
]


# ===========================================================================
#                            LA PAGE FRANCHISE
# ===========================================================================
def page_franchise():
    o = [entete('franchise')]

    # ------------------------------------------------------------------ hero
    o.append('<div class="hero"><div class="enveloppe"><div class="hero-in">')
    o.append('<div>')
    o.append(bi('Franchise', 'Franchise', 'p', 'surtitre'))
    o.append(bi('Tenir une creche de quartier, avec un reseau derriere.',
                'Run a neighbourhood nursery, with a network behind you.',
                'h1'))
    o.append(bi('Le franchise possede son entreprise, son bail et son fonds. '
                'Le reseau lui apporte la marque, la methode ecrite, la '
                'formation, le logiciel et l\'etude de sa zone — et il '
                'l\'accompagne jusqu\'a l\'ouverture.',
                'The franchisee owns their company, their lease and their '
                'business. The network brings the brand, the written method, '
                'the training, the software and the territory study — and '
                'stays alongside until opening day.', 'p', 'chapo'))
    o.append('<div class="actions">'
             '<a class="bouton plein" href="#candidature" '
             'data-fr="Deposer une candidature" data-en="Apply now">'
             'Deposer une candidature</a>'
             '<a class="bouton vide" href="#simulateur" '
             'data-fr="Simuler un compte d\'exploitation" '
             'data-en="Run a P&amp;L simulation">'
             'Simuler un compte d\'exploitation</a></div>')
    o.append('</div>')

    # Ce qui manque, en clair, des le haut de la page franchise. Un candidat
    # qui decouvre a l'etape 4 que le droit d'entree n'est pas fixe se sent
    # promene ; qui le lit ici ne se sent pas promene, il attend.
    o.append('<div class="etat">')
    o.append(bi('Ce qui n\'est pas encore arrete',
                'What has not been settled yet', 'h3'))
    o.append('<ul>')
    for _cle, fr, _pour in C.A_DEFINIR:
        o.append('<li><span>' + e(fr) + '</span></li>')
    o.append('</ul>')
    o.append(bi('Ces points sont affiches « a definir » partout ou ils '
                'apparaissent, plutot que remplis par un ordre de grandeur.',
                'These are shown as "to be set" wherever they appear, rather '
                'than filled in with a ballpark.', 'p', 'note'))
    o.append('</div>')
    o.append('</div></div></div>')

    # Un candidat doit savoir qu'il n'est pas le seul chemin d'ouverture :
    # sa note en prevoit cinq, et un exploitant qui l'apprend apres coup se
    # demande ce qu'on lui a cache. Une ligne suffit, avec le lien.
    o.append('<section class="mince"><div class="enveloppe">')
    o.append('<div class="rappel-modele">'
             + bi('La franchise est l\'un des cinq modeles d\'exploitation du '
                  'reseau — les autres sont l\'exploitation en propre, le '
                  'centre d\'employeur, le partenariat immobilier et le '
                  'partenariat public.',
                  'Franchise is one of the network\'s five operating models — '
                  'the others are company-owned, employer centers, '
                  'real-estate partnerships and public partnerships.', 'p')
             + '<a href="concept.html#exploitation" '
               'data-fr="Voir les cinq" data-en="See all five">'
               'Voir les cinq</a></div>')
    o.append('</div></section>')

    # ---------------------------------------------------------- le parcours
    o.append('<section id="parcours"><div class="enveloppe">')
    o.append('<div class="titre-bloc">')
    o.append(bi('Le parcours, en six etapes', 'The journey, in six steps',
                'h2'))
    o.append(bi('L\'ordre compte : le local et l\'agrement viennent avant la '
                'formation. Une autorite qui refuse un local apres la '
                'formation a fait perdre les deux.',
                'The order matters: premises and licence come before '
                'training. An authority refusing premises after training has '
                'wasted both.'))
    o.append('</div><div class="etapes">')
    for num, fr, en, dfr, den, duree in C.PARCOURS:
        o.append('<div class="etape"><div class="num">%s</div><div>' % e(num))
        o.append('<div class="pastille-titre">' + bi(fr, en, 'h3')
                 + ('' if duree else '') + '</div>')
        o.append(bi(dfr, den))
        o.append('</div></div>')
    o.append('</div>')
    o.append(bi('Les durees ne sont pas indiquees : celle de l\'etape 4 '
                'depend du delai de l\'autorite qui delivre l\'agrement, '
                'donc du pays. Elle sera ecrite ici quand le pays sera '
                'arrete.',
                'No durations are given: step 4 depends on the lead time of '
                'the licensing authority, and therefore on the country. It '
                'will appear here once the country is settled.', 'p', 'note'))
    o.append('</div></section>')

    # ------------------------------------------------------- qui apporte quoi
    o.append('<section class="pale"><div class="enveloppe">')
    o.append('<div class="titre-bloc">')
    o.append(bi('Qui apporte quoi', 'Who brings what', 'h2'))
    o.append(bi('Une franchise se juge sur cette page, pas sur une brochure.',
                'A franchise is judged on this page, not on a brochure.'))
    o.append('</div><div class="listes">')
    o.append('<div class="liste accent">' + bi('Le reseau apporte',
                                               'The network brings', 'h3')
             + '<ul>')
    for fr, en in C.RESEAU_APPORTE:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('<div class="liste">' + bi('Le franchise apporte',
                                        'The franchisee brings', 'h3')
             + '<ul>')
    for fr, en in C.FRANCHISE_APPORTE:
        o.append('<li>' + bi(fr, en, 'span') + '</li>')
    o.append('</ul></div>')
    o.append('</div></div></section>')

    # ------------------------------------------------------ modele economique
    o.append('<section id="modele-eco"><div class="enveloppe">')
    o.append('<div class="titre-bloc">')
    o.append(bi('Le modele economique', 'The economics', 'h2'))
    o.append(bi('Les montants ne sont pas encore arretes. Ils apparaissent '
                'donc en clair comme non fixes : un candidat batit son plan '
                'de financement sur ces lignes, et un ordre de grandeur '
                'invente lui couterait cher.',
                'The amounts have not been set. They therefore appear plainly '
                'as unset: a candidate builds their financing plan on these '
                'lines, and an invented ballpark would cost them dearly.'))
    o.append('</div><div class="enrouleur"><table class="tab"><tbody>')
    for _cle, fr, en, montant, _unite, dfr, den in C.MODELE:
        val = e(montant) if montant is not None else tbc()
        o.append('<tr>' + bi(fr, en, 'th') + '<td class="val">' + val
                 + '</td><td class="exp">' + bi(dfr, den, 'span')
                 + '</td></tr>')
    o.append('</tbody></table></div></div></section>')

    # ------------------------------------------------------------ simulateur
    o.append(bloc_simulateur())

    # ---------------------------------------------------------------- profil
    o.append('<section><div class="enveloppe">')
    o.append('<div class="titre-bloc">')
    o.append(bi('Le profil recherche', 'The profile we look for', 'h2'))
    o.append('</div><div class="grille g4">')
    for fr, en in C.PROFIL:
        o.append('<div class="carte">' + bi(fr, en) + '</div>')
    o.append('</div></div></section>')

    # ----------------------------------------------------------- candidature
    o.append(bloc_formulaire())

    # ------------------------------------------------------------------- faq
    o.append('<section id="faq"><div class="enveloppe">')
    o.append('<div class="titre-bloc">' + bi('Questions', 'Questions', 'h2')
             + '</div><div class="faq">')
    for qfr, qen, rfr, ren in C.FAQ:
        o.append('<details><summary data-fr="%s" data-en="%s">%s</summary>%s'
                 '</details>' % (e(qfr), e(qen), qfr, bi(rfr, ren)))
    o.append('</div></div></section>')

    o.append(pied())
    return squelette('KIMO — devenir franchise',
                     'Ouvrir une micro-creche KIMO : le parcours, ce que le '
                     'reseau apporte, un simulateur et le formulaire de '
                     'candidature.',
                     '\n'.join(o), JS_LANGUE + JS_SIMU + JS_FORM)


def bloc_simulateur():
    v = defauts()
    r = calcul(v)

    o = ['<section id="simulateur" class="pale"><div class="enveloppe">']
    o.append('<div class="titre-bloc">')
    o.append(bi('Simulateur de compte d\'exploitation',
                'P&L simulator', 'h2'))
    o.append('<p class="note" data-fr="%s" data-en="%s">%s</p>'
             % (e(C.SIM_NOTE_FR), e(C.SIM_NOTE_EN), e(C.SIM_NOTE_FR)))
    o.append('</div><div class="simu">')

    # -------------------------------------------------------------- entrees
    o.append('<div class="champs">')
    o.append('<div class="champ">'
             '<label for="s-devise" data-fr="Monnaie" data-en="Currency">'
             'Monnaie</label><select id="s-devise">')
    for code, _sym in C.DEVISES:
        o.append('<option value="%s">%s</option>' % (code, code))
    o.append('</select></div>')
    for cle, fr, en, val, pas, unite in C.SIM_CHAMPS:
        suff = ' (%)' if unite == 'pourcent' else ''
        o.append('<div class="champ">')
        o.append('<label for="s-%s" data-fr="%s" data-en="%s">%s</label>'
                 % (cle, e(fr + suff), e(en + suff), e(fr + suff)))
        o.append('<input type="number" id="s-%s" data-cle="%s" value="%d" '
                 'step="%d" min="0" inputmode="numeric">'
                 % (cle, cle, val, pas))
        o.append('</div>')
    o.append('</div>')

    # -------------------------------------------------------------- sorties
    o.append('<div class="sortie">')
    o.append(bi('Par mois, hors impots et amortissements',
                'Per month, before tax and depreciation', 'h3'))
    o.append('<dl>')
    for cle, fr, en, unite, fort in SORTIES:
        cls = 'ligne' + (' fort' if fort else '')
        txt = (nb(r[cle]) + ' <span class="dev">EUR</span>'
               if unite == 'devise' else nb(r[cle]) + ' %')
        o.append('<div class="%s" data-sortie="%s">'
                 '<dt data-fr="%s" data-en="%s">%s</dt>'
                 '<dd id="r-%s">%s</dd></div>'
                 % (cls, cle, e(fr), e(en), fr, cle, txt))
    o.append('</dl>')
    o.append('<p class="rappel" data-fr="%s" data-en="%s">%s</p>'
             % (e('Le point mort est le taux d\'occupation a partir duquel '
                  'le resultat devient positif, aux memes charges.'),
                e('Break-even is the occupancy rate at which the result turns '
                  'positive, at the same cost base.'),
                e('Le point mort est le taux d\'occupation a partir duquel le '
                  'resultat devient positif, aux memes charges.')))
    o.append('</div>')

    o.append('</div></div></section>')
    return '\n'.join(o)


def bloc_formulaire():
    o = ['<section id="candidature"><div class="enveloppe">']
    o.append('<div class="titre-bloc">')
    o.append(bi('Deposer une candidature', 'Apply', 'h2'))
    o.append(bi('Les champs marques d\'une etoile sont obligatoires. Une '
                'candidature ne vous engage a rien : elle ouvre un '
                'entretien.',
                'Fields marked with a star are required. Applying commits you '
                'to nothing: it opens a conversation.'))
    o.append('</div>')

    # L'identifiant du formulaire est UNIQUE dans la page — la section
    # s'appelle « candidature », le formulaire « demande ». Deux elements de
    # meme id et getElementById rend le premier : l'ecouteur se pose sur la
    # section, le formulaire part en envoi natif, la page se recharge, et
    # rien ne signale l'erreur.
    o.append('<form class="form" id="demande" novalidate>')
    for cle, fr, en, typ, oblig, options in C.FORMULAIRE:
        etoile = ' <span class="oblig">*</span>' if oblig else ''
        o.append('<div>')
        o.append('<label for="f-%s"><span data-fr="%s" data-en="%s">%s</span>'
                 '%s</label>' % (cle, e(fr), e(en), e(fr), etoile))
        req = ' required' if oblig else ''
        if typ == 'select':
            o.append('<select id="f-%s" name="%s"%s>' % (cle, cle, req))
            o.append('<option value="" data-fr="Choisir" data-en="Choose">'
                     'Choisir</option>')
            for ofr, oen in options:
                o.append('<option value="%s" data-fr="%s" data-en="%s">%s'
                         '</option>' % (e(ofr), e(ofr), e(oen), e(ofr)))
            o.append('</select>')
        elif typ == 'textarea':
            o.append('<textarea id="f-%s" name="%s"%s></textarea>'
                     % (cle, cle, req))
        else:
            o.append('<input type="%s" id="f-%s" name="%s"%s>'
                     % (typ, cle, cle, req))
        o.append('</div>')
    o.append('<div class="env">'
             '<button type="submit" data-fr="Envoyer ma candidature" '
             'data-en="Send my application">Envoyer ma candidature</button>'
             '<span class="tbc" data-fr="destination a definir" '
             'data-en="destination to be set">destination a definir</span>'
             '</div>')
    o.append('<div class="recu" id="recu" hidden></div>')
    o.append('</form>')
    o.append('</div></section>')
    return '\n'.join(o)


# ---------------------------------------------------------------------------
# LE SIMULATEUR, cote navigateur. Meme formule qu'en Python, ecrite une
# seule fois ici. Le format des nombres est le meme des deux cotes (espace
# insecable), pour que la comparaison automatique reste lisible.
# ---------------------------------------------------------------------------
JS_SIMU = """
(function(){
  var f=document.getElementById('s-places');
  if(!f) return;
  function val(id){
    var n=parseFloat((document.getElementById('s-'+id)||{}).value);
    return isFinite(n)&&n>=0?n:0;
  }
  function nb(x){
    var neg=x<0; x=Math.round(Math.abs(x));
    var s=String(x), out='';
    while(s.length>3){ out='\\u00a0'+s.slice(-3)+out; s=s.slice(0,-3); }
    return (neg?'-':'')+s+out;
  }
  function calc(){
    var v={places:val('places'),occupation:val('occupation'),
           tarif:val('tarif'),loyer:val('loyer'),etp:val('etp'),
           salaire:val('salaire'),autres:val('autres'),
           redevance:val('redevance')};
    var produits=v.places*v.occupation/100*v.tarif;
    var redevance=produits*v.redevance/100;
    var masse=v.etp*v.salaire;
    var fixes=v.loyer+masse+v.autres;
    var charges=fixes+redevance;
    var resultat=produits-charges;
    var denom=v.places*v.tarif*(1-v.redevance/100);
    var seuil=denom>0?fixes/denom*100:0;
    return {produits:produits,masse:masse,redevance:redevance,
            charges:charges,resultat:resultat,annuel:resultat*12,
            seuil:seuil};
  }
  function pose(){
    var r=calc();
    var d=(document.getElementById('s-devise')||{}).value||'EUR';
    for(var k in r){
      var n=document.getElementById('r-'+k);
      if(!n) continue;
      n.innerHTML = k==='seuil'
        ? nb(r[k])+'\\u00a0%'
        : nb(r[k])+'\\u00a0<span class="dev">'+d+'</span>';
    }
    /* Un resultat negatif doit SE VOIR negatif : le signe moins seul, dans
       une colonne de chiffres, se rate. */
    var lignes=document.querySelectorAll('.sortie .ligne[data-sortie]');
    for(var i=0;i<lignes.length;i++){
      var c=lignes[i].getAttribute('data-sortie');
      if(c==='resultat'||c==='annuel')
        lignes[i].classList.toggle('neg', r[c]<0);
    }
  }
  var champs=document.querySelectorAll('.champs input,.champs select');
  for(var i=0;i<champs.length;i++){
    champs[i].addEventListener('input',pose);
    champs[i].addEventListener('change',pose);
  }
  pose();
})();
"""

JS_FORM = """
(function(){
  var f=document.getElementById('demande');
  if(!f) return;
  var recu=document.getElementById('recu');
  var M={fr:{ok:'Candidature enregistree. Tant que la destination des '+
               'candidatures n\\'est pas fixee, rien n\\'est envoye : '+
               'ce formulaire est complet, il attend son adresse.',
             manque:'Il manque : '},
         en:{ok:'Application recorded. Until the destination for '+
               'applications is set, nothing is sent: this form is '+
               'complete, it is waiting for its address.',
             manque:'Missing: '}};
  f.addEventListener('submit',function(ev){
    ev.preventDefault();
    var l=(window.langue?window.langue():'fr');
    var manque=[];
    var n=f.querySelectorAll('[required]');
    for(var i=0;i<n.length;i++){
      if(!String(n[i].value||'').trim()){
        var lab=f.querySelector('label[for="'+n[i].id+'"] span');
        manque.push(lab?lab.getAttribute('data-'+l):n[i].id);
      }
    }
    recu.hidden=false;
    recu.textContent = manque.length
      ? M[l].manque+manque.join(', ')
      : M[l].ok;
    if(!manque.length) f.reset();
    recu.scrollIntoView({block:'nearest'});
  });
})();
"""



def ecrire():
    os.makedirs(DEMO, exist_ok=True)
    pages = {'index.html': page_accueil(),
             'concept.html': page_concept(),
             'franchise.html': page_franchise()}
    for nom, html in pages.items():
        chemin = os.path.join(DEMO, nom)
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(html)
        print('%-16s %7d octets' % (nom, len(html.encode('utf-8'))))
    return DEMO


if __name__ == '__main__':
    d = ecrire()
    print('ecrit dans %s' % d)
