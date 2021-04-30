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


def bordure():
    """creation bordures"""
    mur1 = canvas.create_line(0,0,0,HAUTEUR, fill="black", width = '8')
    mur2 = canvas.create_line(0,0,LARGEUR,0, fill="black", width = '8') 
    mur3 = canvas.create_line(LARGEUR,0,LARGEUR,HAUTEUR, fill="black", width = '8')
    mur4 = canvas.create_line(0,0,0,HAUTEUR, fill="black", width = '8' )

def obstacle_mur():
    """à modifier afin qu'il est seuleument deux petit murs par côté"""
    for i in range(2,4):
        n = [80,160,240,320,400,480,560]
        """obstacles collés aux murs  du plateau de jeu"""
        petit_mur = rd.choice(n)#mur de gauche
        canvas.create_line(0,petit_mur,40,petit_mur, fill='black', width = '4')
        canvas.create_line(640,petit_mur,600,petit_mur, fill = 'black',width = '4')
        canvas.create_line(petit_mur,0,petit_mur,40,fill='black', width ='4')
        canvas.create_line(petit_mur,640,petit_mur,600, fill = 'black', width='4')


def creer_tableau():
    global tableau
    n = LARGEUR // COTE
    tableau = [[0] * n for i in range(n)]
        
def creer_robot(couleur_robot):
    "dessine robot"
    i = rd.randint(0,14)
    j = rd.randint(0,14)
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



#####################################################Programme Principale##########################################################################
racine = tk.Tk()
racine.title("Jeu des robots")


canvas = tk.Canvas(racine, width=640, height=640, borderwidth=0, highlightthickness=0, bg = COULEUR_FOND)
canvas.grid(column = 1, row = 0)
canvas.pack()


creer_robot(COULEUR_ROBOT1)
creer_robot(COULEUR_ROBOT2)
creer_robot(COULEUR_ROBOT3)
creer_robot(COULEUR_ROBOT4)


obstacle_mur()
creer_carrer()
quadrillage()
bordure()    
racine.mainloop()
