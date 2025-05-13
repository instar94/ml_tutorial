### 문자형 정수로
var = "100"
print(type(var))
var = int(var)
print(type(var))
var = float(var)
print(type(var))

### 논리형 > 정수형
var = True
print(type(var))
var=int(var)
### True=1 False=0
print(var)
print(type(var))

### 논리형 > 실수형
var = True
print(type(var))
var=float(var)
### True=1 False=0
print(var)
print(type(var))