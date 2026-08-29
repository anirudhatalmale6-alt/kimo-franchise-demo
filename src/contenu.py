# -*- coding: utf-8 -*-
"""Tout le TEXTE et tous les REGLAGES de KIMO, en un seul endroit.

Le generateur (page_kimo.py) ne contient aucune phrase et aucun chiffre : il
ne sait que mettre en page. Ce fichier-ci est celui que le client relit.

DEUX REGLES TIENNENT CE FICHIER, et elles expliquent tous les « None » :

  1. LE NOM DU RESEAU D'APPRENTISSAGE QUI A POPULARISE CE MODELE N'APPARAIT
     NULLE PART. Ni dans le site, ni dans le code, ni dans un commentaire,
     ni dans un nom de fichier — c'est une marque deposee et un reseau de
     franchises, et la regle vaut aussi pour les sources. Le MODELE, lui —
     un reseau de petites unites locales tenues par des responsables
     independants, avec une methode commune fournie par le reseau — se
     decrit tres bien sans citer personne, et c'est ce qui est fait ici.
     tests-kimo.py balaie tout le dossier pour le verifier.

  2. JE N'INVENTE NI UN CHIFFRE REGLEMENTAIRE NI UN CHIFFRE COMMERCIAL.
     Le nombre de places d'une micro-creche, le taux d'encadrement, la
     qualification du responsable, la surface par enfant : ce sont des
     regles de droit, elles changent d'un pays a l'autre et parfois d'une
     region a l'autre, et une page qui en annonce une fausse fait prendre un
     risque reel a un candidat franchise. Le droit d'entree et la redevance,
     eux, sont des decisions du groupe, pas les miennes.

     Donc : chaque valeur inconnue vaut None, et le site AFFICHE « a definir »
     a sa place, en clair. Un blanc visible est honnete ; un chiffre
     plausible ne l'est pas. Le jour ou Hakim les donne, on remplit ce
     fichier et les deux pages se remettent a jour.
"""

MARQUE = 'KIMO'

# ---------------------------------------------------------------------------
# SOURCE DU CONTENU
#
# Depuis la note « KIMO — Decentralized Early Learning Network » envoyee par
# Hakim, la pedagogie, le format des unites, la journee type, le modele
# d'exploitation et les phases de deploiement ne sont plus de moi : ils
# viennent de lui. Le site les met en page, il ne les invente plus.
#
# Ce qui reste de moi et qui est signale comme tel :
#   - la traduction FRANCAISE de sa note, qui est ecrite en anglais ;
#   - les chiffres LAISSES VIDES, qui le restent (voir les deux regles
#     ci-dessus, elles n'ont pas bouge) ;
#   - le simulateur, dont la structure est a moi et toutes les valeurs au
#     candidat.
# ---------------------------------------------------------------------------

# La signature de la marque. L'ANGLAIS est de lui, mot pour mot ; le francais
# est ma traduction et il porte une mention « traduction a valider » sur le
# site tant qu'il ne l'a pas confirmee. Une signature de marque ne se traduit
# pas a la place de son fondateur.
SIGNATURE_EN = 'Learn to Think.'
SIGNATURE_FR = 'Apprendre à penser.'
SIGNATURE_TRAD_A_VALIDER = True

# Sa promesse centrale (section 2 de la note), mot pour mot cote anglais.
PROMESSE_EN = ('One educational ecosystem, many local centers: proximity for '
               'families, autonomy for local teams and consistent quality '
               'across the network.')
PROMESSE_FR = ('Un seul écosystème éducatif, beaucoup de centres locaux : la '
               'proximité pour les familles, l\'autonomie pour les équipes '
               'locales, et la même qualité partout dans le réseau.')

# La devise du fondateur, mot pour mot comme sur les autres sites du groupe.
# Un controle compare cette chaine avec prestige/page_prestige.py : une devise
# qui differe d'un site a l'autre n'est plus une devise, c'est deux slogans.
DEVISE_FR = 'Mes sites impactent le monde.'
DEVISE_EN = 'My sites impact the world.'

# Les liens entre sites du groupe sont ABSOLUS (sites separes, pas de chemin
# relatif possible) et ils sont TOUS ICI. Le jour des noms de domaine, on ne
# cherche pas dans le corps des pages.
URL_ANNUAIRE = 'https://anirudhatalmale6-alt.github.io/annuaire-franchises-demo/'
URL_PRESTIGE = 'https://anirudhatalmale6-alt.github.io/maisons-de-prestige/'

# ---------------------------------------------------------------------------
# CE QUI N'EST PAS ENCORE DECIDE. C'est la table la plus importante du
# fichier : elle liste ce qui manque, et le site l'affiche au lieu de le
# combler. Chaque ligne : cle, question posee au client, ou ca se voit.
# ---------------------------------------------------------------------------
A_DEFINIR = [
    ('pays', 'Le PAYS de la première crèche',
     'Le pays commande tout le cadre réglementaire, la monnaie et la langue.'),
    ('ville', 'La VILLE de la première crèche',
     'Agrément, locaux et taux d\'encadrement se traitent au niveau local.'),
    ('domaine', 'Le NOM DE DOMAINE',
     'Aujourd\'hui le site tourne sur une adresse de démonstration.'),
    ('entree', 'Le DROIT D\'ENTRÉE au réseau',
     'Affiché dans le modèle économique et utilisé par le simulateur.'),
    ('redevance', 'La REDEVANCE du réseau',
     'Même chose : en pourcentage du chiffre d\'affaires, ou forfaitaire.'),
    ('apport', 'L\'APPORT PERSONNEL demandé au candidat',
     'C\'est le premier filtre d\'un dossier de franchise.'),
    ('contact', 'L\'ADRESSE qui reçoit les candidatures',
     'Le formulaire est construit ; il lui manque sa destination.'),
]

# ---------------------------------------------------------------------------
# LE MODELE ECONOMIQUE. Tout est a None tant que Hakim n'a pas tranche.
#   montant : nombre, ou None
#   unite   : 'devise' | 'pourcent' | 'texte'
# ---------------------------------------------------------------------------
MODELE = [
    ('entree', 'Droit d\'entrée', 'Entry fee', None, 'devise',
     'Versé une fois à la signature. Il paie la formation initiale, '
     'l\'ouverture accompagnée et la mise en place de la méthode.',
     'Paid once at signature. It covers the initial training, the assisted '
     'opening and the setup of the method.'),
    ('duree', 'Durée du contrat', 'Contract term', None, 'texte',
     'La durée d\'un contrat de franchise se cale sur celle du bail : '
     'un contrat plus court que le bail laisse le franchisé avec un local '
     'et sans marque.',
     'A franchise term is set against the lease: a term shorter than the '
     'lease leaves the franchisee with premises and no brand.'),
    ('redevance', 'Redevance d\'exploitation', 'Ongoing royalty', None,
     'pourcent',
     'Prélevée sur le chiffre d\'affaires encaissé. Elle finance la méthode, '
     'les outils, le support et le contrôle qualité.',
     'Charged on collected revenue. It funds the method, the tools, the '
     'support and the quality control.'),
    ('communication', 'Contribution communication', 'Marketing contribution',
     None, 'pourcent',
     'Fonds commun : campagnes nationales, site, référencement local des '
     'crèches du réseau.',
     'Common fund: national campaigns, website, local search presence for '
     'the network\'s centres.'),
    ('apport', 'Apport personnel demandé', 'Personal contribution required',
     None, 'devise',
     'La part que le candidat finance lui-même, hors emprunt.',
     'The share the candidate finances themselves, outside of borrowing.'),
    ('investissement', 'Investissement total', 'Total investment', None,
     'devise',
     'Travaux, mobilier, matériel pédagogique, trésorerie de démarrage. '
     'Il dépend du local et du pays : il se chiffre par ville, pas en '
     'général.',
     'Fit-out, furniture, teaching material, opening cash. It depends on the '
     'premises and the country: it is costed city by city, not in general.'),
]

# ---------------------------------------------------------------------------
# LE CADRE REGLEMENTAIRE. Meme principe, et ici c'est plus qu'une question de
# style : une micro-creche est un etablissement d'accueil de jeunes enfants,
# donc un etablissement AGREE. Le nombre de places, le taux d'encadrement, la
# qualification du responsable et la surface par enfant sont fixes par le
# droit du pays. Ecrire un chiffre au hasard ici, c'est exposer un candidat.
# ---------------------------------------------------------------------------
REGLEMENTAIRE = [
    ('capacite', 'Capacité maximale de l\'unité',
     'Maximum capacity of a unit',
     'Le nombre de places qui définit une « micro-crèche » est fixé par la '
     'réglementation du pays. Au-delà, l\'établissement change de catégorie '
     'et de règles.',
     'The number of places that defines a "micro-nursery" is set by national '
     'regulation. Above it, the facility changes category and rules.',
     None),
    ('encadrement', 'Taux d\'encadrement',
     'Staff-to-child ratio',
     'Nombre d\'adultes diplômés par enfant, et il diffère souvent selon que '
     'l\'enfant marche ou non.',
     'Number of qualified adults per child, often different for children who '
     'walk and those who do not.',
     None),
    ('responsable', 'Qualification du responsable',
     'Qualification of the manager',
     'Diplôme exigé, années d\'expérience, et parfois une référence '
     'sanitaire distincte.',
     'Required diploma, years of experience, and sometimes a separate health '
     'referent.',
     None),
    ('surface', 'Surface par enfant',
     'Floor area per child',
     'Surface intérieure utile, et accès à un espace extérieur selon les '
     'pays.',
     'Usable indoor area, plus access to outdoor space depending on the '
     'country.',
     None),
    ('agrement', 'Autorité qui délivre l\'agrément',
     'Authority granting the licence',
     'C\'est elle qui visite le local avant l\'ouverture et qui peut la '
     'refuser. Le calendrier d\'ouverture dépend de son délai.',
     'It inspects the premises before opening and can refuse. The opening '
     'schedule depends on its lead time.',
     None),
    ('financement', 'Aides et financement des familles',
     'Family funding and subsidies',
     'Dans plusieurs pays, une partie du prix payé par la famille est prise '
     'en charge. Cela change le tarif affichable, donc tout le modèle.',
     'In several countries part of the fee paid by the family is subsidised. '
     'That changes the price you can charge, and so the whole model.',
     None),
]

