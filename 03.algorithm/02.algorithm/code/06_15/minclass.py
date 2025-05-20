class MinClass:
    def __init__(self,n):
        self.nums=n
        self.minNum=0

    def getMaxNum(self):
        self.minNum = self.nums[0]
        for i in self.nums:
            if i < self.minNum:
                self.minNum = i
        return self.minNum



ma=MinClass([-2,-4,5,7,10,0,8,20,-11])
minNum=ma.getMaxNum()
print(f"minNum : {minNum}")