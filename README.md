# But du jeu
Le but du jeu est de faire rentrer le robot de bonne couleur dans sa cible associée en un minimun de déplacements, par exemple le robot jaune doit aller dans la cible jaune. Une fois rentré dans la cible, une nouvelle cible apparait dans un autre angle. Pour finir la partie vous devez faire rentrer 5 robots dans les cibles. Si vous faites parti du podium, un encadré s'affiche en bas de l'écran vous demandant votre prénom.
Pour jouer au jeu du "Robot-Ricochet", rien de plus simple, cliquez sur un robot et faites-le se déplacer grâce aux flèches situées sur votre clavier. Ensuite, faites aller votre robot dans la cible qui lui est associée. Vous pouvez vous aider des autres robots pour y parvenir.

* Une fois la partie terminée, une nouvelle partie se relance toute seule.

# Explications du programme
Grâce à la fonction "est_dans_le_robot", le progamme sait sur quel robot on a cliqué. Il pourra donc par la suite, déplacer uniquement ce robot-ci. Si vous voulez déplacer un autre robot, il vous suffit de cliquer dessus.
Quant'à la fonction "clavier", elle nous permet d'utiliser les flèches du clavier et possède des fonctions qui lui sont associées, comme par exemple, si l'on appuit sur la flèche du haut, le robot va monter vers le haut jusqu'à ce qu'il rencontre un mur/obstacle sur son chemin.

Pour que le robot puisse détecter les cases, savoir si elles sont vides ou occupées, nous avons rentré les valeurs dans un tableau:

**pour les robots**
- robot jaune = 10
- robot vert = 20
- robot rouge = 30
- robot bleu = 40

**pour les murs**
- bordure de gauche = 1
- bordure de droite = 2
- bordure du bas = 3
- bordure du haut = 4

**pour les angles**
- bordure de gauche + bordure du bas = 5
- bordure de droite + bordure du bas = 6
- bordure de gauche + bordure du haut = 7
- bordure de droite + bordure du haut = 8

**pour les cibles**
- cible jaune = 100
- cible verte = 200
- cible rouge = 300
- cible bleue = 400

**pour le carré central**
- pour les 4 cases = 500

Les cases sont déterminées par les coordonnées i et j. Leurs valeurs vont de 0 à 15.

La fonction "placer_cible" permet de placer la cible dans un angle créé par les murs. Pour chaque partie elle peut prendre une des 4 couleurs associée au robot de façon aléatoire.

Si vous devez quitter la partie mais que vous voulez sauvegarder, appuyer sur le bouton "Sauvegarde". Le bouton "Sauvegarde" va garder en mémoire dans un fichier texte l'emplacement des robots, des murs, le nombre de déplacements etc, là où vous l'avez laissé. Ensuite en rouvrant le jeu, appuyer cette fois-ci sur le bouton "Reprendre la partie sauvegardée" qui va permettre de ré-initialiser la partie là où on l'a sauvegardé pour la dernière fois.

Le bouton "Retour en arrière", permet de revenir en arrière si on le souhaite. Il faut cliquer une seule fois sur le bouton pour que le plateau de jeu se ré-initialise d'une case en arrière, par exemple si vous venez de faire avancer votre robot sur la gauche, il va revenir à sa place sur la droite.

Le bouton "Recommencer", permet de recommencer la partie du début et replace donc les robots à leur position initiale, sans toucher à la position de la cible et des murs.