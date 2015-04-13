def generator2():
    for i in range(10):
        yield i

def generator3():
    for j in range(10, 20):
        yield j

def generator1():
    for i in generator2():
        yield i
    for j in generator3():
        yield j

def _tmpfunc():
    for x in [0,1,2,3,4]: 
        yield x

lst = _tmpfunc()
for w in lst:
    w
