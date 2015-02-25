values = [(yield from (i, i + 1, i)) for i in range(5)]

def _tmpfunc():
    for x in range(5): 
        yield (yield from (i, i + 1, i))

values = list(_tmpfunc())

