input_n=int(input("n항 입력"))

flag=True ### while문 종료를 위한 flag
n=1 ### n군
nCnt=1 ### 전체 항 카운트
search_n=0 ### 찾는 값 = n항의 값

### 군 계산
while flag:
    ### n군 계산 : 1부터 n까지
    for i in range(1, n+1):
        print(f"{i}, ", end="")
        nCnt+=1
        ### nCnt가 input_n보다 커지면 종료
        if nCnt > input_n:
            ### 종료된 시점의 값 = 찾는 값
            search_n=i
            flag=False
            break
    print()
    n+=1

print(f"{input_n}항 : {search_n}")