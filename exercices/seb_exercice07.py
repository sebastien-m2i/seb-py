# 
# Catégorie licence sportive
# 

# saisir age enfant, limite de 3 ans à 14 ans inclus
age : int = int(input("Entrez l'âge de votre enfant (entre 3 et 14 ans inclus): "))
# afficher la catégorie selon la tranche d'âge
if age >= 3 and age <= 6:
    print("Baby")
elif age >= 7 and age <=8:
    print("Poussin")
elif age >=9 and age<=10:
    print("Pupille")
elif age >=11 and age<=12:
    print("Minime")
elif age >=13 and age<=14:
    print("Cadet")
else:
    print("Age incorrect : pas de catégorie associée")
