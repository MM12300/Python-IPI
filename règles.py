if (neighborhood < 2) or (neighborhood > 3):
                    #dead
                    grille[y][x]=0
                #if exactly 3 cells in the neighborhood, the cell is alive
                elif grille[y][x]==0:
                    elif neighborhood == 3:
                        #alive
                        grille[y][x]=1