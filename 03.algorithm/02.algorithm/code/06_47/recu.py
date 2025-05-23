### 최댓값과 최소값을 제외한 나머지 점수의 평균을 구하고 순위를 정하시오
scores=[6.7,5.9,8.1,7.9,6.7,7.3,7.2,8.2,6.2,5.8]
ranks = [9.12,8.95,8.12,6.9,6.18]
def rankFunc(n,s):
    newIdx=0
    for i,v in enumerate(n):
        if v < s :
            newIdx=i-1
    n.insert(newIdx,s)
    n.pop(len(n)-1)
    return n

def getAvg(n):
    maxNum=0
    minNum=n[0]
    for i in n:
        if i > maxNum:
            maxNum=i
        if i < minNum:
            minNum=i
    sumNum=sum(n)-(maxNum+minNum)
    print(f"maxNum : {maxNum}\t minNum : {minNum}\tsumNum : {sumNum}")
    avgNum = sumNum/(len(n)-2)
    return avgNum

if __name__ == "__main__":
    avgNum=getAvg(scores)
    print(f"평균 : {avgNum}")
    newRank=rankFunc(ranks,avgNum)
    print(f"순위 : {newRank}")