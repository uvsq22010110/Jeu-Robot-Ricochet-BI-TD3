import tkinter as tk

cpt = 0
continuer = True

def start():
    """Recommence le jeu du début"""
    global cpt, continuer
    cpt = 0
    continuer = True



def score() :
    #fonction qui compte le nombre de déplacement du robot 
    c=0
    for i in range(1,10001) :
        if robot1 = cible1
            c = c+1
    lbl_delai.config(text="nombre de déplacement du robot : " + str(score))



#création des boutons 
bouton = tk.Button(racine, text="Commencer", command = start)
bouton.grid()
lbl_score = tk.Label(racine, text="nombre de déplacement du robot : " + str(score))
lbl_score.grid(row=3, column=0)

racine.mainloop()
