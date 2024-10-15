class Dog:
    animal = 'dog'
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def setColor(self, color):
        self.color = color
    def getDetails(self):
        print("I have my pet and his name is " + self.name + " and he belongs to the breed of " + self.breed)
    def getColor(self):
        return self.color

petDog = Dog("Jimmy", "Pug")
petDog.setColor("White")
petDog.getDetails()
color = petDog.getColor()
print("Color: ", color)