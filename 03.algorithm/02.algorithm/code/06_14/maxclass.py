class MaxClass:
    def __init__(self,n):
        self.nums=n
        self.maxNum=0

    def getMaxNum(self):
        self.maxNum = self.nums[0]
        for i in self.nums:
            if i > self.maxNum:
                self.maxNum = i
        return self.maxNum



ma=MaxClass([-2,-4,5,7,10,0,8,20,-11])
maxNum=ma.getMaxNum()
print(f"maxNum : {maxNum}")