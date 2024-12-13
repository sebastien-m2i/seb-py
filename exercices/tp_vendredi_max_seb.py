import random

POTION_SOIN = "potion de soin"

# @functions
def ajouter_objets_inventaire(personnage:object):
    inventaire = personnage["inventaire"]
    nouveau_objet={}
    nouveau_objet["nom"] = input("Nom objet:")
    nouveau_objet["quantité"] = int(input("Quantité:"))
    inventaire.append(nouveau_objet)

def modifier_stats_personnage(personnage:object):
    personnage["niveau"] += 1
    personnage["points_de_vie"] += 20

def utiliser_potion_personnage(personnage:object):
    inventaire:list = personnage["inventaire"]
    for it in range (len(inventaire)):
        if inventaire[it]["nom"] == POTION_SOIN:
            inventaire.pop(it)
            personnage["points_de_vie"] += random.randint(1,50)
            break

def details_personnage(personnage:object):
    for cle, valeur in personnage.items():
        print(f"{cle}: {valeur}")
        
def attaquer(personnage1:object, personnage2:object):
    personnage2["points_de_vie"] -= personnage1["niveau"]*10
    if personnage2["points_de_vie"] <= 0:
        inventaire1:list = personnage1["inventaire"]
        inventaire2:list = personnage2["inventaire"]
        while len(inventaire2)>0:
            inventaire1.append(inventaire2.pop())

# @main
print("============== Jeu de rôle ===============")
print()
personnage1 = {
    "nom":"Seb",
    "classe":"Mage",
    "niveau":1,
    "points_de_vie":8,
    "inventaire": [{"nom":POTION_SOIN,"quantité":1}]
}
personnage2 = {
    "nom":"Maxime",
    "classe":"Guerrier",
    "niveau":1,
    "points_de_vie":10,
    "inventaire": [{"nom":"sac à dos","quantité":1},{"nom":"arme","quantité":2}]
}

dico_personnages = {
    "p1" : personnage1,
    "p2" : personnage2,
}

# Afficher les personnages

while True:
    print("(A)jouter un objet dans un inventaire de personnage")
    print("(M)odifier les statistiques d'un personnage")
    print("(U)tiliser une potion de soin pour un personnage")
    print("(D)étails du personnage")
    print("(AT)taquer le personnage")
    print("(Q)Quitter")
    choix_Menu = input("Votre choix (LAQ)>")
    match choix_Menu.upper():
        case "A":
            # Ajouter des objets dans personnage saisi par input 
            key = input("identifiant du personnage :")
            # à tester si valeur ko
            ajouter_objets_inventaire(dico_personnages[key])
        case "M":
            # Modifier statsdans personnage saisi par input 
            key = input("identifiant du personnage :")
            # à tester si valeur ko
            modifier_stats_personnage(dico_personnages[key])
        case "U":
            # Boire une potion 
            key = input("identifiant du personnage :")
            # à tester si valeur ko
            utiliser_potion_personnage(dico_personnages[key])
        case "D":
            key = input("identifiant du personnage :")
            details_personnage(dico_personnages[key])
        case "AT":
            key1 = input("Personnage attaquant :")
            key2 = input("Personnage défenseur :")
            attaquer(dico_personnages[key1], dico_personnages[key2])
        case "Q":
            exit()

