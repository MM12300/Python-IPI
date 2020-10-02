import numpy as np

grille=[]

def brokenGrid(m,n):
    a= [0 for i in range(m)]
    print(a)
    for n in range(n):
        grille.append(a)
    print(grille)

def vanillaGrid(m,n):
    for n in range(n):
        grille.append(['0' for i in range(m)])
    print(grille)

def npGrid(m,n):
    grille = np.array([[0] * m] * n)
    return grille

def main():
       vanillaGrid(5,5)
       grille[1][1] = "ÇA MARCHE"
       print(grille)

if __name__=='__main__':
    main()

total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255) 
  
            # apply Conway's rules 
            if grid[i, j]  == ON: 
                if (total < 2) or (total > 3): 
                    newGrid[i, j] = OFF 
            else: 
                if total == 3: 
                    newGrid[i, j] = ON 