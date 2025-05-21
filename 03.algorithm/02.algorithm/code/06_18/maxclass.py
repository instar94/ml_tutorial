class MaxClass:
    def __init__(self,n):
        self.nums=n
        self.maxNum=0
        self.maxNumIdx=0
    ### 최대값 호출
    def getMax(self):
        self.maxNumIdx=0
        self.maxNum=self.nums[0]

        ### 큰 n값을 max값으로 해당 인덱스는 i
        for i,n in enumerate(self.nums):
            if self.maxNum<n:
                self.maxNum=n
                self.maxNumIdx=i

    ### 최대값 출력
    def getMaNum(self):
        return self.maxNum

    ### 최대값 인덱스 출력
    def getMaxIdx(self):
        return self.maxNumIdx
