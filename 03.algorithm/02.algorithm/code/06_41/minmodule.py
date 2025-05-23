class MinAlgorithm:
    def __init__(self,n):
        self.nums = n
        self.minNum = 0
        self.minCnt=0

    def setMinNum(self):
        self.minNum=self.nums[0]
        for i in self.nums:
            if self.minNum>i:
                self.minNum=i

    def getMinNum(self):
        self.setMinNum()
        return self.minNum

    def setMinCnt(self):
        self.setMinNum()
        for i in self.nums:
            if self.minNum==i:
                self.minCnt+=1
        return self.minCnt

    def getMinCnt(self):
        self.setMinCnt()
        return self.minCnt