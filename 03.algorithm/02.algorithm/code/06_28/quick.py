def qSort(ns):
    ### 원소 1개 리스트가 나올때까지 반복
    if len(ns)<2:
        return ns

    ### 중간 인덱스 및 값
    midIdx=len(ns)//2
    midVal=ns[midIdx]

    ###작은 값/중간 값/큰 값 리스트
    smallNums=[];samNums=[];bigNums=[]

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
    return qSort(smallNums) + samNums + qSort(bigNums)

nums=[8,1,4,3,2,5,4,10,6,8]
print(qSort(nums))