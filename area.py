def triangle():
    base = float(input("enter base"))
    height = float(input("enter "))
    print(0.5 * base * height)


def square():
    side = float(input("enter side"))
    print(side * 4)


def circle():
    r = float(input("enter radius"))
    print(3.14 * r * r)


while True:
    choice = int(input("enter ur choice"))
    areaof = {
        1: triangle,
        2: square,
        3: circle,
        4: exit
    }
    output = areaof[choice]()
    #print(output)
