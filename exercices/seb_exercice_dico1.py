# @functions
def init_dico():return []

def print_dico(dico:list):
    print("+ Liste des adresses")
    print('+' + '-'*96 + '+')
          #|4321|54321|desc56789012345|desc567891012345678901234567890|desc567891012345678901234567890|98765|
    print("|Adr.|Num. |Complement     |Intitulé voie                  |Commune                        |Code |")
    index:int=0
    for adresse in dico:
        index +=1
        print(f"|{index:>4}",end="|")
        print(f"{adresse["num_voie"]:>5}",end="|")
        print(f"{adresse["complement"]:<15}",end="|")
        print(f"{adresse["intitule_voie"]:<31}",end="|")
        print(f"{adresse["commune"]:<31}",end="|")
        print(f"{adresse["code_postal"]:<5}",end="|")
        print()
    print('+' + '-'*96 + '+')

def add_dico(dico:list):
    print("+ Ajouter une adresse")
    adresse:object={}
    adresse["num_voie"] = input("Veuillez entrer le numero de voie SVP :") or 1
    adresse["complement"] = input("Veuillez entrer le complément d'adresse SVP :") or "étage"
    adresse["intitule_voie"] = input("Veuillez entrer l'intitulé de voie SVP :") or "rue"
    adresse["commune"] = input("Veuillez entrer la commune SVP :") or "Commune"
    adresse["code_postal"] = input("Veuillez entrer le code postal SVP :") or 59650
    dico.append(adresse)

def modify_dico(dico:list):
    print("+ Editer une adresse")
    index = int(input("numero d'adresse ? :"))
    if (0<index and index <= len(dico)):
        get_adresse(dico[index-1])

def del_dico(dico:list):
    print("+ Supprimer une adresse")
    index = int(input("numero d'adresse ? :"))
    if (0<index and index <= len(dico)):
        get_adresse(dico[index-1])
        if bool(input("Confirmez suppression O/N?").upper() == 'O'):
            dico.pop(index-1)

def get_adresse(adresse:object):
       for key, value in adresse.items():
            print(f"{key}:{value}")

def menu_dico(dico:list):
    while True:
        print("+ (L)ister", end=" / ")
        print("(A)jouter", end=" / ")
        print("(E)diter", end=" / ")
        print("(S)upprimer", end=" / ")
        print("(Q)Quitter")
        choix_Menu = input("Votre choix (LAESQ)>")
        print()
        match choix_Menu.upper():
            case "L":
                print_dico(dico)
            case "A":
                add_dico(dico)
            case "E":
                modify_dico(dico)
            case "S":
                del_dico(dico)
            case "Q":
                exit()
# @main
dico:list = init_dico()
menu_dico(dico)