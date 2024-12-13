# @functions
def soustraire(_fisrt:int,_second:int,_end=" = "):
    print(f"Je soustrais {_fisrt} et {_second}",end=f"{_end}")
    return int(_fisrt - _second)

def additionner(_fisrt:int,_second:int):
    pass

def multiplier(_fisrt:int,_second:int):
    pass

def diviser(_fisrt:int,_second:int,_end=" = "):
    if int(_second) == 0:
        raise ValueError("Division par 0 interdite")
    print(f"Je divise {_fisrt} par {_second}",end=f"{_end}")
    return float(_fisrt / _second)

# @main
while True:
    try:
        a : int = int(input(">nombre a:"))
        b : int = int(input(">nombre b:"))
        print(soustraire(a,b))
        print(format(diviser(a,b),'.2f'))
        break
    except ValueError as err:
        print(ValueError.__name__,err)