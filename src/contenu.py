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
SIGNATURE_FR = 'Apprendre a penser.'
SIGNATURE_TRAD_A_VALIDER = True

# Sa promesse centrale (section 2 de la note), mot pour mot cote anglais.
PROMESSE_EN = ('One educational ecosystem, many local centers: proximity for '
               'families, autonomy for local teams and consistent quality '
               'across the network.')
PROMESSE_FR = ('Un seul ecosysteme educatif, beaucoup de centres locaux : la '
               'proximite pour les familles, l\'autonomie pour les equipes '
               'locales, et la meme qualite partout dans le reseau.')

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
    ('pays', 'Le PAYS de la premiere creche',
     'Le pays commande tout le cadre reglementaire, la monnaie et la langue.'),
    ('ville', 'La VILLE de la premiere creche',
     'Agrement, locaux et taux d\'encadrement se traitent au niveau local.'),
    ('domaine', 'Le NOM DE DOMAINE',
     'Aujourd\'hui le site tourne sur une adresse de demonstration.'),
    ('entree', 'Le DROIT D\'ENTREE au reseau',
     'Affiche dans le modele economique et utilise par le simulateur.'),
    ('redevance', 'La REDEVANCE du reseau',
     'Meme chose : en pourcentage du chiffre d\'affaires, ou forfaitaire.'),
    ('apport', 'L\'APPORT PERSONNEL demande au candidat',
     'C\'est le premier filtre d\'un dossier de franchise.'),
    ('contact', 'L\'ADRESSE qui recoit les candidatures',
     'Le formulaire est construit ; il lui manque sa destination.'),
]

