### 리스트에서 가장 앞에있는 숫자 7의 위치를 검색
### 인덱스 출력
### 모두 검색 후 인덱스와 검색 갯수 출력

def searchLiner(dates):
    ### 인덱스 리스트
    idxList = []

    ### 찾는 값
    searchNum = int(input("찾으려는 수 : "))
    ### 보초법
    nums.append(searchNum)

    for i in range(0,len(nums)):
        if nums[i]==searchNum:
            ### 보초법 : 마지막에 찾은게 아니여야함
            if i !=len(nums) -1:
                idxList.append(i)

    if len(idxList)==0:
        print(f"{searchNum}은 없음")
    else:
        print(f"가장 앞에 있는 {searchNum} : {idxList[0]}")
        print(f"{searchNum} 인덱스 : {idxList[0]}")
        print(f"{searchNum} 개수 : {len(idxList)}")

### 데이터
nums=[4,7,10,2,4,7,0,2,7,3,9]
searchLiner(nums)