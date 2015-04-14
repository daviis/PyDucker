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
    @e:int**str
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

#incorrect ones 
#todo move to incorrect dir
t = add() #Exceptions.IncorrectMethodException, should raise an exception about not enough args, could make message more helpful
y = add('w') #Exceptions.IncorrectMethodException b/c str
s = add(3, z=2) #Exceptions.IncorrectMethodKeywordException b/c 'z'

pass