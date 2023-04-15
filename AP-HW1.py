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

class Fish(VertebratesAnimal):
    def __init__(self, age, gender, diet, name, habitat, species, color, lifespan: int, gills: int, coldblooded : bool = True):
        super().__init__(age, gender, diet, name, habitat)
        self.Species = species
        self.Color = color
        self.Lifespan = lifespan
        self.Gills = gills
        self.Coldblooded = coldblooded

    def swim(self):
        return f"{self.name} swims in the water"
    def breathe(self):
        return f"{self.name} breathes using {self.Gills} gills."
    def reproduce(self):
        return f"{self.name} reproduces with releasing its gametes"
    def getcolor(self):
        return f"{self.name} is {self.Color}."
    def hunt(self, bait):
        return f"{self.name} hunting the {bait}."
    def description(self):
        if self.Coldblooded == True:
            return f"{self.name} is {self.Species} and coldblooded fish with {self.age} years old"
        else:
            return f"{self.name} is {self.Species} and warmblooded fish with {self.age} years old"
f = Fish(3, "male", "little fish", "fishfish", "water", "Shark", "blue", 10, 5, True)
print(f.breathe())
print(f.swim())
print(f.getcolor())
print(f.description())
print(f.hunt("little fish"))
print(f.reproduce())

class Reptile(VertebratesAnimal):
    def __init__(self, age, gender, diet, name, habitat, weight : int, species, reproduction, is_wild : bool = True):
        super().__init__(age, gender, diet, name, habitat)
        self.Weight = weight
        self.Species = species
        self.Is_wild = is_wild
        self.Reproduction = reproduction
    def move(self):
        return f"{self.name} is moving"
    def hunt(self, bait):
        return f"{self.name} hunted the {bait}"
    def bask(self):
        return f"{self.name} basks in the sun."
    def shed(self):
        return f"{self.name} sheds its skin"
    def description(self):
        return f"{self.name} is {self.age} years old. it reproduces with {self.Reproduction} method. it has {self.Weight} kg."

r = Reptile(4, "male", "meat", "Lizi", "deserts", 5, "Lizard", "lay eggs", False)
print(r.move())
print(r.hunt("fly"))
print(r.shed())
print(r.bask())
print(r.description())