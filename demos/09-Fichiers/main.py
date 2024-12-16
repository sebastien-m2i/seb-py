import os

# définir chemin relatif du fichier
FILE_PATH = "./demos/09-Fichiers/fichier1.txt"

if __name__ == "__main__":
    print("Bienvenue dans la gestion de fichier :")
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="UTF-8") as nom_fichier:
            print(nom_fichier.read())
    else:
        file = open(FILE_PATH, "w", encoding="UTF-8")
        file.write(input("Votre texte >"))
        file.close()