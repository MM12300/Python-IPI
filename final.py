import time
import os
import random


#Creating an empty grid (list)
grille=[]
#Adding n sublist, each of lenght m
def randomGrid(m,n):
    grid=[]
    for n in range(n):
        grid.append([random.randrange(0,2) for i in range(m)])
    return grid

def zeroGrid(m,n):
    grid=[]
    for n in range(n):
        grid.append([0 for i in range(m)])
    return grid



def transfoGrid(grid):
    for key in grid:
        print(key)    

def cap (a, array):
    L = array
    if a < 0:
        a = L
        return a
    elif a > array :
        a = 0
        return a
    else : 
        return a

def voisin3(y,x, grille):
    grilleL=len(grille)-1
    ligneL=len(grille[0])-1

    #voisinage
    NW = grille[cap(y-1, grilleL)][cap(x-1, ligneL)]
    N = grille[cap(y-1, grilleL)][cap(x, ligneL)]
    NE = grille[cap(y-1, grilleL)][cap(x+1, ligneL)]
    W = grille[cap(y, grilleL)][cap(x-1, ligneL)]
    E = grille[cap(y, grilleL)][cap(x+1, ligneL)]
    SW = grille[cap(y+1, grilleL)][cap(x-1, ligneL)]
    S = grille[cap(y+1, grilleL)][cap(x, ligneL)]
    SE = grille[cap(y+1, grilleL)][cap(x+1, ligneL)]

    neighborhood = NW + N + NE + W + E + SW + S + SE
    return neighborhood

def displayMap(map):
    for item in map:
        row = ""
        for value in item:
            row += "X " if(value) else ". "

        print(row)

def GameOfLife(grille, nbLignes, nbColonnes, iterations):
    os.system('cls||clear')
    grille=[]
    grille = randomGrid(nbLignes,nbColonnes)
    
    # ## PARTIE 4 : oscillator
    # grille[1][2]=1
    # grille[2][2]=1
    # grille[3][2]=1
    displayMap(grille)
    
    print('start')
    time.sleep(1)
    for n in range(iterations):
        grilleW = zeroGrid(nbLignes,nbColonnes)
        for indexY, value in enumerate(grille):
            y = indexY
            for cell in range(len(grille[0])):
                x = cell
                neighborhood = voisin3(y,x,grille)
                if grille[y][x] == 1 :
                    if neighborhood == 2 or neighborhood == 3:
                        grilleW[y][x] = 1
                    else:
                        grilleW[y][x] = 0
                else:
                    if neighborhood == 3:
                        grilleW[y][x] = 1
        os.system('cls||clear')
        displayMap(grilleW)
        print("après un tour")
        grille=grilleW.copy()
        time.sleep(1)
        os.system('cls||clear')



def GameOfLifeDemo(grille, nbLignes, nbColonnes, iterations):
    os.system('cls||clear')
    grille=[]
    grille = zeroGrid(nbLignes,nbColonnes)
    
    # ## PARTIE 4 : oscillator
    grille[1][15]=1
    grille[2][15]=1
    grille[3][15]=1

    #Spaceship
    grille[1][2]=1
    grille[2][3]=1
    grille[3][1]=1
    grille[3][2]=1
    grille[3][3]=1


    grille[20][20]=1
    grille[20][21]=1
    grille[20][22]=1
    grille[21][19]=1
    grille[21][18]=1
    grille[21][18]=1


    displayMap(grille)
    
    print('start')
    time.sleep(1)
    for n in range(iterations):
        grilleW = zeroGrid(nbLignes,nbColonnes)
        for indexY, value in enumerate(grille):
            y = indexY
            for cell in range(len(grille[0])):
                x = cell
                neighborhood = voisin3(y,x,grille)
                if grille[y][x] == 1 :
                    if neighborhood == 2 or neighborhood == 3:
                        grilleW[y][x] = 1
                    else:
                        grilleW[y][x] = 0
                else:
                    if neighborhood == 3:
                        grilleW[y][x] = 1
        os.system('cls||clear')
        displayMap(grilleW)
        print("Itérations : "+str(n+1))
        grille=grilleW.copy()
        time.sleep(1)
        os.system('cls||clear')
                




def main():
    # GameOfLife(grille, 10, 10, 30)
    GameOfLifeDemo(grille,25,25,30)
#     grille = vanillaGrid(5,5)


# ## PARTIE 4 : oscillator
#     grille[1][2]=1
#     grille[2][2]=1
#     grille[3][2]=1
#     transfoGrid(grille)


#     print("print état de départ")
    
#     for n in range(10):
#         grilleW = zeroGrid(5,5)
#         for indexY, value in enumerate(grille):
#             y = indexY
#             for cell in range(len(grille[0])):
#                 x = cell
#                 neighborhood = voisin3(y,x,grille)

#                 if grille[y][x] == 1 :
#                     if neighborhood == 2 or neighborhood == 3:
#                         grilleW[y][x] = 1
#                     else:
#                         grilleW[y][x] = 0
#                 else:
#                     if neighborhood == 3:
#                         grilleW[y][x] = 1
#         transfoGrid(grilleW)
#         print("après un tour")
#         grille=grilleW.copy()
#         time.sleep(1)
#         os.system('cls||clear')






if __name__=='__main__':
    main()
    