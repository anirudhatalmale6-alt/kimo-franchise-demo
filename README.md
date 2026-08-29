# KIMO — reseau decentralise d'eveil et d'apprentissage

Site de marque, page concept, page franchise. Demonstration, non indexee.

- `index.html` — le reseau : pourquoi decentralise, la methode, les sept
  piliers en resume, le cadre reglementaire.
- `concept.html` — **le concept, tel que le fondateur l'a ecrit** : qui fait
  quoi, le format d'une unite, la philosophie pedagogique, les sept piliers
  d'apprentissage, la progression par age, la journee type, les educateurs et
  les parents, la plateforme, la securite et la qualite, les cinq modeles
  d'exploitation, les couts et les indicateurs, les cinq phases de
  deploiement, les risques, l'architecture de marque.
- `franchise.html` — devenir franchise : le parcours en six etapes, qui
  apporte quoi, le modele economique, le simulateur de compte d'exploitation,
  le profil recherche, le formulaire de candidature, la FAQ.
- `src/` — les sources. `python3 page_kimo.py` reconstruit les trois pages.
- `apercus/` — captures d'ecran.

## D'ou vient le texte

Le contenu de `concept.html` vient de la note **KIMO — Decentralized Early
Learning Network** ecrite par le fondateur. Cote **anglais**, c'est son texte
mot pour mot ; cote **francais**, c'est une traduction, et la page l'annonce
en haut.

Ce n'est pas une intention, c'est un controle : la suite ouvre le `.docx`
d'origine et verifie que **chacun des 181 passages anglais du site figure
mot pour mot dans la note**. Le controle est essaye sur une phrase fabriquee
pour verifier qu'il sait echouer. Il a d'ailleurs servi des sa premiere
execution : sept passages avaient ete retouches — cinq points finaux ajoutes
dans des cellules de tableau, deux cadratins entoures d'espaces. Rien de
grave a l'oeil, et c'est exactement pour cela que « mot pour mot » se
verifie au lieu de s'affirmer.

La signature **KIMO — Learn to Think.** est la sienne. Sa traduction
francaise est la mienne, et elle porte une mention visible tant qu'il ne l'a
pas confirmee : une signature de marque ne se traduit pas a la place de son
fondateur.

## Les deux regles qui expliquent tous les « a definir »

**1. Aucun chiffre reglementaire n'est ecrit tant qu'il n'est pas verifie
dans le pays retenu.** Une micro-creche est un etablissement autorise : le
nombre de places, le taux d'encadrement, la qualification du responsable et
la surface par enfant sont fixes par le droit du pays, parfois de la region.
Un candidat batit son local et son financement sur ces lignes. Elles sont
donc affichees « a definir », pas comblees par un ordre de grandeur.

**2. Aucun montant commercial n'est invente.** Droit d'entree, redevance,
apport demande : ce sont des decisions du groupe. Meme traitement.

Ces deux regles ne sont pas une prudence de developpeur : elles appliquent ce
que la note dit elle-meme, deux fois. « Final capacity, staff ratios, room
dimensions, sleep arrangements, food preparation and outdoor-space
requirements must be adapted to the jurisdiction in which each unit
operates » (section 4), et « a financial model should be produced separately
for each target jurisdiction » (section 15). Les deux phrases sont reprises
et encadrees sur le site, a l'endroit ou elles expliquent un blanc.

La seule fourchette de capacite ecrite sur le site est la sienne — environ
8 a 20 enfants — et un controle verifie qu'elle **n'apparait jamais sans la
reserve qui l'accompagne** : un chiffre de capacite lu sans sa reserve est lu
comme un plafond legal, et il ne l'est pas. La ligne « capacite » du tableau
reglementaire, elle, reste vide.

Ce qui manque est liste en haut de `franchise.html`, en clair, pour le
visiteur — sept points, dans `contenu.py`, table `A_DEFINIR`.

## Le simulateur

Le candidat saisit ses propres hypotheses (places, occupation, recette par
place, loyer, encadrants, salaires, autres charges, redevance, monnaie) et la
page calcule produits, charges, resultat mensuel et annuel, et le taux
d'occupation au point mort. **Aucune valeur de depart n'est un chiffre
KIMO** : elles sont rondes, arbitraires, et la page le dit.

La formule est ecrite deux fois — en Python pour le rendu a la construction,
en JavaScript pour le recalcul sans rechargement. C'est inevitable ; ce qui
ne l'est pas, c'est de ne pas s'apercevoir qu'elles ont diverge. La suite de
controles ouvre la page dans un vrai navigateur et compare les deux.

## Controles

    cd src && python3 page_kimo.py && python3 tests-kimo.py

134 controles. Les decisifs :

- chaque passage anglais du site figure mot pour mot dans la note du
  fondateur (le `.docx` doit etre a cote du dossier ; sinon le controle
  compte comme un **echec**, pas comme un succes) ;
- le nom du reseau d'apprentissage qui a inspire le modele n'apparait dans
  aucun fichier du dossier — pages, code, commentaires, noms de fichiers ;
  et le controle sait echouer (il est essaye sur un texte fautif) ;
- aucun chiffre dans la colonne des valeurs reglementaires, ni dans celle du
  modele economique ; la fourchette de capacite n'apparait jamais sans sa
  reserve ;
- toute balise porte ses deux langues ou aucune, et le texte servi dit la
  meme chose que son `data-fr` ;
- les ancres d'une page vers une autre pointent sur un element qui existe —
  un `concept.html#p-echecs` casse au clic, pas a la construction ;
- aucune regle de style ne masque du contenu : les trois pages sont lues
  **avec JavaScript desactive**, titres, tableaux, journee type et chiffres
  du simulateur compris ;
- le navigateur est interroge sur ce qu'il a **applique**, pas la feuille sur
  ce qu'elle demande : c'est ce controle-la qui a montre que les longues
  listes annoncees sur deux colonnes n'en avaient qu'une, une regle plus
  generale ayant gagne ;
- le script retrouve les chiffres calcules a la construction, avant et apres
  modification d'une entree ;
- le formulaire refuse un envoi incomplet, dit ce qui manque, et annonce
  qu'il n'envoie rien tant que sa destination n'est pas fixee ;
- en 390 px, aucune des trois pages ne deborde en largeur.

## Marque du groupe

Le diamant et la devise sont repris **mot pour mot** de `maisons-de-prestige`
(un controle compare les deux fichiers). Les liens vers les autres sites du
groupe sont absolus et regroupes en tete de `contenu.py` : ce sont les seules
lignes a changer le jour des noms de domaine.
