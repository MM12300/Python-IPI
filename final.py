#Creating an empty grid (list)
grille=[]

#Adding n sublist, each of lenght m
def vanillaGrid(m,n):
    for n in range(n):
        grille.append([0 for i in range(m)])
    return grille

def transfoGrid(grid):
    for key in grid:
        print(key)    

def cap (a, arrayL):
    #if index is <0 then we go to the other side of the grid : maximum index
    if a < 0 :
        a = arrayL
        return a
    #if index is > to the length of the sublist then we go to the other side of the grid : index [0]
    elif a > arrayL :
        a = 0
        return a
    #in all other cases : value of index doesn't change
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
  

def cap ():pass


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


    print("coordonnées de la grille")
    for indexY, value in enumerate(grille):
        y = indexY
        for cell in range(len(grille[0])):
            x = cell
            print(y,x)
    
    grille[2][2]= 1
    print(grille[2][2])
 
   

    print("une grille de 5 par 5 avec un ensemble de 1 au centre")
    transfoGrid(grille)


    grille[1][1]=1
    grille[1][2]=1
    grille[1][3]=1
    grille[2][1]=1
    grille[2][3]=1
    grille[3][1]=1
    grille[3][2]=1
    grille[3][3]=1

    print("une grille de 5 par 5 avec des nouveaux voisins")
    transfoGrid(grille)

    voisin(2,2)









    # for ligne in grille :
    #     print(ligne)
 
    # for index, value in enumerate(grille):
    #     y = index
    #     for cell in range(5):
    #         x = cell
            

    #         neighborhood=int(grille[cap(y-1,grilleL)][cap(x-1, ligneL)])+int(grille[cap(y-1,grilleL)][cap(x,ligneL)])+int(grille[cap(y-1,grilleL)][cap(x+1,ligneL)])+int(grille[cap(y-1,grilleL)][cap(x+1,ligneL)])+int(grille[cap(y,grilleL)][cap(x-1, ligneL)])+int(grille[cap(y,grilleL)][cap(x+1,ligneL)])+int(grille[cap(y+1,grilleL)][cap(x-1, ligneL)])+int(grille[cap(y+1,grilleL)][cap(x,ligneL)])+int(grille[cap(y+1,grilleL)][cap(x+1,ligneL)])
    #         print(y,x)
    #         print(neighborhood)
    #         if grille[y][x]  == 1: 
    #                 if (neighborhood < 2) or (neighborhood > 3): 
    #                     grille[y][x] = 0 
    #         else: 
    #             if neighborhood == 3: 
    #                 grille[y][x] = 1

if __name__=='__main__':
    main()
    