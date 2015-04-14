class nums:
    def __init__(self, numWanted):
        """
        @numWanted:int
        """
        self.userNum = numWanted
        x = self.userNum
        
    def getNums(self):
        return [x for x in range(self.userNum)]
    
    def __call__(self):
        return 1
    
a = nums(5)
b = a.getNums()
a.userNum = 10
c = a()
        
pass