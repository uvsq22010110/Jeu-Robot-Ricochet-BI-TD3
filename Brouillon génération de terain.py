import tkinter as tk
import random as rd

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


def creer_carrer():
    "dessine carrer"
    i = 16 // 2
    j = 16 // 2 + 1
    carrer = canvas.create_rectangle((40*(i - 1), 40*(i - 1)), (40*j, 40*j), fill = "black")





# programme principal
racine = tk.Tk()
racine.title("Jeu des robots")


# création des widgets
canvas = tk.Canvas(racine, width= LARGEUR, height= HAUTEUR, bg= "navajo white")

canvas.grid()

creer_robot(COULEUR_ROBOT1)
creer_robot(COULEUR_ROBOT2)
creer_robot(COULEUR_ROBOT3)
creer_robot(COULEUR_ROBOT4)

creer_carrer()
quadrillage()
racine.mainloop()
