import random
import math

# @constants
MIN = 1
MAX = 100

# @functions
def setMysteryNumber():
    return random.randint(MIN, MAX)

def setCounts():
    result : int = int(input("Set counts (1 to 10): "))
    if result >0 and result<=10:
        print("Difficulty level :",'🍏'*math.trunc((11-result)/2))
    return result


def printResult(_i_current,_i_myst,_it):
    if _i_current != _i_myst:
        print(f"Lost! mystery is {_i_myst}")
    else:
        print(f"Great! mystery {_i_myst} found {_it}")

# @main
try:
    print("- Mystery number game ------------------------")
    i_mystery_number = setMysteryNumber()
    while True:
        try:
            i_counts = setCounts()
            break
        except ValueError as mess_err:
            print(ValueError.__name__,mess_err)
    i_current : int = 0
    it : int = 0
    while i_current != i_mystery_number and it<i_counts:
        i_current : int = int(input(f"Set your number between {MIN} to {MAX} : "))
        it +=1
        if i_current>i_mystery_number:
            print("Number higher")
        elif i_current<i_mystery_number:
            print("Number lower")
    printResult(i_current,i_mystery_number,it)
except Exception as err:
    print(Exception.__name__,err)