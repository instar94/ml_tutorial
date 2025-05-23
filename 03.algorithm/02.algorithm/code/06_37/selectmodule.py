import copy
def selectSort(nums, asc=True):
    copyNums=copy.copy(nums)
    length=len(copyNums)-1
    for i in range(0,length):
        minIdx=i
        ### 오름차순
        if asc :
            ### i와 i+1~끝까지 비교
            for j in range(i+1,length+1):
                if copyNums[j] < copyNums[minIdx]:
                    minIdx=j
            tempNum=copyNums[i]
            copyNums[i]=copyNums[minIdx]
            copyNums[minIdx]=tempNum
            print(f"nums : {copyNums}")
        ### 내림차순
        else :
            for j in range(i + 1, length + 1):
                if copyNums[j] > copyNums[minIdx]:
                    minIdx = j
            tempNum = copyNums[i]
            copyNums[i] = copyNums[minIdx]
            copyNums[minIdx] = tempNum
            print(f"nums : {copyNums}")
    return copyNums