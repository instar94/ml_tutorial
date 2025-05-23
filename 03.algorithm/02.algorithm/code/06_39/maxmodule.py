class MaxAlgorithm:
    def __init__(self,n):
        self.nums = n
        self.max = 0
        self.maxCnt=0

    def setMaxNum(self):
        self.maxNum=0
        for i in self.nums:
            if self.maxNum<i:
                self.maxNum=i

    def getMaxNum(self):
        self.setMaxNum()
        return self.maxNum

    def setMaxCnt(self):
        self.setMaxNum()
        for i in self.nums:
            if self.maxNum==i:
                self.maxCnt+=1
        return self.maxCnt

    def getMaxCnt(self):
        self.setMaxCnt()
        return self.maxCnt