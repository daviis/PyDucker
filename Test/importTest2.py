from importTest3 import randnum

def sqrr(b):
    '''
    @b:float
    '''
    c =b**2
    return c



def randsqr():
    d = (randnum())**2
    return d

class operations():
    
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        
    def getx(self):
        return self.x