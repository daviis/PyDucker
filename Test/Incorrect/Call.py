# 'a'.uppereddeded(3)
'a'.upper(3)

#this is an exapmle of Exceptions.KeyWordFromAVariable
a = "end"
print("hi", **{a:''})


#this is an example of a keyword that isn't possible:
print("hi", **{"enda":''})

def add(a, b=1):
    '''
    @a:int
    @b:int
    '''
    return a + b 

#incorrect ones 
#todo move to incorrect dir
t = add() #Exceptions.IncorrectMethodException, should raise an exception about not enough args, could make message more helpful
y = add('w') #Exceptions.IncorrectMethodException b/c str
s = add(3, z=2) #Exceptions.IncorrectMethodKeywordException b/c 'z'