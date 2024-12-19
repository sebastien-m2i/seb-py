from classes.Dico import Dico

def menu_dico(carnet:Dico):
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
                carnet.print_dico()
            case "A":
                carnet.add_dico()
            case "E":
                carnet.modify_dico()
            case "S":
                carnet.del_dico()
            case "Q":
                exit()
# @main
carnet = Dico()
menu_dico(carnet)