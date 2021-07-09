class cal:
    def __init__(self,num):
        self.num=num

    def square1(self):
        print(f"square is{self.num**2}")

    def cube(self):
        print(f"cube is{self.num**3}")

    def squareroot(self):
        print(f"square root{self.num**0.5}")
s=int(input("enetr no"))
a = cal(s)
a.square1()
a.cube()
a.squareroot()