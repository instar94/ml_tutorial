### 나머지와 몫연산자
#
num1 = 10
num2 = 3
result = num1 / num2
print("num1 : {}, num2 :{}, result: {}".format(num1,num2,result))

### 나머지 연산자
result = num1 % num2
print("num1 : {}, num2 :{}, result : {}".format(num1,num2,result))

### 몫 연산자
result = num1 // num2
print("num1 : {}, num2 :{}, result : {}".format(num1,num2,result))

### 나머지와 몫을 한번에 구하기
result = divmod(num1,num2) ### (튜플)로 출력
print("num1 : {}, num2 :{}, result : {}".format(num1,num2,result))
print("몫 : {}".format(result[0]))
print("나머지 : {}".format(result[1]))

