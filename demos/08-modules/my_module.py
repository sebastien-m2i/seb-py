import math

def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def soustraction(a, b):
    return a - b

def division(a, b):
    return a + b if b!=0.0 else math.nan

if __name__ == "__main__":
    # Test
    # Args de l'extérieur
    # Si pas d'arguments alors forcer les valeurs par défaut²
    a = 1
    b = 0
    print("tester les 4 fonctions :")
    print(addition(a,b))
    print(multiplication(a,b))
    print(division(a,b))
    print(soustraction(a,b))