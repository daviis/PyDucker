# (1, 2, 3) #tuple
# (x for x in [1,2])  #generatorexp
# 
# # {1, 2, 3} #a set
# { x for x in [1]} #setcomp
# { x for x in [1] if x < 0} #setcomp with an if to test visit_comprehension
#   
# {1:'a', 2:'b'} #dict
# { x : x+1 for x in [1]} #dictcomp
#  
# [1, 2, 3] #a list
# [ x for x in [1]]
 
a, *b = (1, 2, 3) #starred and tuple unpacking
c =1