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

def utiliser_potion_personnage(personnage:object):
    if personnage:
        inventaire:list = personnage["inventaire"]
        for it in range (len(inventaire)):
            if inventaire[it]["nom"] == POTION:
                inventaire.pop(it)
                personnage["points_de_vie"] += random.randint(1,50)
                break

def details_personnage(personnage:object):
    if personnage:
        print(f"= Fiche personnage {personnage["nom"]}")
        for cle, valeur in personnage.items():
            print(f"{cle}: {valeur}")
        
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

def getPersonnageByKey():
    try:
        key = input("identifiant du personnage :")
        return dico_personnages[key]
    except KeyError as err:
        return None

# @main
dico_personnages = init_dico()

# Afficher les personnages
while True:
    print("------------------- Jeu de rôle -------------------")
    print("(D)étails du personnage")
    print("(I)nventaire ajouter un objet ")
    print("(M)odifier les statistiques d'un personnage")
    print("(U)tiliser une potion de soin pour un personnage")
    print("(A)ttaquer un personnage")
    print("(Q)Quitter")
    print("---------------------------------------------------")
    choix_Menu = input("Votre choix (IMUDAQ)>")
    match choix_Menu.upper():
        case "D":
            # Détail du personnage
            details_personnage(getPersonnageByKey())
        case "I":
            # Ajouter des objets dans personnage saisi par input 
            ajouter_objets_inventaire(getPersonnageByKey())
        case "M":
            # Modifier statsdans personnage saisi par input 
            modifier_stats_personnage(getPersonnageByKey())
        case "U":
            # Boire une potion 
            utiliser_potion_personnage(getPersonnageByKey())
        case "A":
            # Attaquer un personnage
            attaquer(getPersonnageByKey(),getPersonnageByKey())
        case "Q":
            exit()