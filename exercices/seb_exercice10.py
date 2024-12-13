it : int = 0
while True:
     nb = int(input("Nombre compris entre 1 et 3 (1 par défaut) : ")) and 1
     it = it + 1
     if nb>=1 and nb <=3:
          break
print(f"> Choix retenu : {nb} en {it} coup(s) !")