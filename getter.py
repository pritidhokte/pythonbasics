class emp:
    sal = 1500
    inc = 2

    @property
    def aftersal(self):
        return self.inc * self.sal

    @aftersal.setter
    def aftersal(self, sai):
        self.inc = sai / self.sal

e=emp()
print(e.aftersal)
print(e.inc)
e.aftersal=2000
print(e.inc)