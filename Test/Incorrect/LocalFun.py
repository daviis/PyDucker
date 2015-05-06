#this test is currently broken, but I dont have time to fix it before Friday

def makeX():
    x = 6
    def makeY(y):
        """
        @y:int
        """
        x = x + 1
        print(x)
    makeY(2)
        
makeX()