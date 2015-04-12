class nums:
    def __init__(self, numWanted):
        """
        @numWanted:int
        """
        self.userNum = numWanted
        
    def getNums(self):
        return [x for x in range(self.userNum)]
    
a = nums(5)
b = a.getNums()
            
pass