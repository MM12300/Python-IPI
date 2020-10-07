import random
import os
import time
import numpy as np

#Creating an empty grid (list)
grille=[]

#Adding n sublist, each of lenght m
def vanillaGrid(m,n):
    for n in range(n):
        grille.append([0 for i in range(m)])
    return grille
  
def displayMap(map):
    for item in map:
        row = ""
        for value in item:
            row += "X " if(value) else ". "

        print(row)

    return "Conway Game of Life"


#Function to calculate if our coordinates in the grid are out of index
#=====> we use indexes to identify our cells in the grid, grid[listIndex][sublistIndex] is used as a coordinates system
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
    #Creating a grid
    vanillaGrid(10,10)

    os.system('cls||clear')
    
    grille[1][1]= 1
    grille[2][1]= 1
    grille[3][1]= 1
   
    
    print(displayMap(grille))
    
    # transfoGrid(grille)
    print("Itération : 0")

    time.sleep(1)
    
    
                      

    #Repeating the code below 30 times
    for n in range(30):
        #assigning 0 and 1 values in order to calcul how many cells in the neighbourhood of the actual cell
        #cleaning the fancier display we will do at the end of the loop
        for ligne in grille:
            for cell in range(10):
                y= grille.index(ligne)
                x= cell
                if grille[y][x] == ".":
                    grille[y][x] = 0
                elif grille[y][x] == "X":
                    grille[y][x] = 1

        #for each line of the grid
        for ligne in grille:
            m = len(ligne)
            grilleL= len(grille)-1
            ligneL = len(ligne)-1
            #for each cell of the grid
            for cell in range(10):
                #coordinates system
                y= grille.index(ligne)
                x= cell
                #how many cell in our neighborhood, at the following coordinates and we used our function cap() to go to the other side of the grid in cases of cells at the edges
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
                
                if grille[y][x]  == 1: 
                    if (neighborhood < 2) or (neighborhood > 3): 
                        grille[y][x] = 0 
                else: 
                    if neighborhood == 3: 
                        grille[y][x] = 1
                
                #Only in this 2 cases the cell state is changing, if none of this 2 rules apply then the cell keep the same state
        os.system('cls||clear')
        
        print(displayMap(grille))
                # transfoGrid(grille)
        print("Itération : "+str(n+1))
        time.sleep(1)


        

if __name__=='__main__':
    main()
    