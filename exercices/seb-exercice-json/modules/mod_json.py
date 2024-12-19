import os
import json

# définir chemin relatif du fichier
PATH = "./exercices/datas/"
FILE_JSON = "music.json"
PATH_JSON = PATH+FILE_JSON

def lire_fichier_json():
    fichier = open(PATH_JSON, "r", encoding="UTF-8")
    result:list = json.load(fichier)
    return result

def dump_fichier_json(list:list):
    fichier = open(PATH_JSON, "w", encoding="UTF-8")
    json.dump(list,fichier, indent=4, ensure_ascii=False)

def charger_liste():
    return lire_fichier_json() if os.path.exists(PATH_JSON) else []

if __name__ == "__main__":
    print("Test mod_json")