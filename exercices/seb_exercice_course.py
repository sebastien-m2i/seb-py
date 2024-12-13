# @functions
def initcourse():
    while True:
        nb_joueurs = int(input("Combien de joueurs:"))
        result : list = []
        for it in range(nb_joueurs):
            result.append(saisieNom(it))
        break
    return result

def saisieNom(it:int):
    return input(f"Joueur en position {it+1}>")

def panne_moteur(list:list):
    if (len(list)>1):list.append(premier = list.pop(0))

def passe_en_tete(list:list):
    if (len(list)>1):list.insert(0,list.pop(1))

def sauve_honneur(list:list):
    if (len(list)>1):list.append(list.pop(-2))

def tir_blaster(list:list):
    if (len(list)>1): list.pop(0)

def retour_inattendu(list:list):
    list.append(input("Nom du nouveau joueur:"))

def menu_course(list:list):
    while True:
        print("1-Panne moteur/2-Acceleration 2eme/3-Dernier sauve honneur/4-Tir de blaster/5-Grand retour")
        print("C-Classement général (mode test)")
        print("Q-Quitter la course")
        choix_Menu = input("Votre choix (12345CQ)>")
        match choix_Menu.upper():
            case "1":
                panne_moteur(list)
            case "2":
                passe_en_tete(list)
            case "3":
                sauve_honneur(list)
            case "4":
                tir_blaster(list)
            case "5":
                retour_inattendu(list)
            case "C":
                print(list)
            case "Q":
                exit()
# @main
joueurs:list = initcourse()
menu_course(joueurs)