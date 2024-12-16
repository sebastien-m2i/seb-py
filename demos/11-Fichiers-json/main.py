import json

# définir chemin relatif du fichier
FILE_PATH = "./demos/11-Fichiers-json/"

def lire_fichier_json(nom_fichier):
    fichier = open(FILE_PATH+nom_fichier, "r", encoding="UTF-8")
    result:list = json.load(fichier)
    # print(result)
    return result

def dump_fichier_json(nom_fichier, list:list):
    fichier = open(FILE_PATH+nom_fichier, "w", encoding="UTF-8")
    json.dump(list,fichier, indent=4)

if __name__ == "__main__":
    print("Bienvenue dans la gestion de fichier JSON :")
    nom_fichier:str = input("entrez le nom du fichier:")
    mes_produits:list = lire_fichier_json(nom_fichier)
    if len(mes_produits)>0:
        print("+---------------------+-------------------+------------------+")
        print("| titre               |              prix |            stock |")
        print("+---------------------+-------------------+------------------+")
        for produit in mes_produits:
            print(f"| {produit["titre"]:<19} | {produit["prix"]:>17} | {produit["stock"]:>16} |")
        print("+---------------------+-------------------+------------------+")
    print("Sauver dans fichier sav.json")
    json_str:str = json.dumps(mes_produits, indent=1)
    type_str = type(json_str)
    print(json_str,type_str)
