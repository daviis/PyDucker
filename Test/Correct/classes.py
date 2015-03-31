
class Animal():
    #x = 1
    def __init__(self, idNum):
        """
        @idNum:int
        """
        #self.id = idNum
        id = idNum
        
    def speak(self):
        print("i dont talk")
        
    class breakStuff():
        def __init__(self):
            things = 'stuff'
        def doThings(self):
            print('i probably broke this')
            
x = Animal(1)
x.speak()

class cat(Animal):
    def fall(self):
        print('i fell')

    
pass