# ---------------------------------------------------------------------------
# LE MODELE DECENTRALISE — les quatre idees qui font KIMO. Ecrit sans citer
# aucun reseau existant.
# ---------------------------------------------------------------------------
PILIERS = [
    ('proximite', 'Une crèche par quartier', 'One nursery per neighbourhood',
     'Le trajet domicile-crèche est le premier critère des parents, avant le '
     'prix. Une unité petite s\'implante dans un quartier où une grande '
     'structure ne rentre pas : un rez-de-chaussée, une maison, un local '
     'commercial reconverti.',
     'The home-to-nursery trip is the first thing parents look at, before '
     'price. A small unit fits into a neighbourhood where a large facility '
     'cannot: a ground floor, a house, a converted shop.'),
    ('taille', 'Petite unité, adulte connu',
     'Small unit, a familiar adult',
     'Un enfant de deux ans ne retient pas quinze visages. Une unité courte '
     'garde le même adulte devant le même groupe toute la journée, et les '
     'parents parlent au responsable, pas à un standard.',
     'A two-year-old does not retain fifteen faces. A small unit keeps the '
     'same adult with the same group all day, and parents talk to the '
     'manager, not to a switchboard.'),
    ('methode', 'Une méthode commune, pas une improvisation',
     'A shared method, not improvisation',
     'Ce que le réseau apporte n\'est pas un logo : c\'est une progression '
     'écrite, des supports, un cahier d\'observation, et la formation qui va '
     'avec. Deux crèches KIMO à deux bouts du pays travaillent de la même '
     'façon.',
     'What the network brings is not a logo: it is a written progression, '
     'materials, an observation record, and the training that goes with it. '
     'Two KIMO nurseries at opposite ends of the country work the same way.'),
    ('couts', 'Les coûts lourds sont mutualisés',
     'The heavy costs are shared',
     'Inscription en ligne, facturation, planning, achats, conformité, site '
     'et référencement : une crèche seule les paie en entier et les fait mal. '
     'Le réseau les porte une fois pour toutes.',
     'Enrolment, billing, scheduling, purchasing, compliance, website and '
     'local search: a standalone nursery pays for all of it and does it '
     'badly. The network carries it once, for everyone.'),
]

# ---------------------------------------------------------------------------
# LA METHODE. Ce bloc N'EST PLUS DE MOI : ce sont les six principes de la
# section 5 de sa note, cote anglais mot pour mot, cote francais traduits.
#
# Les principes sont volontairement laisses NUS, sans paragraphe de
# developpement : un developpement, je l'inventerais, et une doctrine
# pedagogique inventee sous la signature du fondateur, c'est exactement ce
# qu'il ne faut pas faire. Le jour ou une specialiste de la petite enfance
# les transforme en modules par age — c'est la deuxieme ligne de ses
# « next steps » — le developpement viendra d'elle.
# ---------------------------------------------------------------------------
METHODE_A_VALIDER = False

METHODE_INTRO_FR = (
    'KIMO ne cherche pas à transformer la crèche en école primaire. Les '
    'thèmes intellectuels y sont des supports de jeu et de découverte. '
    'L\'objectif est de poser les bases du raisonnement et de la curiosité '
    'sans rien retirer au jeu libre, au développement affectif, à la parole, '
    'à la vie en groupe, à la création et au repos.')
METHODE_INTRO_EN = (
    'KIMO is not intended to turn preschool into primary school. The '
    'curriculum uses intellectual themes as tools for play and discovery. '
    'The objective is to create foundations for reasoning and curiosity '
    'while preserving free play, emotional development, communication, '
    'social interaction, creativity and rest.')

METHODE = [
    ('Poser la question avant de donner la réponse.',
     'Ask questions before giving answers.'),
    ('Manipuler des objets réels avant d\'introduire des symboles '
     'abstraits.',
     'Manipulate real objects before introducing abstract symbols.'),
    ('Demander à l\'enfant d\'expliquer comment il est arrivé à sa solution.',
     'Encourage children to explain how they reached a solution.'),
    ('Se servir de l\'erreur pour essayer une autre approche.',
     'Use mistakes as opportunities to test another approach.'),
    ('Équilibrer les activités dirigées et l\'exploration menée par '
     'l\'enfant.',
     'Balance structured activities with child-led exploration.'),
    ('Régler la difficulté sur la maturité de l\'enfant, pas sur son âge.',
     'Adapt complexity to developmental readiness rather than age alone.'),
]

# ---------------------------------------------------------------------------
# LES SEPT PILIERS D'APPRENTISSAGE (section 6 de sa note). Anglais mot pour
# mot, francais traduit.
# ---------------------------------------------------------------------------
APPRENTISSAGE = [
    ('logique', 'Logique et résolution de problèmes',
     'Logic & Problem Solving',
     'Casse-tête, tris, reconnaissance de motifs, construction, mises en '
     'ordre, labyrinthes, jeux de mémoire et petits défis de stratégie. '
     'L\'enfant apprend à comparer, classer, anticiper et vérifier une '
     'solution.',
     'Puzzles, sorting, pattern recognition, construction, sequencing, '
     'mazes, memory games and simple strategy challenges. Children learn to '
     'compare, classify, anticipate and test solutions.'),
    ('echecs', 'Échecs et pensée stratégique',
     'Chess & Strategic Thinking',
     'Chez les plus jeunes, les échecs commencent par les couleurs, '
     'l\'orientation du plateau, la reconnaissance des pièces et des jeux de '
     'déplacement. Les plus grands passent à des mini-parties avec un nombre '
     'de pièces limité. Le but est l\'attention, le raisonnement dans '
     'l\'espace et l\'anticipation — pas la performance en compétition.',
     'For younger children, chess begins with colors, board orientation, '
     'piece recognition and movement games. Older preschoolers can progress '
     'to mini-games with a limited number of pieces. The purpose is '
     'attention, spatial reasoning and anticipation' + u'\u2014' + 'not competitive '
     'performance.'),
    ('maths', 'Mathématiques', 'Mathematics',
     'Compter avec des objets, quantités, formes, comparaison, mesure, '
     'symétrie, motifs, repérage dans l\'espace et premières idées de '
     'calcul. Les activités restent concrètes et ludiques.',
     'Counting through objects, quantities, shapes, comparison, measurement, '
     'symmetry, patterns, spatial relationships and simple arithmetic '
     'concepts. Activities remain concrete and playful.'),
    ('sciences', 'Physique et sciences', 'Physics & Science',
     'Expériences sans danger autour de l\'eau, l\'air, la lumière, le son, '
     'les aimants, l\'équilibre, la gravité, le mouvement, les plantes et '
     'les matières. On demande à l\'enfant de prévoir ce qui va se passer, '
     'd\'observer le résultat et de le décrire.',
     'Safe experiments involving water, air, light, sound, magnets, balance, '
     'gravity, motion, plants and materials. Children are encouraged to '
     'predict what will happen, observe the result and describe what they '
     'saw.'),
    ('histoire', 'Histoire et civilisations', 'History & Civilizations',
     'Récits illustrés sur les civilisations, les inventions, les '
     'explorateurs, l\'architecture, les transports, les écritures et les '
     'grandes réalisations humaines. L\'accent est mis sur le récit, la '
     'chronologie et la curiosité culturelle, pas sur les dates à retenir.',
     'Illustrated stories about civilizations, inventions, explorers, '
     'architecture, transport, writing systems and major human achievements. '
     'The focus is narrative, chronology and cultural curiosity rather than '
     'memorization of dates.'),
    ('corps', 'Développement physique', 'Physical Development',
     'Du mouvement tous les jours : équilibre, coordination, force, '
     'motricité fine et globale, rythme et jeux coopératifs. L\'activité en '
     'extérieur est intégrée dès que c\'est possible.',
     'Daily movement supporting balance, coordination, strength, fine and '
     'gross motor skills, rhythm and cooperative play. Outdoor activity is '
     'integrated whenever possible.'),
    ('creation', 'Création et expression', 'Creativity & Communication',
     'Dessin, musique, récit, construction, jeux de rôle et travaux manuels '
     'font contrepoids aux activités analytiques et aident l\'enfant à dire '
     'ses idées de plusieurs façons.',
     'Drawing, music, storytelling, building, role play and crafts provide a '
     'counterbalance to analytical activities and help children communicate '
     'ideas in multiple ways.'),
]

