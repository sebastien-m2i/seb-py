import math

print("----------------------------------------------------")
print("Calculer (pi * rayon² hauteur)/3")
print("----------------------------------------------------")

#dialogue avec l'utilisateur : saisie du rayon
str_rayon = input("Entrez le rayon (float > 0): ")
in_rayon : float = float(str_rayon)
print("Rayon   :", in_rayon)

#dialogue avec l'utilisateur : saisie d'un nom
str_hauteur = input("Entrez la hauteur (float > 0 ): ")
in_hauteur : float = float(str_hauteur)
print("Hauteur :", in_hauteur)

out_volume : float = (math.pi * (in_rayon**2) * in_hauteur) / 3

print(f"Le volume du cône droit avec rayon de {str_rayon} et hauteur {str_hauteur} est égal à {out_volume:^.2f}")
print(f"Le volume du cône droit avec rayon de {str_rayon} et hauteur {str_hauteur} est égal à {round(out_volume,2)}")
