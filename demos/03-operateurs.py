# importer des modules
import math
# from math import *

# Operateurs num
a : int = 4
b : float = 8.8

print("addition : " ,a+b) 
print("soustraction : " ,a-b)
print("division : " ,a/b)
print("div entière : " ,a//b)
print("modulo : " ,a%b)
print("multiplication : " ,a*b)
print("puissance : " ,a**2)

# -= += affectation d'une variable avec opérateur préfixé : format unaire
a += 1
b -= 2

print(f"a = {a} / b = {b:7.2f}");

# concatenation de str
str1 : str = "Title"
str2 : str = "Subtitle"
print(f"{str1 + str2}")
print(f" réplication 10 fois title {str1 * 10}")

print(f"{math.pi:^7.2f}")

# relationnels
# > < >= <= == !=
print(25>0) #true
print(25<0) #false
print(25!=0) #true
print(25==0) #false

# logiques
# and or not
print(25>0 and 0!=0) #false
print(25>0 or 0!=0) #true