def binarFuc(nums,inputNum):
    ### 찾는 값의 인덱스
    findIdx=-1
    ### 시작 인덱스와 마지막 인덱스
    startIdx=0
    endIdx=len(nums)-1
    ### 반으로 나눌 인덱스 및 값
    midIdx=(startIdx+endIdx)//2
    midVal=nums[midIdx]
    print(f"startIdx : {startIdx}, endIdx : {endIdx}, midIdx : {midIdx}, midVal : {midVal}")
    print(f"midIdx : {midIdx}, midVal : {midVal}")

    ### 반으로 나누기 시작
    ### 찾는 숫자가 범위 내에 있을 때까지 실행 -> 범위에 없으면 실행 X
    while inputNum>=nums[0] and inputNum<=nums[len(nums)-1]:
        ### 마지막 값과 같다면 그만함
        if inputNum==nums[len(nums)-1]:
            findIdx=len(nums)-1
            break
        ### 무한 루프 방지용
        ### 시작 값과 끝 값이 하나 차이
        ### 값지 같지 않다면 끝
        if startIdx+1==endIdx:
            if nums[startIdx]!=nums[endIdx]:
                break

        ### 반씩 진행
        ### 값이 같지 않다면 새로운 midVal과 midIdx생성
        ### 중간 값보다 큰경우 : 끝값 고정 시작 값 조정
        if inputNum > midVal:
            startIdx=midIdx
            midIdx=(startIdx+endIdx)//2
            midVal=nums[midIdx]
            print(f"startIdx : {startIdx}, endIdx : {endIdx}, midIdx : {midIdx}, midVal : {midVal}")
        ### 중간 값보다 작은 경우 : 끝값 조정 시작 값 고정
        elif inputNum < midVal:
            endIdx=midIdx
            midIdx = (startIdx + endIdx) // 2
            midVal = nums[midIdx]
        ### 값을 찾은 경우
        elif inputNum == midVal:
            findIdx=midIdx
            break

    return findIdx