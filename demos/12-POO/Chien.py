class Chien():
    def __init__(self, nom):
        self.nom:str = nom
        
    def aboyer(self,son:str):
        return f" {self.nom} aboie fort en majuscules : {son.upper()} !"

    def to_String(self):
        return f" {self.nom}"