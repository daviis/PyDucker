class doStuff():
    def __enter__(self):
        pass
    def __exit__(self,type,value,traceback):
        with doStuff() as thing:
            x = 1