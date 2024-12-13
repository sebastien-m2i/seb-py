# @functions
def createTab(size:int=1):
    result : list = []
    for it in range(size):
        result.append(saisieNombre(it))
    return result

def saisieNombre(it:int):
    try:
        return int(input(f"Note {it+1}>"))
    except ValueError:
       return 0

# @main
while True:
    try:
        nb_notes = int(input("Combien de notes:"))
        notes = createTab(nb_notes)
        break
    except ValueError as err:
        print(err)
while True:
    try:
        choix = input("1:Min/2:Max/3:Moy/P:Print/Q:Quit>")
        if choix.upper() == 'Q':
            break
        elif choix == '1':
            print("Note min:",min(notes))
        elif choix == '2':
            print("Note max:",max(notes))
        elif choix == '3':
            print("Note moy:",sum(notes)/len(notes))
        elif choix == 'P':
            print("Notes:",notes)
    except Exception as err:
        print(err)