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

# valeurs des robots
VALEUR_ROBOT1 = 10
VALEUR_ROBOT2 = 20
VALEUR_ROBOT3 = 30
VALEUR_ROBOT4 = 40


# variables
tableau = []


###################################
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
    n = LARGEUR // COTE
    tableau = [[0] * n for i in range(n)]
    # initialisation des valeurs des celulles de la bordure externe
    tableau[0][0] = 7
    tableau[n-1][0] = 8
    tableau[n-1][n-1] = 6
    tableau[0][n-1] = 5
    # valeurs des cases occuppées par le carré noir central
    # 500 (valeur > 10) pour que le robot n'aille jamais dedans
    tableau[7][7] = 500
    tableau[7][8] = 500
    tableau[8][8] = 500
    tableau[8][7] = 500

def bordure():
    """creation bordures"""
    # 4 car sinon la borbure est cachée
    mur1 = canvas.create_line(4,4,4,HAUTEUR, fill="black", width = '4')
    mur2 = canvas.create_line(4,4,LARGEUR,4, fill="black", width = '4') 
    mur3 = canvas.create_line(LARGEUR,0,LARGEUR,HAUTEUR, fill="black", width = '4')
    mur4 = canvas.create_line(0,HAUTEUR,LARGEUR,HAUTEUR, fill="black", width = '4')


def creer_carre():
    "dessine caree"
    i = 16 // 2
    j = 16 // 2 + 1
    carre = canvas.create_rectangle((COTE*(i - 1), COTE*(i - 1)), (COTE*j, COTE*j), fill = "black")


def creer_robot(couleur_robot, valeur_robot):
    global tableau
    "dessine robot"
    # on cherche une case vide pour ne pas qu'il y ait 2 robots dans une même case
    occupe = 20
    i = 0
    j = 0
    while occupe > 10:
        i = rd.randint(0,15)
        j = rd.randint(0,15)
        occupe = tableau[i][j]
    # on définit la case comme étant occupée par le robot
    tableau[i][j] = occupe + valeur_robot
    x,y = i*COTE, j*COTE
    dx, dy = 10, 10
    rayon = COTE
    cercle = canvas.create_oval((x, y), (x+rayon, y+rayon), fill = couleur_robot)
    return [cercle, dx, dy]
    

def est_dans_le_robot(event):
    global robot, selection, valeur_robot
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
        valeur_robot = VALEUR_ROBOT1
        print(valeur_robot)
        selection = True 
    # est dans le robot vert
    elif x2 <= clic_x <= x3 and y2 <= clic_y <= y3:
            print("Tu as cliqué sur le robot vert")
            robot = robot2
            valeur_robot = VALEUR_ROBOT2
            print(valeur_robot)
            selection = True
    # est dans le robot rouge
    elif x4 <= clic_x <= x5 and y4 <= clic_y <= y5:
            print("Tu as cliqué sur le robot rouge")
            robot = robot3
            valeur_robot = VALEUR_ROBOT3
            print(valeur_robot)
            selection = True
    # est dans le robot bleu
    elif x6 <= clic_x <= x7 and y6 <= clic_y <= y7:
            print("Tu as cliqué sur le robot bleu")
            robot = robot4
            valeur_robot = VALEUR_ROBOT4
            print(valeur_robot)
            selection = True
    else:
        selection = False
    return selection


def clavier(event):
    """Entre en jeu lorsque l'on clique sur une flèche. Elle sert à déplacer le robot"""
    global selection, valeur_robot
    touche = event.keysym
    if selection == True:
        # flèche du haut
        if touche == "Up":
            x0, y0, x1, y1 = canvas.coords(robot[0])
            if y0 < HAUTEUR:
                robot[1] = 0
                robot[2] = -y0
                canvas.move(robot[0], robot[1], robot[2])
                if valeur_robot > (valeur_robot + 1):
                    robot[2] = j-1
        
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
creer_tableau()
creer_carre()
quadrillage()
bordure()

robot1 = creer_robot(COULEUR_ROBOT1, VALEUR_ROBOT1)
robot2 = creer_robot(COULEUR_ROBOT2, VALEUR_ROBOT2)
robot3 = creer_robot(COULEUR_ROBOT3, VALEUR_ROBOT3)
robot4 = creer_robot(COULEUR_ROBOT4, VALEUR_ROBOT4)

print(tableau)

racine.mainloop()