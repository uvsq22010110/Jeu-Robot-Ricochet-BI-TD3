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

# constantes


# programme principal

racine = tk.Tk()
racine.title("Jeu des robots")

# création des widgets
canvas = tk.Canvas(racine, width= 640, height= 640, bg= "black")
canvas.grid()

racine.mainloop()