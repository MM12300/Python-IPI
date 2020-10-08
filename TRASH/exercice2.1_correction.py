def nouvelleFiche(nom='',age='',fonction='',tel='',mail='',adresse='') :
    return {'nom':nom,'age':age,'fonction':fonction,'tel':tel,'mail':mail,'adresse':adresse}
    
# Fonction d'affichage d'une fiche du carnet d'adresse suivant
# le format décrit dans le sujet :
# Nom du Champ\t|\tValeur du champ 
# ---------------------------------
# champ1\t|\tval1\n
def afficherFiche(fiche,afficheEntete):
    
    print("Nom du Champ\t| Valeur du champ\n"*afficheEntete+"----------------|----------------");
    for key in fiche:
        print(key+'\t'*(len(key)<=7)+'\t|\t'+str(fiche[key]))
    
# Fonction permettant de saisir une chaîne de caractères 
# sans dépasser une certaine limite et en affiche un message
def saisieTexte(message,limite):
    texte=input(message)
    while len(texte)>limite:
        texte=input('Attention, limite du texte à '+str(limite)+' caractères!\n'+message)
    return(texte)
# Fontion permettant la saisie d'un entier entre deux bornes
# après avoir affiché un message
def saisieEntier(message,bI,bS):
    try :
        entier=int(input(message))
    except Exception:
        print('Attention, seuls les nombres entiers sont acceptés')
        return(saisieEntier(message,bI,bS))
    if bI>entier or entier>bS:
        print('Attention, les entiers acceptés doivent être bornés par '+str(bI)+' et '+str(bS))
        return(saisieEntier(message,bI,bS))
    else:
        return entier
    
# Fonction créant une fiche saisie et l'insérant dans un 
# carnet passé en paramètre.
def creationInsertionFiche(carnet):
    fiche=nouvelleFiche(saisieTexte('Nom?\n',5),saisieEntier('Âge?\n',0,200),saisieTexte('Mail?\n',10),'0'+str(saisieEntier('Tel?\n',100000000,599999999)),saisieTexte('Mail?\n',100),saisieTexte('Adresse?\n',50))
    carnet+=[fiche]
    return carnet
    
def rechercheChamp(nomChamps,valChamps,carnet):
    if nomChamps not in carnet[0]:
        print('La fiche ayant pour valeur '+nomChamps+'='+valChamps+' n\'existe pas')
        return 
    entete=True
    for fiche in carnet:
        if fiche[nomChamps]==valChamps:
            afficherFiche(fiche,entete)
            entete=False
def affichageMenu():
    print("""Menu
\tC\t\t\t\tCréer une nouvelle fiche
\tA\tnom\t\t\tAfficher par rapport à un nom
\tV\tchamps\tval\t\tAfficher par rapport à un couple champs/val
\tQ\t\t\t\tQuitter
Votre choix?""")
# Surcharge de la fonction saisieTexte permettant de limiter 
# les valeur conformes
def saisieTexteL(message,limite,listeChoix):
    texte=input(message)
    while len(texte)>limite or texte.lower() not in listeChoix:
        alerteTaille='limite du texte à '+str(limite)+' caractères!'
        alerteChoix='choix non conforme : '+str(listeChoix)
        texte=input('Attention, '+alerteTaille*(len(texte)>limite)+', '+alerteChoix*(texte not in listeChoix)++'\n'+message)
    return(texte)
def menu(carnet):
    choix=saisieTexteL('',1,['c','a','v','q']).upper()
    if choix=='C':
        carnet=creationInsertionFiche(carnet)
    elif choix=='A':
        rechercheChamp('nom',saisieTexte('Nom?\n',10),carnet)
    elif choix=='V':
        rechercheChamp(saisieTexteL('Champs?',10,nouvelleFiche().keys()),saisieTexte('Nom?\n',10),carnet)
    elif choix=='Q':
        return False
    return True
def main():
    carnet=[]
    affichageMenu()
    while menu(carnet) :
        continue
    print('Bye!')
    
    # for fiche in carnet:
        # afficherFiche(fiche,entete)
        # entete=False
    
if __name__=='__main__':
    main()