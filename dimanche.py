import random
import os
import time

#Création d'une grille vierge
grille=[]

#ajout de n sous tableau, chacun de longueur m
def vanillaGrid(m,n):
    for n in range(n):
        grille.append([random.randrange(0,2) for i in range(m)])
    return grille

#gère l'affiche, fait un print de chaque ligne du tableau dans la console
def transfoGrid(grid):
    for key in grid:
        print(key)

#permet de calculer les coordonnées quand on atteint des valeurs qui sortent du tableau
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
    #Création grille
    vanillaGrid(10,10)

    #Itération : 30
    for n in range(30):

        #pour chaque ligne dans la grille
        for ligne in grille:
            m = len(ligne)
            grilleL= len(grille)-1
            ligneL = len(ligne)-1
            #pour chaque cellule dans la grille
            for cell in range(m):
                y= grille.index(ligne)
                x= cell

                if grille[y][x] == ".":
                    grille[y][x] = 0
                elif grille[y][x] == "X":
                    grille[y][x] = 1



                # z sont nos coordonnées
                # z = (y,x)    

                #calcul la somme de cellule dans le voisinage
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
                #si - de 2 cellule ou +3 cellule : dead
                if (neighborhood < 2) or (neighborhood > 3):
                    #dead
                    grille[y][x]=0
                #si 3 cellule exactement : alive
                elif neighborhood == 3:
                    #alive
                    grille[y][x]=1
                
                #Autrement on touche pas

        #affichage de la grille
        transfoGrid(grille)

        #test
        for ligne in grille:
            for cell in range(m):
                y= grille.index(ligne)
                x= cell
                if grille[y][x] == 0:
                    grille[y][x] = "mort"
                elif grille[y][x] == 1:
                    grille[y][x] = "vivant"
        
        transfoGrid(grille)


        #1 sec entre chaque affichage
        time.sleep(1)
        #nettoyage de la console
        
                    
        os.system('cls||clear')
        

if __name__=='__main__':
    main()
    