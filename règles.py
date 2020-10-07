#Creating an empty grid (list)
grille=[]

#Adding n sublist, each of lenght m
def vanillaGrid(m,n):
    for n in range(n):
        grille.append(["." for i in range(m)])
    return grille
  
def main():
    vanillaGrid(5,5)
    print(grille)
    grille[1][1] = "TEST"
    print(grille)

    for ligne in grille:
        print (ligne)
        print(grille.index(ligne))

        chars = ['A', 'B', 'C']
 
    for index, value in enumerate(grille):
        y = index
        for cell in range(5):
            x = cell
            print(y,x)


if __name__=='__main__':
    main()
    