import random
grille=[]

def vanillaGrid(m,n):
    for n in range(n):
        grille.append([random.randrange(0,2) for i in range(m)])

def transfoGrid(grid):
    for key in grille:
        print(key)


def cap (a, arrayL):
    if a < 0 :
        a = arrayL
        return a
    elif a > arrayL :
        a = 0
        return a
    else : 
        return a


def main():
    vanillaGrid(5,5)
    print(transfoGrid(grille))
    for ligne in grille:
        m = len(ligne)
        grilleL= len(grille)-1
        ligneL = len(ligne)-1

        for cell in range(m):
            y= grille.index(ligne)
            x= cell
            z = (y,x)    
  
            neighborhood=int(
                                grille[cap(x-1,ligneL)][cap(y-1, grilleL)]
                                +grille[cap(x-1,ligneL)][cap(y,grilleL)]
                                +grille[cap(x-1,ligneL)][cap(y+1,grilleL)]
                                +grille[cap(x,ligneL)][cap(y-1, grilleL)]
                                +grille[cap(x,ligneL)][cap(y+1,grilleL)]
                                +grille[cap(x+1,ligneL)][cap(y-1, grilleL)]
                                +grille[cap(x+1,ligneL)][cap(y,grilleL)]
                                +grille[cap(x+1,ligneL)][cap(y+1,grilleL)]
                                )
            
            if (neighborhood < 2) or (neighborhood > 3):
                #dead
                grille[y][x]=0
            elif neighborhood == 3:
                #alive
                grille[y][x]=1
    print(transfoGrid(grille))

if __name__=='__main__':
    main()