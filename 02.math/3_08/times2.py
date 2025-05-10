## 숫자 2개에 대하여 최대 공약수 및 최대 공배수를 출력
num1 = int(input("숫자 1 : "))
num2 = int(input("숫자 2 : "))
num3 = int(input("숫자 3 : "))

### 변수 선언
maxNum = 0

### 최대 공약수 구하기
for i in range(1, num1+1):
    if num1%i==0 and num2%i==0:
        maxNum=i

### 최대 공배수 구하기
### 최대 공배수 = num1 * num2 // 최대공약수
minNum=num1*num2//maxNum

### 3개의 경우 : 두 개의 최소공배수 > 나머지와의 공배수를 구함
### num3와의 공배수를 구함
newNum=minNum
### 최대 공약수 구하기
for i in range(1, num3+1):
    if newNum%i==0 and num3%i==0:
        maxNum=i

minNum=newNum*num3//maxNum
print("최대 공배수 : ", minNum)