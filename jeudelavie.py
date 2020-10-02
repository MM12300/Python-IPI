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
    print(grille)

# def npGrid(m,n):
#     grille = np.array([[0] * m] * n)
#     return grille

def transfoGrid(grid):
    for key in grid :
        print(key)

def cellState(x,y):

    neighborhood=int(grille[x-1][y-1]+grille[x-1][y]+grille[x-1][y+1]
                    +grille[x][y-1]+grille[x][y+1]
                    +grille[x+1][y-1]+grille[x+1][y]+grille[x+1][y+1])

    print (neighborhood)

    if (neighborhood < 2) or (neighborhood > 3):
        grille[x][y]=0
    elif neighborhood == 3:
        grille[x][y]=1
    
    return print(transfoGrid(grille))

def gridCellState(grille):
    #à appliquer la fonction cellstate à toutes les entrées du tableau
    for grille in grille:
        for i in grille:
            print (i)

    


def main():
       vanillaGrid(3,3)
       print(transfoGrid(grille))
       cellState(1,1)
       gridCellState(grille)







if __name__=='__main__':
    main()
