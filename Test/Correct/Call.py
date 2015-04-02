a = 'a'
b = a.upper()
pass

print()
print("hi")
print("hi" + "hi")
print("hi", "hi")
print("hi", end="")
print("hi", **{"end":''})
 
#check for implicit conversions.
print(1)
print("hi", *(1,2), end ="")