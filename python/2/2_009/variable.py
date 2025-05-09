### 빈문자 > 데이터가 없음
var=''
print(var)
print(type(var)) ### 값 str
var=bool(var)
print(var)
print(type(var)) ### 값 False
### 공백 문제 > 데이터가 있음 "공백"
var=' '
print(var)
print(type(var)) ### 값 str
var=bool(var)
print(var)
print(type(var)) ### 값 True

"""
문자 > 논리형 > 산술
"""

var1= "True"
var2= "False"

var1=bool(var1) ### True : 문자가 있어서
var2=bool(var2) ### True : 문자가 있어서
print(type(var1))
print(type(var2))

print(var1 + var2)
print(type(var1 + var2))