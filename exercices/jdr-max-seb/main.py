import mod_json

from classes.Personnage import Personnage
from classes.Marchand import Marchand

def liste_personnages(groupe_personnages:list):
    result:int=0
    if len(groupe_personnages)>0:
        print("+----+----------------------+----------------------+--------+-----+")
        print("|num.| Nom                  | classe               | Niveau |  PV |")
        print("+----+----------------------+----------------------+--------+-----+")
        for it in range(len(groupe_personnages)):
            personnage:Personnage = groupe_personnages[it]
            print(f"|{it+1:>3} | {personnage.nom:<20} | {personnage.classe:<20} | {personnage.niveau:>6} | {personnage.points_de_vie:>3} |")
        print("+----+----------------------+----------------------+--------+-----+")
        result = int(input("Numero personnage actif>"))
        return result

def sauver_personnages(groupe_personnages:list):
    result:list=[]
    if len(groupe_personnages)>0:
        for it in range(len(groupe_personnages)):
            personnage:Personnage = groupe_personnages[it]
            result.append(personnage.to_dict())
    mod_json.dump_fichier_json(result)

def charger_personnages():
    result_json =  mod_json.charger_liste(mod_json.FILE_PERSONNAGES)
    result:list=[]
    for personnage_json in result_json:
        result.append(Personnage.from_dict(personnage_json))
    return result

def acheter_marchand(groupe_personnages:list, index:int):
    result_json =  mod_json.charger_liste(mod_json.FILE_OBJETS)
    result:list=[]
    for objet in result_json:
        result.append(Marchand.from_dict(objet))
    print("= Marchand ===")
    print("+----+---------------------+------------------+--------+")
    print("|num.| Nom                 | catégorie        |   prix |")
    print("+----+---------------------+------------------+--------+")
    for it in range (len(result)):
        print(f"|{it+1:>3} |{result[it].nom:<20} | {result[it].categorie:<16} | {result[it].prix:>6} |")
    print("+------------------------------------------------------+")
    num_objet = int(input("Numero d'objet à acheter>"))
    personnage:Personnage = groupe_personnages[index-1]
    personnage.ajouter_objets_inventaire(result[num_objet-1])

# Créer nb personnages dans un groupe
def creation_groupe(nb:int):
    result:list=[]
    nom:str = None
    classe:str = None
    for it in range(nb):
        print(f"=== Personnage {it+1} ===")
        nom = input("Nom>")
        classe = input("Classe(guerrier/mage/rodeur)>")
        result.append(Personnage(nom,classe))
    return result

if __name__ == "__main__":
    index=0
    groupe:list=[]
    while True:
        print("------------------- Jeu de rôle -------------------")
        prompt:str=">"
        if index == 0:
            print("(N)ouvelle campagne")
            print("(C)harger la campagne")
        else:
            print("---------------------------------------------------")
            print("(A)ctiver personnage")
            print("(M)archand - acheter un objet")
            print("(D)étail personnage")
            print("(S)auver la campagne")
            prompt = groupe[index-1].nom + prompt
        print("(Q)uitter")
        print("---------------------------------------------------")
        choix_Menu = input(f"\033[93m{prompt}\033[0m")
        match choix_Menu.upper():
            case "N":
                groupe = creation_groupe(2)
                index = 1
            case "C":
                groupe = charger_personnages()
                index = 1
            case "A":
                index = liste_personnages(groupe)
            case "M":
                acheter_marchand(groupe, index)
            case "D":
                personnage:Personnage = groupe[index-1]
                personnage.details_personnage()
            case "S":
                sauver_personnages(groupe)
            case "Q":
                exit()