### 거듭제곱 연산자 **
num1 = 2
num2 =3
result = num1 ** num2
print("num1 : {} , num2 : {}, result : {}".format(num1,num2,result))

### 제곱근 구하기
### 분수로 표현함
num3 = 1/3
result = num1 ** num3
print("num1 : %f , num3 : %.2f, result : %.2f"%(num1,num3,result))

### math 모듈의 sqrt() 와 pow() 함수
import math

### sqrt() : 2제곱근 "만" 구해줌
print("2의 제곱근은 : ", math.sqrt(num1))
### pow(x,y) : x의 y 승
print("2의 3제곱승은 ",pow(num1, num2))


### 문제 : 첫달 200원
### 매월 이전달의 2배씩 증가
### 12개월뒤 ?
firstMoney = 200
###12Month=12
###myAnswer= firstMoney*(2**12Month)
after12Month = ((firstMoney*0.01)**12 )*100
after12Month =int(after12Month)
print("정답은 : ",after12Month)
strResult=format(after12Month, ",") ###409,600
print(strResult, "원")


