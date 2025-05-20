class Select:
    def __init__(self, ns, ascTrue):
        self.num=ns
        self.isAsc=ascTrue

    def isAscFunc(self,flag):
        self.isAsc=flag

    def setSort(self,ns,ascTrue):
        if ascTrue:
            for i in range(len(ns) - 1):
                minIdx = i
                for j in range(i + 1, len(ns)):
                    if ns[minIdx] > ns[j]:
                        minIdx = j
                ns[i],ns[minIdx]=ns[minIdx],ns[i]
        else:
            for i in range(len(ns) - 1):
                minIdx = i
                for j in range(i + 1, len(ns)):
                    if ns[minIdx] < ns[j]:
                        minIdx = j
                ns[i],ns[minIdx]=ns[minIdx],ns[i]
        return ns


    def getSortNum(self):
        return self.num

