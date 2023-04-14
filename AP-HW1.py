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
