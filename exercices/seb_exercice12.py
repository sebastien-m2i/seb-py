# Table de multiplication par 9
print("- Table de multiplication ------")
for it in range(11):
     print(f"{it:^2} fois 9 égal à {it*9:^2}")
print("--------------------------------")

# Le nombre max parmi 6 saisis
max : int = 0
for it in range(6):
     nb : int = int(input("saisir un entier positif : "))
     if nb>max:
          max=nb
print(f"> Le nombre max est {max}")