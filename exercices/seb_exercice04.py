print("-------------------------------")
print(" Saisie âge : mineur/majeur ?")
print("-------------------------------")

#option 18 ans ou 21 ans
age_major : int = int(input("Entrez âge majorité (18 ou 21 autorisés): "))

#dialogue avec l'utilisateur : saisie de l'âge
str_age = input("Entrez votre âge (entier >= 0): ")
age : int = int(str_age)

#variable booléenne opérateur logique sur l'âge de majorité 18 ou 21
is_overthan18or21 : bool = age>=age_major

print(f"Majorité à {age} an(s) ? -> {is_overthan18or21}")