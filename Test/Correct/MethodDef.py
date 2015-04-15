def add(a, b=1):
    '''
    @a:int
    @b:int
    '''
    return a + b 
 
def sub(a, b=666, c="w", *d, **e):
    '''
    @a:float
    @b:int
    @d:str*
    @e:**int:str
    '''
    return a - b
  
def noPrams():
    return 5

def takeList(lst):
    """
    @lst:int*
    """
    return lst

#test the set up functions



x = add(3)
w = add(2, 3)
z = add(2, b=4)
v = takeList([1,2,3])

pass