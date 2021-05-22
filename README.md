Le but du jeu est de faire rentrer le robot de bonne couleur dans sa cible associée, par exemple le robot jaune doit aller dans la cible jaune.
Pour jouer au jeu du "Robot-Ricochet", cliquer sur un robot et faites le se déplacer grâce aux flèches situées sur votre clavier.
Ensuite faites aller votre robot dans la cible qui lui est associée. Vous pouvez vous aider des autres robot pour y parvenir.

Grâce à la fonction "est_dans_le_robot", le progamme sait sur quel robot on a cliqué. Il pourra donc par la suite, déplacer uniquement ce robot-ci.
La fonction "clavier" ,elle, nous permet d'utiliser les flèches du clavier et possèdent des fonctions qui lui sont associées, comme par exemple si l'on appuit sur la flèche du haut, le robot va monter jusqu'à ce qu'il rencontre un mur/obstacle sur son chemin.

Pour que le robot puisse détecter les cases, savoir si elles sont vides ou pleines, nous avons rentrer les valeurs dans un tableau:
# pour les robots
- robot jaune = 10
- robot vert = 20
- robot rouge = 30
- robot bleu = 40

# pour les murs
- bordure de gauche = 1
- bordure de droite = 2
- bordure du bas = 3
- bordure du haut = 4

# pour les angles
- bordure de gauche + bordure du bas = 5
- bordure de droite + bordure du bas = 6
- bordure de gauche + bordure du haut = 7
- bordure de droite + bordure du haut = 8

Si vous devez quitter la partie mais que vous voulez sauvegarder, appuyer sur le bouton "sauvegarder". Le bouton "sauvegarder" va garder en mémoire dans un fichier texte l'emplacement des robots, des murs, le nombre de déplacement etc, là où vous l'avez laisser. Ensuite en rouvrant le jeu, appuyer cette fois-ci sur le bouton "charger" qui va permettre de ré-initialiser la partie là où on l'a sauvegardé pour la dernière fois.

Le bouton "retour_en_arrière", permet de revenir en arrière si on le souhaite. Si vous cliquez une fois dessus, le plateau de jeu se ré-initialise d'une case en arrière.