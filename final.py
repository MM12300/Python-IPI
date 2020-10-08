import time
import os


#Creating an empty grid (list)
grille=[]
#Adding n sublist, each of lenght m
def vanillaGrid(m,n):
    grid=[]
    for n in range(n):
        grid.append([0 for i in range(m)])
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


def GameOfLife(grille, nbLignes, nbColonnes, iterations):
    grille=[]
    grille = vanillaGrid(nbLignes,nbColonnes)
    ## PARTIE 4 : oscillator
    grille[1][2]=1
    grille[2][2]=1
    grille[3][2]=1
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
        transfoGrid(grilleW)
        print("après un tour")
        grille=grilleW.copy()
        time.sleep(1)
        os.system('cls||clear')
                




def main():
    GameOfLife(grille, 5, 5, 30)
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
    