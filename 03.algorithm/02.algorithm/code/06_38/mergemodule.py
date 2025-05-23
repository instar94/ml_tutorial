import copy

def mergeSort(nums, asc=True):
    copyNums=copy.copy(nums)
    length=len(copyNums)-1

    for i in range(len(copyNums)-1):
        minIdx=i
        ### 오름차순
        for j in range(i+1,len(copyNums)):
            if asc :
                ### i와 i+1~끝까지 비교
                if copyNums[minIdx]>copyNums[j]:
                    minIdx=j
            ### 내림차순
            else:
                if copyNums[minIdx]<copyNums[j]:
                    minIdx=j
        copyNums[i],copyNums[minIdx]=copyNums[minIdx],copyNums[i]
        print(f"nums : {copyNums}")
    return copyNums