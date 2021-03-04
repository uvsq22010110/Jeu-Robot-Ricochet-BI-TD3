##################################
# Groupe 1  de BI TD3

# Auters: 
# Coraline PELON
# Jacques-Henri Lartigue 
# Nojimba Ahamada
# ALice Dumontroty
# Mathieu Chekroun
# Desira Junior Ebelebe
# lien du github: https://github.com/uvsq22010110/Projet_Incendie.git


# import des modules

import tkinter as tk


# constantes

HAUTEUR = 400
LARGEUR = 600
COULEUR_FOND = "grey60"
COTE = 30
COULEUR_QUADR = "grey20"

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


# prgramme principal

racine = tk.Tk()
racine.title("Simulation d'une propagation d'incendie")

# création des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)

# placement des widgets
canvas.grid(row=0)

# liaison des évènements
quadrillage()

racine.mainloop()