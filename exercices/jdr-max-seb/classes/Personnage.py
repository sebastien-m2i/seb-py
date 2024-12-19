import random

from classes.Marchand import Marchand

class Personnage:
    def __init__(self, nom:str, classe:str, niveau:int=1, point_de_vie:int=10, inventaire:list=[]):
        self.nom:str = nom
        self.classe:str = classe
        self.niveau:int = niveau
        self.points_de_vie:int = point_de_vie
        self.inventaire:list = inventaire

    # attributs lecture seuls
    def nom(self):
        return self.nom
    def classe(self):
        return self.classe
    def niveau(self):
        return self.niveau
    def points_de_vie(self):
        return self.points_de_vie
    
    def ajouter_objets_inventaire(self, objet_achat:Marchand):
        found=False
        for objet in self.inventaire:
            if objet["nom"] == objet_achat.nom:
                objet["quantité"] += 1
                found=True
                break
        if found == False:
            nouveau_objet:object={}
            nouveau_objet["nom"] = objet_achat.nom
            nouveau_objet["quantité"] = 1
            self.inventaire.append(nouveau_objet)

    def modifier_stats_personnage(self):
        self.niveau += 1
        self.points_de_vie += 20
        print(f"\033[92m")
        print(f"{self.nom} est au niveau {self.niveau} et son total de points de vie est à {self.points_de_vie}")
        print(f"\033[0m")

    def utiliser_potion_personnage(self):
        for it in range (len(self.inventaire)):
            objet = self.inventaire[it]
            if objet["nom"] == POTION_SOIN:
                self.inventaire.pop(it)
                self.points_de_vie += random.randint(1,50)
                print(f"\033[92m")
                print(f"{self.nom} a bu une potion, son total de points de vie est à {self.points_de_vie}")
                print(f"\033[0m")
                break

    def details_personnage(self):
            print(f"= Fiche personnage {self.nom}")
            print('+'+'='*60+'+')
            tab_left = []
            tab_left.append(f"| nom:            {self.nom:<14}")
            tab_left.append(f"| classe:         {self.classe:<14}")
            tab_left.append(f"| niveau:         {self.niveau:<14}")
            tab_left.append(f"| points de vie:  {self.points_de_vie:<14}")
            tab_right = [
                "|         INVENTAIRE         |",
                "+----------------------------+"
                ]
            if len(self.inventaire)>0:
                for it in range(len(self.inventaire)):
                    tab_right.append(f"| {self.inventaire[it]["quantité"]} {self.inventaire[it]["nom"]:<24} |")
            #compléter tableau
            for it in range(max(len(tab_right), len(tab_left))):
                if it < len(tab_left):
                    print(tab_left[it], end="")
                else:
                    print("|",' '*30, end="")
                if it < len(tab_right):
                    print(tab_right[it])
                else:
                    print("|",' '*26,"|")
            print('+'+'='*60+'+')
        
    # def attaquer(personnage:object, monstre:object):
    #     if personnage:
    #         print(f"= {personnage["nom"]} attaque {personnage2["nom"]}")
    #         personnage2["points_de_vie"] -= personnage1["niveau"]*10
    #         print(f"{personnage1["nom"]} a infligé {personnage1["niveau"]*10} dégats à {personnage2["nom"]}")
    #         if personnage2["points_de_vie"] <= 0:
    #             print(f"{personnage2["nom"]} est mort, son inventaire a été volé par {personnage1["nom"]}")
    #             inventaire1:list = personnage1["inventaire"]
    #             inventaire2:list = personnage2["inventaire"]
    #             while len(inventaire2)>0:
    #                 inventaire1.append(inventaire2.pop())

    def to_dict(self):
        return {
            "nom" : self.nom,
            "classe" : self.classe,
            "niveau" : self.niveau,
            "points_de_vie" : self.points_de_vie,
            "inventaire" : self.inventaire
        }
    
    @classmethod
    def from_dict(cls,personnage):
        return cls(personnage["nom"], personnage["classe"], personnage["niveau"], personnage["points_de_vie"], personnage["inventaire"])
    # utilisation d'une méthode de classe
    # Personnage.from_dict({})

    # print(f"(I)nventaire ajouter un objet à {getPersonnage(groupe_personnages,index)["nom"]}")
    # print(f"(M)odifier les statistiques de {getPersonnage(groupe_personnages,index)["nom"]}")
    # print(f"(U)tiliser une potion de soin pour {getPersonnage(groupe_personnages,index)["nom"]}")
    # print(f"(A)ttaquer monstre avec {getPersonnage(groupe_personnages,index)["nom"]}")

