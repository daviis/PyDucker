import math


from importTest2 import sqrr
from importTest2 import operations
from importTest2 import randsqr

def sqrt(a):
    '''
    @a:float
    '''
    b = math.sqrt(a)
    return b
print(sqrt(25))
print(sqrr(sqrt(25)))
print(randsqr())
def sqrsum(x,y):
        return((x+y)**2)

fun = operations(5,6)
print(fun.getx())
print(sqrsum(5,2))