# ---------------------------------------------------------------------------
# LE PARCOURS D'UN CANDIDAT. Les DUREES sont a None : elles dependent du
# delai de l'autorite qui delivre l'agrement, donc du pays.
# ---------------------------------------------------------------------------
PARCOURS = [
    ('1', 'Candidature', 'Application',
     'Le formulaire en bas de cette page. Ville visée, situation, apport, '
     'calendrier souhaite.',
     'The form at the bottom of this page. Target city, situation, personal '
     'contribution, target date.', None),
    ('2', 'Entretien et dossier', 'Interview and file',
     'Un entretien, puis le document d\'information précontractuelle : ce '
     'que le réseau apporte, ce qu\'il facture, ce qu\'il exige.',
     'An interview, then the pre-contractual disclosure document: what the '
     'network provides, what it charges, what it requires.', None),
    ('3', 'Étude de la zone', 'Territory study',
     'Nombre de jeunes enfants, offre existante, trajets. Une zone qui ne '
     'porte pas une crèche, on le voit avant le bail, pas après.',
     'Number of young children, existing supply, commutes. A territory that '
     'cannot carry a nursery shows up before the lease, not after.', None),
    ('4', 'Local et agrément', 'Premises and licence',
     'Recherche du local, mise en conformité, dépôt du dossier auprès de '
     'l\'autorité. C\'est l\'étape la plus longue, et sa durée ne dépend pas '
     'de nous.',
     'Finding the premises, bringing them up to standard, filing with the '
     'authority. This is the longest step, and its length is not ours to '
     'set.', None),
    ('5', 'Formation', 'Training',
     'La méthode, les outils, la gestion, la relation aux familles. Le '
     'responsable et le premier encadrant la suivent ensemble.',
     'The method, the tools, day-to-day management, working with families. '
     'The manager and the first practitioner attend together.', None),
    ('6', 'Ouverture accompagnée', 'Assisted opening',
     'Quelqu\'un du réseau est sur place les premiers jours. Les premières '
     'inscriptions se font à deux.',
     'Someone from the network is on site for the first days. The first '
     'enrolments are handled together.', None),
]

# ---------------------------------------------------------------------------
# CE QUE CHACUN APPORTE. Une franchise se juge la-dessus.
# ---------------------------------------------------------------------------
RESEAU_APPORTE = [
    ('La marque et la charte', 'The brand and its guidelines'),
    ('La méthode écrite et ses supports', 'The written method and materials'),
    ('La formation initiale et le recyclage annuel',
     'Initial training and annual refresher'),
    ('Le logiciel : inscriptions, présences, facturation, planning',
     'The software: enrolment, attendance, billing, scheduling'),
    ('L\'étude de zone avant la signature du bail',
     'The territory study before the lease is signed'),
    ('Les achats groupes : mobilier, matériel, consommables',
     'Group purchasing: furniture, equipment, consumables'),
    ('Le site du réseau et la fiche locale de la crèche',
     'The network site and the nursery\'s local page'),
    ('Le contrôle qualité et les visites',
     'Quality control and site visits'),
    ('L\'exclusivité sur une zone définie au contrat',
     'Exclusivity over a territory defined in the contract'),
]

FRANCHISE_APPORTE = [
    ('Le local, et sa mise en conformité',
     'The premises, and bringing them up to standard'),
    ('L\'apport personnel et le financement',
     'The personal contribution and the financing'),
    ('Le recrutement de l\'équipe, avec l\'aide du réseau',
     'Recruiting the team, with the network\'s help'),
    ('Sa présence : ce n\'est pas un placement, c\'est un métier',
     'Their presence: this is not an investment, it is a job'),
    ('Le respect de la méthode et des standards',
     'Applying the method and the standards'),
    ('La relation avec les familles et l\'autorité locale',
     'The relationship with families and the local authority'),
]

PROFIL = [
    ('Un métier de la petite enfance, de la santé ou de l\'éducation — ou '
     'un associé qui l\'exerce.',
     'A background in early years, health or education — or a partner who '
     'has one.'),
    ('L\'envie de tenir un lieu, pas d\'y placer de l\'argent.',
     'Wanting to run a place, not to park money in one.'),
    ('Un ancrage local réel dans la ville visée.',
     'Real local roots in the target city.'),
    ('La capacité à financer l\'apport demandé.',
     'The ability to fund the required contribution.'),
]

# ---------------------------------------------------------------------------
# LE SIMULATEUR. Aucune de ces valeurs n'est un chiffre KIMO : ce sont les
# valeurs de DEPART d'un formulaire que le candidat modifie. Elles sont
# rondes exprès, pour qu'on voie qu'elles sont a remplacer.
#
#   cle, fr, en, valeur de depart, pas, unite ('devise'|'pourcent'|'nombre')
# ---------------------------------------------------------------------------
SIM_CHAMPS = [
    ('places', 'Places agréées', 'Licensed places', 12, 1, 'nombre'),
    ('occupation', 'Taux d\'occupation', 'Occupancy rate', 90, 1, 'pourcent'),
    ('tarif', 'Recette mensuelle par place', 'Monthly revenue per place',
     1300, 10, 'devise'),
    ('loyer', 'Loyer mensuel', 'Monthly rent', 1600, 50, 'devise'),
    ('etp', 'Encadrants (équivalent temps plein)',
     'Practitioners (full-time equivalent)', 4, 1, 'nombre'),
    ('salaire', 'Coût mensuel charge par encadrant',
     'Monthly loaded cost per practitioner', 2500, 50, 'devise'),
    ('autres', 'Autres charges mensuelles', 'Other monthly costs', 1100, 50,
     'devise'),
    ('redevance', 'Redevance réseau', 'Network royalty', 0, 1, 'pourcent'),
]

DEVISES = [('EUR', '€'), ('CAD', '$'), ('CHF', 'CHF'), ('DZD', 'DA'),
           ('MAD', 'DH'), ('GBP', '£')]

SIM_NOTE_FR = ('Aucun chiffre de ce simulateur n\'est un chiffre KIMO, et '
               'les valeurs de départ ne décrivent aucun marché : elles sont '
               'rondes et arbitraires, elles servent à montrer le calcul. '
               'Remplacez-les par les vôtres. La redevance réseau est à zéro '
               'parce qu\'elle n\'est pas encore fixée — posez-la dès '
               'qu\'elle l\'est.')
SIM_NOTE_EN = ('None of the figures in this simulator are KIMO figures, and '
               'the starting values describe no particular market: they are '
               'round and arbitrary, they exist to show the calculation. '
               'Replace them with your own. The network royalty sits at zero '
               'because it has not been set yet — enter it as soon as it is.')

# ---------------------------------------------------------------------------
# LE FORMULAIRE DE CANDIDATURE.
#   cle, fr, en, type, obligatoire, options (fr, en) pour les listes
# ---------------------------------------------------------------------------
FORMULAIRE = [
    ('nom', 'Nom et prénom', 'Full name', 'text', True, None),
    ('tel', 'Téléphone', 'Phone', 'tel', True, None),
    ('courriel', 'Adresse de courriel', 'Email address', 'email', True, None),
    ('pays', 'Pays vise', 'Target country', 'text', True, None),
    ('ville', 'Ville visée', 'Target city', 'text', True, None),
    ('profil', 'Votre situation', 'Your background', 'select', True, [
        ('Professionnel de la petite enfance',
         'Early-years professional'),
        ('Santé ou éducation', 'Health or education'),
        ('Entrepreneur, avec un associé du métier',
         'Entrepreneur, with a partner from the field'),
        ('Autre', 'Other')]),
    ('apport', 'Apport personnel disponible', 'Personal contribution available',
     'text', False, None),
    ('local', 'Avez-vous déjà un local ?', 'Do you already have premises?',
     'select', True, [
         ('Oui, un local identifié', 'Yes, premises identified'),
         ('Une recherche en cours', 'A search under way'),
         ('Pas encore', 'Not yet')]),
    ('echeance', 'Ouverture souhaitée', 'Target opening', 'select', True, [
        ('Dans les 6 mois', 'Within 6 months'),
        ('6 à 12 mois', '6 to 12 months'),
        ('Plus de 12 mois', 'More than 12 months')]),
    ('message', 'Votre projet en quelques lignes',
     'Your project, in a few lines', 'textarea', False, None),
]

# ---------------------------------------------------------------------------
# LA FAQ. Les reponses qui dependent d'un chiffre non fixe le DISENT.
# ---------------------------------------------------------------------------
FAQ = [
    ('Faut-il un diplôme de la petite enfance pour ouvrir une KIMO ?',
     'Do I need an early-years qualification to open a KIMO?',
     'Pour DIRIGER l\'établissement, la loi du pays l\'exige presque '
     'toujours, et c\'est elle qui tranche, pas le réseau. Un candidat sans '
     'ce diplôme ouvre avec un responsable qui l\'a. La qualification exacte '
     'fait partie des points à préciser dès que le pays est arrêté.',
     'To RUN the facility, national law almost always requires one, and that '
     'is what decides, not the network. A candidate without it opens with a '
     'manager who has it. The exact qualification is one of the points to be '
     'settled once the country is chosen.'),
    ('Combien de places par crèche ?',
     'How many places per nursery?',
     'C\'est un plafond réglementaire, pas un choix commercial : le nombre '
     'qui définit une micro-crèche est fixé par le pays. Il sera écrit ici '
     'dès que le pays de la première ouverture sera arrêté.',
     'That is a regulatory ceiling, not a commercial choice: the number that '
     'defines a micro-nursery is set nationally. It will appear here as soon '
     'as the country of the first opening is settled.'),
    ('Quel est le droit d\'entrée ?',
     'What is the entry fee?',
     'Il n\'est pas encore fixé. Tant qu\'il ne l\'est pas, cette page '
     'affiche « à définir » plutôt qu\'un ordre de grandeur : un candidat '
     'construit son financement sur ce chiffre.',
     'It has not been set yet. Until it is, this page shows "to be set" '
     'rather than a ballpark: a candidate builds their financing on that '
     'number.'),
    ('Le réseau prend-il une part du capital de ma société ?',
     'Does the network take equity in my company?',
     'Non. Une franchise n\'est pas une filiale : le franchisé possède son '
     'entreprise, son bail et son fonds. Le réseau vend l\'usage d\'une '
     'marque et d\'une méthode.',
     'No. A franchise is not a subsidiary: the franchisee owns their '
     'company, their lease and their business. The network licenses the use '
     'of a brand and a method.'),
    ('Puis-je ouvrir plusieurs crèches ?',
     'Can I open several nurseries?',
     'C\'est le sens du modèle : de petites unités, donc plusieurs. En '
     'pratique, la deuxième se signe après une première année complète, '
     'agrément obtenu et équipe stable.',
     'That is the point of the model: small units, therefore several. In '
     'practice the second is signed after a full first year, with the licence '
     'obtained and a stable team.'),
    ('Qu\'est-ce qui est exclusif ?',
     'What exactly is exclusive?',
     'Une zone définie au contrat, pas une ville entière par principe. La '
     'taille de la zone se décide sur le nombre de jeunes enfants qui y '
     'vivent, ce que mesure l\'étude de zone.',
     'A territory defined in the contract, not a whole city as a matter of '
     'course. Its size is set from the number of young children living '
     'there, which the territory study measures.'),
    ('Le réseau aide-t-il à trouver le financement ?',
     'Does the network help with financing?',
     'Il fournit le dossier : étude de zone, prévisionnel, description du '
     'concept. Il ne prête pas et ne se porte pas caution.',
     'It provides the file: territory study, forecast, description of the '
     'concept. It does not lend and does not act as guarantor.'),
    ('Que se passe-t-il si l\'agrément est refusé ?',
     'What happens if the licence is refused?',
     'C\'est pour cela que le local et l\'agrément viennent AVANT la '
     'formation dans le parcours, et que le contrat doit prévoir ce cas '
     'explicitement. La rédaction exacte fait partie du dossier juridique à '
     'faire établir dans le pays retenu.',
     'That is why premises and licence come BEFORE training in the journey, '
     'and why the contract must address the case explicitly. The exact '
     'wording belongs to the legal file to be drawn up in the chosen '
     'country.'),
]

