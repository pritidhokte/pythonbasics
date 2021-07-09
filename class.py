class programer:
    comp = "microsoft"

    def __init__(self, nm, prod):
        self.name = nm
        self.product = prod

    def getinfo(self):
        print("name is:", self.name)
        print("product is:", self.product)
        print("company is:", self.comp)


aaru = programer("Aru", "spky")
priti = programer("priti", "java")
aaru.getinfo()
priti.getinfo()
