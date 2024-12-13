AUTH_LIST = ['a','c','g','t']

# @functions
def verificationAdn(_adn:str):
    if _adn == "": return False
    for c in _adn:
        if c not in AUTH_LIST: return False
    return True

def saisieAdn(_nb_car:int=0):
    if _nb_car == 0:
        result =  input(f">saisir adn {AUTH_LIST} :")
    else:
        result =  input(f">saisir une séquence d'adn {AUTH_LIST} de 1 à {_nb_car} caractères :")
    if verificationAdn(result):
        return result 
    else: 
        raise Exception("Adn string not authorized")

def proportion(_completed_adn:str,_sub_adn:str):
    result :int = 0
    index :int = 0
    while index != -1:
        index = proportionIndex(_completed_adn,_sub_adn,index)
        if index == -1: break
        result +=1
        index +=1
    return result 

def proportionIndex(_completed_adn:str,_sub_adn:str,_index:int):
    try:
        return _completed_adn.index(_sub_adn,_index)
    except Exception as err:
        return -1

def launchTests():
    # @testCT1
    pass
    # @testCT2
    pass
    # @testCT3
    pass
    # @testCT4
    pass
    # @testCT5
    print(f"@testCT5 {proportion("acgt","t")}")
    # @testCT6
    print(f"@testCT6 {proportion("aaccggttccggtt","cc")}")

def executeAdn():
    while True:
        try:
            adn :str = saisieAdn()
            print(f"Completed adn :{adn}")
            seq_adn :str = saisieAdn(4)
            print(f"Sequence adn :{seq_adn}")
            nb_occurences :int = proportion(adn,seq_adn)
            print(f"Nombre d'occurrence : {nb_occurences}")
            break
        except Exception as err:
            print(Exception.__name__,err)

# @main
if (input("(T)ests or (M)ain ? :") == 'T'):
    launchTests() 
else:
    executeAdn()