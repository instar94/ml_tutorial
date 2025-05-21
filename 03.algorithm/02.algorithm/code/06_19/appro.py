class ApproClass:
    def __init__(self,n):
        self.nums=n
        self.absNum=[]
        self.minNum=0

    ### 차이의 절대값 찾기
    def getAbs(self,inputNum):
        for i in self.nums:
            tempNum = abs(i - inputNum)
            self.absNum.append(tempNum)
        return self.absNum

    ### 최소값 찾기
    def getMin(self,absNum):
        ### 첫번째 값으로 초기화
        minNum=absNum[0]
        ### 작은 값으로 minNum선언
        for i in absNum:
            if i < minNum:
                minNum = i
        return minNum

nums=[7,43,14,44,6,26,24,3,25,47,2,32,27,38,18,17,33,29,29,0]
inputNum = int(input("근사값을 찾을 값 : "))

ac=ApproClass(nums)
ain=ac.getAbs(inputNum)
print(ain)
minNum=ac.getMin(ain)
print(f"{minNum}")