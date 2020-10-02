#t0 2 cas possible:
#- cellule allumée (vivante)
#   si la cellule dispose de exactement 2 cellules allumée dans son voissinage proche (8 voisines) alors elle reste allumée à t+1
#   sinon elle s'éteint 
#- cellule éteinte (morte)
#   si la cellule a 3 voisines proches allumées : elle s'allume
#   sinon elle reste éteinte


#Réaliser en programmation fonctionnelle une simulation du jeu de la vie 
#Le programme pourra être paramétré en fichier ou en argument concernant la taille de la grille (en x ou en y) et savoir si les bords de la grille sont connectés

#Les configurations de base seront stockés dans des fichiers au format :
# 5 //taille en x
# 5 //taille en y
# 0 //wrap ou non
#(1,2) //coordonnées des cellules actives
#(3,5)
#(3,3)

#L'affichage est laissé à l'appréciation
#Le format texte est encouragé 

#Bonus : 
#modifier votre programme pour permettre la description de règle différente de celles de Conway




#faire une matrice et afficher une case noire ou blanche sur la matrice 
#créer l'algo pour changer l'état des cases en fonction des voisins 
#boucler étape par étape




plotX = 10 
plotY = 10
wrap = 0 #pas de wrap, torus

cell1 = (0,0)
cell2 = (1,0)
cell3 = (0,1)

import numpy as np
def main():
    t=np.zeros((100,100),dtype=np.int32) # tableau 100x100 d'entiers mis à 0
    t2=t.copy() # Réalise une copie du tableau t (alors qu'une simple affectation ajouterait simplement une référence)
    t2.shape # Tuple de deux valeurs indique la taille de t2



ON = 255
OFF = 0
vals = [ON, OFF] 
def randomGrid(N): 
  
    # """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N) 

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

if __name__ == '__main__': 
    randomGrid(10)