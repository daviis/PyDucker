class Animal():
    def __init__(self,animalId):
        """
        @animalId:int
        """
        self.animalId = animalId
        
    def speak(self):
        print('I can speak')
        
class Cat(Animal):
    def speak(self):
        print('I can change my speaking')
        
x = Animal(1)
y = Cat(2)

x.speak()
y.speak()
        