### 소인수 분해
### 100~1000까지 수 랜덤
### 소인수 분해
import random

rNum= random.randint(100, 1000)
print("rNum: ", rNum)
result=[]

###소수라서 2부터 시작
n=2
while  n<= rNum:
    ### n으로 안 나눠 떨어질때까지
    if rNum%n==0:
        print(f"소인수 : {n}")
        ### 리스트에 추가
        result.append(n)
        ### 나누기
        rNum= rNum/n
    else:
        n+=1

tempNum=0
for s in result:
    if tempNum!=s:
        print(f"{s} 개수 : {result.count(s)}")
        tempNum=s

print("소인수 리스트: ", result)