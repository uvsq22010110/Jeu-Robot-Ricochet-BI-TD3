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
COULEUR_ROBOT1 = "yellow"
COULEUR_ROBOT2 = "green"
COULEUR_ROBOT3 = "red"
COULEUR_ROBOT4 = "blue"
COULEUR_CIBLE = "aleatoire"

# variables
tableau = []


###################################
# fonctions

def creer_mur1():
    x0 = 80
    y0 = 80
    x1 = x0 + 40
    y1 = y0
    canvas.create_line(x0,y0,x1,y1, width = 5 , fill = "black")

def creer_mur2():
    x0 = 160
    y0 = 160
    x1 = x0
    y1 = y0 + 40
    canvas.create_line(x0,y0,x1,y1, width = 5 , fill = "black")

def creer_mur3():
    x0 = 240
    y0 = 160
    x1 = x0
    y1 = y0 + 40
    x2 = x0 
    y2 = y0
    x3 = x0 + 40
    y3 = y0 
    canvas.create_line(x0,y0,x1,y1, width = 5 , fill = "black")
    canvas.create_line(x2,y2,x3,y3, width = 5 , fill = "black")

def creer_mur4():
    x0 = 560
    y0 = 160
    x1 = x0
    y1 = y0 + 40
    x2 = x0 
    y2 = y0
    x3 = x0 - 40
    y3 = y0 
    canvas.create_line(x0,y0,x1,y1, width = 5 , fill = "black")
    canvas.create_line(x2,y2,x3,y3, width = 5 , fill = "black")

def creer_mur5():
    x0 = 160
    y0 = 560
    x1 = x0
    y1 = y0 - 40
    x2 = x0 
    y2 = y0 
    x3 = x0 - 40
    y3 = y0 
    canvas.create_line(x0,y0,x1,y1, width = 5 , fill = "black")
    canvas.create_line(x2,y2,x3,y3, width = 5 , fill = "black")

def creer_mur6():
    x0 = 560
    y0 = 560
    x1 = x0
    y1 = y0 - 40
    x2 = x0 
    y2 = y0 
    x3 = x0 + 40
    y3 = y0 
    canvas.create_line(x0,y0,x1,y1, width = 5 , fill = "black")
    canvas.create_line(x2,y2,x3,y3, width = 5 , fill = "black")


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
    for i in range(n):
        tableau = [[0] * n]


def creer_carre():
    "dessine caree"
    i = 16 // 2
    j = 16 // 2 + 1
    carre = canvas.create_rectangle((COTE*(i - 1), COTE*(i - 1)), (COTE*j, COTE*j), fill = "black")


def creer_robot(couleur_robot):
    "dessine robot"
    i = rd.randint(0,15)
    j = rd.randint(0,15)
    x,y = i*COTE, j*COTE
    dx, dy = 10, 10
    rayon = COTE
    cercle = canvas.create_oval((x, y), (x+rayon, y+rayon), fill = couleur_robot)
    return [cercle, dx, dy]
    

def est_dans_le_robot(event):
    global robot, selection
    """Retourne True si on a cliqué sur un robot sinon False"""
    x0, y0, x1, y1 = canvas.coords(robot1[0])
    x2, y2, x3, y3 = canvas.coords(robot2[0])
    x4, y4, x5, y5 = canvas.coords(robot3[0])
    x6, y6, x7, y7 = canvas.coords(robot4[0])
    clic_x = event.x
    clic_y = event.y
    # est dans le robot jaune
    if x0 <= clic_x <= x1 and y0 <= clic_y <= y1:
        print("Tu as cliqué sur le robot jaune")
        robot = robot1
        selection = True 
    # est dans le robot vert
    elif x2 <= clic_x <= x3 and y2 <= clic_y <= y3:
            print("Tu as cliqué sur le robot vert")
            robot = robot2
            selection = True
    # est dans le robot rouge
    elif x4 <= clic_x <= x5 and y4 <= clic_y <= y5:
            print("Tu as cliqué sur le robot rouge")
            robot = robot3
            selection = True
    # est dans le robot bleu
    elif x6 <= clic_x <= x7 and y6 <= clic_y <= y7:
            print("Tu as cliqué sur le robot bleu")
            robot = robot4
            selection = True
    else:
        selection = False
    return selection


def clavier(event):
    """Entre en jeu lorsque l'on clique sur une flèche. Elle sert à déplacer le robot"""
    global selection
    touche = event.keysym
    if selection == True:
        # flèche du haut
        if touche == "Up":
            x0, y0, x1, y1 = canvas.coords(robot[0])
            if y0 < HAUTEUR:
                robot[1] = 0
                robot[2] = -y0
                canvas.move(robot[0], robot[1], robot[2])
        
        # flèche du bas
        elif touche == "Down":
            x0, y0, x1, y1 = canvas.coords(robot[0])
            if y0 < HAUTEUR:
                robot[1] = 0
                robot[2] = +(HAUTEUR-y1)
                canvas.move(robot[0], robot[1], robot[2])
        
        # flèche de droite
        elif touche == "Right":
            x0, y0, x1, y1 = canvas.coords(robot[0])
            if x0 < LARGEUR:
                robot[2] = 0
                robot[1] = +(LARGEUR-x1)
                canvas.move(robot[0], robot[1], robot[2])

        # flèche de gauche
        elif touche == "Left":
            x0, y0, x1, y1 = canvas.coords(robot[0])
            if x0 < LARGEUR:
                robot[2] = 0
                robot[1] = -x0
                canvas.move(robot[0], robot[1], robot[2])


####################################
# programme principal
racine = tk.Tk()
racine.title("Jeu du robot-ricochet")

# création des widgets
canvas = tk.Canvas(racine, width= LARGEUR, height= HAUTEUR, bg= "navajo white")

# liaison des événements
canvas.bind("<Button-1>", est_dans_le_robot)
racine.bind("<Key>", clavier)

# placement des widgets
canvas.grid()

# programme principal
robot1 = creer_robot(COULEUR_ROBOT1)
robot2 = creer_robot(COULEUR_ROBOT2)
robot3 = creer_robot(COULEUR_ROBOT3)
robot4 = creer_robot(COULEUR_ROBOT4)

creer_carre()
quadrillage()

creer_mur1()
creer_mur2()
creer_mur3()
creer_mur4()
creer_mur5()
creer_mur6()

racine.mainloop()
