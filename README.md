# Projet_Incendie
Projet python de simulation d'incendie du groupe 1 de BI TD3

Le projet a pour objet la simulation de la propagation d’un incendie. Il comporte une partie graphique qui permettra de visualiser ce que l’on cherche à simuler, ainsi qu’un ensemble de fonctionnalités qui enrichiront le programme.

Contraintes de programmation :

Bien que ce ne soit pas la meilleure façon de programmer et même si vous savez faire autrement, vous respecterez les contraintes suivantes liées aux prérequis attendus pour faire le projet:

-le programme doit être écrit dans un unique fichier qui s’appelle incendie.py;

-le programme ne doit pas définir de classes d’objets;

-vous devez utiliser la librairie graphique tkinter;

-quand ce n’est pas possible de faire autrement (notamment pour les widgets graphiques mais pas uniquement), vous pouvez utiliser des variables globales;

le programme sera découpé de la manière suivante (chaque partie devant apparaître bien distinctement en utilisant des commentaires):
-informations liées au groupe
-import des librairies
-définition des constantes (écrites en majuscule)
-définition des variables globales
-définition des fonctions (chaque fonction devra contenir une docstring)
-programme principal contenant la définition des widgets et des événements qui leur sont liés et l’appel à la boule de gestion des événements

Sujet:

On considère un terrain rectangulaire constitué de LARGEUR x HAUTEUR parcelles, où LARGEUR et HAUTEUR sont des constantes définies au début du programme et laissées à votre appréciation. Chaque parcelle est représentée par un carré dont la couleur est donnée par le type du terrain, couleurs données par le tableau suivant:

-Type	Couleur	Durée de l’état
-Eau	Bleu	 + ∞
-Forêt	Vert	Dépend des voisins
-Feu	Rouge	Constante DUREE_FEU
-Prairie	Jaune	Dépend des voisins
-Cendres tièdes	Gris	Constante DUREE_CENDRE
-Cendres éteintes	Noir	 + ∞

Les règles d’évolution sont les suivantes:

-une parcelle d’eau reste une parcelle d’eau durant toute la simulation;
-une parcelle qui devient en feu reste en feu durant la durée DUREE_FEU avant de devenir des cendres tièdes pendant la durée DUREE_CENDRE et enfin devenir des cendres éteintes durant le reste de la simulation; les valeurs de ces deux constantes sont à définir et laissées à votre appréciation;
-une parcelle de prairie prend feu dès qu’une des 4 cases voisines (gauche, droite, haut, bas) est en feu;
-une parcelle de forêt prend feu avec la probabilité 0.1 × nf où nf est le nombre de ses voisins en feu;
On considère que les bords du terrain ne peuvent pas brûler et qu’ils n’interviennent pas dans la propagation du feu. Le programme doit malgré tout être adapté pour les parcelles du bord.

Votre programme devra contenir les fonctionnalités suivantes:

-fonctionnalités liées au choix du terrain:
-un bouton qui génère un terrain au hasard avec des parcelles d’eau, de forêt et de prairie;
-un clic sur une parcelle de forêt ou de prairie la transforme en parcelle en feu;
-un bouton pour sauvegarder l’état du terrain dans un fichier;
-un bouton pour charger un terrain depuis un fichier;

fonctionnalités liées à la simulation:
-un bouton permet d’effectuer une étape de simulation; cela doit aussi être possible en appuyant sur une touche du clavier (à définir);
-un bouton qui permet de démarrer une simulation; le nombre d’étapes doit alors s’afficher, ainsi que le nombre de parcelles en feu, et la simulation s’arrête quand il n’y a plus de parcelle en feu;
-un bouton pour arrêter la simulation;
-une touche (à définir) pour accélérer la vitesse de la simulation et une touche (à définir) pour la réduire; la vitesse de simulation doit être affichée en nombre d’étapes par secondes;
