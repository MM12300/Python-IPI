#Creating an empty grid (list)
grille=[]

#Adding n sublist, each of lenght m
def vanillaGrid(m,n):
    for n in range(n):
        grille.append([0 for i in range(m)])
    return grille

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
  
def main():
    vanillaGrid(5,5)

    ligneL=len(grille[0])-1
    grilleL=len(grille)-1
    print(ligneL)
    print(grilleL)


    for ligne in grille :
        print(ligne)
 
    for index, value in enumerate(grille):
        y = index
        for cell in range(5):
            x = cell
            

            neighborhood=int(grille[cap(y-1,grilleL)][cap(x-1, ligneL)])+int(grille[cap(y-1,grilleL)][cap(x,ligneL)])+int(grille[cap(y-1,grilleL)][cap(x+1,ligneL)])+int(grille[cap(y-1,grilleL)][cap(x+1,ligneL)])+int(grille[cap(y,grilleL)][cap(x-1, ligneL)])+int(grille[cap(y,grilleL)][cap(x+1,ligneL)])+int(grille[cap(y+1,grilleL)][cap(x-1, ligneL)])+int(grille[cap(y+1,grilleL)][cap(x,ligneL)])+int(grille[cap(y+1,grilleL)][cap(x+1,ligneL)])
            print(y,x)
            print(neighborhood)
            if grille[y][x]  == 1: 
                    if (neighborhood < 2) or (neighborhood > 3): 
                        grille[y][x] = 0 
            else: 
                if neighborhood == 3: 
                    grille[y][x] = 1

if __name__=='__main__':
    main()
    