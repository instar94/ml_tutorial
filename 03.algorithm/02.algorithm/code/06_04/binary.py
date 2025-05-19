def serachBinary(datas):
    findNum=int(input("찾으려는 값 : "))
    findIdx=-1

    ### 데이터 정렬
    datas.sort()
    print(f"datas : {datas}")

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
        ### 숫자가 크면 뒷쪽에서 찾음
        if findNum > midVal:
            startIdx=midIdx
            midIdx=(startIdx+endIdx)//2
            midVal=datas[midIdx]
            print(midIdx)
        ### 숫자가 작으면 앞쪽에서 찾음
        elif findNum < midVal:
            endIdx=midIdx
            midIdx = (startIdx + endIdx) // 2
            midVal = datas[midIdx]
            print(midIdx)
        elif findNum == midVal:
            findIdx=midIdx
            break

    print(f"찾던 값의 인덱스 : {findIdx}")


datas = [4,10,22,5,0,17,7,11,9,61,88]
print(f"datas : {datas}")
serachBinary(datas)