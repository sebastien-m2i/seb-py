# Dico <=> objet

# liste
print("---------------------------------")
print("--- DICOS -----------------------")
print("---------------------------------")

mon_dico = {"key1":1, "key2":"name"}
print(mon_dico)
print(mon_dico["key1"])
print(mon_dico["key2"])

personne1 = {
    "nom":"Quin",
    "prenom":"Sébastien",
    "age":52,
    "email":"quin.sebastien@labom2iformation.fr",
    "isLogged":True
}
# Un an de plus
personne1["age"] += 1
# supprimer un champ
del personne1["isLogged"]
# ajouter un champ
personne1["Ville"] = "Ascq"
print(personne1)
# les contenus
for value in personne1.values():print(value)
for key in personne1:print(key)
for key,value in personne1.items():
    print(f"{key}:{value}")

personne2 = {
    "nom":"Dupont",
    "prenom":"Jean",
    "age":74,
    "email":"jean.dupont@labom2iformation.fr",
    "isLogged":False
}
personne3 = {
    "nom":"Durand",
    "prenom":"Marie",
    "age":68,
    "email":"marie.durand@labom2iformation.fr",
    "isLogged":True
}

# liste d'objets
annuaire = [personne1,personne2,personne3]
# charger les formats json
for personne in annuaire:
    for key, value in personne.items():
        print(f"{key}:{value}")
annuaire[1]["email"] = "dupont.jean@labom2iformation.fr"