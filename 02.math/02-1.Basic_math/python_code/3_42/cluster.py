### 수열의 합이 최초 100 초과하는 n항
###n구하기

flag=True
sumN=0
### n군
n=1
### n항
nCnt=1
searchNCnt=0;searchNp=0

while flag:
    ## 군단위로 더하기
    for i in range(1, n+1):
       print(f"{i}/{(n-i+1)}", end=" ")
       sumN+=i/(n-i+1)
       nCnt+=1
       ### 단 합이 100일 때 멈추기
       if sumN>100:
           flag=False
           searchNCnt=i
           searchNp=n-i+1
    ### n+1군으로
    print()
    n+=1

print(f"합이 100을 초과 : {nCnt}항 + 값 : {round(sumN,2)}")