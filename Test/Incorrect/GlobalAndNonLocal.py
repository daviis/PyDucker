#This will generate an error about how nonlocal a was really supposed to be global a
a = 'a'
def makeA():
    global a
    a = 'b'
    def makeB():
        nonlocal a
        a = 'c'
        print("makeb: ", a)
    makeB()
    print("makeba:", a)
makeA()
print("global: ", a)


#This will generate a warning about how b isn't really a global var.
a = 'a'
def makeA():
    global b
    a = 'b'
    def makeB():
        nonlocal a
        a = 'c'
        print("makeb: ", a)
    makeB()
    print("makeba:", a)
makeA()
print("global: ", a)