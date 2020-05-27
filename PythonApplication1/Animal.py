class Animal(object):
    """description of class"""
    def descrire(self):
        print("je suis animal")

class chien(Animal):
    def descrire(self):
        Animal.descrire(self)
        print("je suis uyn chien")


c = chien()
c.descrire()




