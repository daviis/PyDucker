'''
aTuple = (1, 2, 3) #tuple
aTupleComp = (x for x in [1,2])  #generatorexp
  
aSet = {1, 2, 3} #a set
aSetComp = { x for x in [1]} #setcomp
aSetCompIf = { x for x in [1] if x < 0} #setcomp with an if to test visit_comprehension
    
aDict = {1:'a', 2:'b'} #dict
aDictComp = { x : x+1 for x in [1]} #dictcomp
   
aList = [1, 2, 3] #a list
aListComp = [ x for x in [1]]
 
nonStarred, *aStarred = (1, 2, 3) #starred and tuple unpacking

x = 'hello'
x[1]
z = 'hello'[0]
a = x[0]
b = x[0]


y = [1,2,3]
y[0]
c = y[1]
'''
d = {'a':1, 'b':2}

e = d['a']

pass