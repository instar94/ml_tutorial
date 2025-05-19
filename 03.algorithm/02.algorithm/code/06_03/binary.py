datas = [1,2,3,4,5,6,7,8,9,10,11]
print(f"datas : {datas}")

findNum=int(input("찾으려는 값 : "))
findIdx=-1

### 이진 검색을 위한 중앙값 찾기
startIdx=0
endIdx=len(datas)
midIdx=(startIdx+endIdx)//2

### 중앙값
midVal=datas[midIdx]

### 찾으려는 값이 마지막 값보다 같거나
### 찾으려는 값이 첫번째 값과 같기전까지
while datas[len(datas) - 1] >= findNum >= datas[0]:
    if findNum == datas[len(datas)-1]:
        findIdx=len(datas)-1
        break
    if findNum > midVal:
        startIdx=midIdx
        midIdx=(startIdx+endIdx)//2
        midVal=datas[midIdx]
        print(midIdx)
    elif findNum < midVal:
        endIdx=midIdx
        midIdx = (startIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(midIdx)
    elif findNum == midVal:
        findIdx=midIdx
        break

print(f"찾던 값의 인덱스 : {findIdx}")