### 100~1000 사이 난수 생성
### 약수, 소수, 소인수

import random

### 100~1000 사이의 난수 생성
num= random.randint(100, 1000)
print("num:", num)

### 약수 구하기
### 나눴을 때 나머지 0
for i in range(1, num+1):
    soinFlag=0

    if num % i == 0:
        print(f"약수: {i}")
        soinFlag +=1

### 소수 구하기
### 1과 자기 자신만으로 나누어 떨어지는 수
    if i!=1:
        flag =True
        for j in range (2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(f"소수: {i}")
            soinFlag+=1
### 소인수 구하기
    if soinFlag >=2:
        print(f"소인수: {i}")
        soinFlag=0