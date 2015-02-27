x = 0
def makeX():
#     global x
    x = 1
    def makeY():
        nonlocal x
        x = 2
#         print("makey: ", x)
    makeY()
#     print("makex: ", x)
makeX()
# print("global: ", x)