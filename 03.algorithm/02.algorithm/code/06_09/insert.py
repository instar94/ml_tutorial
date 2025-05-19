nums=[5,10,2,1,0]

### range(1,len(nums)) : 0번째부터 할 필요 없음
for i in range(1,len(nums)):
    j = i - 1
    cNum = nums[i]

    ### 현재 숫자 보다  다음 수가 크거나
    ### 인덱스가 0이 될 때 까지
    while nums[j] > cNum and j >=0:
        nums[j+1]=nums[j]
        j-=1
    ### 다음 꺼로 변경
    nums[j+1]=cNum
    print(f"nums : {nums}")