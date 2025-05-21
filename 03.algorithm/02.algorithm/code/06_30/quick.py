### 1~100까지의 난수 10개 생성
### 퀵정렬을 이용하여 ASC DESC로
import random


def qSort(ns,isAsc):
    ### 원소 1개 리스트가 나올때까지 반복
    if len(ns)<2:
        return ns

    ### 중간 인덱스 및 값
    midIdx=len(ns)//2
    midVal=ns[midIdx]

    ###작은 값/중간 값/큰 값 리스트
    smallNums=[];samNums=[];bigNums=[]
    if isAsc:
        ### 분류
        for n in ns:
            ###작은 값일 경우
            if n < midVal:
                smallNums.append(n)
            ### 같은 값일 경우
            elif n == midVal:
                samNums.append(n)
            ### 큰 값일 경우
            else:
                bigNums.append(n)
        return qSort(smallNums,isAsc) + samNums + qSort(bigNums,isAsc)
    else:
        for n in ns:
            ###작은 값일 경우
            if n < midVal:
                smallNums.append(n)
            ### 같은 값일 경우
            elif n == midVal:
                samNums.append(n)
            ### 큰 값일 경우
            else:
                bigNums.append(n)
        return  qSort(bigNums, isAsc) + samNums  + qSort(smallNums, isAsc)



rNums=random.sample(range(1,101),10)
print(f"정렬 전 - rNums : {rNums}")
ascSort=qSort(rNums,True)
print(f"오름차순- rNums : {ascSort}")
descSort=qSort(rNums,False)
print(f"내림차순- rNums : {descSort}")