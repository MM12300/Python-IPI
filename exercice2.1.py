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
    print(new)
    book={"Fiche1" : [new]}
    print(book)

if __name__=='__main__':
    subscribe()
