### 공약수 중에서 가장 큰 수
### 1~1000까지의 2개 난수
### 최대 공약수 및 공약수 출력
### 서로소 인지 확인

import random

rNum1 = random.randint(100, 1000)
rNum2 = random.randint(100, 1000)

rNumList = []
maxPrime = 0

### 공약수 구하기
for i in range(1, rNum1 + 1):
    ### 둘 다 0으로 나눠 떨어지면 공약수
    if rNum1 % i == 0 and rNum2 % i == 0:
        rNumList.append(i)
        maxPrime=i

print(f"공약수 : {rNumList}")
print(f"최대 공약수 : {maxPrime}")

### 서로소인지 확인
if maxPrime == 1:
    print(f"{rNum1}과 {rNum2}는 서로소")
else:
    print(f"{rNum1}과 {rNum2}는 서로소가 아님")