import copy
def bubbleSort(nums, asc=True):
    copyNums=copy.copy(nums)
    length=len(copyNums)-1

    for i in range(length):
        for j in range(length):
            ### 큰데 뒷쪽으로 가도록 설정
            if asc:
                if copyNums[j]<copyNums[j+1]:
                    copyNums[j],copyNums[j+1]=copyNums[j+1],copyNums[j]
                if copyNums[j]>copyNums[j+1]:
                    copyNums[j], copyNums[j + 1] = copyNums[j+1], copyNums[j]
                print(f"nums : {copyNums}")
            else :
                if copyNums[j] > copyNums[j + 1]:
                    copyNums[j], copyNums[j + 1] = copyNums[j + 1], copyNums[j]
                if copyNums[j] < copyNums[j + 1]:
                    copyNums[j], copyNums[j + 1] = copyNums[j + 1], copyNums[j]
                print(f"nums : {copyNums}")
    return copyNums