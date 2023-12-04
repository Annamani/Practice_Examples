# # Instance Attributes
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.legs = 4
    
#     def speak(self):
#         print(self.name + ' says: Bark!')

# myDog = Dog('Rover')
# print(myDog.name)
# print(myDog.legs)

# Static Atributes
class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name
        
    def getLegs(self):
        return self._legs
    
    def speak(self):
        print(self.name + ' says: Bark!')
    def eat(self):
        print(self.name + ' Eat: Chicken!')

myDog = Dog('Rover')
myDog._legs = 3
print(myDog.name)
print(myDog.getLegs())
print(Dog._legs)
print(myDog.speak())