class Adress():
    def __init__(self, numero:int, complement:str, voie:str, commune:str, code_postal:int):
        self._numero:int = numero
        self._15_complement:str = complement[:15]
        self._30_voie:str = voie[:30]
        self._30_commune:str = commune[:30]
        self._5_code_postal:str = code_postal[:5]

    def print(self):
        return self

    def get_adresse(self):
        for key, value in self.items():
                print(f"{key}:{value}")
