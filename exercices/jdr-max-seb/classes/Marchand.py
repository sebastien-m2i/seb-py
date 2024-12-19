class Marchand:
    def __init__(self, nom:str, categorie:str, prix:int):
        self.nom:str = nom
        self.categorie:str = categorie
        self.prix:int = prix

    # attributs lecture seuls
    def nom(self):
        return self.nom
    def categorie(self):
        return self.categorie
    def prix(self):
        return self.prix
    
    def details_marchand(self):
        print('+'+'='*60+'+')
        print('+'+'='*60+'+')
            
    @classmethod
    def from_dict(cls,marchand):
        return cls(marchand["nom"], marchand["categorie"], marchand["prix"])
    # utilisation d'une méthode de classe
    # Marchand.from_dict({})