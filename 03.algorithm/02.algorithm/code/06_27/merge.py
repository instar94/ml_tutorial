def mergeSort(n):
    ### 하나가 남을 때까지 반복
    if len(n)<2:
        return n
    ### 중간 지점의 지표
    midIdx = len(n)//2
    ### 왼쪽 : 0 ~ 중간까지
    leftNum = mergeSort(n[0:midIdx])
    ### 오른쪽 : 중간 ~ 끝까지
    rightNum = mergeSort(n[midIdx:len(n)])
    print(f"midIdx : {midIdx}\nleftNum  {leftNum}\nrightNum : {rightNum}")

    ###병합단계
    mergeNums=[]
    leftIdx=0;rightIdx=0
    ### 각 방향 인덱스가 중간 까지 될 때 까지
    while leftIdx<len(leftNum) and rightIdx < len(rightNum):
        ### 왼쪽꺼가 작으면 왼쪽꺼를 추가
        if leftNum[leftIdx] < rightNum[rightIdx]:
            mergeNums.append(leftNum[leftIdx])
            leftIdx+=1
        ### 오른쪽꺼가 작으면 오른쪽 꺼를 추가
        else:
            mergeNums.append(rightNum[rightIdx])
            rightIdx+= 1

    mergeNums= mergeNums + leftNum[leftIdx:]
    mergeNums = mergeNums + rightNum[rightIdx:]
    return mergeNums

nums=[8,1,4,3,2,5,10,6]
print(mergeSort(nums))