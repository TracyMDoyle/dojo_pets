class Pet:
    def __init__(self, name , type , tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy = self.energy + 25
        return self

    def play(self):
        self.health = self.health + 5
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def call(self):
        print(self.noise)


class Ninja:
    def __init__ (self, first_name , last_name , treats , pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self
            
    def bathe(self):
        self.pet.call()


Fido = Pet("Fido", "Dog", "RollOver", "RuffRuff")
John = Ninja("John", "Smith", "cookies", "kibble", Fido)





print(Fido.health)
print(John.pet.name)
John.bathe()
John.walk()
print(Fido.health)
John.feed()
print(Fido.health)