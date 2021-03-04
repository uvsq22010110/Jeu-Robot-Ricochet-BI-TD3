##################################
# Groupe 1  de BI TD3

# Auters: 
# Coraline PELON
# Jacques-Henri Lartigue 
# Nojimba Ahamada
# Alice Dumontroty
# Mathieu Chekroun
# Desira Junior Ebelebe
# lien du github: https://github.com/uvsq22010110/Projet_Incendie.git


# import des modules

import tkinter as tk
import random
#Initialisation

tableau = None

cases = []

# constantes

HAUTEUR = 390
LARGEUR = 600
COULEUR_FOND = "grey60"
COTE = 30
COULEUR_QUADR = "grey20"

NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

COULEUR_FORET = "green"
COULEUR_EAU = "blue"
COULEUR_PRAIRIE = "yellow"
COULEUR_CENDRES_TIEDES = "grey80"
COULEUR_CENDRES_ETEINTES = "black"
COULEUR_FEU = "red"
COULEUR_ELEM = ["yellow", "blue", "green"]
# fonctions

def quadrillage():
    """Affiche un quadrillage sur le canvas."""
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADR)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADR)
        x += COTE
        
def coord_to_lg(x, y):
    """Fonction qui retourne la colonne et la ligne du quadrillage
    à partir des coordonnées x et y"""
    return x // COTE, y // COTE        

def feu(event):
    """Mettre feu au carré sur lequel on a cliqué"""
    i, j = coord_to_lg(event.x, event.y)
    if tableau[i][j] == -1:
        x, y = i * COTE, j * COTE
        carre = canvas.create_rectangle(x, y, x + COTE,
                                        y + COTE, fill=COULEUR_FEU,
                                        outline=COULEUR_QUADR)
        tableau[i][j] = carre

def creer_tableau():
    """initialise un tableau à deux dimensions qui vaut -1 partout
    -1 est pour une case morte
    identifiant du carré dessiné si une case est vivante
    tableau[i][j] est la valeur de la case à la colonne i et la ligne j
    """
    global tableau
    tableau = []
    for i in range(NB_COL):
        tableau.append([-1] * NB_LINE)

def load_map():
    """Chargement du terrain"""
    for i in range(COTE):
        for j in range(COTE):
            x, y = i * COTE, j * COTE
            carre = canvas.create_rectangle(x, y, x + COTE, y + COTE, fill = random.choice(COULEUR_ELEM), outline=COULEUR_QUADR)

        
# programme principal

racine = tk.Tk()
racine.title("Simulation d'une propagation d'incendie")

# création des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)

#creation des boutons

bouton_play = tk.Button(text = "PLAY", font = ("Times", "15"), bg = "white")
bouton_save = tk.Button(text = "SAVE", font = ("Times", "15"), bg = "white")
bouton_load = tk.Button(text = "LOAD", font = ("Times", "15"), bg = "white", command = load_map)
bouton_end = tk.Button(text = "END", font = ("Times", "15"), bg = "white")
bouton_quit = tk.Button(text = "QUIT", font = ("Times", "15"), bg = "white",command=racine.quit)

#
#bouton_fire = tk.Button(text = "FIRE", font = ("Times", "15"), bg = "red")
#bouton_water = tk.Button(text = "WATER", font = ("Times", "15"), bg = "blue")
#bouton_forest = tk.Button(text = "FOREST", font = ("Times", "15"), bg = "green")
#


bouton_fire = tk.Button(text = "FIRE", font = ("Times", "15"), bg = "red")
bouton_water = tk.Button(text = "WATER", font = ("Times", "15"), bg = "blue")
bouton_forest = tk.Button(text = "FOREST", font = ("Times", "15"), bg = "green")


# placement des widgets
canvas.grid(row=0)

# placement des boutons
bouton_play.grid(column = 0, row = 1)
bouton_save.grid(column = 1, row = 1)
bouton_load.grid(column = 2, row = 1)
bouton_end.grid(column = 3, row = 1)
bouton_quit.grid(column = 4, row = 1)
#bouton_fire.grid(column = 0, row = 2)
#bouton_water.grid(column = 1, row = 2)
#bouton_forest.grid(column = 2, row = 2)

#Assignation des commandes aux touches du clavier ou souris
canvas.bind("<Button-1>", feu)



# liaison des évènements
quadrillage()
creer_tableau()
racine.mainloop()
