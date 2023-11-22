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
    legs = 4
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)