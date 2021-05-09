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
liste_couleur = ["red", "green", "blue", "yellow"]


# fonctions
def quadrillage():
    """Dessine un quadrillage sur le canva"""
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
    """Retourne les coordonnées"""
    return x // COTE, y // COTE        

def creer_tableau():
    """Récupère les valeurs des cases en les plaçants dans un tableau"""
    global tableau
    n = LARGEUR // COTE
    tableau = [[0] * n for i in range(n)]
    # initialisation des celulles de la bordure 
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

   
def creer_carre():
    "dessine caree"
    i = 16 // 2
    j = 16 // 2 + 1
    carre = canvas.create_rectangle((COTE*(i - 1), COTE*(i - 1)), (COTE*j, COTE*j), fill = "black")


def creer_robot(couleur_robot, valeur_robot):
    "dessine robot"
    # on cherche une case vide
    occupe = 20
    i = 1
    j = 1
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
    print(i,j)
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
    valeur_robot = 0
    # est dans le robot rouge
    if x0 <= clic_x <= x1 and y0 <= clic_y <= y1:
        print("Tu as cliqué sur le robot rouge")
        robot = robot1
        valeur_robot = VALEUR_ROBOT1
        x = int(x0 // COTE)
        y = int(y0 // COTE)
        selection = True
    # est dans le robot vert
    elif x2 <= clic_x <= x3 and y2 <= clic_y <= y3:
        print("Tu as cliqué sur le robot vert")
        robot = robot2
        valeur_robot = VALEUR_ROBOT2
        x = int(x2 // COTE)
        y = int(y2 // COTE)
        selection = True
    # est dans le robot bleu
    elif x4 <= clic_x <= x5 and y4 <= clic_y <= y5:
        print("Tu as cliqué sur le robot blue")
        robot = robot3
        valeur_robot = VALEUR_ROBOT3
        x = int(x4 // COTE)
        y = int(y4 // COTE)
        selection = True
    # est dans le robot jaune
    elif x6 <= clic_x <= x7 and y6 <= clic_y <= y7:
        print("Tu as cliqué sur le robot jaune")
        robot = robot4
        valeur_robot = VALEUR_ROBOT4
        x = int(x6 // COTE)
        y = int(y6 // COTE)
        selection = True
    else:
        selection = False
    return selection, valeur_robot


def clavier(event):
    """sert à déplacer les robots graces aux touches du clavier"""
    global selection, valeur_robot, cible
    touche = event.keysym # pour pouvoir reccuperer la touche appuyee
    if selection == True:
        x8, y8, x9, y9 = canvas.coords(robot[0])
        if touche == "Up":
            stop = 0
            k = 0 # constante
            monte = 0 # case de fin
            depart = int(y8 // COTE) # case de depart
            while stop == 0:
                i = int(x8 // COTE)
                j = int(y8 // COTE) - k
                valeur = tableau[i][j]
                valeur_depart = tableau[i][depart]
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
                    else:
                        stop = 1
                        j = j - 1
                monte = j
            print(monte-depart)
            canvas.move(robot[0], 0, ((monte-depart)*COTE))
            if (monte - depart) < 0:
                tableau[i][j] = valeur + valeur_robot
                tableau[i][depart] = valeur_depart - valeur_robot
                if tableau[i][j] > 100:
                    #faire disparraitre la cible lorsqu'elle est atteinte
                    canvas.delete(cible)
                    # pour remettre la valeur
                    tableau[i][j] = tableau[i][j] - (valeur_robot*10)
                    print("gagné")
            print("valeur départ",tableau[i][depart])
            print("valeur arrivée",tableau[i][j])
        
        elif touche == "Down":
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
                        j = j - 1
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
                    else:
                        stop = 1
                        j = j - 1
                descends = j
            print(descends-depart)
            canvas.move(robot[0], 0, ((descends-depart)*COTE))
            if (descends - depart) > 0:
                tableau[i][j] = valeur + valeur_robot
                tableau[i][depart] = valeur_depart - valeur_robot
                if tableau[i][j] > 100:
                    # faire disparraitre la cible lorsqu'elle est atteinte
                    canvas.delete(cible)
                    # remettre la valeur de la case initiale sans la cible
                    tableau[i][j] = tableau[i][j] - (valeur_robot*10)
                    print("gagné")
            print("valeur départ",tableau[i][depart])
            print("valeur arrivée",tableau[i][j])
             
        elif touche == "Right":
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
                    else:
                        stop = 1
                        i = i - 1
                droite = i
            print(droite-depart)
            canvas.move(robot[0], ((droite-depart)*COTE), 0)
            if (droite - depart) > 0:
                tableau[i][j] = valeur + valeur_robot
                tableau[depart][j] = valeur_depart - valeur_robot
                if tableau[i][j] > 100:
                    # faire disparraitre la cible lorsqu'elle est atteinte
                    canvas.delete(cible)
                    tableau[i][j] = tableau[i][j] - (valeur_robot*10)
                    print("gagné")
            print("valeur départ",tableau[depart][j])
            print("valeur arrivée",tableau[i][j])

        elif touche == "Left":
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
                # si le robot atteri dans la bonne cible
                elif (valeur>100):
                    if (valeur == valeur_robot*10+5) or (valeur == valeur_robot*10+7):
                        stop = 1
                    else:
                        stop = 1
                        i = i + 1
                gauche = i
            print(gauche-depart)
            canvas.move(robot[0], ((gauche-depart)*COTE), 0)
            if (gauche - depart) < 0:
                tableau[i][j] = valeur + valeur_robot
                tableau[depart][j] = valeur_depart - valeur_robot
                if tableau[i][j] > 100:
                    # faire disparraitre la cible lorsqu'elle est atteinte
                    canvas.delete(cible)
                    tableau[i][j] = tableau[i][j] - (valeur_robot*10)
                    print("gagné")
            print("valeur départ",tableau[depart][j])
            print("valeur arrivée",tableau[i][j])


def bordure():
    """creation bordures"""
    mur1 = canvas.create_line(4,4,4,LARGEUR, fill='black', width = '4')
    mur2 = canvas.create_line(4,4,LARGEUR,4, fill='black', width = '4') 
    mur3 = canvas.create_line(LARGEUR,0,LARGEUR,LARGEUR, fill='black', width = '4')
    mur4 = canvas.create_line(0,LARGEUR,LARGEUR,LARGEUR, fill='black', width = '4')


def creer_cible():
    """dessine cible"""
    x = rd.randint(1,14)
    y = rd.randint(1,14)
    color = rd.choice(liste_couleur)   
    x,y = x*COTE, y*COTE
    cible = canvas.create_rectangle((x, y), (x+COTE, y+COTE), fill = color) #(#liste_couleur[i])
    return cible

# Exemple pour JH
#def angle_L():
    #i = rd.randint(1,14)
    #j = rd.randint(1,14)
    #canvas.create_line(i*COTE,j*COTE,(i+1)*COTE,j*COTE, width = 5 , fill = "black")
    #canvas.create_line(i*COTE,j*COTE,i*COTE,(j+1)*COTE, width = 5 , fill = "black")
    #tableau[i][j] = 5

# Exemple pour Nojimba
#def mur():
    #i = rd.randint(1,15)
    #j = 0
    #mur = canvas.create_line(i*COTE,j*COTE,iCOTE,(j+1)*COTE, fill='black', width = '4')
    #tableau[i][j] = 4

# programme principal
racine = tk.Tk()
racine.title("Jeu du Robot-Ricochet")

# création des widgets
canvas = tk.Canvas(racine, width= LARGEUR, height= HAUTEUR, bg= "navajo white")

# liaison des événements
canvas.bind("<Button-1>", est_dans_le_robot)
racine.bind("<Key>", clavier)

# placement des widgets
canvas.grid()

# programme principal
creer_carre()
quadrillage()
creer_cible()
bordure()
creer_tableau()
#angle_L()
#mur()

robot1 = creer_robot(COULEUR_ROBOT1,VALEUR_ROBOT1)
robot2 = creer_robot(COULEUR_ROBOT2,VALEUR_ROBOT2)
robot3 = creer_robot(COULEUR_ROBOT3,VALEUR_ROBOT3)
robot4 = creer_robot(COULEUR_ROBOT4,VALEUR_ROBOT4)

print(tableau)

racine.mainloop()