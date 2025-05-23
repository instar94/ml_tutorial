def rankFuc(nums):
    ### 순위용 리스트 생성
    ### 0이 nums 길이 만큼 생성
    ranks=[0 for i in range(len(nums))]
    ### 순위 계산
    for idx,i in enumerate(nums):
        ### i와 j(i 이후의 것)들과 비교
        ### j보다 크다면 rank에 1을 더함
        for j in nums:
            if i<j:
                ranks[idx]+=1
    print(f"rank : {ranks}")

    return ranks