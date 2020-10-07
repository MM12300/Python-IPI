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
    vanillaGrid(5,5)
    print(grille)
    time.sleep(5)

    os.system('cls||clear')
    
    # grille[1][1]= 1
    # grille[1][1]= 1
    # grille[2][2]= 1
    # grille[2][3]= 1
    # grille[3][1]= 1
    # grille[3][2]= 1

    # grille[4][3]= 1
   
    
    print(displayMap(grille))
    
    # transfoGrid(grille)
    print("Itération : 0")

    time.sleep(1)
    
    
                      

    #Repeating the code below 30 times
    for n in range(30):
        #for each line of the grid
        for ligne, value in enumerate(grille):
            m = len(grille[0])
            grilleL= len(grille)-1
            ligneL = len(grille[0])-1
            #for each cell of the grid
            y= ligne
            print(y)
            for cell in range(m):
                #coordinates system
                x= cell

                
                neighborhood=int(
                                    grille[cap(y-1,grilleL)][cap(x-1, ligneL)]
                                    +grille[cap(y-1,grilleL)][cap(x,ligneL)]
                                    +grille[cap(y-1,grilleL)][cap(x+1,ligneL)]
                                    +grille[cap(y,grilleL)][cap(x-1, ligneL)]
                                    +grille[cap(y,grilleL)][cap(x+1,ligneL)]
                                    +grille[cap(y+1,grilleL)][cap(x-1, ligneL)]
                                    +grille[cap(y+1,grilleL)][cap(x,ligneL)]
                                    +grille[cap(y+1,grilleL)][cap(x+1,ligneL)]
                                    )
                
                time.sleep(1)
                print(y,x)


                if grille[y][x]  == 1: 
                    if (neighborhood < 2) or (neighborhood > 3): 
                        grille[y][x] = 0 
                else: 
                    if neighborhood == 3: 
                        grille[y][x] = 1
                
                #Only in this 2 cases the cell state is changing, if none of this 2 rules apply then the cell keep the same state
        time.sleep(10)
        os.system('cls||clear')
        
        print(displayMap(grille))
                # transfoGrid(grille)
        print("Itération : "+str(n+1))
        


        

if __name__=='__main__':
    main()
    