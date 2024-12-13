# Calcul du nombre d'années avant doublement d'un capital investi cap
# au taux annuel moyen taux
cap : float = float(input("Votre capital de départ : "))
taux : float = float(input("Taux en % (>0): "))
nb_years = 0
cap_2 = cap*2
# eviter boucle sans fin : taux > 0
while cap < cap_2:
     nb_years += 1
     cap *= (1+taux/100)
     print(f"capital accumulée année {nb_years} : {cap:.2f} ")

print(f"> Nombre d'années avant de doubler le capital de {cap_2/2} : {nb_years} année(s)")

# Population même régle
pop : int = int(input("Population en 2024 : "))
taux : float = float(input("Taux d'accroissement en %: "))
pop_final : int = int(input("Population visée : "))
year = 2024
while pop < pop_final:
     year += 1
     pop *= (1+taux/100)
     print(f"Population mondiale en {year} : {pop:.0f} ")
