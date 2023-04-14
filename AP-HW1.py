class VertebratesAnimal:
    def __init__(self, age: int, gender: str, diet: str, name: str, habitat: str):
        self.age = age
        self.gender = gender
        self.diet = diet
        self.name = name
        self.habitat = habitat
    def genAge(self):
        return self.age
    def getGender(self):
        return self.gender
    def getDiet(self):
        return self.diet
    def getName(self):
        return self.name
    def getHabitat(self):
        return self.habitat

v = VertebratesAnimal(15,"male","food","odise","place")
print(v.name)

class Mammals(VertebratesAnimal):
    def __init__(self, age, gender, diet, name, habitat, species, covering, lifespan, fourchamberedheart, hibernate: bool = True):
        super().__init__(age, gender, diet, name, habitat)
        self.species = species
        self.covering = covering
        self.lifespan = lifespan
        self.fourchamberedheart = fourchamberedheart
        self.Hibernate = hibernate
    def move(self):
        return f"{self.name} is moving"
    def swim(self):
        return f"{self.name} can swim"
    def communicate(self):
        return f"{self.name} can communicate"
    def hibernate(self):
        if self.hibernate == True:
            return f"{self.name} can hibernate"
        else:
            return f"{self.name} can not hibernate"
    def description(self):
        return f"{self.name} is {self.species} mammals with {self.covering} body and {self.age} years old "

m = Mammals(23, "male", "meat", "Beeeear", "snow", "polar bear", "hair", 15, "Yes",False)
print(m.swim())
print(m.covering)
print(m.hibernate())
print(m.description())
print(m.move())
print(m.communicate())

class Birds(VertebratesAnimal):
    def __init__(self, age: int, gender: str, diet: str, name: str, habitat: str, species, wingspan, lifespan, beakkind, is_wild: bool = True):
        super().__init__(age, gender, diet, name, habitat)
        self.Species = species
        self.Wingspan = wingspan
        self.Lifespan = lifespan
        self.Beakkind = beakkind
        self.Is_wild = is_wild

    def fly(self):
        return f"{self.name} is flying"
    def sing(self):
        return f"{self.name} is singing"
    def buildnests(self):
        return f"{self.name} builds a nest"
    def migrate(self):
        return f"Many species of bird migrate"
    def hunt(self, bait):
        if self.Is_wild == True:
            return f"{self.name} hunted the {bait}"
        else:
            return f"{self.name} is not wild"
b = Birds(12,"male","wheat","parrot","nest","house sparrow", "circle",20,"curvy",True )
print(b.fly())
print(b.sing())
print(b.name)
print(b.migrate())
print(b.Wingspan)
print(b.hunt("rabbit"))
print(b.buildnests())
