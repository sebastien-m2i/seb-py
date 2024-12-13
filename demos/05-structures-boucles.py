# boucle increment
# break sortir de la boucle, continue force l'iteration suivante
increment = 0
while increment < 10:
    if increment >= 6:
        pass #print(f"mon increment à traiter à partir du step 6: {increment}")
    increment += 1
    if increment <=5:
        continue

#boucle de 3 avec itération suite arrêt de la boucle avec break
for it in range(0, 20):
    pass #print(f"{it+1} - ")
    if it == 2:
        break

buffer : str = ""
for i in range(122,96,-1):
    buffer = buffer + chr(i)
print(f" Alphabet inversé :{buffer}")

for it in range(1,10,+2):
    buffer[it].upper()
print(f" Alphabet MajMin :{buffer}")

#liste finie for in
fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    pass #Je ne sais encore quoi faire avec ces fruits mais je veux tester la suite de mon code

print("- Menu végétarien ------------------------")
#sortie de la boucle si condition fausse
it : int = 0
for fruit in fruits:
    it += 1
    print(f"fruit {it} : {fruit}")
menu_fruits : int = int(input("> Choisir un fruit (de 1 à 5) : "))
# match case
match menu_fruits:
    case 1:
        print(fruits[0])
    case 2:
        print(fruits[1])
    case 3:
        print(fruits[2])
    case 4:
        print(fruits[3])
    case 5:
        print(fruits[4])
    case _:
        print("Pas de fruit")
print(fruits[menu_fruits-1]*int(input("> Combien de fruits ? : ")))
