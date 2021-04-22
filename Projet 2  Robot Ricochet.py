##################################
# Groupe 1  de BI TD3

# Auteurs: 
# Coraline PELON
# Jacques-Henri LARTIGUE
# Nojimba AHAMADA
# Alice DUMONTROTY
# Mathieu CHEKROUN
# Desira Junior EBELEBE

# lien du github:https://github.com/uvsq22010110/Projet-2-Robot-Ricochet.git


###################################
# Comment le programme fonctionne :

# import des modules
import tkinter as tk
import random as rd

# constantes
HAUTEUR = 640
LARGEUR = 640
COULEUR_FOND = "navajo white"
COTE = 40
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

COULEUR_QUADRILLAGE = "black"
COULEUR_ROBOT1 = "red"
COULEUR_ROBOT2 = "green"
COULEUR_ROBOT3 = "blue"
COULEUR_ROBOT4 = "yellow"
COULEUR_CIBLE = "aleatoire"

# fonctions
def quadrillage():
    global COULEUR_QUADRILLAGE
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADRILLAGE)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADRILLAGE)
        x += COTE

def coord_to_lg(x, y):
    
    return x // COTE, y // COTE        


def creer_tableau():
    
    global tableau
    tableau = []
    for i in range(NB_COL):
        tableau.append([-1] * NB_LINE)
        
def creer_robot(couleur_robot):
    "dessine robot"
    i = rd.randint(0,15)
    j = rd.randint(0,15)
    #attention pas sous le carré noir
    x,y = i*COTE, j*COTE
    dx,dy = 10, 10
    rayon = COTE
    cercle = canvas.create_oval((x, y), (x+rayon, y+rayon), fill = couleur_robot)
    return [cercle, dx, dy]


def creer_caree():
    "dessine caree"
    i = 16 // 2
    j = 16 // 2 + 1
    caree = canvas.create_rectangle((40*(i - 1), 40*(i - 1)), (40*j, 40*j), fill = "black")


def est_dans_le_robot(event):
    """Retourne True si on a cliqué sur un robot sinon False"""
    print("Tu as cliqué sur un robot")


def deplacement_gauche(event):
    """Déplace notre robot vers la gauche lorsque l'on appui sur la touche "flèche gauche" """
    print("Tu as appuyé sur la flèche gauche")


def deplacement_droite(event):
    """Déplace notre robot vers la droite lorsque l'on appui sur la touche "flèche droite" """
    print("Tu as appuyé sur la flèche droite")


def deplacement_haut(event):
    """Déplace notre robot vers le haut lorsque l'on appui sur la touche "flèche du haut" """
    print("Tu as appuyé sur la flèche du haut")


def deplacement_bas(event):
    """Déplace notre robot vers le bas lorsque l'on appui sur la touche "flèche du bas" """
    print("Tu as appuyé sur la flèche du bas")


# programme principal
racine = tk.Tk()
racine.title("Jeu des robots")

# création des widgets
canvas = tk.Canvas(racine, width= LARGEUR, height= HAUTEUR, bg= "navajo white")

# liaison des événements
canvas.bind("<Button-1>", est_dans_le_robot)
racine.bind("<KeyPress-Left>", deplacement_gauche)
racine.bind("<KeyPress-Right>", deplacement_droite)
racine.bind("<KeyPress-Down>", deplacement_bas)
racine.bind("<KeyPress-Up>", deplacement_haut)

# placement des widgets
canvas.grid()

# programme principal
creer_robot(COULEUR_ROBOT1)
creer_robot(COULEUR_ROBOT2)
creer_robot(COULEUR_ROBOT3)
creer_robot(COULEUR_ROBOT4)

creer_caree()
quadrillage()

racine.mainloop()