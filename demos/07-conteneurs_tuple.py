# Conteneurs

# tuple
print("----------------------------------")
print("--- TUPLE -----------------------")
print("----------------------------------")

# @functions
def test_tuple_packing():
    return ("valeur1",None, 20, True, 3.2) # tuple packing

# @main
tuple_1 = test_tuple_packing()
print(tuple_1)
# Unpackaging
var1, var2, var3, var4, var5 = tuple_1
print(var1,var2,var3,var4,var5)
for item in tuple_1:
    print(item, type(item),end="/")
print()

# Masquer une variable de programmation grâce à _
for _ in range(0,10):print("+",end="")
var1, _, var3, _, var5 = test_tuple_packing()

# inversion de valeurs
var1, var3 = var3, var1
print()
print(var1,var2,var3, var4, var5)
