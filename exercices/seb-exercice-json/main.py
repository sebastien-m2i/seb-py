import modules.mod_chansons

if __name__ == "__main__":
    print("=== MENU PRINCIPAL ===================================================================")
    mes_chansons:list=modules.mod_chansons.charger_chansons()
    while True:
        print("1. Ajouter une chanson")
        print("2. Voir les chansons")
        print("3. Editer une chanson")
        print("4. Supprimer une chanson")
        print("0. Quitter le programme")
        choix = input("(12340)>")
        match choix:
            case "1":
                modules.mod_chansons.ajouter_chanson(mes_chansons)
            case "2":
                modules.mod_chansons.print_chansons(mes_chansons)
            case "3":
                modules.mod_chansons.modifier_chanson(mes_chansons)
            case "4":
                modules.mod_chansons.supprimer_chanson(mes_chansons)
            case "0":
                modules.mod_chansons.sauver_chansons(mes_chansons)
                exit()