AVERT_FR = ('DÉMONSTRATION. KIMO est un réseau en cours de constitution : '
            'aucune crèche n\'est ouverte à ce jour. Les valeurs marquées '
            '« à définir » ne sont pas des oublis, ce sont des décisions qui '
            'n\'ont pas encore été prises, ou des règles qui dépendent du '
            'pays retenu. Aucun chiffre réglementaire n\'est avancé ici tant '
            'qu\'il n\'a pas été vérifié dans le pays concerné.')
AVERT_EN = ('DEMONSTRATION. KIMO is a network being set up: no nursery is '
            'open to date. Values marked "to be set" are not omissions, they '
            'are decisions not yet taken, or rules that depend on the country '
            'chosen. No regulatory figure is stated here until it has been '
            'checked in the country concerned.')


# ===========================================================================
#  LE CONCEPT, tel qu'il l'a ecrit. Sections 3 a 21 de sa note.
#
#  Regle de ce bloc : cote ANGLAIS, c'est son texte, mot pour mot. Cote
#  FRANCAIS, c'est ma traduction de son texte. Je n'ajoute pas d'idee, je
#  n'enleve pas de reserve — en particulier les siennes, qui disent que la
#  capacite, les taux d'encadrement et le modele financier dependent de la
#  juridiction. Elles vont dans le meme sens que les blancs du site.
# ===========================================================================

# --- 3. Le modele decentralise : qui fait quoi ------------------------------
COUCHES = [
    ('KIMO Central', 'KIMO Central',
     'Standards, programme, technologie, marque, formation et contrôle',
     'Standards, curriculum, technology, brand, training and audit',
     'Conception du programme, certification des éducateurs, plateforme, '
     'achats',
     'Program design, educator certification, platform, procurement'),
    ('L\'unité KIMO locale', 'Local KIMO Unit',
     'L\'accueil des enfants et la pédagogie au quotidien',
     'Daily childcare and educational delivery',
     'Équipe, activités, relation aux parents, planning local',
     'Staffing, activities, parent relationships, local scheduling'),
    ('Les partenaires', 'Partners',
     'Apportent des locaux, du capital, des familles ou des services '
     'complémentaires',
     'Provide sites, capital, referrals or complementary services',
     'Employeurs, municipalités, promoteurs, universités',
     'Employers, municipalities, developers, universities'),
    ('Les familles', 'Families',
     'Choisissent leur centre et participent au développement de l\'enfant',
     'Choose centers and participate in child development',
     'Inscription, retours, points sur les progrès, activités à la maison',
     'Enrollment, feedback, progress discussions, home activities'),
]

# --- 4. Le format d'une unite ----------------------------------------------
# La fourchette 8-20 est SA cible, et il l'assortit lui-meme de « subject to
# local childcare regulations ». Elle est donc reproduite AVEC sa reserve, et
# elle ne remplace pas la ligne « capacite » du tableau reglementaire, qui
# reste a definir : une cible de reseau n'est pas un plafond de droit.
FORMAT = [
    ('Capacité visée : environ 8 à 20 enfants par micro-centre, sous réserve '
     'de la réglementation locale de la petite enfance.',
     'Target capacity: approximately 8-20 children per micro-center, subject '
     'to local childcare regulations.'),
    ('Implantations possibles : maisons aménagées, rez-de-chaussée '
     'résidentiels, locaux commerciaux, sites d\'employeurs ou bâtiments '
     'modulaires conçus pour cela.',
     'Possible locations: adapted houses, ground-floor residential spaces, '
     'commercial units, employer campuses or purpose-built modular '
     'facilities.'),
    ('Groupes d\'âge souples, selon les règles d\'agrément et les besoins de '
     'développement de l\'enfant.',
     'Flexible age grouping based on licensing requirements and '
     'child-development needs.'),
    ('Des zones dédiées : apprentissage calme, construction et casse-tête, '
     'mouvement, création, repas et repos.',
     'Dedicated zones for quiet learning, construction/puzzles, movement, '
     'creative work, meals and rest.'),
    ('Un accès extérieur, ou des sorties programmées, partout où c\'est exigé '
     'et réalisable.',
     'Outdoor access or scheduled outdoor activity wherever required and '
     'feasible.'),
    ('Entrée sécurisée, remise de l\'enfant contrôlée, procédures d\'urgence '
     'et sécurisation adaptée aux jeunes enfants.',
     'Secure entry, controlled child release, emergency procedures and '
     'appropriate childproofing.'),
]
FORMAT_AVERT_FR = (
    'Un établissement KIMO ne doit jamais échanger la sécurité ou la '
    'conformité contre de la compacité. La capacité définitive, les taux '
    'd\'encadrement, les dimensions des pièces, le couchage, la préparation '
    'des repas et les exigences d\'espace extérieur doivent être adaptés à la '
    'juridiction dans laquelle chaque unité fonctionne.')
FORMAT_AVERT_EN = (
    'KIMO facilities must never trade safety or regulatory compliance for '
    'compactness. Final capacity, staff ratios, room dimensions, sleep '
    'arrangements, food preparation and outdoor-space requirements must be '
    'adapted to the jurisdiction in which each unit operates.')

# --- 7. Le parcours par age ------------------------------------------------
AGES = [
    ('Premiers pas', 'Early toddler',
     'Découverte sensorielle, langage, mouvement',
     'Sensory discovery, language, movement',
     'Tris, empilements, chansons, matières, cause et effet simples',
     'Sorting, stacking, songs, textures, simple cause-and-effect',
     'Jeu court et très surveillé', 'Short, highly supervised play'),
    ('Grands petits', 'Older toddler',
     'Motifs, coordination, premières quantités',
     'Patterns, coordination, early quantities',
     'Appariements, formes, parcours de motricité, construction, observation '
     'de la nature',
     'Matching, shapes, obstacle courses, building, nature observation',
     'Répétition et exploration', 'Repetition and exploration'),
    ('Maternelle', 'Preschool',
     'Raisonnement, stratégie, récit, sciences',
     'Reasoning, strategy, storytelling, science',
     'Casse-tête, mini-parties d\'échecs, mesure, expériences, récits de '
     'civilisations',
     'Puzzles, chess mini-games, measurement, experiments, civilization '
     'stories',
     'Découverte guidée', 'Guided discovery'),
    ('Avant la grande section', 'Pre-kindergarten',
     'Raisonnement en plusieurs étapes et autonomie',
     'Multi-step thinking and independence',
     'Jeux de planification, défis de nombres, expériences, cartes et frises, '
     'projets collectifs',
     'Planning games, number challenges, experiments, maps/timelines, '
     'collaborative projects',
     'Projets et discussion', 'Projects and discussion'),
]

# --- 8. La journee type ----------------------------------------------------
JOURNEE = [
    ('07:30-09:00', 'Arrivée, jeu libre et transmission avec la famille',
     'Arrival, free play and family handover'),
    ('09:00-09:20', 'Regroupement du matin, langage, on annonce la journée',
     'Morning circle, language and planning'),
    ('09:20-10:00', 'Rotation logique / mathématiques / échecs',
     'Logic / mathematics / chess rotation'),
    ('10:00-10:30', 'Collation et temps social', 'Snack and social time'),
    ('10:30-11:30', 'Mouvement en extérieur, développement physique',
     'Outdoor movement / physical development'),
    ('11:30-12:00', 'Sciences, ou récit et activité d\'histoire',
     'Science or history story/activity'),
    ('12:00-14:00', 'Repas, hygiène, repos et temps calme',
     'Lunch, hygiene, rest/quiet time'),
    ('14:00-15:00', 'Atelier créatif, construction, projet',
     'Creative workshop / construction / project'),
    ('15:00-15:30', 'Collation', 'Snack'),
    ('15:30-16:30', 'Jeu guide et apprentissage en petits groupes',
     'Guided play and small-group learning'),
    ('16:30-18:00', 'Jeu libre, départ des enfants et retour aux parents',
     'Free play, parent pickup and daily feedback'),
]

# --- 9. Les educateurs -----------------------------------------------------
EDUCATEURS_INTRO_FR = (
    'Les éducateurs restent le coeur de KIMO. La technologie soutient leur '
    'travail, elle ne remplace ni leur observation, ni leur attention, ni '
    'leur jugement.')
