print("----------------------------------------------------")
print("Afficher le message Bonjour M. ou Mme {Prenom} {NOM}")
print("----------------------------------------------------")

#dialogue avec l'utilisateur : saisie d'un prénom
req_first_name = input("Entrez votre prénom : ")
# print("Prénom :", req_first_name)

#dialogue avec l'utilisateur : saisie d'un nom
req_name = input("Entrez votre nom : ")
# print("Nom :", req_name)

print(f"Bonjour M. Ou Mme {req_first_name.capitalize()} {req_name.upper()}")
