class Adresse():
    def __init__(self, numero:int, complement:str, voie:str, commune:str, code_postal:int):
        self._numero:int = numero
        self._30_complement:str = complement[:30]
        self._50_voie:str = voie[:50]
        self._30_commune:str = commune[:30]
        self._5_code_postal:str = code_postal[:5]
    
    def get_numero(self):
        return self._numero
    
    def to_String(self):
        return f" {self._numero} {self._50_voie} {self._30_commune} {self._5_code_postal}"