EDUCATEURS_INTRO_EN = (
    'Educators remain the core of KIMO. Technology supports their work but '
    'does not replace human observation, care or judgment.')
EDUCATEURS = [
    ('Un parcours d\'intégration obligatoire à la pédagogie KIMO et à la '
     'protection de l\'enfance.',
     'Mandatory onboarding in KIMO pedagogy and safeguarding.'),
    ('Des fiches d\'activité avec objectifs d\'apprentissage, matériel, '
     'adaptations et consignes de sécurité.',
     'Activity guides with learning objectives, materials, adaptations and '
     'safety notes.'),
    ('Une formation continue : développement de l\'enfant, communication, '
     'premiers secours, conduite du groupe.',
     'Continuous professional development in child development, '
     'communication, first aid and classroom practice.'),
    ('Une équipe locale libre d\'adapter les activités à son groupe, dans le '
     'respect des standards du réseau.',
     'Local leadership empowered to adapt activities to the group while '
     'respecting network standards.'),
    ('Un suivi fondé sur l\'observation, pas sur des tests sous pression ni '
     'sur un classement des enfants.',
     'Observation-based progress records rather than high-pressure testing or '
     'child ranking.'),
]

# --- 10. La plateforme -----------------------------------------------------
PLATEFORME = [
    ('Compte parent, inscription et dossier de l\'enfant sécurisé.',
     'Parent account, enrollment and secure child profile.'),
    ('Gestion des places, en temps réel ou programmée, entre les centres '
     'KIMO proches.',
     'Real-time or scheduled capacity management across nearby KIMO '
     'centers.'),
    ('Présences, personnes autorisées à venir chercher l\'enfant, absences.',
     'Attendance, authorized pickup and absence management.'),
    ('Facturation, aides et suivi des paiements là où la loi le permet.',
     'Billing, subsidies and payment records where legally permitted.'),
    ('Messagerie parents-éducateurs et résumé quotidien.',
     'Parent-educator messaging and daily summaries.'),
    ('Bibliothèque d\'activités et plans hebdomadaires pour les éducateurs.',
     'Curriculum library and weekly activity plans for educators.'),
    ('Portail de formation et de certification du personnel.',
     'Training and certification portal for staff.'),
    ('Déclaration des incidents, de la maintenance et de la conformité.',
     'Incident, maintenance and compliance reporting.'),
    ('Tableau de bord du réseau : occupation, effectifs, indicateurs qualité '
     'et satisfaction des parents.',
     'Network dashboard covering occupancy, staffing, quality indicators and '
     'parent satisfaction.'),
]
PLATEFORME_NOTE_FR = (
    'Les données des enfants doivent être réduites au minimum, leur accès '
    'contrôle, leur conservation limitée à ce qui est exigé. Protection des '
    'la conception, chiffrement, journaux d\'accès et règles propres à chaque '
    'juridiction doivent être intégrés dès le départ.')
PLATEFORME_NOTE_EN = (
    'Child data should be minimized, access-controlled and retained only as '
    'required. Privacy-by-design, encryption, audit logs and '
    'jurisdiction-specific data protection requirements should be '
    'incorporated from the beginning.')

# --- 11. Cote parents ------------------------------------------------------
PARENTS = [
    ('Un seul compte KIMO pour tout le réseau.',
     'One KIMO account across the network.'),
    ('Une vue claire du centre, de ses horaires et des programmes '
     'disponibles.',
     'Clear view of center information, operating hours and available '
     'programs.'),
    ('Les mêmes procédures d\'accueil et de sécurité partout.',
     'Consistent onboarding and safety procedures.'),
    ('Un échange quotidien, sans surveillance excessive des enfants.',
     'Daily communication without excessive surveillance of children.'),
    ('Des points réguliers sur le développement avec les éducateurs.',
     'Periodic development discussions with educators.'),
    ('Des activités à la maison, facultatives, qui prolongent les thèmes KIMO '
     'sans créer une pression de devoirs.',
     'Optional home activities that extend KIMO themes without creating '
     'homework pressure.'),
]

# --- 12. Securite et conformite --------------------------------------------
SECURITE_INTRO_FR = (
    'L\'accueil de jeunes enfants est très encadré, et les exigences varient '
    'fortement d\'un pays, d\'une province ou d\'une commune à l\'autre. KIMO '
    'doit poser un cadre de conformité central tout en exigeant de chaque '
    'unité locale qu\'elle satisfasse la règle locale la plus stricte.')
SECURITE_INTRO_EN = (
    'Childcare is highly regulated and requirements vary significantly by '
    'country, province/state and municipality. KIMO should establish a '
    'central compliance framework while requiring each local unit to satisfy '
    'the stricter applicable local rules.')
SECURITE = [
    ('Vérification des antécédents et des références du personnel, dans les '
     'limites de la loi.',
     'Background screening and reference checks for staff as legally '
     'required.'),
    ('Taux d\'encadrement et taille maximale des groupes.',
     'Child-to-educator ratios and group-size limits.'),
    ('Couverture premiers secours et formation aux situations d\'urgence.',
     'First-aid/CPR coverage and emergency-response training.'),
    ('Sécurité incendie, plans d\'évacuation et exercices.',
     'Fire safety, evacuation plans and drills.'),
    ('Procédures allergies alimentaires et administration de médicaments.',
     'Food allergy and medication procedures.'),
    ('Protocoles de sommeil sécurisé et d\'hygiène là où ils s\'appliquent.',
     'Safe sleep and hygiene protocols where applicable.'),
    ('Entrée contrôlée et remise de l\'enfant vérifiée.',
     'Controlled entry and verified child release.'),
    ('Consignation obligatoire des incidents et remontée hiérarchique.',
     'Mandatory incident documentation and escalation.'),
    ('Politique de protection de l\'enfance, canaux de signalement et '
     'tolérance zéro en cas de maltraitance ou de négligence.',
     'Safeguarding policy, reporting channels and zero-tolerance procedures '
     'for abuse or neglect.'),
    ('Une assurance adaptée à l\'accueil de jeunes enfants.',
     'Insurance coverage appropriate to childcare operations.'),
]

# --- 13. Qualite -----------------------------------------------------------
QUALITE = [
    ('Certification de chaque unité KIMO avant son ouverture.',
     'Pre-opening certification of every KIMO unit.'),
    ('Contrôles qualité périodiques, annoncés et inopinés, là où le droit le '
     'permet.',
     'Periodic announced and unannounced quality reviews where legally '
     'appropriate.'),
    ('Des listes de contrôle et des standards de programme communs.',
     'Common operational checklists and curriculum standards.'),
    ('Mesure de la satisfaction des parents.',
     'Parent satisfaction measurement.'),
    ('Suivi de la fidélisation du personnel, des formations suivies et des '
     'incidents.',
     'Staff retention, training completion and incident metrics.'),
    ('Plans de correction pour les centres qui passent sous les standards.',
     'Corrective-action plans for centers falling below standards.'),
    ('La possibilité de suspendre la licence et la marque KIMO quand des '
     'manquements graves ne sont pas corrigés.',
     'Ability to suspend the KIMO license/brand when serious deficiencies are '
     'not corrected.'),
]

# --- 14. Les cinq facons d'exploiter un centre -----------------------------
# La franchise est UNE de ces cinq. C'est la seule que la page franchise
# detaille, parce que c'est la seule qui s'adresse a un lecteur exterieur ;
# les quatre autres sont des accords qui se negocient, pas des candidatures.
EXPLOITATION = [
    ('propre', 'En propre', 'Company-owned',
     'KIMO exploite le centre directement',
     'KIMO operates the center directly',
     'Frais de garde et de scolarité', 'Childcare/tuition fees', False),
    ('franchise', 'Licence ou franchise', 'Licensed / franchise',
     'Un exploitant local qualifié utilise le système et la marque KIMO',
     'Qualified local operator uses KIMO system and brand',
     'Droit d\'entrée, puis redevance ou frais de service récurrents',
     'Initial fee + recurring royalty/service fee', True),
    ('employeur', 'KIMO employeur', 'Employer KIMO',
     'Un centre réservé en partie ou en totalité aux salariés d\'une '
     'entreprise',
     'Center dedicated partly or fully to an employer\'s workforce',
     'Contrat avec l\'employeur, plus la part des familles',
     'Employer contract + family fees', False),
    ('immobilier', 'Partenariat immobilier', 'Real-estate partnership',
     'Un promoteur intègre une KIMO dans un projet résidentiel',
     'Developer integrates KIMO into a residential project',
     'Bail ou accord de soutien, plus l\'exploitation',
     'Lease/support agreement + operating revenue', False),
    ('public', 'Partenariat public', 'Public partnership',
     'Des places créées avec des municipalités ou des institutions '
     'publiques',
     'Capacity created with municipalities or public institutions',
     'Contrat ou subvention, plus les tarifs encadrés des familles',
     'Contract/subsidy + regulated family fees', False),
]

# --- 15. La structure de couts ---------------------------------------------
COUTS = [
    ('Achat ou location du local, et travaux d\'aménagement.',
     'Premises acquisition or lease and fit-out.'),
    ('Agrément, honoraires et visites de contrôle.',
     'Licensing, professional services and inspections.'),
    ('Salaires des éducateurs et de l\'encadrement.',
     'Educator and management payroll.'),
    ('Assurance et conformité.', 'Insurance and compliance.'),
    ('Mobilier, matériel pédagogique et équipement extérieur.',
     'Furniture, educational materials and outdoor equipment.'),
    ('Repas et consommables.', 'Meals and consumables.'),
    ('Plateforme technique et sécurité informatique.',
     'Technology platform and cybersecurity.'),
    ('Formation, recrutement et contrôle qualité.',
     'Training, recruitment and quality assurance.'),
    ('Programme central, marketing et administration.',
     'Central curriculum, marketing and administrative functions.'),
]
COUTS_NOTE_FR = (
    'Un modèle financier doit être établi séparément pour chaque juridiction '
    'visée, parce que les taux d\'encadrement, les salaires, les aides, les '
    'loyers et les règles d\'agrément peuvent changer profondément '
    'l\'économie d\'un centre.')
