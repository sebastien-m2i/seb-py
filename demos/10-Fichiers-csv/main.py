import csv

# définir chemin relatif du fichier
FILE_PATH = "./demos/10-Fichiers-csv/"

def lire_fichier_csv(nom_fichier):
    fichier = open(FILE_PATH+nom_fichier, "rt")
    lecteurCSV = csv.reader(fichier, delimiter=";")
    for ligne in lecteurCSV:
        print(ligne)

if __name__ == "__main__":
    print("Bienvenue dans la gestion de fichier CSV :")
    nom_fichier:str = input("entrez le nom du fichier:")
    lire_fichier_csv(nom_fichier)
