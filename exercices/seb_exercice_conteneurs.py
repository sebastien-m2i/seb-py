# @functions
def createTab(size:int=1):
    result : list = []
    for it in range(size):
        result.append(saisieNombre(it))
    return result

def saisieNombre(it:int):
    try:
        return int(input(f"Position {it+1} > nombre:"))
    except ValueError:
       return 0

# @main

#Liste compréhension
print([it for it in range(10,1,-1)][8])
# N notes
notes = createTab(15)
print(notes)