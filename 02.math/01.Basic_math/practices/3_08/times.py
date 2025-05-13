## 숫자 2개에 대하여 최대 공약수 및 최대 공배수를 출력

num1 = int(input("숫자 1 : "))
num2 = int(input("숫자 2 : "))

### 변수 선언
maxNum = 0

### 최대 공약수 구하기
for i in range(1, num1):
    if num1%i==0 and num2%i==0:
        maxNum=i

print("최대 공약수 : ", maxNum)

### 최대 공배수 구하기
### 최대 공배수 = num1 * num2 // 최대공약수
minNum=num1*num2//maxNum
print("최대 공배수 : ", minNum)