COUTS_NOTE_EN = (
    'A financial model should be produced separately for each target '
    'jurisdiction because staff ratios, wages, subsidies, rent and licensing '
    'rules can materially change center economics.')

# --- 16. Les indicateurs du reseau -----------------------------------------
KPI = [
    ('Places agréées et taux d\'occupation.',
     'Licensed capacity and occupancy rate.'),
    ('Recette par place disponible.',
     'Revenue per available childcare place.'),
    ('Coût du personnel en pourcentage du chiffre d\'affaires.',
     'Staff cost as a percentage of revenue.'),
    ('Respect du taux d\'encadrement.', 'Educator-to-child ratio compliance.'),
    ('Fidélité des parents et taux de recommandation.',
     'Parent retention and referral rate.'),
    ('Rotation du personnel et formations achevées.',
     'Staff turnover and training completion.'),
    ('Fréquence des incidents et délai de clôture des actions correctives.',
     'Incident frequency and corrective-action closure time.'),
    ('Distance ou temps moyen entre les familles et leur centre.',
     'Average distance/time between families and their assigned center.'),
    ('Marge de contribution par centre et frais de structure par unité.',
     'Center-level contribution margin and central overhead per unit.'),
]

# --- 17. Les cinq phases de deploiement ------------------------------------
PHASES = [
    ('1', 'Conception', 'Design',
     'Arrêter la pédagogie, la marque, le cadre réglementaire, le prototype '
     'de centre, les besoins techniques et les hypothèses financières.',
     'Finalize pedagogy, brand, regulatory framework, center prototype, '
     'technology requirements and financial assumptions.'),
    ('2', 'Pilote', 'Pilot',
     'Ouvrir environ 3 à 5 centres dans une même agglomération, sur des '
     'quartiers de profils différents. Mesurer la demande, les effectifs, '
     'l\'expérience des parents et la qualité pédagogique.',
     'Open approximately 3-5 centers in one metropolitan area with different '
     'neighborhood profiles. Measure demand, staffing, parent experience and '
     'educational delivery.'),
    ('3', 'Réseau local', 'Local Network',
     'Densifier jusqu\'à former une grappe de centres, pour que les familles '
     'bénéficient d\'une vraie proximité et des services mutualisés.',
     'Expand to a dense cluster of centers so that families can benefit from '
     'genuine proximity and shared network services.'),
    ('4', 'Plusieurs villes', 'Multi-city Expansion',
     'Répliquer le système d\'exploitation validé, en propre et avec des '
     'partenaires choisis avec soin.',
     'Replicate the validated operating system through company-owned centers '
     'and carefully selected partners.'),
    ('5', 'National, puis international', 'National / International Platform',
     'Adapter le cadre KIMO à de nouvelles juridictions, en gardant une '
     'identité éducative commune et une conformité locale.',
     'Adapt the KIMO framework to additional jurisdictions while maintaining '
     'a global educational identity and local regulatory compliance.'),
]

# --- 18. La validation du pilote -------------------------------------------
PILOTE = [
    ('Interroger parents et employeurs avant de choisir les quartiers du '
     'pilote.',
     'Interview parents and employers before selecting pilot neighborhoods.'),
    ('Vérifier que le format micro-centre est agréable dans la juridiction '
     'visée.',
     'Validate local licensing feasibility for the micro-center format.'),
    ('Prototyper le programme avec des professionnels qualifiés de la petite '
     'enfance.',
     'Prototype the curriculum with qualified early-childhood '
     'professionals.'),
    ('Tester les parcours d\'inscription et de communication aux parents.',
     'Test enrollment and parent communication workflows.'),
    ('Mesurer la charge des éducateurs et le temps de préparation des '
     'activités.',
     'Measure educator workload and activity preparation time.'),
    ('Suivre occupation, liste d\'attente, présences, satisfaction et '
     'fidélité.',
     'Track occupancy, waitlist, attendance, satisfaction and retention.'),
    ('Mener des revues formelles de sécurité et de protection de l\'enfance '
     'avant de passer à l\'échelle.',
     'Conduct formal safety and safeguarding reviews before scaling.'),
    ('Se servir des résultats du pilote pour décider quel format de centre et '
     'quel modèle de partenariat standardiser.',
     'Use pilot evidence to decide which center format and partnership model '
     'should be standardized.'),
]

# --- 19. Les risques et ce qu'on y oppose ----------------------------------
RISQUES = [
    ('Une qualité inégale d\'un centre à l\'autre',
     'Inconsistent quality across decentralized centers',
     'Certification exigeante, formation, audits et standards de marque '
     'opposables.',
     'Strong certification, training, audits and enforceable brand '
     'standards.'),
    ('La pénurie d\'éducateurs', 'Educator shortages',
     'Filière de recrutement, conditions compétitives, partenariats de '
     'formation et planification des effectifs.',
     'Recruitment pipeline, competitive conditions, training partnerships and '
     'workforce planning.'),
    ('Un programme trop scolaire pour la petite enfance',
     'Over-academic early childhood program',
     'Le jeu d\'abord, une revue par des spécialistes du développement, et la '
     'liberté d\'appréciation de l\'éducateur.',
     'Play-first curriculum, developmental review and educator discretion.'),
    ('Les différences de réglementation', 'Regulatory differences',
     'Un manuel d\'exploitation par juridiction et une revue juridique '
     'locale.',
     'Jurisdiction-specific operating manuals and local legal/licensing '
     'review.'),
    ('Le risque sur les données des enfants', 'Child-data privacy risk',
     'Minimisation des données, accès strictement contrôlés, chiffrement et '
     'règles de conservation écrites.',
     'Data minimization, strict access controls, encryption and documented '
     'retention rules.'),
    ('Une croissance trop rapide qui abîme la culture',
     'Rapid expansion weakens culture',
     'Une croissance par grappes et une accréditation des partenaires par '
     'paliers.',
     'Cluster-based growth and staged partner accreditation.'),
    ('Une occupation trop faible dans un micro-centre',
     'Low occupancy in a micro-center',
     'Cartographie de la demande, partenariats employeurs et choix du site '
     'avant l\'ouverture.',
     'Demand mapping, employer partnerships and flexible site selection '
     'before opening.'),
]

# --- 20. L'architecture de marque ------------------------------------------
ARCHI_MARQUE = [
    ('Marque mère : KIMO.', 'Master brand: KIMO.'),
    ('Signature : KIMO — Apprendre à penser.',
     'Core signature: KIMO — Learn to Think.'),
    ('Nommage possible des centres : KIMO [Quartier] ou KIMO [Partenaire].',
     'Possible center naming: KIMO [Neighborhood] or KIMO [Partner].'),
    ('Familles de programmes possibles : KIMO Logic, KIMO Chess, KIMO '
     'Science, KIMO Move, KIMO Stories.',
     'Possible program families: KIMO Logic, KIMO Chess, KIMO Science, KIMO '
     'Move, KIMO Stories.'),
    ('Une identité visuelle intelligente et moderne, sans être scolaire ni '
     'institutionnelle.',
     'Visual identity should feel intelligent and modern without appearing '
     'overly academic or institutional.'),
]

# --- 21. Ce qui vient apres -----------------------------------------------
HORIZON_FR = (
    'Une fois le réseau d\'accueil éprouvé, KIMO peut aller au-delà des '
    'centres : formation d\'éducateurs, licence de programme, kits '
    'd\'apprentissage pour les parents, clubs de logique après l\'école, '
    'partenariats avec des écoles. Ces prolongements doivent SUIVRE la '
    'validation du modèle d\'accueil, pas la précéder.')
HORIZON_EN = (
    'Once the childcare network is proven, KIMO could extend beyond physical '
    'centers through educator training, curriculum licensing, parent learning '
    'kits, after-school logic clubs and partnerships with schools. These '
    'extensions should follow' + u'\u2014' + 'not precede' + u'\u2014' + 'the validation of the core '
    'childcare model.')


# ===========================================================================
#  KIMO TUTORING — sa note « Website & Platform Specification, Ages 6-17 ».
#
#  Meme regle que pour la note de concept : cote ANGLAIS c'est son texte, mot
#  pour mot ; cote FRANCAIS c'est ma traduction. Un controle compare les deux
#  documents.
#
#  ET UNE REGLE DE PLUS, propre a celui-ci. Ce document decrit une
#  PLATEFORME A CONSTRUIRE : une place de marche de tuteurs, des reservations,
#  des paiements, une classe virtuelle. Rien de tout cela n'existe. La page
#  presente donc le PROJET, et elle ne montre AUCUN tuteur : pas de fiche, pas
#  de photo, pas de note, pas d'avis de parent, pas de prix. Inventer un
#  tuteur, ce serait inventer une personne — et un parent choisit quelqu'un a
#  qui il confie son enfant.
# ===========================================================================

TUT_MARQUE_EN = 'KIMO Tutoring'
TUT_AGES_TITRE_FR = 'de 6 à 17 ans'
TUT_AGES_TITRE_EN = 'Ages 6-17'

TUT_INTRO_FR = (
    'KIMO Tutoring est une plateforme numérique pour les élèves de 6 à 17 '
    'ans, qui met les familles en relation avec des tuteurs qualifies et des '
    'programmes d\'enrichissement structures. Le service combine le tutorat '
    'individuel, les petits groupes, les cours en ligne et des séances en '
    'présentiel choisies. La plateforme est conçue autour du soutien '
    'scolaire, du raisonnement, de la curiosité et de progrès mesurables.')
