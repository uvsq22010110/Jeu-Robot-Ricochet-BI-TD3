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
# constantes

HAUTEUR = 390
LARGEUR = 600
COULEUR_FOND = "grey60"
COTE = 30
COULEUR_QUADR = "grey20"

COULEUR_FORET = "green"
COULEUR_EAU = "blue"
COULEUR_PRAIRIE = "yellow"
COULEUR_CENDRES_TIEDES = "grey80"
COULEUR_CENDRES_ETEINTES = "black"
COULEUR_FEU = "red"

# fonctions

def quadrillage():
    """Dessine un quadrillage dans le canvas avec des carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    i = 0
    while i*COTE <= LARGEUR:
        x = i*COTE
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        i += 1


# programme principal

racine = tk.Tk()
racine.title("Simulation d'une propagation d'incendie")

# création des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)

#creation des boutons

bouton_play = tk.Button(text = "PLAY", font = ("Times", "15"), bg = "white")
bouton_save = tk.Button(text = "SAVE", font = ("Times", "15"), bg = "white")
bouton_load = tk.Button(text = "LOAD", font = ("Times", "15"), bg = "white")
bouton_end = tk.Button(text = "END", font = ("Times", "15"), bg = "white")
bouton_quit = tk.Button(text = "QUIT", font = ("Times", "15"), bg = "white",command=racine.quit)

bouton_fire = tk.Button(text = "FIRE", font = ("Times", "15"), bg = "red")
bouton_water = tk.Button(text = "WATER", font = ("Times", "15"), bg = "blue")


# placement des widgets
canvas.grid(row=0)

# placement des boutons
bouton_play.grid(column = 0, row = 1)
bouton_save.grid(column = 1, row = 1)
bouton_load.grid(column = 2, row = 1)
bouton_end.grid(column = 3, row = 1)
bouton_quit.grid(column = 4, row = 1)
bouton_fire.grid(column = 0, row = 2)
bouton_water.grid(column = 1, row = 2)

# liaison des évènements
quadrillage()

racine.mainloop()