import modules.mod_json

def print_chansons(mes_chansons:list):
    if len(mes_chansons)>0:
        print("+----+--------------------------------+----------------------+---------------+-------+")
        print("|num.| titre                          | artiste              | categorie     | score |")
        print("+----+--------------------------------+----------------------+---------------+-------+")
        for it in range(len(mes_chansons)):
            chanson = mes_chansons[it]
            print(f"|{it+1:>3} | {chanson["titre"]:<30} | {chanson["artiste"]:<20} | {chanson["points_de_vie"]:<13} | {chanson["niveau"]:>5} |")
        print("+----+--------------------------------+----------------------+---------------+-------+")

def ajouter_chanson(mes_chansons:list):
    print("=== AJOUTER UNE CHANSON ===")
    titre30 = input("Titre (max 30):")
    artiste20 = input("Artiste (max 20):")
    categorie:int = int(input("1-Pop 2-Rock 3-Electro 4-Classique:"))
    score:int = int(input("Score (de 1 à 5):"))
    mes_chansons.append({"titre": titre30,"artiste":artiste20,"categorie":categorie,"score":score})
    print(f"Le titre {titre30} a été ajouté à la play-list")

def modifier_chanson(mes_chansons:list):
    print("=== MODIFIER UNE CHANSON ===")
    longueur = len(mes_chansons)
    if longueur>0:
        index = int(input(f"Quel numéro de chanson à modifier (de 1 à {longueur})?"))
        if index<=longueur:
            chanson:list = mes_chansons[index-1]
            new_titre = input(f"{chanson["titre"]}>")
            if new_titre:
                chanson["titre"] = new_titre
            new_artiste = input(f"{chanson["artiste"]}>")
            if new_artiste:
                chanson["artiste"] = new_artiste
            new_categorie = input(f"{chanson["categorie"]}>")
            if new_categorie:
                chanson["categorie"] = int(new_categorie)
            new_score = input(f"{chanson["score"]}>")
            if new_score:
                chanson["score"] = int(new_score)
            print(f"Chanson num {index} a été modifiée")
    else:
        print("Modification impossible, la play-list est vide :")


def supprimer_chanson(mes_chansons:list):
    print("=== SUPPRIMER UNE CHANSON ===")
    longueur = len(mes_chansons)
    if longueur>0:
        index = int(input(f"Quel numéro de chanson à supprimer (de 1 à {longueur})?"))
        if index<=longueur:
            mes_chansons.pop(index-1)
    else:
        print("Suppression impossible, la play-list est vide :")

def sauver_chansons(mes_chansons:list):
    if len(mes_chansons)>0:
        modules.mod_json.dump_fichier_json(mes_chansons)
    else:
        modules.mod_json.dump_fichier_json([])

def charger_chansons():
    return modules.mod_json.charger_liste()

if __name__ == "__main__":
    print("Test mod_chansons")

    # Récupérer les arguments