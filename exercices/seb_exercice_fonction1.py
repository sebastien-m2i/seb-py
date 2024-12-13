# @functions
def printNames(_s50_first_name,_s50_name,_b_cap=False):
    s_100_result = f"{_s50_first_name} {_s50_name}"
    return print(s_100_result.upper()) if _b_cap else print(s_100_result)

def findCarA(_s50_string):
    it = 0
    for car in _s50_string:
        if car.upper() == "A": it +=1
    return it

# @main
while True:
    try:
        s50_first_name = input(">set your firstname :")
        s50_name = input(">set your name :")
        printNames(s50_first_name,s50_name)
        printNames(s50_first_name,s50_name,True)
        print(f"Nombre de a dans {s50_first_name} =",findCarA(s50_first_name))
        findCarA("")
        break
    except Exception as _mess_err:
        print(Exception.__name__,_mess_err)

# @test1
# >set your firstname :seb
# >set your name :quin
# seb quin
# SEB QUIN