# ---------------------------------------------------------------------------
# LE MODELE ECONOMIQUE. Tout est a None tant que Hakim n'a pas tranche.
#   montant : nombre, ou None
#   unite   : 'devise' | 'pourcent' | 'texte'
# ---------------------------------------------------------------------------
MODELE = [
    ('entree', 'Droit d\'entree', 'Entry fee', None, 'devise',
     'Verse une fois a la signature. Il paie la formation initiale, '
     'l\'ouverture accompagnee et la mise en place de la methode.',
     'Paid once at signature. It covers the initial training, the assisted '
     'opening and the setup of the method.'),
    ('duree', 'Duree du contrat', 'Contract term', None, 'texte',
     'La duree d\'un contrat de franchise se cale sur celle du bail : '
     'un contrat plus court que le bail laisse le franchise avec un local '
     'et sans marque.',
     'A franchise term is set against the lease: a term shorter than the '
     'lease leaves the franchisee with premises and no brand.'),
    ('redevance', 'Redevance d\'exploitation', 'Ongoing royalty', None,
     'pourcent',
     'Prelevee sur le chiffre d\'affaires encaisse. Elle finance la methode, '
     'les outils, le support et le controle qualite.',
     'Charged on collected revenue. It funds the method, the tools, the '
     'support and the quality control.'),
    ('communication', 'Contribution communication', 'Marketing contribution',
     None, 'pourcent',
     'Fonds commun : campagnes nationales, site, referencement local des '
     'creches du reseau.',
     'Common fund: national campaigns, website, local search presence for '
     'the network\'s centres.'),
    ('apport', 'Apport personnel demande', 'Personal contribution required',
     None, 'devise',
     'La part que le candidat finance lui-meme, hors emprunt.',
     'The share the candidate finances themselves, outside of borrowing.'),
    ('investissement', 'Investissement total', 'Total investment', None,
     'devise',
     'Travaux, mobilier, materiel pedagogique, tresorerie de demarrage. '
     'Il depend du local et du pays : il se chiffre par ville, pas en '
     'general.',
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
    ('capacite', 'Capacite maximale de l\'unite',
     'Maximum capacity of a unit',
     'Le nombre de places qui definit une « micro-creche » est fixe par la '
     'reglementation du pays. Au-dela, l\'etablissement change de categorie '
     'et de regles.',
     'The number of places that defines a "micro-nursery" is set by national '
     'regulation. Above it, the facility changes category and rules.',
     None),
    ('encadrement', 'Taux d\'encadrement',
     'Staff-to-child ratio',
     'Nombre d\'adultes diplomes par enfant, et il differe souvent selon que '
     'l\'enfant marche ou non.',
     'Number of qualified adults per child, often different for children who '
     'walk and those who do not.',
     None),
    ('responsable', 'Qualification du responsable',
     'Qualification of the manager',
     'Diplome exige, annees d\'experience, et parfois une reference '
     'sanitaire distincte.',
     'Required diploma, years of experience, and sometimes a separate health '
     'referent.',
     None),
    ('surface', 'Surface par enfant',
     'Floor area per child',
     'Surface interieure utile, et acces a un espace exterieur selon les '
     'pays.',
     'Usable indoor area, plus access to outdoor space depending on the '
     'country.',
     None),
    ('agrement', 'Autorite qui delivre l\'agrement',
     'Authority granting the licence',
     'C\'est elle qui visite le local avant l\'ouverture et qui peut la '
     'refuser. Le calendrier d\'ouverture depend de son delai.',
     'It inspects the premises before opening and can refuse. The opening '
     'schedule depends on its lead time.',
     None),
    ('financement', 'Aides et financement des familles',
     'Family funding and subsidies',
     'Dans plusieurs pays, une partie du prix paye par la famille est prise '
     'en charge. Cela change le tarif affichable, donc tout le modele.',
     'In several countries part of the fee paid by the family is subsidised. '
     'That changes the price you can charge, and so the whole model.',
     None),
]

# ---------------------------------------------------------------------------
# LE MODELE DECENTRALISE — les quatre idees qui font KIMO. Ecrit sans citer
# aucun reseau existant.
# ---------------------------------------------------------------------------
PILIERS = [
    ('proximite', 'Une creche par quartier', 'One nursery per neighbourhood',
     'Le trajet domicile-creche est le premier critere des parents, avant le '
     'prix. Une unite petite s\'implante dans un quartier ou une grande '
     'structure ne rentre pas : un rez-de-chaussee, une maison, un local '
     'commercial reconverti.',
     'The home-to-nursery trip is the first thing parents look at, before '
     'price. A small unit fits into a neighbourhood where a large facility '
     'cannot: a ground floor, a house, a converted shop.'),
    ('taille', 'Petite unite, adulte connu',
     'Small unit, a familiar adult',
     'Un enfant de deux ans ne retient pas quinze visages. Une unite courte '
     'garde le meme adulte devant le meme groupe toute la journee, et les '
     'parents parlent au responsable, pas a un standard.',
     'A two-year-old does not retain fifteen faces. A small unit keeps the '
     'same adult with the same group all day, and parents talk to the '
     'manager, not to a switchboard.'),
    ('methode', 'Une methode commune, pas une improvisation',
     'A shared method, not improvisation',
     'Ce que le reseau apporte n\'est pas un logo : c\'est une progression '
     'ecrite, des supports, un cahier d\'observation, et la formation qui va '
     'avec. Deux creches KIMO a deux bouts du pays travaillent de la meme '
     'facon.',
     'What the network brings is not a logo: it is a written progression, '
     'materials, an observation record, and the training that goes with it. '
     'Two KIMO nurseries at opposite ends of the country work the same way.'),
    ('couts', 'Les couts lourds sont mutualises',
     'The heavy costs are shared',
     'Inscription en ligne, facturation, planning, achats, conformite, site '
     'et referencement : une creche seule les paie en entier et les fait mal. '
     'Le reseau les porte une fois pour toutes.',
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
    'KIMO ne cherche pas a transformer la creche en ecole primaire. Les '
    'themes intellectuels y sont des supports de jeu et de decouverte. '
    'L\'objectif est de poser les bases du raisonnement et de la curiosite '
    'sans rien retirer au jeu libre, au developpement affectif, a la parole, '
    'a la vie en groupe, a la creation et au repos.')
METHODE_INTRO_EN = (
    'KIMO is not intended to turn preschool into primary school. The '
    'curriculum uses intellectual themes as tools for play and discovery. '
    'The objective is to create foundations for reasoning and curiosity '
    'while preserving free play, emotional development, communication, '
    'social interaction, creativity and rest.')

METHODE = [
    ('Poser la question avant de donner la reponse.',
     'Ask questions before giving answers.'),
    ('Manipuler des objets reels avant d\'introduire des symboles '
     'abstraits.',
     'Manipulate real objects before introducing abstract symbols.'),
    ('Demander a l\'enfant d\'expliquer comment il est arrive a sa solution.',
     'Encourage children to explain how they reached a solution.'),
    ('Se servir de l\'erreur pour essayer une autre approche.',
     'Use mistakes as opportunities to test another approach.'),
    ('Equilibrer les activites dirigees et l\'exploration menee par '
     'l\'enfant.',
     'Balance structured activities with child-led exploration.'),
    ('Regler la difficulte sur la maturite de l\'enfant, pas sur son age.',
     'Adapt complexity to developmental readiness rather than age alone.'),
]

# ---------------------------------------------------------------------------
# LES SEPT PILIERS D'APPRENTISSAGE (section 6 de sa note). Anglais mot pour
# mot, francais traduit.
# ---------------------------------------------------------------------------
APPRENTISSAGE = [
    ('logique', 'Logique et resolution de problemes',
     'Logic & Problem Solving',
     'Casse-tete, tris, reconnaissance de motifs, construction, mises en '
     'ordre, labyrinthes, jeux de memoire et petits defis de strategie. '
     'L\'enfant apprend a comparer, classer, anticiper et verifier une '
     'solution.',
     'Puzzles, sorting, pattern recognition, construction, sequencing, '
     'mazes, memory games and simple strategy challenges. Children learn to '
     'compare, classify, anticipate and test solutions.'),
    ('echecs', 'Echecs et pensee strategique',
     'Chess & Strategic Thinking',
     'Chez les plus jeunes, les echecs commencent par les couleurs, '
     'l\'orientation du plateau, la reconnaissance des pieces et des jeux de '
     'deplacement. Les plus grands passent a des mini-parties avec un nombre '
     'de pieces limite. Le but est l\'attention, le raisonnement dans '
     'l\'espace et l\'anticipation — pas la performance en competition.',
     'For younger children, chess begins with colors, board orientation, '
     'piece recognition and movement games. Older preschoolers can progress '
     'to mini-games with a limited number of pieces. The purpose is '
     'attention, spatial reasoning and anticipation' + u'\u2014' + 'not competitive '
     'performance.'),
    ('maths', 'Mathematiques', 'Mathematics',
     'Compter avec des objets, quantites, formes, comparaison, mesure, '
     'symetrie, motifs, reperage dans l\'espace et premieres idees de '
     'calcul. Les activites restent concretes et ludiques.',
     'Counting through objects, quantities, shapes, comparison, measurement, '
     'symmetry, patterns, spatial relationships and simple arithmetic '
     'concepts. Activities remain concrete and playful.'),
    ('sciences', 'Physique et sciences', 'Physics & Science',
     'Experiences sans danger autour de l\'eau, l\'air, la lumiere, le son, '
     'les aimants, l\'equilibre, la gravite, le mouvement, les plantes et '
     'les matieres. On demande a l\'enfant de prevoir ce qui va se passer, '
     'd\'observer le resultat et de le decrire.',
     'Safe experiments involving water, air, light, sound, magnets, balance, '
     'gravity, motion, plants and materials. Children are encouraged to '
     'predict what will happen, observe the result and describe what they '
     'saw.'),
    ('histoire', 'Histoire et civilisations', 'History & Civilizations',
     'Recits illustres sur les civilisations, les inventions, les '
     'explorateurs, l\'architecture, les transports, les ecritures et les '
     'grandes realisations humaines. L\'accent est mis sur le recit, la '
     'chronologie et la curiosite culturelle, pas sur les dates a retenir.',
     'Illustrated stories about civilizations, inventions, explorers, '
     'architecture, transport, writing systems and major human achievements. '
     'The focus is narrative, chronology and cultural curiosity rather than '
     'memorization of dates.'),
    ('corps', 'Developpement physique', 'Physical Development',
     'Du mouvement tous les jours : equilibre, coordination, force, '
     'motricite fine et globale, rythme et jeux cooperatifs. L\'activite en '
     'exterieur est integree des que c\'est possible.',
     'Daily movement supporting balance, coordination, strength, fine and '
     'gross motor skills, rhythm and cooperative play. Outdoor activity is '
     'integrated whenever possible.'),
    ('creation', 'Creation et expression', 'Creativity & Communication',
     'Dessin, musique, recit, construction, jeux de role et travaux manuels '
     'font contrepoids aux activites analytiques et aident l\'enfant a dire '
     'ses idees de plusieurs facons.',
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
     'Le formulaire en bas de cette page. Ville visee, situation, apport, '
     'calendrier souhaite.',
     'The form at the bottom of this page. Target city, situation, personal '
     'contribution, target date.', None),
    ('2', 'Entretien et dossier', 'Interview and file',
     'Un entretien, puis le document d\'information precontractuelle : ce '
     'que le reseau apporte, ce qu\'il facture, ce qu\'il exige.',
     'An interview, then the pre-contractual disclosure document: what the '
     'network provides, what it charges, what it requires.', None),
    ('3', 'Etude de la zone', 'Territory study',
     'Nombre de jeunes enfants, offre existante, trajets. Une zone qui ne '
     'porte pas une creche, on le voit avant le bail, pas apres.',
     'Number of young children, existing supply, commutes. A territory that '
     'cannot carry a nursery shows up before the lease, not after.', None),
    ('4', 'Local et agrement', 'Premises and licence',
     'Recherche du local, mise en conformite, depot du dossier aupres de '
     'l\'autorite. C\'est l\'etape la plus longue, et sa duree ne depend pas '
     'de nous.',
     'Finding the premises, bringing them up to standard, filing with the '
     'authority. This is the longest step, and its length is not ours to '
     'set.', None),
    ('5', 'Formation', 'Training',
     'La methode, les outils, la gestion, la relation aux familles. Le '
     'responsable et le premier encadrant la suivent ensemble.',
     'The method, the tools, day-to-day management, working with families. '
     'The manager and the first practitioner attend together.', None),
    ('6', 'Ouverture accompagnee', 'Assisted opening',
     'Quelqu\'un du reseau est sur place les premiers jours. Les premieres '
     'inscriptions se font a deux.',
     'Someone from the network is on site for the first days. The first '
     'enrolments are handled together.', None),
]

# ---------------------------------------------------------------------------
# CE QUE CHACUN APPORTE. Une franchise se juge la-dessus.
# ---------------------------------------------------------------------------
RESEAU_APPORTE = [
    ('La marque et la charte', 'The brand and its guidelines'),
    ('La methode ecrite et ses supports', 'The written method and materials'),
    ('La formation initiale et le recyclage annuel',
     'Initial training and annual refresher'),
    ('Le logiciel : inscriptions, presences, facturation, planning',
     'The software: enrolment, attendance, billing, scheduling'),
    ('L\'etude de zone avant la signature du bail',
     'The territory study before the lease is signed'),
    ('Les achats groupes : mobilier, materiel, consommables',
     'Group purchasing: furniture, equipment, consumables'),
    ('Le site du reseau et la fiche locale de la creche',
     'The network site and the nursery\'s local page'),
    ('Le controle qualite et les visites',
     'Quality control and site visits'),
    ('L\'exclusivite sur une zone definie au contrat',
     'Exclusivity over a territory defined in the contract'),
]

FRANCHISE_APPORTE = [
    ('Le local, et sa mise en conformite',
     'The premises, and bringing them up to standard'),
    ('L\'apport personnel et le financement',
     'The personal contribution and the financing'),
    ('Le recrutement de l\'equipe, avec l\'aide du reseau',
     'Recruiting the team, with the network\'s help'),
    ('Sa presence : ce n\'est pas un placement, c\'est un metier',
     'Their presence: this is not an investment, it is a job'),
    ('Le respect de la methode et des standards',
     'Applying the method and the standards'),
    ('La relation avec les familles et l\'autorite locale',
     'The relationship with families and the local authority'),
]

PROFIL = [
    ('Un metier de la petite enfance, de la sante ou de l\'education — ou '
     'un associe qui l\'exerce.',
     'A background in early years, health or education — or a partner who '
     'has one.'),
    ('L\'envie de tenir un lieu, pas d\'y placer de l\'argent.',
     'Wanting to run a place, not to park money in one.'),
    ('Un ancrage local reel dans la ville visee.',
     'Real local roots in the target city.'),
    ('La capacite a financer l\'apport demande.',
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
    ('places', 'Places agreees', 'Licensed places', 12, 1, 'nombre'),
    ('occupation', 'Taux d\'occupation', 'Occupancy rate', 90, 1, 'pourcent'),
    ('tarif', 'Recette mensuelle par place', 'Monthly revenue per place',
     1300, 10, 'devise'),
    ('loyer', 'Loyer mensuel', 'Monthly rent', 1600, 50, 'devise'),
    ('etp', 'Encadrants (equivalent temps plein)',
     'Practitioners (full-time equivalent)', 4, 1, 'nombre'),
    ('salaire', 'Cout mensuel charge par encadrant',
     'Monthly loaded cost per practitioner', 2500, 50, 'devise'),
    ('autres', 'Autres charges mensuelles', 'Other monthly costs', 1100, 50,
     'devise'),
    ('redevance', 'Redevance reseau', 'Network royalty', 0, 1, 'pourcent'),
]

DEVISES = [('EUR', '€'), ('CAD', '$'), ('CHF', 'CHF'), ('DZD', 'DA'),
           ('MAD', 'DH'), ('GBP', '£')]

SIM_NOTE_FR = ('Aucun chiffre de ce simulateur n\'est un chiffre KIMO, et '
               'les valeurs de depart ne decrivent aucun marche : elles sont '
               'rondes et arbitraires, elles servent a montrer le calcul. '
               'Remplacez-les par les votres. La redevance reseau est a zero '
               'parce qu\'elle n\'est pas encore fixee — posez-la des '
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
    ('nom', 'Nom et prenom', 'Full name', 'text', True, None),
    ('tel', 'Telephone', 'Phone', 'tel', True, None),
    ('courriel', 'Adresse de courriel', 'Email address', 'email', True, None),
    ('pays', 'Pays vise', 'Target country', 'text', True, None),
    ('ville', 'Ville visee', 'Target city', 'text', True, None),
    ('profil', 'Votre situation', 'Your background', 'select', True, [
        ('Professionnel de la petite enfance',
         'Early-years professional'),
        ('Sante ou education', 'Health or education'),
        ('Entrepreneur, avec un associe du metier',
         'Entrepreneur, with a partner from the field'),
        ('Autre', 'Other')]),
    ('apport', 'Apport personnel disponible', 'Personal contribution available',
     'text', False, None),
    ('local', 'Avez-vous deja un local ?', 'Do you already have premises?',
     'select', True, [
         ('Oui, un local identifie', 'Yes, premises identified'),
         ('Une recherche en cours', 'A search under way'),
         ('Pas encore', 'Not yet')]),
    ('echeance', 'Ouverture souhaitee', 'Target opening', 'select', True, [
        ('Dans les 6 mois', 'Within 6 months'),
        ('6 a 12 mois', '6 to 12 months'),
        ('Plus de 12 mois', 'More than 12 months')]),
    ('message', 'Votre projet en quelques lignes',
     'Your project, in a few lines', 'textarea', False, None),
]

# ---------------------------------------------------------------------------
# LA FAQ. Les reponses qui dependent d'un chiffre non fixe le DISENT.
# ---------------------------------------------------------------------------
FAQ = [
    ('Faut-il un diplome de la petite enfance pour ouvrir une KIMO ?',
     'Do I need an early-years qualification to open a KIMO?',
     'Pour DIRIGER l\'etablissement, la loi du pays l\'exige presque '
     'toujours, et c\'est elle qui tranche, pas le reseau. Un candidat sans '
     'ce diplome ouvre avec un responsable qui l\'a. La qualification exacte '
     'fait partie des points a preciser des que le pays est arrete.',
     'To RUN the facility, national law almost always requires one, and that '
     'is what decides, not the network. A candidate without it opens with a '
     'manager who has it. The exact qualification is one of the points to be '
     'settled once the country is chosen.'),
    ('Combien de places par creche ?',
     'How many places per nursery?',
     'C\'est un plafond reglementaire, pas un choix commercial : le nombre '
     'qui definit une micro-creche est fixe par le pays. Il sera ecrit ici '
     'des que le pays de la premiere ouverture sera arrete.',
     'That is a regulatory ceiling, not a commercial choice: the number that '
     'defines a micro-nursery is set nationally. It will appear here as soon '
     'as the country of the first opening is settled.'),
    ('Quel est le droit d\'entree ?',
     'What is the entry fee?',
     'Il n\'est pas encore fixe. Tant qu\'il ne l\'est pas, cette page '
     'affiche « a definir » plutot qu\'un ordre de grandeur : un candidat '
     'construit son financement sur ce chiffre.',
     'It has not been set yet. Until it is, this page shows "to be set" '
     'rather than a ballpark: a candidate builds their financing on that '
     'number.'),
    ('Le reseau prend-il une part du capital de ma societe ?',
     'Does the network take equity in my company?',
     'Non. Une franchise n\'est pas une filiale : le franchise possede son '
     'entreprise, son bail et son fonds. Le reseau vend l\'usage d\'une '
     'marque et d\'une methode.',
     'No. A franchise is not a subsidiary: the franchisee owns their '
     'company, their lease and their business. The network licenses the use '
     'of a brand and a method.'),
    ('Puis-je ouvrir plusieurs creches ?',
     'Can I open several nurseries?',
     'C\'est le sens du modele : de petites unites, donc plusieurs. En '
     'pratique, la deuxieme se signe apres une premiere annee complete, '
     'agrement obtenu et equipe stable.',
     'That is the point of the model: small units, therefore several. In '
     'practice the second is signed after a full first year, with the licence '
     'obtained and a stable team.'),
    ('Qu\'est-ce qui est exclusif ?',
     'What exactly is exclusive?',
     'Une zone definie au contrat, pas une ville entiere par principe. La '
     'taille de la zone se decide sur le nombre de jeunes enfants qui y '
     'vivent, ce que mesure l\'etude de zone.',
     'A territory defined in the contract, not a whole city as a matter of '
     'course. Its size is set from the number of young children living '
     'there, which the territory study measures.'),
    ('Le reseau aide-t-il a trouver le financement ?',
     'Does the network help with financing?',
     'Il fournit le dossier : etude de zone, previsionnel, description du '
     'concept. Il ne prete pas et ne se porte pas caution.',
     'It provides the file: territory study, forecast, description of the '
     'concept. It does not lend and does not act as guarantor.'),
    ('Que se passe-t-il si l\'agrement est refuse ?',
     'What happens if the licence is refused?',
     'C\'est pour cela que le local et l\'agrement viennent AVANT la '
     'formation dans le parcours, et que le contrat doit prevoir ce cas '
     'explicitement. La redaction exacte fait partie du dossier juridique a '
     'faire etablir dans le pays retenu.',
     'That is why premises and licence come BEFORE training in the journey, '
     'and why the contract must address the case explicitly. The exact '
     'wording belongs to the legal file to be drawn up in the chosen '
     'country.'),
]

AVERT_FR = ('DEMONSTRATION. KIMO est un reseau en cours de constitution : '
            'aucune creche n\'est ouverte a ce jour. Les valeurs marquees '
            '« a definir » ne sont pas des oublis, ce sont des decisions qui '
            'n\'ont pas encore ete prises, ou des regles qui dependent du '
            'pays retenu. Aucun chiffre reglementaire n\'est avance ici tant '
            'qu\'il n\'a pas ete verifie dans le pays concerne.')
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
     'Standards, programme, technologie, marque, formation et controle',
     'Standards, curriculum, technology, brand, training and audit',
     'Conception du programme, certification des educateurs, plateforme, '
     'achats',
     'Program design, educator certification, platform, procurement'),
    ('L\'unite KIMO locale', 'Local KIMO Unit',
     'L\'accueil des enfants et la pedagogie au quotidien',
     'Daily childcare and educational delivery',
     'Equipe, activites, relation aux parents, planning local',
     'Staffing, activities, parent relationships, local scheduling'),
    ('Les partenaires', 'Partners',
     'Apportent des locaux, du capital, des familles ou des services '
     'complementaires',
     'Provide sites, capital, referrals or complementary services',
     'Employeurs, municipalites, promoteurs, universites',
     'Employers, municipalities, developers, universities'),
    ('Les familles', 'Families',
     'Choisissent leur centre et participent au developpement de l\'enfant',
     'Choose centers and participate in child development',
     'Inscription, retours, points sur les progres, activites a la maison',
     'Enrollment, feedback, progress discussions, home activities'),
]

# --- 4. Le format d'une unite ----------------------------------------------
# La fourchette 8-20 est SA cible, et il l'assortit lui-meme de « subject to
# local childcare regulations ». Elle est donc reproduite AVEC sa reserve, et
# elle ne remplace pas la ligne « capacite » du tableau reglementaire, qui
# reste a definir : une cible de reseau n'est pas un plafond de droit.
FORMAT = [
    ('Capacite visee : environ 8 a 20 enfants par micro-centre, sous reserve '
     'de la reglementation locale de la petite enfance.',
     'Target capacity: approximately 8-20 children per micro-center, subject '
     'to local childcare regulations.'),
    ('Implantations possibles : maisons amenagees, rez-de-chaussee '
     'residentiels, locaux commerciaux, sites d\'employeurs ou batiments '
     'modulaires concus pour cela.',
     'Possible locations: adapted houses, ground-floor residential spaces, '
     'commercial units, employer campuses or purpose-built modular '
     'facilities.'),
    ('Groupes d\'age souples, selon les regles d\'agrement et les besoins de '
     'developpement de l\'enfant.',
     'Flexible age grouping based on licensing requirements and '
     'child-development needs.'),
    ('Des zones dediees : apprentissage calme, construction et casse-tete, '
     'mouvement, creation, repas et repos.',
     'Dedicated zones for quiet learning, construction/puzzles, movement, '
     'creative work, meals and rest.'),
    ('Un acces exterieur, ou des sorties programmees, partout ou c\'est exige '
     'et realisable.',
     'Outdoor access or scheduled outdoor activity wherever required and '
     'feasible.'),
    ('Entree securisee, remise de l\'enfant controlee, procedures d\'urgence '
     'et securisation adaptee aux jeunes enfants.',
     'Secure entry, controlled child release, emergency procedures and '
     'appropriate childproofing.'),
]
FORMAT_AVERT_FR = (
    'Un etablissement KIMO ne doit jamais echanger la securite ou la '
    'conformite contre de la compacite. La capacite definitive, les taux '
    'd\'encadrement, les dimensions des pieces, le couchage, la preparation '
    'des repas et les exigences d\'espace exterieur doivent etre adaptes a la '
    'juridiction dans laquelle chaque unite fonctionne.')
FORMAT_AVERT_EN = (
    'KIMO facilities must never trade safety or regulatory compliance for '
    'compactness. Final capacity, staff ratios, room dimensions, sleep '
    'arrangements, food preparation and outdoor-space requirements must be '
    'adapted to the jurisdiction in which each unit operates.')

# --- 7. Le parcours par age ------------------------------------------------
AGES = [
    ('Premiers pas', 'Early toddler',
     'Decouverte sensorielle, langage, mouvement',
     'Sensory discovery, language, movement',
     'Tris, empilements, chansons, matieres, cause et effet simples',
     'Sorting, stacking, songs, textures, simple cause-and-effect',
     'Jeu court et tres surveille', 'Short, highly supervised play'),
    ('Grands petits', 'Older toddler',
     'Motifs, coordination, premieres quantites',
     'Patterns, coordination, early quantities',
     'Appariements, formes, parcours de motricite, construction, observation '
     'de la nature',
     'Matching, shapes, obstacle courses, building, nature observation',
     'Repetition et exploration', 'Repetition and exploration'),
    ('Maternelle', 'Preschool',
     'Raisonnement, strategie, recit, sciences',
     'Reasoning, strategy, storytelling, science',
     'Casse-tete, mini-parties d\'echecs, mesure, experiences, recits de '
     'civilisations',
     'Puzzles, chess mini-games, measurement, experiments, civilization '
     'stories',
     'Decouverte guidee', 'Guided discovery'),
    ('Avant la grande section', 'Pre-kindergarten',
     'Raisonnement en plusieurs etapes et autonomie',
     'Multi-step thinking and independence',
     'Jeux de planification, defis de nombres, experiences, cartes et frises, '
     'projets collectifs',
     'Planning games, number challenges, experiments, maps/timelines, '
     'collaborative projects',
     'Projets et discussion', 'Projects and discussion'),
]

# --- 8. La journee type ----------------------------------------------------
JOURNEE = [
    ('07:30-09:00', 'Arrivee, jeu libre et transmission avec la famille',
     'Arrival, free play and family handover'),
    ('09:00-09:20', 'Regroupement du matin, langage, on annonce la journee',
     'Morning circle, language and planning'),
    ('09:20-10:00', 'Rotation logique / mathematiques / echecs',
     'Logic / mathematics / chess rotation'),
    ('10:00-10:30', 'Collation et temps social', 'Snack and social time'),
    ('10:30-11:30', 'Mouvement en exterieur, developpement physique',
     'Outdoor movement / physical development'),
    ('11:30-12:00', 'Sciences, ou recit et activite d\'histoire',
     'Science or history story/activity'),
    ('12:00-14:00', 'Repas, hygiene, repos et temps calme',
     'Lunch, hygiene, rest/quiet time'),
    ('14:00-15:00', 'Atelier creatif, construction, projet',
     'Creative workshop / construction / project'),
    ('15:00-15:30', 'Collation', 'Snack'),
    ('15:30-16:30', 'Jeu guide et apprentissage en petits groupes',
     'Guided play and small-group learning'),
    ('16:30-18:00', 'Jeu libre, depart des enfants et retour aux parents',
     'Free play, parent pickup and daily feedback'),
]

# --- 9. Les educateurs -----------------------------------------------------
EDUCATEURS_INTRO_FR = (
    'Les educateurs restent le coeur de KIMO. La technologie soutient leur '
    'travail, elle ne remplace ni leur observation, ni leur attention, ni '
    'leur jugement.')
EDUCATEURS_INTRO_EN = (
    'Educators remain the core of KIMO. Technology supports their work but '
    'does not replace human observation, care or judgment.')
EDUCATEURS = [
    ('Un parcours d\'integration obligatoire a la pedagogie KIMO et a la '
     'protection de l\'enfance.',
     'Mandatory onboarding in KIMO pedagogy and safeguarding.'),
    ('Des fiches d\'activite avec objectifs d\'apprentissage, materiel, '
     'adaptations et consignes de securite.',
     'Activity guides with learning objectives, materials, adaptations and '
     'safety notes.'),
    ('Une formation continue : developpement de l\'enfant, communication, '
     'premiers secours, conduite du groupe.',
     'Continuous professional development in child development, '
     'communication, first aid and classroom practice.'),
    ('Une equipe locale libre d\'adapter les activites a son groupe, dans le '
     'respect des standards du reseau.',
     'Local leadership empowered to adapt activities to the group while '
     'respecting network standards.'),
    ('Un suivi fonde sur l\'observation, pas sur des tests sous pression ni '
     'sur un classement des enfants.',
     'Observation-based progress records rather than high-pressure testing or '
     'child ranking.'),
]

# --- 10. La plateforme -----------------------------------------------------
PLATEFORME = [
    ('Compte parent, inscription et dossier de l\'enfant securise.',
     'Parent account, enrollment and secure child profile.'),
    ('Gestion des places, en temps reel ou programmee, entre les centres '
     'KIMO proches.',
     'Real-time or scheduled capacity management across nearby KIMO '
     'centers.'),
    ('Presences, personnes autorisees a venir chercher l\'enfant, absences.',
     'Attendance, authorized pickup and absence management.'),
    ('Facturation, aides et suivi des paiements la ou la loi le permet.',
     'Billing, subsidies and payment records where legally permitted.'),
    ('Messagerie parents-educateurs et resume quotidien.',
     'Parent-educator messaging and daily summaries.'),
    ('Bibliotheque d\'activites et plans hebdomadaires pour les educateurs.',
     'Curriculum library and weekly activity plans for educators.'),
    ('Portail de formation et de certification du personnel.',
     'Training and certification portal for staff.'),
    ('Declaration des incidents, de la maintenance et de la conformite.',
     'Incident, maintenance and compliance reporting.'),
    ('Tableau de bord du reseau : occupation, effectifs, indicateurs qualite '
     'et satisfaction des parents.',
     'Network dashboard covering occupancy, staffing, quality indicators and '
     'parent satisfaction.'),
]
PLATEFORME_NOTE_FR = (
    'Les donnees des enfants doivent etre reduites au minimum, leur acces '
    'controle, leur conservation limitee a ce qui est exige. Protection des '
    'la conception, chiffrement, journaux d\'acces et regles propres a chaque '
    'juridiction doivent etre integres des le depart.')
PLATEFORME_NOTE_EN = (
    'Child data should be minimized, access-controlled and retained only as '
    'required. Privacy-by-design, encryption, audit logs and '
    'jurisdiction-specific data protection requirements should be '
    'incorporated from the beginning.')

# --- 11. Cote parents ------------------------------------------------------
PARENTS = [
    ('Un seul compte KIMO pour tout le reseau.',
     'One KIMO account across the network.'),
    ('Une vue claire du centre, de ses horaires et des programmes '
     'disponibles.',
     'Clear view of center information, operating hours and available '
     'programs.'),
    ('Les memes procedures d\'accueil et de securite partout.',
     'Consistent onboarding and safety procedures.'),
    ('Un echange quotidien, sans surveillance excessive des enfants.',
     'Daily communication without excessive surveillance of children.'),
    ('Des points reguliers sur le developpement avec les educateurs.',
     'Periodic development discussions with educators.'),
    ('Des activites a la maison, facultatives, qui prolongent les themes KIMO '
     'sans creer une pression de devoirs.',
     'Optional home activities that extend KIMO themes without creating '
     'homework pressure.'),
]

# --- 12. Securite et conformite --------------------------------------------
SECURITE_INTRO_FR = (
    'L\'accueil de jeunes enfants est tres encadre, et les exigences varient '
    'fortement d\'un pays, d\'une province ou d\'une commune a l\'autre. KIMO '
    'doit poser un cadre de conformite central tout en exigeant de chaque '
    'unite locale qu\'elle satisfasse la regle locale la plus stricte.')
SECURITE_INTRO_EN = (
    'Childcare is highly regulated and requirements vary significantly by '
    'country, province/state and municipality. KIMO should establish a '
    'central compliance framework while requiring each local unit to satisfy '
    'the stricter applicable local rules.')
SECURITE = [
    ('Verification des antecedents et des references du personnel, dans les '
     'limites de la loi.',
     'Background screening and reference checks for staff as legally '
     'required.'),
    ('Taux d\'encadrement et taille maximale des groupes.',
     'Child-to-educator ratios and group-size limits.'),
    ('Couverture premiers secours et formation aux situations d\'urgence.',
     'First-aid/CPR coverage and emergency-response training.'),
    ('Securite incendie, plans d\'evacuation et exercices.',
     'Fire safety, evacuation plans and drills.'),
    ('Procedures allergies alimentaires et administration de medicaments.',
     'Food allergy and medication procedures.'),
    ('Protocoles de sommeil securise et d\'hygiene la ou ils s\'appliquent.',
     'Safe sleep and hygiene protocols where applicable.'),
    ('Entree controlee et remise de l\'enfant verifiee.',
     'Controlled entry and verified child release.'),
    ('Consignation obligatoire des incidents et remontee hierarchique.',
     'Mandatory incident documentation and escalation.'),
    ('Politique de protection de l\'enfance, canaux de signalement et '
     'tolerance zero en cas de maltraitance ou de negligence.',
     'Safeguarding policy, reporting channels and zero-tolerance procedures '
     'for abuse or neglect.'),
    ('Une assurance adaptee a l\'accueil de jeunes enfants.',
     'Insurance coverage appropriate to childcare operations.'),
]

# --- 13. Qualite -----------------------------------------------------------
QUALITE = [
    ('Certification de chaque unite KIMO avant son ouverture.',
     'Pre-opening certification of every KIMO unit.'),
    ('Controles qualite periodiques, annonces et inopines, la ou le droit le '
     'permet.',
     'Periodic announced and unannounced quality reviews where legally '
     'appropriate.'),
    ('Des listes de controle et des standards de programme communs.',
     'Common operational checklists and curriculum standards.'),
    ('Mesure de la satisfaction des parents.',
     'Parent satisfaction measurement.'),
    ('Suivi de la fidelisation du personnel, des formations suivies et des '
     'incidents.',
     'Staff retention, training completion and incident metrics.'),
    ('Plans de correction pour les centres qui passent sous les standards.',
     'Corrective-action plans for centers falling below standards.'),
    ('La possibilite de suspendre la licence et la marque KIMO quand des '
     'manquements graves ne sont pas corriges.',
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
     'Frais de garde et de scolarite', 'Childcare/tuition fees', False),
    ('franchise', 'Licence ou franchise', 'Licensed / franchise',
     'Un exploitant local qualifie utilise le systeme et la marque KIMO',
     'Qualified local operator uses KIMO system and brand',
     'Droit d\'entree, puis redevance ou frais de service recurrents',
     'Initial fee + recurring royalty/service fee', True),
    ('employeur', 'KIMO employeur', 'Employer KIMO',
     'Un centre reserve en partie ou en totalite aux salaries d\'une '
     'entreprise',
     'Center dedicated partly or fully to an employer\'s workforce',
     'Contrat avec l\'employeur, plus la part des familles',
     'Employer contract + family fees', False),
    ('immobilier', 'Partenariat immobilier', 'Real-estate partnership',
     'Un promoteur integre une KIMO dans un projet residentiel',
     'Developer integrates KIMO into a residential project',
     'Bail ou accord de soutien, plus l\'exploitation',
     'Lease/support agreement + operating revenue', False),
    ('public', 'Partenariat public', 'Public partnership',
     'Des places creees avec des municipalites ou des institutions '
     'publiques',
     'Capacity created with municipalities or public institutions',
     'Contrat ou subvention, plus les tarifs encadres des familles',
     'Contract/subsidy + regulated family fees', False),
]

# --- 15. La structure de couts ---------------------------------------------
COUTS = [
    ('Achat ou location du local, et travaux d\'amenagement.',
     'Premises acquisition or lease and fit-out.'),
    ('Agrement, honoraires et visites de controle.',
     'Licensing, professional services and inspections.'),
    ('Salaires des educateurs et de l\'encadrement.',
     'Educator and management payroll.'),
    ('Assurance et conformite.', 'Insurance and compliance.'),
    ('Mobilier, materiel pedagogique et equipement exterieur.',
     'Furniture, educational materials and outdoor equipment.'),
    ('Repas et consommables.', 'Meals and consumables.'),
    ('Plateforme technique et securite informatique.',
     'Technology platform and cybersecurity.'),
    ('Formation, recrutement et controle qualite.',
     'Training, recruitment and quality assurance.'),
    ('Programme central, marketing et administration.',
     'Central curriculum, marketing and administrative functions.'),
]
COUTS_NOTE_FR = (
    'Un modele financier doit etre etabli separement pour chaque juridiction '
    'visee, parce que les taux d\'encadrement, les salaires, les aides, les '
    'loyers et les regles d\'agrement peuvent changer profondement '
    'l\'economie d\'un centre.')
COUTS_NOTE_EN = (
    'A financial model should be produced separately for each target '
    'jurisdiction because staff ratios, wages, subsidies, rent and licensing '
    'rules can materially change center economics.')

# --- 16. Les indicateurs du reseau -----------------------------------------
KPI = [
    ('Places agreees et taux d\'occupation.',
     'Licensed capacity and occupancy rate.'),
    ('Recette par place disponible.',
     'Revenue per available childcare place.'),
    ('Cout du personnel en pourcentage du chiffre d\'affaires.',
     'Staff cost as a percentage of revenue.'),
    ('Respect du taux d\'encadrement.', 'Educator-to-child ratio compliance.'),
    ('Fidelite des parents et taux de recommandation.',
     'Parent retention and referral rate.'),
    ('Rotation du personnel et formations achevees.',
     'Staff turnover and training completion.'),
    ('Frequence des incidents et delai de cloture des actions correctives.',
     'Incident frequency and corrective-action closure time.'),
    ('Distance ou temps moyen entre les familles et leur centre.',
     'Average distance/time between families and their assigned center.'),
    ('Marge de contribution par centre et frais de structure par unite.',
     'Center-level contribution margin and central overhead per unit.'),
]

# --- 17. Les cinq phases de deploiement ------------------------------------
PHASES = [
    ('1', 'Conception', 'Design',
     'Arreter la pedagogie, la marque, le cadre reglementaire, le prototype '
     'de centre, les besoins techniques et les hypotheses financieres.',
     'Finalize pedagogy, brand, regulatory framework, center prototype, '
     'technology requirements and financial assumptions.'),
    ('2', 'Pilote', 'Pilot',
     'Ouvrir environ 3 a 5 centres dans une meme agglomeration, sur des '
     'quartiers de profils differents. Mesurer la demande, les effectifs, '
     'l\'experience des parents et la qualite pedagogique.',
     'Open approximately 3-5 centers in one metropolitan area with different '
     'neighborhood profiles. Measure demand, staffing, parent experience and '
     'educational delivery.'),
    ('3', 'Reseau local', 'Local Network',
     'Densifier jusqu\'a former une grappe de centres, pour que les familles '
     'beneficient d\'une vraie proximite et des services mutualises.',
     'Expand to a dense cluster of centers so that families can benefit from '
     'genuine proximity and shared network services.'),
    ('4', 'Plusieurs villes', 'Multi-city Expansion',
     'Repliquer le systeme d\'exploitation valide, en propre et avec des '
     'partenaires choisis avec soin.',
     'Replicate the validated operating system through company-owned centers '
     'and carefully selected partners.'),
    ('5', 'National, puis international', 'National / International Platform',
     'Adapter le cadre KIMO a de nouvelles juridictions, en gardant une '
     'identite educative commune et une conformite locale.',
     'Adapt the KIMO framework to additional jurisdictions while maintaining '
     'a global educational identity and local regulatory compliance.'),
]

# --- 18. La validation du pilote -------------------------------------------
PILOTE = [
    ('Interroger parents et employeurs avant de choisir les quartiers du '
     'pilote.',
     'Interview parents and employers before selecting pilot neighborhoods.'),
    ('Verifier que le format micro-centre est agreable dans la juridiction '
     'visee.',
     'Validate local licensing feasibility for the micro-center format.'),
    ('Prototyper le programme avec des professionnels qualifies de la petite '
     'enfance.',
     'Prototype the curriculum with qualified early-childhood '
     'professionals.'),
    ('Tester les parcours d\'inscription et de communication aux parents.',
     'Test enrollment and parent communication workflows.'),
    ('Mesurer la charge des educateurs et le temps de preparation des '
     'activites.',
     'Measure educator workload and activity preparation time.'),
    ('Suivre occupation, liste d\'attente, presences, satisfaction et '
     'fidelite.',
     'Track occupancy, waitlist, attendance, satisfaction and retention.'),
    ('Mener des revues formelles de securite et de protection de l\'enfance '
     'avant de passer a l\'echelle.',
     'Conduct formal safety and safeguarding reviews before scaling.'),
    ('Se servir des resultats du pilote pour decider quel format de centre et '
     'quel modele de partenariat standardiser.',
     'Use pilot evidence to decide which center format and partnership model '
     'should be standardized.'),
]

# --- 19. Les risques et ce qu'on y oppose ----------------------------------
RISQUES = [
    ('Une qualite inegale d\'un centre a l\'autre',
     'Inconsistent quality across decentralized centers',
     'Certification exigeante, formation, audits et standards de marque '
     'opposables.',
     'Strong certification, training, audits and enforceable brand '
     'standards.'),
    ('La penurie d\'educateurs', 'Educator shortages',
     'Filiere de recrutement, conditions competitives, partenariats de '
     'formation et planification des effectifs.',
     'Recruitment pipeline, competitive conditions, training partnerships and '
     'workforce planning.'),
    ('Un programme trop scolaire pour la petite enfance',
     'Over-academic early childhood program',
     'Le jeu d\'abord, une revue par des specialistes du developpement, et la '
     'liberte d\'appreciation de l\'educateur.',
     'Play-first curriculum, developmental review and educator discretion.'),
    ('Les differences de reglementation', 'Regulatory differences',
     'Un manuel d\'exploitation par juridiction et une revue juridique '
     'locale.',
     'Jurisdiction-specific operating manuals and local legal/licensing '
     'review.'),
    ('Le risque sur les donnees des enfants', 'Child-data privacy risk',
     'Minimisation des donnees, acces strictement controles, chiffrement et '
     'regles de conservation ecrites.',
     'Data minimization, strict access controls, encryption and documented '
     'retention rules.'),
    ('Une croissance trop rapide qui abime la culture',
     'Rapid expansion weakens culture',
     'Une croissance par grappes et une accreditation des partenaires par '
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
    ('Marque mere : KIMO.', 'Master brand: KIMO.'),
    ('Signature : KIMO — Apprendre a penser.',
     'Core signature: KIMO — Learn to Think.'),
    ('Nommage possible des centres : KIMO [Quartier] ou KIMO [Partenaire].',
     'Possible center naming: KIMO [Neighborhood] or KIMO [Partner].'),
    ('Familles de programmes possibles : KIMO Logic, KIMO Chess, KIMO '
     'Science, KIMO Move, KIMO Stories.',
     'Possible program families: KIMO Logic, KIMO Chess, KIMO Science, KIMO '
     'Move, KIMO Stories.'),
    ('Une identite visuelle intelligente et moderne, sans etre scolaire ni '
     'institutionnelle.',
     'Visual identity should feel intelligent and modern without appearing '
     'overly academic or institutional.'),
]

# --- 21. Ce qui vient apres -----------------------------------------------
HORIZON_FR = (
    'Une fois le reseau d\'accueil eprouve, KIMO peut aller au-dela des '
    'centres : formation d\'educateurs, licence de programme, kits '
    'd\'apprentissage pour les parents, clubs de logique apres l\'ecole, '
    'partenariats avec des ecoles. Ces prolongements doivent SUIVRE la '
    'validation du modele d\'accueil, pas la preceder.')
HORIZON_EN = (
    'Once the childcare network is proven, KIMO could extend beyond physical '
    'centers through educator training, curriculum licensing, parent learning '
    'kits, after-school logic clubs and partnerships with schools. These '
    'extensions should follow' + u'\u2014' + 'not precede' + u'\u2014' + 'the validation of the core '
    'childcare model.')
