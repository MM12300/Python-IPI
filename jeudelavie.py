def gridDesign(m,n):
    a = [0 for i in range(m)]
    b = [a for x in range(n)]
    for key in b:
        print(key)


def main(): 
    gridDesign(5,5)

if __name__=='__main__':
    main()


# def makeArray(x):
#     a = [0 for i in range(x)]
#     # print(array)

# def makeGrid(y):
#     a=makeArray(6)
#     return [a for j in range(y)]

# def afficheGrid(a):
#     for key in a:
#         print(key)

# def main():
#     grid=makeGrid(6)
#     afficheGrid(grid)


