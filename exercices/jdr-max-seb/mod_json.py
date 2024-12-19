import os
import json

PATH_DATAS = "./exercices/jdr-max-seb/datas/"
FILE_PERSONNAGES = "personnages.json"
FILE_OBJETS = "objets.json"
FILE_MONSTRES = "monstres.json"
FILE_CLASSES = "classes.json"

def lire_fichier_json(file:str):
    fichier = open(file, "r", encoding="UTF-8")
    result:list = json.load(fichier)
    return result

def dump_fichier_json(list:list, file:str):
    fichier = open(PATH_DATAS + file, "w", encoding="UTF-8")
    json.dump(list,fichier, indent=4, ensure_ascii=False)

def charger_liste(file:str):
    return lire_fichier_json(file) if os.path.exists(file) else []

if __name__ == "__main__":
    print("Test mod_json accés au datas")