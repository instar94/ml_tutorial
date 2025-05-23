import copy
def insertSort(nums,asc=True):
    cNums = copy.copy(nums)
    for i in range(1,len(cNums)):
        ### 전에 꺼에 계속 비교
        j=i-1
        ### 현재 정렬을 하고자 하는 원소
        cNum=cNums[i]
        if asc:
            ### 현재 숫자보다 다음수가 크거나
            ### 인덱스가 0보다 클 때 까지 반복
            while cNums[j] > cNum and j >= 0:
                cNums[j + 1] = cNums[j]
                j -= 1
        else:
            while cNums[j] < cNum and j >= 0:
                cNums[j + 1] = cNums[j]
                j -= 1
        cNums[j+1]=cNum
        print(f"cNums : {cNums}")
    return cNums