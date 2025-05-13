### 최소 공배수
### 100~1000사이 난수
### 최대공약수와 최대공배수  구하기

import random
rNum1= random.randint(100, 1000)
rNum2= random.randint(100, 1000)
print("랜덤 숫자 1: ", rNum1)
print("랜덤 숫자 2: ", rNum2)
maxNum=0
minNum=0

### 최대공약수 구하기
for i in range(1, min(rNum1,rNum2)+1):
    if rNum1 % i == 0 and rNum2 % i == 0:
        maxNum = i

print("최대공약수: ", maxNum)

minNum= (rNum1 * rNum2) // maxNum
print("최소공배수: ", minNum)


