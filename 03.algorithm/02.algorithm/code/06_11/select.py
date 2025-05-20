num = [4,2,5,1,3]
print(f"num : {num}")

for i in range(len(num)-1):
    ### 교체 할 인덱스
    ### i번째로 작은 값
    minIdx=i

    ### i를
    ### i+1부터 끝까지 비교
    for j in range(i+1,len(num)):
        ### i번째 값과 그 다음값과 한번씩 비교
        ### i값보다 j값이 크다면 j값으로 변경
        if num[minIdx] > num[j]:
            minIdx = j

    ### 인덱스를 서로 변경
    tempNum=num[i]
    ### i번째 값을 가장 작은 값으로 변경
    num[i] = num[minIdx]
    ### 기존 값은 서로 변경
    num[minIdx]=tempNum
    print(f"num : {num}")

print(f"num : {num}")