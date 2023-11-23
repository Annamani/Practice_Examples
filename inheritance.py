class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark!')
    
    def getLegs(self):
        return self._legs

class Snoopy(Dog):
    def speak(self):
        print(f'{self.name} says: Bow Bow Bow')


dog=Dog("Booster")
dog.speak()