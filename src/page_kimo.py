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
        .replace('__L2__', lien('index.html#methode', '', 'La methode',
                                'The method')) \
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
    o.append(bi('Reseau de micro-creches decentralisees',
                'A decentralised network of micro-nurseries', 'p', 'surtitre'))
    o.append(bi('Une creche a taille humaine, la ou les familles habitent.',
                'A nursery on a human scale, where families actually live.',
                'h1'))
    o.append(bi('KIMO ouvre de petites unites de quartier, tenues par des '
                'responsables independants, avec une methode commune et les '
                'memes outils partout. Une creche courte se place ou une '
                'grande structure ne rentre pas — et l\'enfant y retrouve '
                'chaque matin le meme adulte.',
                'KIMO opens small neighbourhood units, run by independent '
                'managers, with a shared method and the same tools '
                'everywhere. A small nursery fits where a large facility '
                'cannot — and the child meets the same adult every morning.',
                'p', 'chapo'))
    o.append('<div class="actions">'
             '<a class="bouton plein" href="franchise.html" '
             'data-fr="Ouvrir une KIMO" data-en="Open a KIMO">'
             'Ouvrir une KIMO</a>'
             '<a class="bouton vide" href="#modele" '
             'data-fr="Comprendre le modele" data-en="Understand the model">'
             'Comprendre le modele</a></div>')
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
    o.append('<section id="methode" class="pale"><div class="enveloppe">')
    o.append('<div class="titre-bloc"><div class="pastille-titre">')
    o.append(bi('La methode', 'The method', 'h2'))
    if C.METHODE_A_VALIDER:
        # Une pastille honnete : c'est MA redaction, pas sa doctrine.
        o.append('<span class="tbc" data-fr="texte a valider" '
                 'data-en="draft, to be approved">texte a valider</span>')
    o.append('</div>')
    o.append(bi('Ce qui suit est une proposition de redaction, a corriger. '
                'La pedagogie d\'un reseau se decide par son fondateur ; ce '
                'texte sert a montrer ou elle se place sur le site et '
                'combien de place elle prend.',
                'What follows is a draft, to be corrected. A network\'s '
                'pedagogy is its founder\'s decision; this text shows where '
                'it sits on the site and how much room it takes.'))
    o.append('</div><div class="grille g4">')
    for _cle, fr, en, dfr, den in C.METHODE:
        o.append('<div class="carte">' + bi(fr, en, 'h3') + bi(dfr, den)
                 + '</div>')
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
    pages = {'index.html': page_accueil(), 'franchise.html': page_franchise()}
    for nom, html in pages.items():
        chemin = os.path.join(DEMO, nom)
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(html)
        print('%-16s %7d octets' % (nom, len(html.encode('utf-8'))))
    return DEMO


if __name__ == '__main__':
    d = ecrire()
    print('ecrit dans %s' % d)
