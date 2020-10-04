import numpy as np
import random

# def brokenGrid(m,n):
#     a= [0 for i in range(m)]
#     print(a)
#     for n in range(n):
#         grille.append(a)
#     print(grille)

# def npGrid(m,n):
#     grille = np.array([[0] * m] * n)
#     return grille


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
    #si x=longueur tableau, retirer les x+1
    #si y=0 : retirer les y-1
    #si y=longueur tableau, retirer les y+1
    #si x=0 et y=0, retirer les x-1 et y-1
    #si x=longueur et y=longueur, retirer les x+1 et y+1
    #si x=longueur y=0, retirer les x+1 et y-1
    #si x=0 et y=longueur, retirer x-1 et y+1

    
    neighborhood=3
    print(neighborhood)
    if (neighborhood < 2) or (neighborhood > 3):
        grille[y][x]=0
    elif neighborhood == 3:
        grille[y][x]=1
    
    
    # print(transfoGrid(grille))
   

def gridSize(grille,m,n):
    vanillaGrid(m,n)
    for list in grille:
        for cell in list:
            print(cell)
    for m in grille:
        print(grille.index(m))
        for n in grille:
            print(grille.index(n))
            cellState(grille.index(m), grille.index(n))

 


def main():
    vanillaGrid(5,5)
    print(transfoGrid(grille))
    cellState(3,1)
    print(transfoGrid(grille))
    









if __name__=='__main__':
    main()
