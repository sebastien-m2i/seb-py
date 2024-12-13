# Fonctions

HELLO = "Hello"

# @functions
def printHelloMessage(_s20_hello=HELLO):
    print(_s20_hello)

def printMessage(_s50_first_name):
    print(HELLO+" ", _s50_first_name)

def return_number(_i_nombre):
    return _i_nombre

def operation(_i_left:int,_i_right:int,_c_operation='+'):
    result : int = None
    if _c_operation == '+':
        result = _i_left+_i_right
    return result

# @main
try:
    printHelloMessage()
    printMessage(input(">What's your first name :"))
    try:
        i_1 = return_number(int(input(">Set a first number : ")))
        i_2 = return_number(int(input(">Set a second number : ")))
        print(f"{i_1} + {i_2} = {operation(i_1,i_2)}")
    except ValueError as _ERR:
        print(ValueError.__name__,_ERR)
    exit()
except Exception as _ERR:
    print(Exception.__name__,_ERR)