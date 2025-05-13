inputN= int(input("팩토리얼 n항까지 실행 :"))

### 재귀 함수 이용 방법
# def factorialFun(n):
#     if n==1 : return 1
#
#     return n*factorialFun(n-1)
#
# print(f"팩토리얼 {inputN}항 : {factorialFun(inputN)}")

### 반복문 이용 방법
# result=1
#
# for i in range(1,inputN+1):
#     result*=i
#
# print(f"팩토리얼 {inputN}항 : {result}")

### math 모듈 이용 방법
import math

result=math.factorial(inputN)
print(f"팩토리얼 {inputN}항 : {result}")