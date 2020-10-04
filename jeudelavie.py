import numpy as np
import random

# def brokenGrid(m,n):
#     a= [0 for i in range(m)]
#     print(a)
#     for n in range(n):
#         grille.append(a)
#     print(grille)

#-----------------------------------
# def npGrid(m,n):
#     grille = np.array([[0] * m] * n)
#     return grille


#------------------------------------------
#Si on fait cell State de [0][0] on trouve bien 8, preuve que on est dans le modèle torus
# grilleTorus=[
#     [0,1,0,0,1],
#     [1,1,0,0,1],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [1,1,0,0,1]
# ]

#---------------------------------------------
# printcontenu de chaque cellule
# for list in grille:
#         for cell in list:
#             print(cell)



#----------------------------------------------------
# for ligne in grille:
#             x = len(ligne)
#             for cell in range(x):
#                 z = (grille.index(ligne),cell)
#                 print(z)




grille=[]


def vanillaGrid(m,n):
    for n in range(n):
        grille.append([random.randrange(0,2) for i in range(m)])
    

def transfoGrid(grid):
    for key in grille:
        print(key)

def cellState(y,x):
    neighborhood=int(
        grille[x-1][y-1]
        +grille[x-1][y]
        +grille[x-1][y+1]
        +grille[x][y-1]
        +grille[x][y+1]
        +grille[x+1][y-1]
        +grille[x+1][y]
        +grille[x+1][y+1]
        )


    #si x=0 : retirer les x-1
    if x == 0 : 
        neighborhood=int(
        +grille[x][y-1]
        +grille[x][y+1]
        +grille[x+1][y-1]
        +grille[x+1][y]
        +grille[x+1][y+1]
        )
    
    #si x=longueur tableau, retirer les x+1

    #si y=0 : retirer les y-1
    #si y=longueur tableau, retirer les y+1
    #si x=0 et y=0, retirer les x-1 et y-1
    #si x=longueur et y=longueur, retirer les x+1 et y+1
    #si x=longueur y=0, retirer les x+1 et y-1
    #si x=0 et y=longueur, retirer x-1 et y+1

    
    print(neighborhood)
    if (neighborhood < 2) or (neighborhood > 3):
        grille[y][x]=0
    elif neighborhood == 3:
        grille[y][x]=1
    
    
    # print(transfoGrid(grille))
   

def gridSize(grille,m,n):
    # vanillaGrid(m,n)

    grille =[
    [0,1,0,0,1],
    [1,1,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,0,0,1]
]
    
    # for list in grille:
    #     for cell in list:
    #         print(cell)
    # for m in grille:
    #     print(grille.index(m))
    #     for n in grille:
    #         print(grille.index(n))
    #         cellState(grille.index(m), grille.index(n))


    # for ligne in grille:
    #     #permet de connaître Y
    #     # print(grille.index(list))
    #     for cell in ligne:

    # cellState(
    #     grille.index
    # )


    # print(transfoGrid(grille))






def gameOfLife(grille,m,n):
    #Créer une grille : 
    grille=[]






def main():
    vanillaGrid(5,5)
    print(transfoGrid(grille))
    for ligne in grille:
            x = len(ligne)
            print(x)
            for cell in range((x)):
                z = (grille.index(ligne),cell)
                print(z)
                cellState(z[0],z[1])
    cellState(4,0)
            




    









if __name__=='__main__':
    main()


# 1 - Créer une grille rempli de nombre aléatoire entre 0 et 1, 0 = mort et 1 = vivant
# 2 - Créer une fonction qui permet de changer la valeur d'une cellule en fonction des règles du jeu de la vie 
# ATTENTION, cette fonction marche dans le modèle TORON/DONUT
# 3 - Appliquer cette règle à chacun des cellules du tableau
# 4 - Répéter autant de fois que faire se peut : BOUCLE

