print('hello world')

def exceptionSample():
    try:
        entier=int(a)
        print(entier)
    except Exception as e:
        print(e)




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