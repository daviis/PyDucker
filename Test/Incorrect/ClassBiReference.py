"""
This will infinitely recurse upon building an object
"""

class a():
    def __init__(self):
        self.z = b()
        
    def __add__(self, other):
        return self.z + other
    
class b():
    def __init__(self):
        self.w = a()
        
        
        
def main():
    h = a()
    j = b()
    print(h + 1)
    print(j + 1)
    
main()