book={}

def nouvelleFiche(vNom, vAge, vFonction, vTel, vMail, vAdresse):
    return { 
    "nom": vNom,
    "age": vAge,
    "fonction": vFonction,
    "tel": vTel,
    "mail": vMail,
    "adresse": vAdresse }
    




def test():
    print(nouvelleFiche("Michel", "15", "test", "0565432546", "sfsddf@gmail.com", "31400 Toulouse"))


def subscribe():
    name= input("Nom ?")
    age = input("Age?")
    fonction = input("fonction?")
    tel = input("tel?")
    mail = input("mail?")
    adresse = input("adresse?")

    new = nouvelleFiche(name, age, fonction,tel,mail,adresse)
    print("resultat: FICHE")
    print(new)
    book={"Fiche1" : [new]}
    print("resultat: BOOK")
    print(book)

    # print(book.get("Fiche1"))

    # print(findFile('Fiche1'))
    print("resultat: FIND")
    findFile(book, "Fiche1")
    print("resultat: FIND key value")
    findKeyValue(book, name, "Michel")

    

def findFile(array, key):
    research=array.get(key)
    return print(research)

def findKeyValue(array, key, value):
    for key, value in array.items():
        print(key, value)

def questionNom():
    file = input("Qui cherchez-vous (nom) ?")
    findFile(book, file)

def questionFile():
    file = input("Qui cherchez-vous (nom) ?")
    findFile(book, file)

def questionClefValue():
    clef = input("type information recherchée")
    valeur = input("valeur de l'information recherchée")
    findKeyValue(book, clef, valeur)


def dispMenu():
    menu = [
		"C. Créer une nouvelle",
		"A. Afficher la fiche correspondante à un nom donné",
		"V. Fiches ayant une valeur donnée pour un champ donné",
		"S. Fiches qui satisfont le critère donné",
		"Q. Quitter ce programme",
	]
    print(menu)
    choice = input("Choix :")
    if choice == "C":
        subscribe
    elif choice == "A":
        questionNom
    elif choice == "V":
        questionClefValue

    # elif choix == "S":

    # elif choix == "Q":



if __name__=='__main__':
    dispMenu()
