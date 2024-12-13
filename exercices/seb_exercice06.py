# 
# calculer le cout global d'une commande de photocopies
# 
print("Moins de 10 copies : 0.50 euro par copie")
print("Entre 10 et 20 copies inclus : 0.40 euro par copie")
print("Plus de 20 copies : 0.30 euro par copie")

# saisir un nombre de copies et vérifier nombre positif
nombre : int = int(input("Entrez un nombre de copies (>0): "))
# cout
cout : float = 0.0
if nombre > 20:
    cout = nombre * 0.3
elif nombre >= 10:
    cout = nombre * 0.4
elif nombre > 0:
    cout = nombre * 0.5
else:
    print("Saisie incorrecte")    
if cout>0:
    print(f"Le prix à payer est de {cout:^.2f} euro(s)")