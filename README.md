# KIMO — reseau de micro-creches decentralisees

Site de marque + page franchise. Demonstration, non indexee.

- `index.html` — le reseau : le modele decentralise, la methode, le cadre
  reglementaire.
- `franchise.html` — devenir franchise : le parcours en six etapes, qui
  apporte quoi, le modele economique, le simulateur de compte d'exploitation,
  le profil recherche, le formulaire de candidature, la FAQ.
- `src/` — les sources. `python3 page_kimo.py` reconstruit les deux pages.
- `apercus/` — captures d'ecran.

## Les deux regles qui expliquent tous les « a definir »

**1. Aucun chiffre reglementaire n'est ecrit tant qu'il n'est pas verifie
dans le pays retenu.** Une micro-creche est un etablissement autorise : le
nombre de places, le taux d'encadrement, la qualification du responsable et
la surface par enfant sont fixes par le droit du pays, parfois de la region.
Un candidat batit son local et son financement sur ces lignes. Elles sont
donc affichees « a definir », pas comblees par un ordre de grandeur.

**2. Aucun montant commercial n'est invente.** Droit d'entree, redevance,
apport demande : ce sont des decisions du groupe. Meme traitement.

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

91 controles. Les decisifs :

- le nom du reseau d'apprentissage qui a inspire le modele n'apparait dans
  aucun fichier du dossier — pages, code, commentaires, noms de fichiers ;
  et le controle sait echouer (il est essaye sur un texte fautif) ;
- aucun chiffre dans la colonne des valeurs reglementaires, ni dans celle du
  modele economique ;
- toute balise porte ses deux langues ou aucune, et le texte servi dit la
  meme chose que son `data-fr` ;
- aucune regle de style ne masque du contenu : les deux pages sont lues
  **avec JavaScript desactive**, titres, tableaux et chiffres du simulateur
  compris ;
- le script retrouve les chiffres calcules a la construction, avant et apres
  modification d'une entree ;
- le formulaire refuse un envoi incomplet, dit ce qui manque, et annonce
  qu'il n'envoie rien tant que sa destination n'est pas fixee ;
- en 390 px, aucune des deux pages ne deborde en largeur.

## Marque du groupe

Le diamant et la devise sont repris **mot pour mot** de `maisons-de-prestige`
(un controle compare les deux fichiers). Les liens vers les autres sites du
groupe sont absolus et regroupes en tete de `contenu.py` : ce sont les seules
lignes a changer le jour des noms de domaine.
