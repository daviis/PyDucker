def makeX():
    x = 6
    def makeY(y):
        x = x + 1
        print(x)
    makeY(2)
        
makeX()