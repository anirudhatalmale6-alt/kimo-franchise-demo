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
# LA METHODE. TEXTE DE TRAVAIL — c'est une proposition, pas une doctrine.
# La page l'affiche avec une pastille « a valider ». La pedagogie est une
# decision du fondateur, pas de son developpeur.
# ---------------------------------------------------------------------------
METHODE_A_VALIDER = True
METHODE = [
    ('observer', 'Observer avant de proposer', 'Observe before proposing',
     'Chaque enfant a un cahier d\'observation tenu par l\'adulte qui '
     's\'occupe de lui. On y note ce qu\'il fait seul, ce qu\'il fait avec '
     'aide, ce qu\'il evite. C\'est ce cahier qui decide de la suite, pas le '
     'calendrier.',
     'Every child has an observation record kept by the adult who looks after '
     'them: what they do alone, what they do with help, what they avoid. That '
     'record decides what comes next, not the calendar.'),
    ('etapes', 'Une progression en petites etapes',
     'A progression in small steps',
     'Les activites sont classees par etapes courtes et ordonnees. Un enfant '
     'avance a son rythme dans une suite connue, au lieu de suivre le groupe '
     'ou de l\'attendre.',
     'Activities are ordered in short, sequenced steps. A child moves at '
     'their own pace through a known sequence, instead of following the group '
     'or waiting for it.'),
    ('autonomie', 'Faire seul, des que c\'est possible',
     'Doing it alone, as soon as possible',
     'Le materiel est a hauteur d\'enfant et range toujours au meme endroit. '
     'L\'adulte montre une fois, puis se retire. Ce qu\'un enfant peut faire '
     'seul, on ne le fait pas a sa place.',
     'Material is at child height and always stored in the same place. The '
     'adult demonstrates once, then steps back. Whatever a child can do '
     'alone is not done for them.'),
    ('parents', 'Les parents recoivent la meme trace',
     'Parents get the same record',
     'Ce qui est note dans le cahier est ce qui est envoye a la famille le '
     'soir. Pas un resume different, pas un compte rendu ecrit pour '
     'rassurer.',
     'What goes into the record is what is sent to the family in the '
     'evening. Not a different summary, not a report written to reassure.'),
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
