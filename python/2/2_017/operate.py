### 복합 연산자
### += :덧셈 후 대입
### -= :뺄셈 후 대입
### *= :곱셈 후 대입
### /= :나눗셈 후 대입
### %= :나머지 후 대입
### //= :몫 후 대입
### **= :거듭제곱 후 대입
### cf) 대입 연산자 = : 오른쪽 값을 왼쪽으로 대입


num1=0
num2=0
### 동일한 값을 가짐
num1 = num1 +5
num2+=5
print("동일한 값을 가짐 \nnum1 : {}\tnum2: {}".format(num1,num2))

### 누적 강수량 구하기
totalRainAmount=0

rainAmount = 30
totalRainAmount+=rainAmount
print("1월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 45
totalRainAmount+=rainAmount
print("2월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 47
totalRainAmount+=rainAmount
print("3월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 55
totalRainAmount+=rainAmount
print("4월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 65
totalRainAmount+=rainAmount
print("5월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 100
totalRainAmount+=rainAmount
print("6월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 128
totalRainAmount+=rainAmount
print("7월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 209
totalRainAmount+=rainAmount
print("8월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 204
totalRainAmount+=rainAmount
print("9월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 186
totalRainAmount+=rainAmount
print("10월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 67
totalRainAmount+=rainAmount
print("11월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAmount = 25
totalRainAmount+=rainAmount
print("12월 강수량 : {}, 누적 강수량 {}".format(rainAmount,totalRainAmount))

rainAvg=totalRainAmount/12
print("연간 누적 강수량 : {}mm/n연 평균 누적강수량 {}mm".format(totalRainAmount,rainAvg) )

