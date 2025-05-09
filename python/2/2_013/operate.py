#### 덧셈
num1=3.14
num2=0.12
print("num1 + num2 =%.2f" %(num1+num2))

### 덧셈이 불가능한 케이스
### 문자열 + 숫자
str1 = "20.5"
###print("str1 + num2 =%.2f" %(str1+num2))
### 결과 : TypeError: can only concatenate str (not "float") to str

### 문자열 뺄셈은 불가
str2 = "0.5"
###result=str1-str2
###print("문자열 뺄셈은 안됨 : {}".format(result))
### 결과값 : TypeError: unsupported operand type(s) for -: 'str' and 'str'
