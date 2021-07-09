class Emp:
    comp="google"
    def show(self):
        print("this is emp")


class c():
    comp = "oooooe"
    def greet(self):
      print("helooooooo")

class progrm(c,Emp):
     lang="python"

     def get(self):
         print("company is", self.comp)
         print("languae is",self.lang)


a=progrm()
a.show()
a.get()
a.greet()