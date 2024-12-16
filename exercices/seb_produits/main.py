import csv

# définir chemin relatif du fichier

FILE_PATH = "./exercices/seb_produits/"
FILE_PRODUCT= "produits.csv"

def lire_fichier_csv(nom_fichier):
    fichier = open(FILE_PATH+nom_fichier, "rt")
    lecteurCSV = csv.reader(fichier, delimiter=";")
    for ligne in lecteurCSV:
        print(ligne)
    fichier.close()

def ecrire_fichier_csv(nom_fichier,ligne):
    fichier = open(FILE_PATH+nom_fichier, "a")
    writerCSV = csv.writer(fichier,delimiter=";")
    writerCSV.writerow(ligne)
    fichier.close()
    # with open(FILE_PATH+nom_fichier, "a", newline="") as fichier_produits:
    #     writer = csv.writer(fichier_produits, delimiter="|")
    #     writer.writerow(ligne)

if __name__ == "__main__":
    print("Bienvenue dans la gestion de produits (CSV) :")
    lire_fichier_csv(FILE_PRODUCT)
    new_product = []
    new_product.append(input("Titre>"))
    new_product.append(input("Prix>"))
    new_product.append(input("Stock>"))
    print(new_product)
    ecrire_fichier_csv(FILE_PRODUCT,new_product)
    print("Après insertion du nouveau produit :")
    lire_fichier_csv(FILE_PRODUCT)