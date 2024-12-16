import os

FILE_PATH = "./exercices/seb_exercice_fichier/filepsw.txt"

def ecrire_fichier(mess):
    with open(FILE_PATH, "w", encoding="UTF-8") as file:
        file.write(input(f"{mess} : "))

if __name__ == "__main__":
    print("Bienvenue dans la gestion de sauvegarde de votre mot de passe :")
    if not(os.path.exists(FILE_PATH)):
        ecrire_fichier("Votre nouveau mot de passe")
    else:
        print("V-oir le mot de passe")
        print("M-odifier le mot de passe")
        choix = input("CM>")
        match choix.upper():
            case 'V':
                file = open(FILE_PATH, encoding="UTF-8")
                print(file.read())
                file.close()
            case 'M':
                ecrire_fichier("Modifier mot de passe")
    exit()