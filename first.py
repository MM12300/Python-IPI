import matplotlib.pyplot as plt


print('hello world')

# def palyndrome(chaine):


def listSample():
    l=[5,5.1,True,'coucou', 15+2j, [1,2,3]]
    print(l[0])#premier élément
    print(l[-1])#dernier élément
    print(l[5][0])#premier élément du sous tableau
    for elt in l:
        print(elt)
    print(l[0:4])#affiche une sous liste des index 1 à 3, borne exclusive

    r=list(range(100))
    print(r[0::2]) #afficher nombre pair

    m=[i for i in range(10) if i%2==0 if i<7]
    print(m)

    n=[x*x for x in [.1*i for i in range(100)]]
    #son truc de PLOT ne marche pas 
    plt.plot(n)
    plt.ylabel('test')
    plt.show()

    #CONCATENATION
    #'aaaa'+'bbbb'='aaaabbbb'

    #les chaines de caractères sont immuables
    #chaine[1]='c' INTERDIT !

    l[0]=1983
    l2=[2]*10
    l3=l+l2+[152]*2
    print('l3')
    print(l3)

def exceptionSample(a):
    try:
        entier=int(a)
        print(entier)
    except Exception as e:
        if 'int()' in str(e):
            print("Attention erreur de conversion d'entier")


def afficher(n):
    message="yo"
    # if n <= 2:
    #     print(message)
    #     print(message)
    # elif n==3:
    #     print(message)
    #     print(message)
    #     print(message)
    # else :
    #     print(message)
    
    i=0
    while i<n:
        print(message)
        i+=1
        
    for i in range(n):
        if i==6:
            #permet de passer à l'instruction suivante
            continue 
        print(i)
        if i==8:
            break
        
    


def main():
    listSample()
    exceptionSample("test")
    
    #les variables sont fortement typées mais déclarées à l'affectation et du type de leur contenu

    message="Comment vas-tu ajourd'hui ?"
    #chaine de caractères sont définis avec simple/double quotes
    #double quote peuvent contenir des simples quotes, ou inverssement
    #on peut quand même échapper avec \

    #transforme int en string
    nombreEntier=1
    message=str(nombreEntier)
    print(message)

    #transforme string en int
    msg='123456'
    inte=int(msg)
    print(inte)

    #nombreflottant
    nombreFlottant=.000001
    nombreFlottantBis=10e-15
    print(nombreFlottant)
    print(nombreFlottantBis)
    nombreFlottantTer="10.2"
    test=float(nombreFlottantTer)
    print(test)

    #Booleans
    true=bool(1)
    false=bool(0)
    print(true)
    print(false)
    

    if True:
        print('toto')
    print('How are you?')

    afficher(10)







if __name__=='__main__': 
    #cet embranchement conditionnel permet de vérifier si le programme a été lancé en exécution ou par importation
    main()