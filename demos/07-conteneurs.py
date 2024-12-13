# Conteneurs

# liste
print("----------------------------------")
print("--- LISTES -----------------------")
print("----------------------------------")
print("\n--- Ma liste complète-------------")
# Index              0        1 2    3
ma_liste_complete = ["chaine",2,True,[1,2,3]]
print(ma_liste_complete)
ma_liste_complete[2] = False
# panda pour manipuler des objets imbriqués
for item in ma_liste_complete:
    print(item, type(item),end="/")
    if type(item) == str: print(end="STR/")

print("\n--- Ma liste vide-----------------")
ma_liste_vide = []
print(ma_liste_vide)
ma_liste_vide.append(4)
ma_liste_vide.append('c')
ma_liste_vide.append("chaine")
for item in ma_liste_vide:
    print(item, type(item),end="/")

objet:object = ma_liste_vide.pop()
print("\n",ma_liste_vide,objet)

print("--- Ma liste prete----------------")
ma_liste_prete = [1,3,2]
print(ma_liste_prete)
ma_liste_prete.sort()
print(ma_liste_prete)
# ajouter 4 à la fin
ma_liste_prete.append(5)
print(ma_liste_prete)
# inserer 4 à l'index 3
ma_liste_prete.insert(3,4)
print(ma_liste_prete)
# ajouter plusieurs éléments à la fin
ma_liste_prete.extend([6,7]) 
print(ma_liste_prete)
# retirer la dernière valeur
ma_liste_prete.pop() 
print(ma_liste_prete)
# retirer une valeur précise valeur
ma_liste_prete.remove(2)
print(ma_liste_prete)
# tri inversé
ma_liste_prete.sort(reverse=True)
print(ma_liste_prete)

# sorted: trier la liste selon certains critères
# filter: filtrer les éléments de la liste
# map : créer une nouvelle liste avec tous les éléments
# reduce : en une seule valeur