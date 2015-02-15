class doStuff():
    def __enter__(self):
        pass
    def __exit__(self,type,value,traceback):
        with doStuff() as thing:
            x = 1
y = [1,2,3]
z = '1'
del(y[0])
del(z)