# choix des chemins par des conditions
# test est vrai -> bloc d'instructions chemin vrai
# test est faux -> bloc d'instructions chemin faux ou rien

age : int = int(input("saisir un age (>0): "))

# instruction simple
if age<=0: print("Vous n'êtes pas encore né!")
if age>=64: print("Vous avez le droit à la retraite")
else : print("Au travail !")

# instructions bloc tabulation OBLIGATOIRE avec py
if age>=21:
    print("Majorité aux USA")
    print("Vous pouvez ouvrir un compte et avoir des bitcoins")
elif age>=18:
    print("Majorité en France")
    print("vous avez le droit de voter et passer le permis!")
else:
    print("Mineur : continuer d'apprendre : courage")

# Version 2 : accumulé les pays avec condition majorité
if age>=21:
    print("USA")
if age>=18:
    print("France")
else:
    print("Mineur : continuer d'apprendre : courage")

# function exit() pour sortir de l'application python