TUT_INTRO_EN = (
    'KIMO Tutoring is a digital platform for students aged 6 to 17 that '
    'connects families with qualified tutors and structured enrichment '
    'programs. The service combines one-to-one tutoring, small groups, '
    'online lessons and selected in-person sessions. The platform is '
    'designed around academic support, reasoning, curiosity and measurable '
    'progress.')

TUT_PRINCIPES = [
    ('Utilisateurs vises : élèves de 6 à 17 ans, parents et tuteurs légaux, '
     'tuteurs et administrateurs.',
     'Target users: students aged 6-17, parents/guardians, tutors and '
     'administrators.'),
    ('Formats principaux : individuel en ligne, petits groupes, programmes '
     'récurrents et, là où c\'est possible, tutorat local en présentiel.',
     'Core formats: online 1:1, small groups, recurring programs and, where '
     'available, local in-person tutoring.'),
    ('Positionnement : soutien scolaire ET enrichissement intellectuel, pas '
     'seulement de l\'aide aux devoirs.',
     'Positioning: academic support plus intellectual enrichment rather than '
     'homework assistance alone.'),
    ('Principe premier : une réservation simple pour les parents, un '
     'apprentissage vivant pour les élèves, et de vrais contrôles '
     'd\'exploitation pour KIMO.',
     'Primary principle: simple booking for parents, engaging learning for '
     'students and strong operational controls for KIMO.'),
]

TUT_MATIERES = [
    ('Mathématiques', 'Mathematics'),
    ('Logique et résolution de problèmes', 'Logic & problem solving'),
    ('Échecs et stratégie', 'Chess & strategy'),
    ('Physique', 'Physics'),
    ('Sciences générales', 'General science'),
    ('Histoire et civilisations', 'History & civilizations'),
    ('Langues et lecture', 'Languages & literacy'),
    ('Programmation et compétences numériques', 'Coding & digital skills'),
    ('Aide aux devoirs', 'Homework support'),
    ('Préparation aux examens', 'Exam preparation'),
    ('Méthodes de travail et organisation', 'Study methods & organization'),
]

# Les quatre programmes par age. Les NOMS sont les siens.
TUT_PROGRAMMES = [
    ('6-8', 'KIMO Discover',
     'Fondations, curiosité, calcul, lecture, logique et sciences par le jeu.',
     'Foundations, curiosity, numeracy, reading, logic and playful science.'),
    ('9-11', 'KIMO Explore',
     'Fondamentaux scolaires, échecs, expériences, résolution de problèmes et '
     'méthodes de travail.',
     'Core academics, chess, experiments, problem solving and study habits.'),
    ('12-14', 'KIMO Advance',
     'Mathématiques et sciences approfondies, histoire, langues, '
     'programmation et autonomie.',
     'Deeper mathematics/science, history, languages, coding and independent '
     'learning.'),
    ('15-17', 'KIMO Master',
     'Soutien au secondaire, examens, matières avancées, méthodologie et '
     'préparation de la suite.',
     'Secondary-school support, exams, advanced subjects, methodology and '
     'future preparation.'),
]

TUT_RESERVATION = [
    ('Calendrier de disponibilité du tuteur en temps réel.',
     'Real-time tutor availability calendar.'),
    ('Réservation d\'une séance unique ou d\'un cours récurrent.',
     'Single or recurring lesson booking.'),
    ('Planification en ligne qui tient compte des fuseaux horaires.',
     'Timezone-aware online scheduling.'),
    ('Report et annulation selon la politique de la plateforme.',
     'Reschedule/cancel workflow based on platform policy.'),
    ('Confirmation et rappels automatiques.',
     'Automated confirmation and reminders.'),
    ('Liste d\'attente quand un tuteur ou un programme est complet.',
     'Waitlist for full tutors/programs.'),
    ('Forfaits et abonnements.', 'Package and subscription support.'),
    ('Réservation contrôlée par le parent pour les mineurs.',
     'Parent-controlled booking for minors.'),
]

TUT_CLASSE = [
    ('Salle de cours vidéo sécurisée, ou intégration d\'un fournisseur vidéo '
     'approuvé.',
     'Secure video lesson room or integration with an approved video '
     'provider.'),
    ('Tableau blanc interactif et partage d\'écran.',
     'Interactive whiteboard and screen sharing.'),
    ('Partage de documents et d\'exercices.',
     'Document and exercise sharing.'),
    ('Notes du tuteur et compte rendu après la séance.',
     'Tutor lesson notes and post-session summary.'),
    ('Travaux et ressources entre deux séances.',
     'Assignments/resources between sessions.'),
    ('Suivi de la présence aux séances.', 'Session attendance tracking.'),
    ('Aucun enregistrement par défaut ; toute fonction d\'enregistrement doit '
     'suivre un consentement explicite et les règles applicables à la vie '
     'privée des enfants.',
     'No recording by default; any recording feature must follow explicit '
     'consent and applicable child-privacy rules.'),
]

TUT_PARENTS = [
    ('Gérer un ou plusieurs enfants depuis un seul compte.',
     'Manage one or multiple children from one account.'),
    ('Réserver et gérer les séances.', 'Book and manage sessions.'),
    ('Voir les cours à venir et la présence.',
     'View upcoming lessons and attendance.'),
    ('Échanger avec le tuteur par la messagerie encadrée de la plateforme.',
     'Tutor messages through controlled platform communication.'),
    ('Bilans de progrès et objectifs d\'apprentissage.',
     'Progress summaries and learning objectives.'),
    ('Factures, paiements, forfaits et reçus.',
     'Invoices, payments, packages and receipts.'),
    ('Gérer les consentements, les contacts d\'urgence et les réglages de '
     'confidentialité.',
     'Manage consent, emergency/contact and privacy settings.'),
    ('Signaler un problème ou demander de l\'aide.',
     'Report a concern or request support.'),
]

TUT_ELEVE = [
    ('Une interface adaptée à son âge.', 'Age-appropriate interface.'),
    ('Le cours du jour et le planning à venir.',
     'Today\'s lesson and upcoming schedule.'),
    ('Objectifs d\'apprentissage et progrès.', 'Learning goals and progress.'),
    ('Exercices, ressources et travaux à faire.',
     'Exercises, resources and assignments.'),
    ('Des réussites qui encouragent la régularité, sans classement malsain.',
     'Achievements that encourage consistency without unhealthy ranking.'),
    ('Une messagerie sure, limitée aux échanges pédagogiques autorises.',
     'Safe messaging limited to authorized educational interactions.'),
]

TUT_TUTEUR = [
    ('Gestion du profil et des diplômes.',
     'Profile and credential management.'),
    ('Calendrier de disponibilité.', 'Availability calendar.'),
    ('Réservations et liste des élèves.', 'Bookings and student roster.'),
    ('Préparation des cours et bibliothèque de ressources KIMO.',
     'Lesson planning and KIMO resource library.'),
    ('Notes de séance et compte rendu de progrès.',
     'Session notes and progress reporting.'),
    ('Revenus, factures et état des versements le cas échéant.',
     'Earnings, invoices/payout status where applicable.'),
    ('Modules de formation et acceptation des règles.',
     'Training modules and policy acknowledgements.'),
    ('Outils de signalement et d\'escalade en cas d\'incident.',
     'Incident/safeguarding escalation tools.'),
]

TUT_VERIF_INTRO_FR = (
    'Parce que KIMO s\'adresse à des mineurs, le recrutement des tuteurs doit '
    'être plus rigoureux que sur une place de marché de tutorat pour '
    'adultes.')
TUT_VERIF_INTRO_EN = (
    'Because KIMO serves minors, tutor onboarding must be more rigorous than '
    'a conventional adult tutoring marketplace.')
TUT_VERIF = [
    ('Candidature et vérification d\'identité.',
     'Application and identity verification.'),
    ('Examen des diplômes et de la formation, en rapport avec la matière '
     'annoncée.',
     'Education/credential review appropriate to the advertised subject.'),
    ('Références, entretien et cours d\'essai.',
     'References and interview/sample lesson.'),
    ('Vérification des antécédents, là où la loi locale l\'exige ou le '
     'permet.',
     'Background/vulnerable-sector screening where required or available '
     'under local law.'),
    ('Formation à la protection de l\'enfance et code de conduite.',
     'Safeguarding training and code of conduct.'),
    ('Prise en main de la plateforme et du programme.',
     'Platform and curriculum onboarding.'),
    ('Période d\'essai et revue de qualité.',
     'Probation/quality-review period.'),
    ('Traitement continu des plaintes, des avis et des ré-vérifications.',
     'Ongoing complaint, review and re-verification process.'),
]

TUT_SECURITE = [
    ('Le parent ou le tuteur légal possède ou autorise le compte du mineur, '
     'selon l\'âge et la juridiction.',
     'Parent/guardian owns or authorizes accounts for minors as required by '
     'age and jurisdiction.'),
    ('Des règles claires sur les échanges tuteur-élève et sur tout contact '
     'hors plateforme.',
     'Clear rules governing tutor-student communication and off-platform '
     'contact.'),
    ('Messagerie encadrée, modération, escalade et journaux d\'audit.',
     'Controlled messaging, moderation/escalation capabilities and audit '
     'trails.'),
    ('Aucune collecte ni publication inutile de données personnelles '
     'd\'enfants.',
     'No unnecessary collection or publication of children\'s personal '
     'information.'),
    ('Un moyen de signalement pour les élèves et pour les parents.',
     'Reporting mechanism for students and parents.'),
    ('Une procédure d\'urgence et d\'escalade définie.',
     'Defined emergency and safeguarding escalation procedure.'),
    ('Accès du personnel aux dossiers sensibles selon son rôle.',
     'Role-based staff access to sensitive records.'),
    ('Des règles pour les cours en présentiel : lieux approuvés, remise de '
     'l\'enfant, surveillance.',
     'In-person lesson standards covering approved locations, pickup/guardian '
     'rules and supervision.'),
    ('Une revue juridique avant le lancement : protection de l\'enfance, vie '
     'privée, droit de la consommation, règles du tutorat et du travail dans '
     'chaque juridiction.',
     'Legal review before launch for child protection, privacy, consumer '
     'protection and tutoring/employment rules in each jurisdiction.'),
]

