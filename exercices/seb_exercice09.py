age : int = int(input("Age : "))
salaire_min : int = int(input("Salaire minimum : "))
annees_experience : int = int(input("Années d'expérience : "))

# Candidature acceptée/refusée avec message pour chaque critère non remplie
mess_err : str = ""
if age < 30:
     mess_err = mess_err + "\n- age minimum 30 ans "
if salaire_min < 40000:
     mess_err = mess_err + "\n- salaire minimum 40000 euros "
if annees_experience <5 :
     mess_err = mess_err + "\n- expérience minimale 5 ans"

if mess_err == "":
    print("> Candidature acceptée")
else:
    print("> Candidature refusée :",mess_err)