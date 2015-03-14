
values = [(yield from (i, i + 1, i)) for i in [0,1,2,3,4]]

def _tmpfunc():
    for x in [0,1,2,3,4]: 
        yield x

lst = _tmpfunc()
for w in lst:
    w
