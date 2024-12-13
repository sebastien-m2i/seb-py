# le jeu du Fizz Buzz : afficher 100 nombres de 1 à 100

for it in range(1,101):
     outline = ""
     # commencer par multiple de 3, gére Fizz et FizzBuzz
     if (it%3==0):
          outline = outline + "Fizz"
     # finir par multiple de 5, gére Buzz et FizzBuzz
     if (it%5==0):
          outline = outline + "Buzz"
     print(outline if (outline!="") else it)
