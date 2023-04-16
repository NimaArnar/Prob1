class Feather():
    def __init__(self, owner: str, length: int, color: str, sort: str, is_curvy: bool, is_prickly: bool):
        self.Owner = owner
        self.Length = length
        self.Color = color
        self.Sort = sort
        self.Is_curvy = is_curvy
        self.Is_prickly = is_prickly
    def __str__(self):
        return f"owner = {self.Owner}, length = {self.Length}, sort = {self.Sort}, color = {self.Color}"
    def growth(self):
        return f"{self.Owner}'s feather is growing"
    def fall(self):
        return f"{self.Owner}'s feather is falling"
    def fly(self):
        return f"{self.Owner}' feather can be used for flight"
    def insulate(self):
        return f"feathers can insulate {self.Owner} from cold weather"
    def description(self):
        return f"{self.Owner} feather's color is {self.Color}. it is {self.Length} cm."

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
    def __init__(self, age, gender, diet, name, habitat, species: str, covering: str, lifespan: int, fourchamberedheart: bool = True, hibernate: bool = True):
        super().__init__(age, gender, diet, name, habitat)
        self.Species = species
        self.Covering = covering
        self.Lifespan = lifespan
        self.FourChamberedHeart = fourchamberedheart
        self.Hibernate = hibernate
    def move(self):
        return f"{self.name} is moving"
    def swim(self):
        return f"{self.name} can swim"
    def communicate(self):
        return f"{self.name} can communicate"
    def hibernate(self):
        if self.Hibernate == True:
            return f"{self.name} can hibernate"
        else:
            return f"{self.name} can not hibernate"
    def description(self):
        return f"{self.name} is {self.Species} mammals with {self.Covering} body and {self.age} years old "

m = Mammals(23, "male", "meat", "Beeeear", "snow", "polar bear", "hair", 15, False,False)
print(m.swim())
print(m.Covering)
print(m.hibernate())
print(m.description())
print(m.move())
print(m.communicate())

class Birds(VertebratesAnimal):
    def __init__(self, age: int, gender: str, diet: str, name: str, habitat: str, species: str, wingspan: str, lifespan: int, beakkind: str, is_wild: bool = True):
        super().__init__(age, gender, diet, name, habitat)
        self.Species = species
        self.Wingspan = wingspan
        self.Lifespan = lifespan
        self.Beakkind = beakkind
        self.Is_wild = is_wild
        self.Feather = None # Composition
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
b.Feather = Feather(b.name,10,"black","Down", True,False)
print(b.fly())
print(b.sing())
print(b.name)
print(b.migrate())
print(b.Wingspan)
print(b.hunt("rabbit"))
print(b.buildnests())
print(b.Feather.fall())
print(b.Feather)

class Fish(VertebratesAnimal):
    def __init__(self, age, gender, diet, name, habitat, species, color, lifespan: int, gills: int, coldblooded : bool = True):
        super().__init__(age, gender, diet, name, habitat)
        self.Species = species
        self.Color = color
        self.Lifespan = lifespan
        self.Gills = gills
        self.Coldblooded = coldblooded

    def swim(self):
        return f"{self.name} swims in the water."
    def breathe(self):
        return f"{self.name} breathes using {self.Gills} gills."
    def reproduce(self):
        return f"{self.name} reproduces with releasing its gametes."
    def getcolor(self):
        return f"{self.name} is {self.Color}."
    def hunt(self, bait):
        return f"{self.name} hunting the {bait}."
    def description(self):
        if self.Coldblooded == True:
            return f"{self.name} is {self.Species} and coldblooded fish with {self.age} years old."
        else:
            return f"{self.name} is {self.Species} and warmblooded fish with {self.age} years old."
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
        return f"{self.name} is moving."
    def hunt(self, bait):
        return f"{self.name} hunted the {bait}."
    def bask(self):
        return f"{self.name} basks in the sun."
    def shed(self):
        return f"{self.name} sheds its skin."
    def description(self):
        return f"{self.name} is {self.age} years old. it reproduces with {self.Reproduction} method. it has {self.Weight} kg."

