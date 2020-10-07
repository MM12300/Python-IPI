import random as random


def displayMap(map):
    for item in map:
        row = ""
        for value in item:
            row += "O " if(value) else ". "

        print(row)

    return True


grille=[]


def initMap(x, y):
    map = []
    for i in range(0, x):
        map.append([])
        for j in range(0, y):
            map[i].append(0)

    return map

def update(map):
    xmap = initMap(len(map), len(map[0]))

    for x in range(0, len(map)-1):
        for y in range(0, len(map[x])-1):
            xmap[x][y] = map[x][y]
            active = 0
            active += map[x-1][y-1]
            active += map[x-1][y]
            active += map[x-1][y+1]
            active += map[x][y-1]
            active += map[x][y+1]
            active += map[x+1][y-1]
            active += map[x+1][y]
            active += map[x+1][y+1]

            xmap[x][y] = 1 if((active == 3) or (map[x][y] and (active == 2))) else 0

    return xmap


def main():
    initMap(5,5)
    print(map)


if __name__=='__main__':
    main()