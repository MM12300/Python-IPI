import numpy as np
import random

grille=[]

# def brokenGrid(m,n):
#     a= [0 for i in range(m)]
#     print(a)
#     for n in range(n):
#         grille.append(a)
#     print(grille)

def vanillaGrid(m,n):
    for n in range(n):
        grille.append([random.randrange(0,2) for i in range(m)])
    
    # print(grille)

# def npGrid(m,n):
#     grille = np.array([[0] * m] * n)
#     return grille

def transfoGrid(grid):
    for key in grille:
        print(key)

def cellState(x,y):

    #si x=0 : retirer les x-1
    #si x=longueur tableau, retirer les x+1
    #si y=0 : retirer les y-1
    #si y=longueur tableau, retirer les y+1
    #si x=0 et y=0, retirer les x-1 et y-1
    #si x=longueur et y=longueur, retirer les x+1 et y+1
    #si x=longueur y=0, retirer les x+1 et y-1
    #si x=0 et y=longueur, retirer x-1 et y+1



    
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

    # print (neighborhood)

    if (neighborhood < 2) or (neighborhood > 3):
        grille[x][y]=0
    elif neighborhood == 3:
        grille[x][y]=1
    
    # print(transfoGrid(grille))

def gridCellState(grill,m,n):
    vanillaGrid(n,m)
    #lis chaque entrée de la grille
    for x in range(m): 
        for y in range(n): 
            cellState(x,y)

    


def main():
    gridCellState(grille,10,10)
    transfoGrid(grille)
    gridCellState(grille,10,10)
    transfoGrid(grille)
    









if __name__=='__main__':
    main()
