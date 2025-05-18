### 튜플 오름차순 및 내림차순
fruits = ({"수박":8},{"포도": 13},{"참외" : 12},{"사과": 17},{"자두" : 19},{"자몽" : 15})

fruits = list(fruits)
cIdx=0;nIdx=1;eIdx=len(fruits)-1
flag = True

while flag:
    curDic = fruits[cIdx]
    nextDic = fruits[nIdx]

    curDicCnt = list(curDic.values())[0]
    nexDicCnt = list(nextDic.values())[0]

    if nexDicCnt < curDicCnt:
        fruits.insert(cIdx,fruits.pop(nIdx))
        nIdx = cIdx + 1
        continue
    nIdx += 1
    if nIdx > eIdx:
        cIdx += 1
        nIdx =cIdx+1
        if cIdx == 5:
            flag = False


print(f"오름차순 : {fruits}")