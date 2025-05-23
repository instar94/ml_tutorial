class FreqAlgorithm:
    def __init__(self,n):
        self.nums = n
        self.maxNum = 0
        self.freqCnt=[]

    def getMaxNum(self):
        self.maxNum = self.nums[0]
        for i in self.nums:
            if i > self.maxNum:
                self.maxNum = i
        print(f"maxNum : {self.maxNum}")
        return self.maxNum

    def setFreqNum(self):
        self.freqNum=self.nums[0]
        self.maxNum=self.getMaxNum()
        self.freqCnt=[0 for i in range(self.maxNum)]
        for i,v in enumerate(self.nums):
            self.freqCnt[v-1]=self.freqCnt[v-1]+1
        print(f"freqCnt : {self.freqCnt}")

    def getFreqNum(self):
        self.setFreqNum()
        return self.freqCnt
