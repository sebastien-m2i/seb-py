import random
import math

try:
    # constantes par convention _<AllMaj>
    MIN = 1
    MAX = 100

    print("- Jeu du nombre mystère ------------------------")
    nombre_mystere = random.randint(MIN, MAX)
    while True:
        try:
            i_nb_coups : int = int(input("Saisir un nombre de coups (de 1 à 10): "))
            if i_nb_coups >0 and i_nb_coups<=10:
                print("Niveau de difficulté :",'🍏'*math.trunc((11-i_nb_coups)/2))
                break
        except ValueError as _mess_err:
            print(ValueError.__name__,_mess_err)
    nombre : int = 0
    it : int = 0
    while nombre_mystere != nombre and it<i_nb_coups:
        nombre : int = int(input(f"Entrez un nombre entier entre {MIN} et {MAX} : "))
        it +=1
        if nombre>nombre_mystere:
            print("votre nombre est trop élevé")
        elif nombre<nombre_mystere:
            print("votre nombre est trop bas")
    if nombre_mystere != nombre:
        print(f"Perdu! Le nombre mystère était {nombre_mystere}")
    else:
        print(f"Bravo! Le nombre mystère {nombre_mystere} trouvé en {it} coup(s)")
except Exception as _err:
    print(Exception.__name__,_err)