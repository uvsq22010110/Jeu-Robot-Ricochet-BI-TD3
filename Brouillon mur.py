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

Liste_de_type_de_mur = ['mur1','mur2','mur3','mur4','mur5','mur6','mur7','mur8']


# variables
tableau = []


###################################
# fonctions


def creer_mur1():
    # random i
    # random j
    #Exception : Si le mur est dans le carré au centre relancé la fonction créer_mur
    i = rd.randint(1,14)
    j = rd.randint(1,14)
    if (6 < i < 11) and (6 < j < 11):
        creer_mur1()
    else:
     mur1 = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, width = 5 , fill = "black")
     mur1 = 1

def creer_mur2():

    i = rd.randint(2,14)
    j = rd.randint(1,14)
    if (6 < i < 11) and (6 < j < 11):
        creer_mur2()
    else:
     mur2 = canvas.create_line(i*COTE,j*COTE,(i-1)*COTE,j*COTE, width = 5 , fill = "black")
     mur2 = 2


def creer_mur3():
    i = rd.randint(1,14)
    j = rd.randint(1,14)
    if (6 < i < 11) and (6 < j < 11):
        creer_mur3()
    else:
     mur3 = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, width = 5 , fill = "black")
     mur3 = 3

def creer_mur4():
    i = rd.randint(1,14)
    j = rd.randint(2,14)
    if (6 < i < 11) and (6 < j < 11):
        creer_mur4()
    else:
     mur4 = canvas.create_line(i*COTE,j*COTE,i*COTE,(j-1)*COTE, width = 5 , fill = "black")
     mur4 = 4

def creer_mur5():
    i = rd.randint(2,13)
    j = rd.randint(2,13)
    if (6 < i < 11) and (6 < j < 11):
        creer_mur5()
    else:
        mur5 = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, width = 5 , fill = "black")
        mur5 = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, width = 5 , fill = "black")
        mur5 = 5


def creer_mur6():
    i = rd.randint(2,13)
    j = rd.randint(2,13)
    if (6 < i < 11) and (6 < j < 11):
        creer_mur6()
    else:
        mur6 = canvas.create_line(i*COTE,j*COTE,(i-1)*COTE,j*COTE, width = 5 , fill = "black")
        mur6 = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, width = 5 , fill = "black")
        mur6 = 6

def creer_mur7():
    i = rd.randint(2,13)
    j = rd.randint(2,13)
    if (6 < i < 11) and (6 < j < 11):
        creer_mur7()
    else:
        mur7 = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, width = 5 , fill = "black")
        mur7 = canvas.create_line(i*COTE,j*COTE,i*COTE,(j-1)*COTE, width = 5 , fill = "black")
        mur7 = 7


def creer_mur8():
    i = rd.randint(2,13)
    j = rd.randint(2,13)
    if (6 < i < 11) and (6 < j < 11):
        creer_mur8()
    else:
        mur8 = canvas.create_line(i*COTE,j*COTE,(i-1)*COTE,j*COTE, width = 5 , fill = "black")
        mur8 = canvas.create_line(i*COTE,j*COTE,i*COTE,(j-1)*COTE, width = 5 , fill = "black")
        mur8 = 8

def creation_de_mur():
    import random
    n = 0
    while n != 18:
        n = n + 1
        Mur_choisie = random.choice(Liste_de_type_de_mur)
        if Mur_choisie == 'mur1':
            creer_mur1()
        elif Mur_choisie == 'mur2':
            creer_mur2()
        elif Mur_choisie == 'mur3':
            creer_mur3()
        elif Mur_choisie == 'mur4':
            creer_mur4()
        elif Mur_choisie == 'mur5':
            creer_mur5()
        elif Mur_choisie == 'mur6':
            creer_mur6()
        elif Mur_choisie == 'mur7':
            creer_mur7()
        elif Mur_choisie == 'mur8':
            creer_mur8()


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
creation_de_mur()

racine.mainloop()