r = Reptile(4, "male", "meat", "Lizi", "deserts", 5, "Lizard", "lay eggs", False)
print(r.move())
print(r.hunt("fly"))
print(r.shed())
print(r.bask())
print(r.description())

class Amphibians(VertebratesAnimal):
    def __init__(self, age, gender, diet, name, habitat, skintype, reproduction, breathe, species, hibernates: bool = False):
        super().__init__(age, gender, diet, name, habitat)
        self.Skintype = skintype
        self.Reproduction = reproduction
        self.Hibernates = hibernates
        self.Breathe = breathe
        self.Species = species
    def breathing(self):
        return f"{self.name} breathes through its {self.Breathe}."
    def swim(self):
        return f"{self.name} can swim."
    def jump(self):
        return f"{self.name} is jumping."
    def camouflage(self, place):
        return  f"{self.name} can camouflage with {place}."
    def description(self):
        return f"{self.name} is {self.Species} amphibian with {self.Skintype} skin. "
a = Amphibians(2,"male","fly","frogy","fresh water","smooth","eggs","skin","grass frogs",True)
print(a.breathing())
print(a.swim())
print(a.jump())
print(a.camouflage("trees"))
print(a.description())

class Whale(Mammals):
    def __init__(self, age, gender, diet, name, habitat, species, covering, lifespan, fourchamberedheart, hibernate, weight, color, length):
        super().__init__(age, gender, diet, name, habitat, species, covering, lifespan, fourchamberedheart, hibernate)
        self.Weight = weight
        self.Color = color
        self.Length = length
    def getWeight(self):
        return f"{self.name}'s weight is {self.Weight} Kgs."
    def getColor(self):
        return f"{self.name}'s color is {self.Color}."
    def getLentgh(self):
        return f"{self.name}'s length is {self.Length} meters."
    def hunt(self, bait):
        return f"{self.name} is hunting the {bait}."
w = Whale(12,"male","fish","whalee","water","Whales","smooth skin",20,True,False,"500","White","10")
print(w.swim())
print(w.description())
print(w.move())
print(w.hibernate())
print(w.getLentgh())
print(w.getColor())
print(w.getWeight())
print(w.hunt("red fish"))

class Humans(Mammals):
    def __init__(self, age, gender, diet, name, habitat, species, covering, lifespan, fourchamberedheart, hibernate, left_eye_level: float = 0.0, right_eye_level: float = 0.0 , hair_color: str = "Black",skin_color: str = "White", heart_side: str = "Left"):
        super().__init__(age, gender, diet, name, habitat, species, covering, lifespan, fourchamberedheart, hibernate)
        self.Left_Eye_Level = left_eye_level
        self.Right_Eye_Level = right_eye_level
        self.Hair_Color = hair_color
        self.Skin_Color = skin_color
        self.Heart_side = heart_side
    def display(self):
        if self.gender == "male":
            return f"{self.name}' hair color is {self.Hair_Color} and his skin color is {self.Skin_Color}. his heart in {self.Heart_side} side of the body."
        else:
            return f"{self.name}' hair color is {self.Hair_Color} and her skin color is {self.Skin_Color}. her heart in {self.Heart_side} side of the body."
    def eyeslevel(self):
        return f"{self.name}'s left and right level is ({self.Left_Eye_Level},{self.Right_Eye_Level})."
    def see(self, target):
        return f"{self.name} is seeing the {target}."
    def hear(self, voice):
        return f"{self.name} is listening to the {voice}."
    def touch(self, object):
        return f"{self.name} is touching the {object}."
h = Humans(20, "male", "milk", "Nima", "house", "Humans", "hair", 80, True, False, 2.5, 1.5,"Black", "White", "Left")
print(h.description())
print(h.display())
print(h.see("flower"))
print(h.hibernate())
print(h.hear("music"))
print(h.touch("water"))
print(h.eyeslevel())