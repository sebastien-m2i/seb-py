# Fonctions traitement avec paramétres en entrée retourne une valeur
# Appel avec les parenthèses
print("Mon message est une chaine de caractères en entrée, en sortie j'ai l'affichage dans la console")
# Méthodes sont appliquées à un objet
test_maj = "test".upper()
print("test".upper())

#dialogue avec l'utilisateur : saisie d'une valeur qui retourne une chaine de caractères
req = input("Entrez votre valeur svp (entier de 1 à 100) :")
print("Votre valeur saisie :", req)
print("Type de valeur :", type(req))
# Cast de variable
val_int : int = int(req)
print("La valeur castée en entier :", val_int)

#cast et input en une seule ligne
req_int : int = int(input("Entrez une 2eme valeur svp (entier de 1 à 100) :"))
print("La valeur castée en entier :", req_int)

# formater une chaine dans le print
print(f"La première valeur est : {val_int} et la deuxième valeur est : {req_int}")
val_float : float =  val_int / req_int
print(f"Résulat de {val_int} / {req_int} = {val_float:7.2f}")

# formater une variable en enlevant les cars spéciaux
print(f"\n{val_float} et est de type {type(val_float)}")

# caster en bool
isBool : bool = bool(None)