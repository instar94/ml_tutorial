class Insert:
    def __init__(self, ns, ascTrue):
        self.num=ns
        self.isAsc=ascTrue

    def isAscFunc(self,flag):
        self.isAsc=flag

    def setSort(self):
        for i in range(1,len(self.num)):
            j = i -1
            cNum = self.num[i]

            if self.isAsc:
                while self.num[j]> cNum>=0 and j>=0:
                    self.num[j+1] = self.num[j]
                    j-=1
            else :
                while self.num[j]<cNum and j>=0:
                    self.num[j+1]=self.num[j]
                    j-=1

            self.num[j+1]=cNum

    def getSortNum(self):
        return self.num

    def getMin(self):
        if self.isAsc:
            return self.num[0]
        else:
            return self.num[len(self.num)-1]

    def getMax(self):
        if self.isAsc:
            return self.num[len(self.num) - 1]
        else:
            return self.num[0]

