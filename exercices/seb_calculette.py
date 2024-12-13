import math
# @functions
def calculer(ope1:float,ope2:float):
    return ope1+ope2, ope1-ope2, ope1/ope2 if(ope2!=0) else math.nan, ope1*ope2
# @main
print("Résultats:", calculer(float(input("Calculette:\nope1>")),float(input("ope2>"))))

# @tests package squash tm
# Données en entrées
FILE = [(1, 2),(2.5, 3),(12, 4),(10,0)]
#for item in FILE:
#    ope1, ope2 = item
#    print(calculer(ope1, ope2))