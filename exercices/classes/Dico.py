from classes import Address

class Dico():

    def __init__(self):
        self._liste_adresses:list = []

    def print_dico(self):
        print("+ Liste des adresses")
        print('+' + '-'*96 + '+')
            #|4321|54321|desc56789012345|desc567891012345678901234567890|desc567891012345678901234567890|98765|
        print("|Adr.|Num. |Complement     |Intitulé voie                  |Commune                        |Code |")
        index:int=0
        for adresse in self._liste_adresses:
            index +=1
            print(f"|{index:>4}",end="|")
            print(f"{adresse["_numero"]:>5}",end="|")
            print(f"{adresse["_15_complement"]:<15}",end="|")
            print(f"{adresse["_30_voie"]:<31}",end="|")
            print(f"{adresse["_30_commune"]:<31}",end="|")
            print(f"{adresse["_5_code_postal"]:<5}",end="|")
            print()
        print('+' + '-'*96 + '+')

    def add_dico(self):
        print("+ Ajouter une adresse")
        adresse:Address = Address()
        adresse["_numero"] = input("Numero de voie>")
        adresse["_15_complement"] = input("Complément>")
        adresse["_30_voie"] = input("Voie>")
        adresse["_30_commune"] = input("commune>")
        adresse["_5_code_postal"] = input("Code postal>")
        self.append(adresse)

    def modify_dico(self):
        print("+ Editer une adresse")
        index = int(input("numero d'adresse ? :"))
        if (0<index and index <= len(self)):
            adresse:Address = self[index-1]
            adresse.get_adresse()

    def del_dico(self):
        print("+ Supprimer une adresse")
        index = int(input("numero d'adresse ? :"))
        if (0<index and index <= len(self)):
            adresse:Address = self[index-1]
            adresse.get_adresse()
            if bool(input("Confirmez suppression O/N?").upper() == 'O'):
                self.pop(index-1)