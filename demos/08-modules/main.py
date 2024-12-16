import my_module

def operation():
    a = int(input("nombre 1>"))
    b = int(input("nombre 2>"))
    return a,b

if __name__ == "__main__":
    print("Bienvenue dans l'application calculette :")
    while True :
        print("A-ddition")
        print("M-ultiplication")
        print("D-ivision")
        print("S-oustraction")
        print("Q-uiter")
        choix = input("AMDSQ>")
        result = None
        match choix.upper():
            case 'A':
                result = my_module.addition(operation())
            case 'D':
                result = my_module.division(operation())
            case 'S':
                result = my_module.soustraction(operation())
            case 'M':
                result = my_module.multiplication(operation())
            case 'Q':
                exit()
        print("Résultat = ", result)
 