TUT_PAIEMENT = [
    ('Commission sur les séances de tutorat individuelles.',
     'Commission on individual tutoring sessions.'),
    ('Forfaits mensuels ou prépayés.',
     'Monthly or prepaid tutoring packages.'),
    ('Frais des programmes de groupe.', 'Group-program fees.'),
    ('Adhésion optionnelle avec avantages inclus.',
     'Optional membership with bundled benefits.'),
    ('Contrats avec des écoles, des employeurs, des associations ou des '
     'municipalités.',
     'Institutional contracts with schools, employers, community '
     'organizations or municipalities.'),
    ('Versements aux tuteurs, avec des frais et des relevés transparents.',
     'Tutor payout system with transparent fees and statements.'),
]
TUT_PAIEMENT_NOTE_FR = (
    'La plateforme doit prendre en charge les taxes, les monnaies, les '
    'remboursements et les règles de paiement propres à chaque marche de '
    'lancement.')
TUT_PAIEMENT_NOTE_EN = (
    'The platform should support taxes, currencies, refunds and payment '
    'rules appropriate to each launch market.')

TUT_SEO_INTRO_FR = (
    'KIMO doit être construit avec des pages d\'entrée indexables, en nombre, '
    'plutôt qu\'en s\'appuyant seulement sur la recherche interne.')
TUT_SEO_INTRO_EN = (
    'KIMO should be built with scalable, indexable landing pages rather than '
    'relying only on marketplace search.')
TUT_SEO = ['/tutors/[subject]', '/tutors/[subject]/[city]',
           '/programs/[age-group]', '/subjects/[subject]',
           '/online-tutoring/[subject]', '/resources/[topic]']
TUT_SEO_NOTE_FR = (
    'Chaque page engendrée doit contenir un contenu réellement utile et '
    'unique, et ne doit être indexée que lorsque KIMO à un service ou une '
    'information qui vaut la peine pour cette page-la.')
TUT_SEO_NOTE_EN = (
    'Every generated page should contain genuinely useful, unique content and '
    'should only be indexed when KIMO has relevant services or meaningful '
    'information for that page.')

TUT_MVP = [
    ('Accueil et pages par matière.', 'Home and subject pages.'),
    ('Inscription des parents et des élèves.',
     'Parent/student registration.'),
    ('Inscription et validation des tuteurs.',
     'Tutor registration and approval.'),
    ('Profils de tuteurs et recherche.', 'Tutor profiles and search.'),
    ('Calendrier de disponibilité et réservation.',
     'Availability calendar and booking.'),
    ('Paiements en ligne.', 'Online payments.'),
    ('Intégration du cours vidéo.', 'Video lesson integration.'),
    ('Tableaux de bord parent, élève et tuteur.',
     'Parent, student and tutor dashboards.'),
    ('Messagerie et notifications de base.',
     'Basic messaging and notifications.'),
    ('Console d\'administration.', 'Admin console.'),
    ('Notes de progrès.', 'Progress notes.'),
    ('Circuit de signalement et de protection de l\'enfance.',
     'Safeguarding/reporting workflow.'),
]
TUT_MVP_NOTE_FR = (
    'La ludification avancée, les recommandations par intelligence '
    'artificielle, les applications natives et une expansion géographique de '
    'grande ampleur doivent venir APRÈS la validation du parcours de tutorat '
    'de base.')
TUT_MVP_NOTE_EN = (
    'Advanced gamification, AI recommendations, native apps and large-scale '
    'geographic expansion should follow validation of the core tutoring '
    'workflow.')

TUT_IA = [
    ('Mise en relation élève-tuteur selon la matière, les disponibilités, les '
     'besoins et les préférences des parents.',
     'Tutor matching based on subject, availability, learning needs and '
     'parent preferences.'),
    ('Exercices suggères à partir des objectifs définis par le tuteur.',
     'Suggested exercises based on tutor-defined learning objectives.'),
    ('Bilans de progrès rédigés à partir des notes structurées de '
     'l\'éducateur, sous revue humaine.',
     'Progress summaries generated from structured educator notes, subject to '
     'human review.'),
    ('Aide administrative pour la planification et le support.',
     'Administrative assistance for scheduling and support.'),
]
TUT_IA_LIMITE_FR = (
    'L\'intelligence artificielle ne doit pas prendre seule de décision '
    'lourde de conséquences au sujet d\'un enfant, ni remplacer le jugement '
    'd\'un éducateur qualifie.')
TUT_IA_LIMITE_EN = (
    'AI must not autonomously make high-impact decisions about a child or '
    'replace qualified educator judgment.')

TUT_KPI = [
    ('Visiteur → inscription.', 'Visitor → registration conversion.'),
    ('Inscription → première réservation.',
     'Registration → first booking conversion.'),
    ('Taux de réservation répétée.', 'Repeat booking rate.'),
    ('Fidélité des élèves à 30, 90 et 180 jours.',
     'Student retention by 30/90/180 days.'),
    ('Taux d\'occupation et fidélité des tuteurs.',
     'Tutor utilization and retention.'),
    ('Nombre moyen de séances par élève actif.',
     'Average sessions per active student.'),
    ('Taux d\'annulation et d\'absence.', 'Cancellation/no-show rate.'),
    ('Satisfaction des parents.', 'Parent satisfaction.'),
    ('Objectifs d\'apprentissage atteints.', 'Learning-goal completion.'),
    ('Délais de réponse du support et de la protection de l\'enfance.',
     'Safeguarding and support response times.'),
    ('Chiffre d\'affaires et marge de contribution par élève actif.',
     'Revenue and contribution margin per active student.'),
]

TUT_PHASES = [
    ('1', 'Définition', 'Definition',
     'Choisir la juridiction de lancement, valider la réglementation, arrêter '
     'les catégories du programme et le modèle économique.',
     'Choose launch jurisdiction, validate regulations, finalize curriculum '
     'categories and business model.'),
    ('2', 'MVP', 'MVP',
     'Construire la place de marché, la réservation, le paiement, les '
     'tableaux de bord et l\'infrastructure de sécurité.',
     'Build the marketplace, booking, payment, dashboards and safety '
     'infrastructure.'),
    ('3', 'Pilote tuteurs', 'Tutor Pilot',
     'Recruter une première cohorte de tuteurs, encadrée, et tester les cours '
     'avec un nombre limite de familles.',
     'Recruit a controlled initial cohort of tutors and test lessons with a '
     'limited group of families.'),
    ('4', 'Lancement public', 'Public Launch',
     'Ouvrir les matières principales pour des tranches d\'âge et des lieux '
     'choisis ; mesurer la conversion et la fidélité.',
     'Launch core subjects for selected age groups and locations; measure '
     'conversion and retention.'),
    ('5', 'Expansion', 'Expansion',
     'Ajouter des matières, des villes, des programmes de groupe, des '
     'partenariats institutionnels et des technologies avancées.',
     'Add subjects, cities, group programs, institutional partnerships and '
     'advanced technology.'),
]

TUT_POSITION_FR = (
    'KIMO Tutoring doit se placer entre une place de marché de tutorat et un '
    'réseau éducatif structure. Les familles gardent la liberté de choisir '
    'leur tuteur, pendant que KIMO définit la qualité, la sécurité et les '
    'standards pédagogiques de tout l\'écosystème.')
TUT_POSITION_EN = (
    'KIMO Tutoring should sit between a tutoring marketplace and a structured '
    'educational network. Families receive the flexibility of choosing a '
    'tutor while KIMO defines quality, safety and educational standards '
    'across the ecosystem.')

# Ce qui manque pour cette plateforme-la, en plus des points deja listes.
TUT_A_DEFINIR = [
    ('La JURIDICTION de lancement — c\'est la première ligne de sa propre '
     'phase 1, et elle commande la revue juridique et la vérification des '
     'antécédents.',
     'The launch JURISDICTION - the first line of his own phase 1, and what '
     'drives the legal review and the background screening.'),
    ('Les PRIX : commission, forfaits, frais de groupe, adhésion.',
     'PRICING: commission, packages, group fees, membership.'),
    ('Le FOURNISSEUR VIDÉO retenu pour la classe virtuelle.',
     'The VIDEO PROVIDER chosen for the virtual classroom.'),
    ('Le prestataire de PAIEMENT et les monnaies acceptées.',
     'The PAYMENT provider and the accepted currencies.'),
    ('Qui conduit la REVUE JURIDIQUE avant le lancement.',
     'Who runs the LEGAL REVIEW before launch.'),
]

TUT_AVERT_FR = (
    'Cette page présente un PROJET de plateforme. Rien n\'est en service : il '
    'n\'y a pas de tuteur inscrit, pas de cours réservable, pas de paiement. '
    'Aucune fiche de tuteur, aucune photo, aucune note et aucun avis de '
    'parent ne figure ici, et il n\'y en aura pas tant qu\'il n\'y aura pas '
    'de vrais tuteurs : un parent choisit la personne à qui il confie son '
    'enfant, et une fiche inventée serait une personne inventée.')
TUT_AVERT_EN = (
    'This page presents a PLATFORM PROJECT. Nothing is in service: there is '
    'no registered tutor, no bookable lesson, no payment. No tutor card, no '
    'photograph, no rating and no parent review appears here, and none will '
    'until there are real tutors: a parent is choosing the person they trust '
    'with their child, and an invented profile would be an invented person.')
