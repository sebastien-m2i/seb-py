import random

POTION = "potion"
EPEE = "épée"
SAC = "sac à dos"

# @functions
def init_dico():
    personnage1 = {
        "nom":"Seb",
        "classe":"Mage",
        "niveau":1,
        "points_de_vie":8,
        "inventaire": [{"nom":POTION,"quantité":1}]
    }
    personnage2 = {
        "nom":"Maxime",
        "classe":"Guerrier",
        "niveau":1,
        "points_de_vie":10,
        "inventaire": [{"nom":SAC,"quantité":1},{"nom":EPEE,"quantité":2}]
    }

    return {
        "p1" : personnage1,
        "p2" : personnage2,
    }

def ajouter_objets_inventaire(personnage:object):
    if personnage:
        inventaire = personnage["inventaire"]
        nouveau_objet={}
        nouveau_objet["nom"] = input("Nom objet:")
        nouveau_objet["quantité"] = int(input("Quantité:"))
        inventaire.append(nouveau_objet)

def modifier_stats_personnage(personnage:object):
    if personnage:
        personnage["niveau"] += 1
        personnage["points_de_vie"] += 20
        print(f"\033[92m")
        print(f"{personnage["nom"]} est au niveau {personnage["niveau"]} et son total de points de vie est à {personnage["points_de_vie"]}")
        print(f"\033[0m")

def utiliser_potion_personnage(personnage:object):
    if personnage:
        inventaire:list = personnage["inventaire"]
        for it in range (len(inventaire)):
            if inventaire[it]["nom"] == POTION:
                inventaire.pop(it)
                personnage["points_de_vie"] += random.randint(1,50)
                print(f"\033[92m")
                print(f"{personnage["nom"]} a bu une potion, son total de points de vie est à {personnage["points_de_vie"]}")
                print(f"\033[0m")
                break

def details_personnage(personnage:object):
    if personnage:
        print(f"= Fiche personnage {personnage["nom"]}")
        print('+'+'='*60+'+')
        tab_left = []
        tab_right = [
            "|         INVENTAIRE         |",
            "+----------------------------+"
            ]
        for cle, valeur in personnage.items():
            if cle!="inventaire":
                tab_left.append(f"| {cle:<14}: {valeur:<14}")
            else:
                if len(valeur)>0:
                    for it in range(len(valeur)):
                        tab_right.append(f"| {valeur[it]["quantité"]} {valeur[it]["nom"]:<24} |")
        for it in range(max(len(tab_right), len(tab_left))):
            if it < len(tab_left):
                 print(tab_left[it], end="")
            else:
                print("|",' '*30, end="")
            if it < len(tab_right):
                 print(tab_right[it])
            else:
                print("|",' '*26,"|")
        print('+'+'='*60+'+')
    
def attaquer(personnage1:object, personnage2:object):
    if personnage1 and personnage2:
        print(f"= {personnage1["nom"]} attaque {personnage2["nom"]}")
        personnage2["points_de_vie"] -= personnage1["niveau"]*10
        print(f"{personnage1["nom"]} a infligé {personnage1["niveau"]*10} dégats à {personnage2["nom"]}")
        if personnage2["points_de_vie"] <= 0:
            print(f"{personnage2["nom"]} est mort, son inventaire a été volé par {personnage1["nom"]}")
            inventaire1:list = personnage1["inventaire"]
            inventaire2:list = personnage2["inventaire"]
            while len(inventaire2)>0:
                inventaire1.append(inventaire2.pop())

def getPersonnageByKey(prompt:str="Personnage"):
    try:
        for key in dico_personnages:
            prompt = prompt + "/" + key
        key = input(f"{prompt}>")
        return dico_personnages[key]
    except KeyError as err:
        return None

if __name__ == "__main__":
    dico_personnages = init_dico()
    while True:
        print("------------------- Jeu de rôle -------------------")
        print("(D)étails du personnage")
        print("(I)nventaire ajouter un objet ")
        print("(M)odifier les statistiques d'un personnage")
        print("(U)tiliser une potion de soin pour un personnage")
        print("(A)ttaquer un personnage")
        print("(Q)Quitter")
        print("---------------------------------------------------")
        choix_Menu = input(f"Votre choix (DIMUAQ)>")
        match choix_Menu.upper():
            case "D":
                details_personnage(getPersonnageByKey())
            case "I":
                ajouter_objets_inventaire(getPersonnageByKey())
            case "M":
                modifier_stats_personnage(getPersonnageByKey())
            case "U":
                utiliser_potion_personnage(getPersonnageByKey())
            case "A":
                attaquer(getPersonnageByKey("Attaquant"),getPersonnageByKey("Défenseur"))
            case "Q":
                exit()