class FrequentNum:
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


nums = [1,3,7,6,7,7,7,12,12,17]
mn=FrequentNum(nums)
mn.getMax()
maxN=mn.getMaNum()

### 0도 포함해야 해서 maxN + 1
indexes=[0 for i in range(maxN+1)]

### nums에서 i값이 나올 때마다 indexs[i]에 1을 추가
for i in nums:
    indexes[i]=indexes[i]+1

maxAlgo = FrequentNum(indexes)
maxAlgo.getMax()
print(f"최빈값 : {maxAlgo.maxNumIdx}\t최빈값 : {maxAlgo.maxNum}")