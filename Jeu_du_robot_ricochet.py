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

# import des modules
import tkinter as tk
import random as rd
import os
import time
from tkinter.constants import ALL


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

VALEUR_ROBOT1 = 30
VALEUR_ROBOT2 = 20
VALEUR_ROBOT3 = 40
VALEUR_ROBOT4 = 10


# variables
tableau = []
cpt = 0
total = 0
couleur_precedente = ""
couleur_cible = ""
chargement = 0
nb_robot = 0
nom1 = ""
nom2 = ""
nom3 = ""
score1 = 0
score2 = 0
score3 = 0
PhotoImage = ""
cwd = os.getcwd()
filePath = __file__


# fonctions
def quadrillage():
    """Dessine un quadrillage sur le canvas"""
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


def creer_tableau():
    """Récupère les valeurs des cases en les plaçants dans un tableau"""
    global tableau
    n = LARGEUR // COTE
    tableau = [[0] * n for i in range(n)]
    # initialisation des celulles de la bordure externe
    # les 4 coins
    tableau[0][0] = 7
    tableau[n-1][0] = 8
    tableau[n-1][n-1] = 6
    tableau[0][n-1] = 5

    # valeurs des côtés sans petits murs
    i = 1
    # gauche
    while i < n-1:
        tableau[0][i] = 1
        i = i + 1
    i = 1 # on réinitialise i à 1 car à la fin de chaque boucle il vaut 15
    # droit
    while i < n-1:
        tableau[n-1][i] = 2
        i = i + 1
    i = 1
    # haut
    while i < n-1:
        tableau[i][0] = 4
        i = i + 1
    i = 1
    # bas
    while i < n-1:
        tableau[i][n-1] = 3
        i = i + 1
    
    # cases au-dessus du carré
    tableau[7][6] = 3
    tableau[8][6] = 3
    
    # cases à gauche du carré
    tableau[6][7] = 2
    tableau[6][8] = 2

    # cases occuppées par le carré noir central
    tableau[7][7] = 500
    tableau[7][8] = 500
    tableau[8][7] = 500
    tableau[8][8] = 500

    # cases en-dessous du carré
    tableau[7][9] = 4
    tableau[8][9] = 4

    # cases à droite du carré
    tableau[9][7] = 1
    tableau[9][8] = 1

    # contraintes et création des 17 angles
    angle = 0
    k = 5
    while angle != 17:
        i = rd.randint(1,15)
        j = rd.randint(1,15)
        if (tableau[i][j] == 0) and (tableau[i][j-1] == 0) and (tableau[i][j+1] == 0) and (tableau[i-1][j] == 0) and (tableau[i+1][j] == 0):
            tableau[i][j] = k
            if k == 5:
                # création de l'angle 5
                tableau[i-1][j] = 2
                mur5 = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, fill='black', width = '4')
                tableau[i][j+1] = 4
                mur6 = canvas.create_line(i*COTE,(j+1)*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == 6:
                # création de l'angle 6
                tableau[i+1][j] = 1
                mur6 = canvas.create_line((i+1)*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
                tableau[i][j+1] = 4
                mur7 = canvas.create_line(i*COTE,(j+1)*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == 7:
                # création de l'angle 7
                tableau[i-1][j] = 2
                mur8 = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, fill='black', width = '4')
                tableau[i][j-1] = 3
                mur9 = canvas.create_line((i)*COTE,j*COTE,i*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == 8:
                # création de l'angle 8
                tableau[i][j-1] = 3
                mur10 = canvas.create_line((i)*COTE,j*COTE,(i+1)*COTE,j*COTE, fill='black', width = '4')
                tableau[i+1][j] = 1
                mur11 = canvas.create_line((i+1)*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
                k = 4
            k += 1
            angle +=  1

def creer_carre():
    "dessine caree"
    i = 16 // 2
    j = 16 // 2 + 1
    carre = canvas.create_rectangle((40*(i - 1), 40*(i - 1)), (40*j, 40*j), fill = "black")

def creer_robot(couleur_robot, valeur_robot, i, j):
    "dessine robot"
    if chargement == 0:
        # on cherche une case vide
        occupe = 20
        while occupe > 10:
            i = rd.randint(0,15)
            j = rd.randint(0,15)
            occupe = tableau[i][j]
        # on définit la case comme étant occupée par le robot
        tableau[i][j] = occupe + valeur_robot
    #attention pas sous le carré noir
    x,y = i*COTE, j*COTE
    dx, dy = 10, 10
    rayon = COTE
    cercle = canvas.create_oval((x, y), (x+rayon, y+rayon), fill = couleur_robot)
    return [cercle, dx, dy]
    
def est_dans_le_robot(event):
    global robot, selection, valeur_robot, valeur_touche
    """Retourne True si on a cliqué sur un robot sinon False"""
    x0, y0, x1, y1 = canvas.coords(robot1[0])
    x2, y2, x3, y3 = canvas.coords(robot2[0])
    x4, y4, x5, y5 = canvas.coords(robot3[0])
    x6, y6, x7, y7 = canvas.coords(robot4[0])
    clic_x = event.x
    clic_y = event.y
    valeur_robot = 0
    # est dans le robot rouge
    if x0 <= clic_x <= x1 and y0 <= clic_y <= y1:
        print("Tu as cliqué sur le robot rouge")
        robot = robot1
        valeur_robot = VALEUR_ROBOT1
        x = int(x0 // COTE)
        y = int(y0 // COTE)
        selection = True
        valeur_touche = ""
    # est dans le robot vert
    elif x2 <= clic_x <= x3 and y2 <= clic_y <= y3:
        print("Tu as cliqué sur le robot vert")
        robot = robot2
        valeur_robot = VALEUR_ROBOT2
        x = int(x2 // COTE)
        y = int(y2 // COTE)
        selection = True
        valeur_touche = ""
    # est dans le robot bleu
    elif x4 <= clic_x <= x5 and y4 <= clic_y <= y5:
        print("Tu as cliqué sur le robot blue")
        robot = robot3
        valeur_robot = VALEUR_ROBOT3
        x = int(x4 // COTE)
        y = int(y4 // COTE)
        selection = True
        valeur_touche = ""
    # est dans le robot jaune
    elif x6 <= clic_x <= x7 and y6 <= clic_y <= y7:
        print("Tu as cliqué sur le robot jaune")
        robot = robot4
        valeur_robot = VALEUR_ROBOT4
        x = int(x6 // COTE)
        y = int(y6 // COTE)
        selection = True
        valeur_touche = ""
    else:
        selection = False
    perdu.grid_forget()
    return selection, valeur_robot

def clavier(event):
    """Sert à déplacer les robots grâces aux touches du clavier"""
    global selection, valeur_robot, cible1, etoile1, valeur_touche, cpt, gagne, total, nb_robot, fic_move
    touche = event.keysym # pour pouvoir réccupérer la touche appuyée
    if selection == True:
        x8, y8, x9, y9 = canvas.coords(robot[0])
        gagne = 0
        # Flèche du haut
        if (touche == "Up") and (valeur_touche != "Up"):
            valeur_touche = "Up"
            stop = 0
            k = 0
            monte = 0 # case de fin
            depart = int(y8 // COTE) # case de depart
            while stop == 0:
                i = int(x8 // COTE)
                j = int(y8 // COTE) - k
                valeur_depart = tableau[i][depart]
                valeur = tableau[i][j]
                k = k + 1
                # le robot continue d'avancer
                if (valeur == 0) or (valeur == 1) or (valeur == 2):
                    stop = 0
                # le robot se stoppe car il y a un mur haut
                elif (valeur == 7) or (valeur == 8) or (valeur == 4):
                    stop = 1
                    print(valeur)
                # déplacements
                elif (10 <= valeur) and (valeur <= 48):
                    # le robot se stoppe s'il rencontre un mur haut
                    if (valeur == valeur_robot+4) or (valeur == valeur_robot+7) or (valeur == valeur_robot+8):
                        stop = 1
                        #j = j - 1
                    # continue car aucun obstable rencontré
                    elif (valeur == valeur_robot) or (valeur == valeur_robot+1) or (valeur == valeur_robot+2) or (valeur == valeur_robot+3) or (valeur == valeur_robot+5) or (valeur == valeur_robot+6):
                        stop = 0
                    else:
                        stop = 1
                        j = j + 1
                        valeur = tableau[i][j]
                # si le robot atterit sur la bonne cible
                elif (valeur>100):
                    if (valeur == valeur_robot*10+7) or (valeur == valeur_robot*10+8):
                        stop = 1
                        gagne = 1
                    else:
                        stop = 1
                        j = j + 1
                        valeur = tableau[i][j]
                monte = j
            print(monte-depart)
            canvas.move(robot[0], 0, ((monte-depart)*COTE))
            if (monte - depart) < 0:
                # compteur
                cpt += 1
                tableau[i][j] = valeur + valeur_robot
                tableau[i][depart] = valeur_depart - valeur_robot
                # récupère valeurs et commandes effectuées dans un fichier texte
                fic_move = open(rep + "\move.txt", "a")
                fic_move.write("Up")
                fic_move.write(";")
                fic_move.write(str(valeur_robot))
                fic_move.write(";")
                fic_move.write(str(i))
                fic_move.write(";")
                fic_move.write(str(j))
                fic_move.write(";")
                fic_move.write(str(monte-depart) + '\n')
                fic_move.close()
                if gagne == 1:
                # faire disparraitre la cible lorsqu'elle est atteinte
                    canvas.delete(cible1)
                    canvas.delete(etoile1)
                    tableau[i][j] = tableau[i][j] - (valeur_robot*10)
                    total = total + cpt
                    nb_robot += 1
                    mvt_total.config(text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)", font=("Helvetica", "15"))
                    cpt = 0
                    gagner()
            print("valeur départ",tableau[i][depart])
            print("valeur arrivée",tableau[i][j])

        # Flèche du bas
        elif (touche == "Down") and (valeur_touche != "Down"):
            valeur_touche = "Down"
            k = 0
            stop = 0
            descends = 0 # case de fin
            depart = int(y8 // COTE) # case de depart
            while stop == 0:
                i = int(x8 // COTE)
                j = int(y8 // COTE) + k
                valeur_depart = tableau[i][depart]
                valeur = tableau[i][j]
                k = k + 1
                # le robot continue d'avancer
                if (valeur == 0) or (valeur == 1) or (valeur == 2):
                    stop = 0
                # le robot se stoppe car il y a un mur bas
                elif (valeur == 3) or (valeur == 5) or (valeur == 6):
                    stop = 1
                elif (10<=valeur) and (valeur<=48):
                    # le robot se stoppe s'il rencontre un mur bas
                    if (valeur == valeur_robot+3) or (valeur == valeur_robot+5) or (valeur == valeur_robot+6):
                        stop = 1
                    # continue car aucun obstable rencontré
                    elif (valeur == valeur_robot) or (valeur == valeur_robot+1) or (valeur == valeur_robot+2)  or (valeur == valeur_robot+4) or (valeur == valeur_robot+7) or (valeur == valeur_robot+8):
                        stop = 0
                    else:
                        stop = 1
                        j = j - 1
                        valeur = tableau[i][j]
                # si le robot atterit sur la bonne cible
                elif (valeur>100):
                    if (valeur == valeur_robot*10+5) or (valeur == valeur_robot*10+6):
                        stop = 1
                        gagne = 1
                    else:
                        stop = 1
                        j = j - 1
                        valeur = tableau[i][j]
                descends = j
            print(descends-depart)
            canvas.move(robot[0], 0, ((descends-depart)*COTE))
            if (descends - depart) > 0:
                # compteur
                cpt += 1
                tableau[i][j] = valeur + valeur_robot
                tableau[i][depart] = valeur_depart - valeur_robot
                # récupère valeurs et commandes effectuées dans un fichier texte
                fic_move = open(rep + "\move.txt", "a")
                fic_move.write("Down")
                fic_move.write(";")
                fic_move.write(str(valeur_robot))
                fic_move.write(";")
                fic_move.write(str(i))
                fic_move.write(";")
                fic_move.write(str(j))
                fic_move.write(";")
                fic_move.write(str(descends-depart) + '\n')
                fic_move.close()
                if gagne == 1:
                # faire disparraitre la cible lorsqu'elle est atteinte
                    canvas.delete(cible1)
                    canvas.delete(etoile1)
                    tableau[i][j] = tableau[i][j] - (valeur_robot*10)
                    total = total + cpt
                    nb_robot += 1
                    mvt_total.config(text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)", font=("Helvetica", "15"))
                    cpt = 0
                    gagner()
            print("valeur départ",tableau[i][depart])
            print("valeur arrivée",tableau[i][j])
            print(tableau[i][j])
            print(valeur_touche)

        # Flèche de droite  
        elif touche == "Right" and valeur_touche != "Right":
            valeur_touche = "Right"
            k = 0
            stop = 0
            droite = 0 # case de fin
            depart = int(x8 // COTE) # case de depart
            while stop == 0:
                i = int(x8 // COTE) + k
                j = int(y8 // COTE)
                valeur = tableau[i][j]
                valeur_depart = tableau[depart][j]
                k = k + 1
                if (valeur == 1) or (valeur == 3) or (valeur == 4):
                    stop = 0
                elif (valeur == 2) or (valeur == 6) or (valeur == 8):
                    stop = 1
                elif (10<=valeur) and (valeur<=48):
                    if (valeur == valeur_robot+2) or (valeur == valeur_robot+6) or (valeur == valeur_robot+8):
                        stop = 1
                    elif (valeur == valeur_robot) or (valeur == valeur_robot+1) or (valeur == valeur_robot+3) or (valeur == valeur_robot+4) or (valeur == valeur_robot+5) or (valeur == valeur_robot+7):
                        stop = 0
                    else:
                        stop = 1
                        i = i - 1
                        valeur = tableau[i][j]
                # si le robot atterit dans la bonne cible
                elif (valeur>100):
                    if (valeur == valeur_robot*10+6) or (valeur == valeur_robot*10+8):
                        stop = 1
                        gagne = 1
                    else:
                        stop = 1
                        i = i - 1
                        valeur = tableau[i][j]
                droite = i
            print(droite-depart)
            canvas.move(robot[0], ((droite-depart)*COTE), 0)
            if (droite - depart) > 0:
                # compteur
                cpt += 1
                tableau[i][j] = valeur + valeur_robot
                tableau[depart][j] = valeur_depart - valeur_robot
                # récupère valeurs et commandes effectuées dans un fichier texte
                fic_move = open(rep + "\move.txt", "a")
                fic_move.write("Right")
                fic_move.write(";")
                fic_move.write(str(valeur_robot))
                fic_move.write(";")
                fic_move.write(str(i))
                fic_move.write(";")
                fic_move.write(str(j))
                fic_move.write(";")
                fic_move.write(str(droite-depart) + '\n')
                fic_move.close()
                if gagne == 1:
                # faire disparraitre la cible lorsqu'elle est atteinte
                    canvas.delete(cible1)
                    canvas.delete(etoile1)
                    tableau[i][j] = tableau[i][j] - (valeur_robot*10)
                    total = total + cpt
                    nb_robot += 1
                    mvt_total.config(text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)", font=("Helvetica", "15"))
                    cpt = 0
                    gagner()
            print("valeur départ",tableau[depart][j])
            print("valeur arrivée",tableau[i][j])
            print(tableau[i][j])
            print(valeur_touche)

        # Flèche de gauche
        elif touche == "Left" and valeur_touche != "Left":
            valeur_touche = "Left"
            k = 0
            stop = 0
            gauche = 0 # case de fin
            depart = int(x8 // COTE) # case de depart
            while stop == 0:
                i = int(x8 // COTE) - k
                j = int(y8 // COTE)
                valeur = tableau[i][j]
                valeur_depart = tableau[depart][j]
                k = k + 1
                if (valeur == 2) or (valeur == 3) or (valeur == 4):
                    stop = 0
                elif (valeur == 1) or (valeur == 5) or (valeur == 7):
                    stop = 1
                elif (10<=valeur) and (valeur<=48):
                    if (valeur == valeur_robot+1) or (valeur == valeur_robot+5) or (valeur == valeur_robot+7):
                        stop = 1
                    elif (valeur == valeur_robot) or (valeur == valeur_robot+2) or (valeur == valeur_robot+3) or (valeur == valeur_robot+4) or (valeur == valeur_robot+6) or (valeur == valeur_robot+8):
                        stop = 0
                    else:
                        stop = 1
                        i = i + 1
                        valeur = tableau[i][j]
                # si le robot atterit dans la bonne cible
                elif (valeur>100):
                    if (valeur == valeur_robot*10+5) or (valeur == valeur_robot*10+7):
                        stop = 1
                        gagne = 1
                    else:
                        stop = 1
                        i = i + 1
                        valeur = tableau[i][j]
                gauche = i
            print(gauche-depart)
            canvas.move(robot[0], ((gauche-depart)*COTE), 0)
            if (gauche - depart) < 0:
                # compteur
                cpt += 1
                tableau[i][j] = valeur + valeur_robot
                tableau[depart][j] = valeur_depart - valeur_robot
                # récupère valeurs et commandes effectuées dans un fichier texte
                fic_move = open(rep + "\move.txt", "a")
                fic_move.write("Left")
                fic_move.write(";")
                fic_move.write(str(valeur_robot))
                fic_move.write(";")
                fic_move.write(str(i))
                fic_move.write(";")
                fic_move.write(str(j))
                fic_move.write(";")
                fic_move.write(str(gauche-depart) + '\n')
                fic_move.close()
                if gagne == 1:
                # faire disparraitre la cible lorsqu'elle est atteinte
                    canvas.delete(cible1)
                    canvas.delete(etoile1)
                    tableau[i][j] = tableau[i][j] - (valeur_robot*10)
                    total = total + cpt
                    nb_robot += 1
                    mvt_total.config(text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)", font=("Helvetica", "15"))
                    cpt = 0
                    gagner()
            print("valeur départ",tableau[depart][j])
            print("valeur arrivée",tableau[i][j])
            print(tableau[i][j])
        nb_de_deplacements.config(text="Tu as fait: " + str(cpt) + " déplacement(s)", font=("Helvetica", "15"))

def bordure():
    """creation bordures"""
    mur1 = canvas.create_line(4,4,4,LARGEUR, fill='black', width = '4')
    mur2 = canvas.create_line(4,4,LARGEUR,4, fill='black', width = '4') 
    mur3 = canvas.create_line(LARGEUR,0,LARGEUR,LARGEUR, fill='black', width = '4')
    mur4 = canvas.create_line(0,LARGEUR,LARGEUR,LARGEUR, fill='black', width = '4')

def obstacle_mur():
    """Créer les petits murs"""
    # petits murs du haut
    petit_mur = rd.randint(2,8)
    canvas.create_line(petit_mur*COTE,0,petit_mur*COTE,COTE, fill='black', width = '4')
    choix = petit_mur
    tableau[petit_mur][0] = 7
    tableau[petit_mur-1][0] = 8
    while (int(petit_mur-choix) < 2):
        petit_mur = rd.randint(9,14)
    canvas.create_line(petit_mur*COTE,0,petit_mur*COTE,COTE, fill='black', width = '4')
    tableau[petit_mur][0] = 7
    tableau[petit_mur-1][0] = 8

    # petits murs de droite
    petit_mur = rd.randint(2,8)
    canvas.create_line(LARGEUR-COTE,petit_mur*COTE,LARGEUR,petit_mur*COTE, fill='black', width = '4')
    tableau[(LARGEUR // COTE)-1][petit_mur] = 8
    tableau[(LARGEUR // COTE)-1][petit_mur-1] = 6
    choix = petit_mur
    while (int(petit_mur-choix) < 2):
        petit_mur = rd.randint(9,14)
    canvas.create_line(LARGEUR-COTE,petit_mur*COTE,LARGEUR,petit_mur*COTE, fill='black', width = '4')
    tableau[(LARGEUR // COTE)-1][petit_mur] = 8
    tableau[(LARGEUR // COTE)-1][petit_mur-1] = 6

    # petits murs du bas
    petit_mur = rd.randint(2,8)
    canvas.create_line(petit_mur*COTE,HAUTEUR,petit_mur*COTE,HAUTEUR-COTE, fill='black', width = '4')
    tableau[petit_mur-1][(LARGEUR // COTE)-1] = 6
    tableau[petit_mur][(LARGEUR // COTE)-1] = 5
    choix = petit_mur
    while (int(petit_mur-choix) < 2):
        petit_mur = rd.randint(9,14)
    canvas.create_line(petit_mur*COTE,HAUTEUR,petit_mur*COTE,HAUTEUR-COTE, fill='black', width = '4')
    tableau[petit_mur-1][(LARGEUR // COTE)-1] = 6
    tableau[petit_mur][(LARGEUR // COTE)-1] = 5

    # petits murs de droite
    petit_mur = rd.randint(2,8)
    canvas.create_line(0,petit_mur*COTE,COTE,petit_mur*COTE, fill='black', width = '4')
    tableau[0][petit_mur-1] = 5
    tableau[0][petit_mur] = 7
    choix = petit_mur
    while (int(petit_mur-choix) < 2):
        petit_mur = rd.randint(9,14)
    canvas.create_line(0,petit_mur*COTE,COTE,petit_mur*COTE, fill='black', width = '4')
    tableau[0][petit_mur-1] = 5
    tableau[0][petit_mur] = 7

def placer_cible():
    """Place la cible dans un angle"""
    global VALEUR_ROBOT1, VALEUR_ROBOT2, VALEUR_ROBOT3, VALEUR_ROBOT4, cible1, etoile1, couleur_cible, couleur_precedente
    cible = 0
    liste_couleur = ['yellow','blue','red','green']
    couleur_cible = couleur_precedente
    while couleur_precedente == couleur_cible:
        couleur_cible = rd.choice(liste_couleur)
    while cible not in (5,8):
        i = rd.randint(1,14)
        j = rd.randint(1,14)
        cible = tableau[i][j]
    if couleur_cible == COULEUR_ROBOT1:
        tableau[i][j] = cible + VALEUR_ROBOT1*10
    elif couleur_cible == COULEUR_ROBOT2:
        tableau[i][j] = cible + VALEUR_ROBOT2*10
    elif couleur_cible == COULEUR_ROBOT3:
        tableau[i][j] = cible + VALEUR_ROBOT3*10
    elif couleur_cible == COULEUR_ROBOT4:
        tableau[i][j] = cible + VALEUR_ROBOT4*10
    couleur_precedente = couleur_cible
    cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=couleur_cible)
    # dessin de l'etoile au cercle de la cible
    etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")

def gagner():
    """"Entre en jeu lorsqu'on le joueur à fait rentré les 5 robots"""
    """si on gagne, nous demande d'inscrire notre nom sinon affiche dommage"""
    global score1, score2, score3, nom, nom1, nom2, nom3, nb_robot, total, perdu
    if nb_robot == 5:
        # si le joueur gagne
        if total < int(score3):
            demande_nom()
        # si le joueur perd
        else:
            perdu = tk.Label(racine, text="Dommage, vous ne faites pas parti(e) du podium. Essayez encore!", font=("Helvetica", "15"), bg = "navajo white")
            perdu.grid(row=7, columnspan=5)
            nb_robot = 0
            total = 0
            cpt = 0
            mvt_total.config(text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)")
            nb_de_deplacements.config(text="Tu as fait: " + str(cpt) + " déplacement(s)", font=("Helvetica", "15"))

    cpt = 0
    placer_cible()
    racine.bind("<Key>", clavier)
    print("gagné")

def repertoire_courant():
    """récupération du chemin du répertoire où se trouve le programme et les sauvegardes"""
    global rep
    # chemin complet du fichier
    absFilePath = os.path.abspath(__file__)
    # décomposition du chemin en répertoire et fichier
    path, filename = os.path.split(absFilePath)
    rep = path
    print("repertoire :", rep)
    # pour récupérer les informations sur les déplacements éffectués par les différents robots
    fic_move = open(rep + "\move.txt", "w")
    

def sauvegarder():
    """Récupère les valeurs du tableau dans un fichier texte"""
    # récupération des valeurs du tableau dans un fichier texte
    fic_out = open(rep + "\sauvegarde.txt", "w")
    for i in range(16):
        for j in range(16):
            fic_out.write(str(tableau[i][j]))
            fic_out.write(';')
        fic_out.write('\n')
    # récupération des valeurs : compteur, nombre de robots, couleur de la cible, total dans un fichier texte
    fic2_out = open(rep + "\sauvegarde_score_en_cours.txt", "w")
    fic2_out.write(str(cpt))
    fic2_out.write('\n')
    fic2_out.write(str(nb_robot))
    fic2_out.write('\n')
    fic2_out.write(couleur_precedente)
    fic2_out.write('\n')
    fic2_out.write(str(total))
    fic_out.close()
    fic2_out.close()

def meilleur_score5():
    """Garde les valeurs et les noms pour le podium"""
    global score1, score2, score3, nom1, nom2, nom3, rep
    score_in = open(rep + "\meilleur_score5.txt", "r")
    ligne = score_in.readline()
    l = ligne.split(';')
    score1 = l[1]
    nom1 = l[0]
    score2 = l[3]
    nom2 = l[2]
    score3 = l[5]
    nom3 = l[4]
    score_in.close()
    score_1er.config(text=nom1 + " : " + str(score1), font=("Helvetica", "15"))
    score_2e.config(text=nom2 + " : " + str(score2), font=("Helvetica", "15"))
    score_3e.config(text=nom3 + " : " + str(score3), font=("Helvetica", "15"))

def reprendre_la_partie():
    """Récupère les valeurs comprises dans le tableau de sauvegarde et les ré-affichent """
    global ligne, i, j, k, l, chargement, robot1, robot2, robot3, robot4, cible1, etoile1, cpt, total, nb_robot, couleur_cible
    chargement = 1
    canvas.delete(ALL)
    creer_carre()
    quadrillage()
    bordure()
    fic_in = open(rep + "\sauvegarde.txt", "r")
    ligne = fic_in.readline()
    i = 0
    while ligne:
        for j in range(16):
            l = ligne.split(';')
            k = l[j]
            tableau[i][j] = int(k)
            if k == '1':
                mur = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '2':
                mur = canvas.create_line((i+1)*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '3':
                mur = canvas.create_line(i*COTE,(j+1)*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '4':
                mur = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, fill='black', width = '4')
            if k == '5':
                mur = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, fill='black', width = '4')
                mur = canvas.create_line(i*COTE,(j+1)*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '6':
                mur = canvas.create_line((i+1)*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
                mur = canvas.create_line(i*COTE,(j+1)*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '7':
                mur = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, fill='black', width = '4')
                mur = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '8':
                mur = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, fill='black', width = '4')
                mur = canvas.create_line((i+1)*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if 0 <= (int(k) - VALEUR_ROBOT1) <= 8:
                x0, y0, x1, y1 = i*COTE ,j*COTE , (i+1)*COTE, (j+1)*COTE
                robot1 = creer_robot(COULEUR_ROBOT1,VALEUR_ROBOT1, i, j)
            if 0 <= (int(k) - VALEUR_ROBOT2) <= 8:
                x2, y2, x3, y3 = i*COTE ,j*COTE , (i+1)*COTE, (j+1)*COTE
                robot2 = creer_robot(COULEUR_ROBOT2,VALEUR_ROBOT2, i, j)
            if 0 <= (int(k) - VALEUR_ROBOT3) <= 8:
                x4, y4, x5, y5 = i*COTE ,j*COTE , (i+1)*COTE, (j+1)*COTE
                robot3 = creer_robot(COULEUR_ROBOT3,VALEUR_ROBOT3, i, j)
            if 0 <= (int(k) - VALEUR_ROBOT4) <= 8:
                x6, y6, x7, y7 = i*COTE ,j*COTE , (i+1)*COTE, (j+1)*COTE
                robot4 = creer_robot(COULEUR_ROBOT4,VALEUR_ROBOT4, i, j)
            if 0 <= (int(k) - VALEUR_ROBOT1*10) <= 8:
                cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=COULEUR_ROBOT1)
                couleur_precedente = COULEUR_ROBOT1
                # dessin de l'etoile au cercle de la cible
                etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")
            if 0 <= (int(k) - VALEUR_ROBOT2*10) <= 8:
                cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=COULEUR_ROBOT2)
                couleur_precedente = COULEUR_ROBOT2
                # dessin de l'etoile au cercle de la cible
                etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")
            if 0 <= (int(k) - VALEUR_ROBOT3*10) <= 8:
                cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=COULEUR_ROBOT3)
                couleur_precedente = COULEUR_ROBOT3
                # dessin de l'etoile au cercle de la cible
                etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")
            if 0 <= (int(k) - VALEUR_ROBOT4*10) <= 8:
                cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=COULEUR_ROBOT4)
                couleur_precedente = COULEUR_ROBOT4
                # dessin de l'etoile au cercle de la cible
                etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")
        ligne = fic_in.readline()
        i += 1
    fic2_in = open(rep + "\sauvegarde_score_en_cours.txt", "r")
    cpt = int(fic2_in.readline())
    nb_robot = int(fic2_in.readline())
    couleur_cible = str(fic2_in.readline())
    total = int(fic2_in.readline())
    mvt_total.config(text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)")
    nb_de_deplacements.config(text="Tu as fait: " + str(cpt) + " déplacement(s)", font=("Helvetica", "15"))
    fic_in.close()
    fic2_in.close()

def recommencer():
    """Récupère les valeurs comprises dans le tableau de sauvegarde et les ré-affichent """
    global ligne, i, j, k, l, chargement, robot1, robot2, robot3, robot4, cible1, etoile1, cpt, total, nb_robot, couleur_cible
    chargement = 1
    canvas.delete(ALL)
    creer_carre()
    quadrillage()
    bordure()
    fic_in = open(rep + "\sauvegarde_initiale.txt", "r")
    ligne = fic_in.readline()
    i = 0
    while ligne:
        for j in range(16):
            l = ligne.split(';')
            k = l[j]
            tableau[i][j] = int(k)
            if k == '1':
                mur = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '2':
                mur = canvas.create_line((i+1)*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '3':
                mur = canvas.create_line(i*COTE,(j+1)*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '4':
                mur = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, fill='black', width = '4')
            if k == '5':
                mur = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, fill='black', width = '4')
                mur = canvas.create_line(i*COTE,(j+1)*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '6':
                mur = canvas.create_line((i+1)*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
                mur = canvas.create_line(i*COTE,(j+1)*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '7':
                mur = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, fill='black', width = '4')
                mur = canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, fill='black', width = '4')
            if k == '8':
                mur = canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, fill='black', width = '4')
                mur = canvas.create_line((i+1)*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE, fill='black', width = '4')
            if 0 <= (int(k) - VALEUR_ROBOT1) <= 8:
                x0, y0, x1, y1 = i*COTE ,j*COTE , (i+1)*COTE, (j+1)*COTE
                robot1 = creer_robot(COULEUR_ROBOT1,VALEUR_ROBOT1, i, j)
            if 0 <= (int(k) - VALEUR_ROBOT2) <= 8:
                x2, y2, x3, y3 = i*COTE ,j*COTE , (i+1)*COTE, (j+1)*COTE
                robot2 = creer_robot(COULEUR_ROBOT2,VALEUR_ROBOT2, i, j)
            if 0 <= (int(k) - VALEUR_ROBOT3) <= 8:
                x4, y4, x5, y5 = i*COTE ,j*COTE , (i+1)*COTE, (j+1)*COTE
                robot3 = creer_robot(COULEUR_ROBOT3,VALEUR_ROBOT3, i, j)
            if 0 <= (int(k) - VALEUR_ROBOT4) <= 8:
                x6, y6, x7, y7 = i*COTE ,j*COTE , (i+1)*COTE, (j+1)*COTE
                robot4 = creer_robot(COULEUR_ROBOT4,VALEUR_ROBOT4, i, j)
            if 0 <= (int(k) - VALEUR_ROBOT1*10) <= 8:
                cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=COULEUR_ROBOT1)
                couleur_precedente = COULEUR_ROBOT1
                # dessin de l'etoile au cercle de la cible
                etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")
            if 0 <= (int(k) - VALEUR_ROBOT2*10) <= 8:
                cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=COULEUR_ROBOT2)
                couleur_precedente = COULEUR_ROBOT2
                # dessin de l'etoile au cercle de la cible
                etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")
            if 0 <= (int(k) - VALEUR_ROBOT3*10) <= 8:
                cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=COULEUR_ROBOT3)
                couleur_precedente = COULEUR_ROBOT3
                # dessin de l'etoile au cercle de la cible
                etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")
            if 0 <= (int(k) - VALEUR_ROBOT4*10) <= 8:
                cible1 = canvas.create_rectangle(i*COTE+4,j*COTE+4,(i+1)*COTE-4,(j+1)*COTE-4, fill=COULEUR_ROBOT4)
                couleur_precedente = COULEUR_ROBOT4
                # dessin de l'etoile au cercle de la cible
                etoile1 = canvas.create_polygon(19+i*COTE,4+j*COTE,15.2+i*COTE,14.8+j*COTE,4+i*COTE,14.8+j*COTE,13.2+i*COTE,21.6+j*COTE,9.6+i*COTE,32.6+j*COTE,19+i*COTE,26.6+j*COTE,28.6+i*COTE,32.6+j*COTE,24.6+i*COTE,21.6+j*COTE,34+i*COTE,14.8+j*COTE,22.6+i*COTE,14.8+j*COTE,fill="black")
        ligne = fic_in.readline()
        i += 1
    fic2_in = open(rep + "\sauvegarde_initiale_score_en_cours.txt", "r")
    cpt = int(fic2_in.readline())
    nb_robot = int(fic2_in.readline())
    couleur_cible = str(fic2_in.readline())
    total = int(fic2_in.readline())
    mvt_total.config(text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)")
    nb_de_deplacements.config(text="Tu as fait: " + str(cpt) + " déplacement(s)", font=("Helvetica", "15"))
    fic_in.close()
    fic2_in.close()

def sauvegarde_mouvement():
    """Effectue un retour en arrière lorsque l'on clique dessus"""
    global descends, monte, droite, gauche, depart, cpt
    fic_move = open(rep + "\move.txt", "r")
    ligne = fic_move.readline()
    while ligne:
        if ligne != "" :
            l = ligne.split(';')
        ligne = fic_move.readline()
    if l[0] == "Up":
        canvas.move(robot[0], 0, -int(l[4])*COTE)
    elif l[0] == "Down":
        canvas.move(robot[0], 0, -int(l[4])*COTE, 0)
    elif l[0] == "Left":
        canvas.move(robot[0], -int(l[4])*COTE, 0)
    elif l[0] == "Right":
        canvas.move(robot[0], -int(l[4])*COTE, 0)
    cpt -= 1
    nb_de_deplacements.config(text="Tu as fait: " + str(cpt) + " déplacement(s)", font=("Helvetica", "15"))
    fic_move.close()

def sauvegarde_initiale():
    """Récupère les valeurs du tableau dans un fichier texte"""
    # récupération des valeurs du tableau dans un fichier texte
    fic_out = open(rep + "\sauvegarde_initiale.txt", "w")
    for i in range(16):
        for j in range(16):
            fic_out.write(str(tableau[i][j]))
            fic_out.write(';')
        fic_out.write('\n')
    # récupération des valeurs : compteur, nombre de robots, couleur de la cible, total dans un fichier texte
    fic2_out = open(rep + "\sauvegarde_initiale_score_en_cours.txt", "w")
    fic2_out.write(str(cpt))
    fic2_out.write('\n')
    fic2_out.write(str(nb_robot))
    fic2_out.write('\n')
    fic2_out.write(couleur_precedente)
    fic2_out.write('\n')
    fic2_out.write(str(total))
    fic_out.close()
    fic2_out.close()


def taper_nom():
    """Rentrer son nom lorsqu'on rentre dans le top 3"""
    global nom1, nom2, nom3, score1, score2, score3, total, nb_robot
    # 1ère place du podium
    if total < int(score1):
        nom3 = nom2
        score3 = score2
        nom2 = nom1
        score2 = score1
        score1 = total
        nom1 = (e1.get())
    # 2ème place du podium
    elif int(score1) <= total <= int(score2):
        score3 = score2
        nom3 = nom2
        score2 = total
        nom2 = (e1.get())
    # 3ème place du podium
    elif int(score2) <= total < int(score3):
        score3 = total
        nom3 = (e1.get())
    score_out = open(rep + "\meilleur_score5.txt", "w")
    score_out.write(nom1)
    score_out.write(";")
    score_out.write(str(score1))
    score_out.write(";")
    score_out.write(nom2)
    score_out.write(";")
    score_out.write(str(score2))
    score_out.write(";")
    score_out.write(nom3)
    score_out.write(";")
    score_out.write(str(score3))
    score_out.close()
    meilleur_score5()
    nb_robot = 0
    total = 0
    mvt_total.config(text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)")
    e1.grid_forget()
    bouton.grid_forget()
    lab1.grid_forget()

def demande_nom():
    """Demande le nom du joueur"""
    global e1, racine, bouton, lab1
    racine.unbind("<Key>")
    lab1 = tk.Label(racine, text="Bravo, vous faites parti(e) du top 3 ! Veuillez entrer votre nom : ", font=("Helvetica", "15"), bg = "navajo white")
    lab1.grid(row=7, columnspan=2)
    e1 = tk.Entry(racine, width=20, font=("Helvetica", "15"), bg="navajo white")
    e1.grid(row=7, column=2)
    bouton = tk.Button(racine, text='Valider', command=taper_nom, font=("Helvetica", "15"))
    bouton.grid(row=7, column=3)


# programme principal
racine = tk.Tk()
racine.title("Jeu des robots")

# création des widgets
# canvas
canvas = tk.Canvas(racine, width= LARGEUR, height= HAUTEUR, bg= "navajo white")
#labels
nb_de_deplacements = tk.Label(racine, text="Tu as fait: " + str(cpt) + " déplacement(s)", font=("Helvetica", "15"))
mvt_total = tk.Label(racine, text="Tu as fait rentrer : " + str(nb_robot) + " robot(s) en " + str(total) + " déplacement(s)", font=("Helvetica", "15"))
meilleurs_score = tk.Label(racine, text="Meilleurs scores pour 5 robots de rentrés : ", font=("Helvetica", "15"))
podium_1 = tk.Label(racine, text="1er", font=("Helvetica", "20"), bg = "gold", relief = "raised")
score_1er = tk.Label(racine, text="", font=("Helvetica", "15"))
podium_2 = tk.Label(racine, text="2ème", font=("Helvetica", "20"), bg = "silver", relief = "raised")
score_2e = tk.Label(racine, text="", font=("Helvetica", "15"))
podium_3 = tk.Label(racine, text="3ème", font=("Helvetica", "20"), bg = "orange", relief = "raised")
score_3e = tk.Label(racine, text="", font=("Helvetica", "15"))
# buttons
sauvegarde = tk.Button(text = "Sauvegarde", font=("Helvetica", "15"), fg='blue', relief = "raised", borderwidth = 5, command = sauvegarder)
reprendre = tk.Button(text = "Reprendre la partie sauvegardée", font=("Helvetica", "15"), fg='red', relief = "raised", borderwidth = 5, command = reprendre_la_partie)
retour_en_arriere = tk.Button(text = "Retour en arrière", font=("Helvetica", "15"), fg='purple', relief = "raised", borderwidth = 5, command = sauvegarde_mouvement)
recommencer_partie = tk.Button(text = "Recommencer", font=("Helvetica", "15"), fg='magenta', relief = "raised", borderwidth = 5, command = recommencer)

# liaison des événements
canvas.bind("<Button-1>", est_dans_le_robot)
racine.bind("<Key>", clavier)

# placement des widgets
# canvas
canvas.grid(row=1, columnspan=2, rowspan=5)
# labels
meilleurs_score.grid(row=1, column=2, columnspan=2)
podium_1.grid(row=2, column=2, columnspan=2)
score_1er.grid(row=3, column=2, columnspan=2)
podium_2.grid(row=4, column=2)
score_2e.grid(row=5, column=2)
podium_3.grid(row=4, column=3)
score_3e.grid(row=5, column=3)
nb_de_deplacements.grid(row = 0, column=0)
mvt_total.grid(row=0, column=1)
# bouttons
sauvegarde.grid(row=6, column=0)
reprendre.grid(row=6, column=1)
retour_en_arriere.grid(row=6, column=2)
recommencer_partie.grid(row=6, column=3)

# programme principal
creer_carre()
quadrillage()
bordure()
creer_tableau()
obstacle_mur()
repertoire_courant()
meilleur_score5()
robot1 = creer_robot(COULEUR_ROBOT1,VALEUR_ROBOT1, 1, 1)
robot2 = creer_robot(COULEUR_ROBOT2,VALEUR_ROBOT2, 1, 1)
robot3 = creer_robot(COULEUR_ROBOT3,VALEUR_ROBOT3, 1, 1)
robot4 = creer_robot(COULEUR_ROBOT4,VALEUR_ROBOT4, 1, 1)
placer_cible()
sauvegarde_initiale()

racine.mainloop()