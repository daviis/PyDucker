#global check
x = 0
def makeX():
    global x
    x = 1
    pass
    def makeY():
        x = 2
        pass
#         print("makey: ", x)
    pass
    makeY()
#     print("makex: ", x)
pass
makeX()
# print("global: ", x)

#nonlocal check
a = 'a'
b = 1
def makeA():
    a = 'b'
    
    def makeB():
        nonlocal a
        a = 'c'
        def makeC():
            nonlocal a
            a = 'd'
            b =2
            pass
        makeC()
    makeB()
makeA()
