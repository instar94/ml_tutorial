### 곱셈 연산자
### 정수와 실수 = 아는 맛
num1 = 20
fNum1 = 3.14
result = num1 * fNum1
print("result : %.2f" %result)

### 문자열 곱하기
str1 = "안녕"
result = num1 * str1
print("result : %s" %result)

### 나눗셈
num2 = 2
result = num1 / num2
print("result : %d" %result)

### 0을 나누는 경우 > 항상 0
### 0으로 나누는 경우 > 연산 불가
num0=0
result = num0 / num2
print("result : %f" %result)

###result = num2 / num0
###print("result : %f" %result)
###결과값 : ZeroDivisionError: division by zero

### 딱 떨어지는 수로 계산해도 float이다
result2 = num1 / num2
print("result2 : %f" %result2)
print(type(result2))

