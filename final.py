import time


#Creating an empty grid (list)
grille=[]


#Adding n sublist, each of lenght m
def vanillaGrid(m,n):
    for n in range(n):
        grille.append([1 for i in range(m)])
    return grille

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

def voisin(y,x):
    #voisinage
    NW = grille[y-1][x-1]
    N = grille[y-1][x]
    NE = grille[y-1][x+1]
    W = grille[y][x-1]
    E = grille[y][x+1]
    SW = grille[y+1][x-1]
    S = grille[y+1][x]
    SE = grille[y+1][x+1]

    neighborhood = NW + N + NE + W + E + SW + S + SE
    return print(neighborhood)
  
def voisin2(y,x, grille):
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
    return print(neighborhood)


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


def voisin4(y,x, indexM):

    #voisinage
    NW = grille[cap(y-1, indexM)][cap(x-1, indexM)]
    N = grille[cap(y-1, indexM)][cap(x, indexM)]
    NE = grille[cap(y-1, indexM)][cap(x+1, indexM)]
    W = grille[cap(y, indexM)][cap(x-1, indexM)]
    E = grille[cap(y, indexM)][cap(x+1, indexM)]
    SW = grille[cap(y+1, indexM)][cap(x-1, indexM)]
    S = grille[cap(y+1, indexM)][cap(x, indexM)]
    SE = grille[cap(y+1, indexM)][cap(x+1, indexM)]

    neighborhood = NW + N + NE + W + E + SW + S + SE
    return neighborhood


def main():
    vanillaGrid(5,5)

    print("Création de la grille")
    print(grille)

    print("Index [Y] maximum")
    grilleL=len(grille)-1
    print(grilleL)

    print("Index [X] maximum")
    ligneL=len(grille[0])-1
    print(ligneL)
    
    print("test de cap sur grilleL")
    print("Cap de 0-1 renvoit bien 4, soit la longueur max du tableau")
    print(cap(0-1, grilleL))

    print("Cap de 2 renvoit bien 2, car 2<4")
    print(cap(2, grilleL))

    print("Cap de 0 renvoit bien 2, car 4+1 > L tableau")
    print(cap(4+1, grilleL))

    # time.sleep(100)

    



    print("coordonnées de la grille")
    for indexY, value in enumerate(grille):
        y = indexY
        for cell in range(len(grille[0])):
            x = cell
            print(y,x)

    
    # time.sleep(100)
    


    ####### PARTIE 1
    # grille[2][2]= 1
    # print(grille[2][2])
    # print("une grille de 5 par 5 avec un ensemble de 1 au centre")
    # transfoGrid(grille)




    ##### PARTIE 2
    # grille[1][1]=1
    # grille[1][2]=1
    # grille[1][3]=1
    # grille[2][1]=1
    # grille[2][3]=1
    # grille[3][1]=1
    # grille[3][2]=1
    # grille[3][3]=1

    # print("une grille de 5 par 5 avec des nouveaux voisins")
    # transfoGrid(grille)

   
    # print("le voisinage est bien de 8")
    # voisin2(2,2, grille)




##### PARTIE 3
    # grille[0][0]=1
    # grille[0][1]=1
    # grille[3][4]=1
    # grille[4][4]=1
    # grille[3][0]=1
    # grille[3][1]=1
    # grille[4][1]=1
    # grille[0][4]=1


    # print("voisinage d'une cellule en coin")
    # transfoGrid(grille)
    # voisin2(4,0, grille)
    # print("on a bien 8 donc l'hypothèse d'un wrap fonctionnel est confirmé")




### PARTIE 4 : oscillator
    # grille[1][2]=1
    # grille[2][2]=1
    # grille[3][2]=1
    transfoGrid(grille)


    print("print état de départ")
    
    for n in range(1):
        for indexY, value in enumerate(grille):
            y = indexY
            for cell in range(len(grille[0])):
                x = cell
                neighborhood = voisin4(y,x,4)
                print(y,x)
                print(neighborhood)

                if grille[y][x] == 1 :
                    if neighborhood == 2 or neighborhood == 3:
                        grille[y][x] = 1
                    else:
                        grille[y][x] = 0
                else:
                    if neighborhood == 3:
                        grille[y][x] = 1
        transfoGrid(grille)
        print("après un tour")




if __name__=='__main__':
    main()
    