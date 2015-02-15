class doStuff():
    def __enter__(self):
        pass
    def __exit__(self,type,value,traceback):
        bytes(1)
        with doStuff() as thing:
            x = 1
y = 'y'
del(y)