# 
# Etat eau
# 

# saisir la température
temp : float = float(input("Entrez la température : "))
# etat eau 3 états possible solide, liquide et gazeux
if temp < 0:
    print("Solide")
elif temp <=100:
    print("Liquide")
elif temp >100:
    print("Gazeux")

# ternaire
etat = "Solide" if (temp<0) else ("Liquide" if (temp<=100) else "Gazeux")