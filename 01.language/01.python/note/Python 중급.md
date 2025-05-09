# 함수(Function)

## 함수란? 
> 수학의 함수와 같이 특정 기능 / 연산을 하는 것 

## 함수의 선언 
- `def`를 통해 함수를 선언 
- `( )` 안에 파라미터를 넣음 
- `return`을 통해 어떤 값을 output 할지 선언
```python 
def funcName(x,y):
    return x + y
print(funcName(3,4))
```

## 내장함수 VS 사용자 함수 
### 내장 함수 
> 파이썬에서 기본적으로 제공해주는 함수 

```python 
print ("Hello Python!")

str = input()

```

### 사용자 함수 
> 사용자가 원하는대로 선언한 함수 

```python
def printUser(name):
    print(f"{name} 고객님, 안녕하세요")
```


## 함수를 사용하는 이유 
- 특정 기능을 재사용 하기 위하여 사용 
- 코드를 간단하게 만들 수 있음 


## 함수의 선언과 호출 
### 함수의 선언 
- `def <함수명> : `
	- 함수명 명 첫글자는 영어 소문자가 국룰
	- 특수문자, 숫자, 영어 대문자는 좀...
	- 들여 쓰기를 통해 코드 블럭을 만듦 
 ```python
 def addCal():
     n1 = int(input("n1 입력 : "))
     n2 = int(input("n2 입력 : "))
     print(f"n1 + n2 = {n1 + n2}")
```

- 호출 되지 않으면 기능하지 않는다. 

### 함수의 호출 
- 함수명과 `()`를 이용하여 선언 가능 

> 정수 2개 -> 곱셈 / 나눗셈


```python 
def calFunc():
     n1 = int(input("n1 입력 : "))
     n2 = int(input("n2 입력 : "))
     print(f"n1 * n2 = {n1 * n2}")
     print(f"n1 / n2 = {rount(n1 / n2,2)}")

calFunc()
```

### 함수 내에서 다른 함수 
``` python 
def fun1():
    print("func1 호출")
    func2()

def func2():
    print("func2호출")
    func3()
    
def func3():
    print("func3 호출")

func1

```


**결과물** 
```text
func1호출
func2호출
func3호출
```

### pass 
> 실행문 (return) 없이 생략

```python 
def printToday() : 
    pass

printToday()
```

## 인수와 매개변수 
### 인수 - parameter
> 함수를 호출 할 때, 전달 하는 값 

### 매개변수 
> 함수를 실행 시키기 위해 필요한 값 

```python 
### customer : 매개 변수 
### 홍길동 : 인수 

def greet(customer):
    print(f"{customer} 고객님, 안녕하세요")

greet("홍길동")
```

### 인수와 매개변수의 갯수
#### 원칙
- 인수와 매개 변수의 수는 일치 해야함 

#### 정해지지 않는 경우 \*
- 매개변수 개수가 정해지지 않은 경우 `*`를 사용
```python 
def printNum(*numbers)
    for numbers in numbers:
        print(number, end="")
    print()
```


## 데이터의 반환
> 함수의 실행 결과를 돌려주는 것 

- `return` 키워드를 이용해 함수 실행 결과를 호출부로 반환 가능 

```python
def calcul(n1,n2):
    result = n1 + n2
    return result 

returnValue = calcul(20,10)
print(f"returnValue: {returnValue}")

```

### return 구문을 만나면 실행이 종료 
```python 
def dividNum(n):
    if n %2 == 0 :
        return "짝수"
    else : 
	    return  "홀수"
### 아래 내용은 실행되지 않음 	
```


## 지역변수 VS 전역변수 
### 전역 변수 (Global)
> 함수 밖에서 선언되어 어디서든 사용 가능하지만 함수 안에서 수정 불가능한 변수 


```python
numOut=10 ## 전역변수임 
def printNum():
    numOut=20 ## 지역 변수임 
    print(numOut)
printNum() ## 20
print(numOut) ##10
```

### 지역 변수(local)
> 함수 안에서 선언되어 함수 안에서 정의되고 수정 가능 


### Global 키워드
- `global` 키워드를 이용하면 전역변수를 수정 할 수 있음

```python
numOut=10 ## 전역변수임 
def printNum():
    global numOut
    numOut=20 ## 지역 변수임 
    print(numOut)
printNum() ## 20
print(numOut) ##20
```


## 중첩함수
> 함수 안에 또 다른 함수가 있는 형태 

```python

def out_func():
    print("out_func called")
    def in_func():
	    print("in_func called")
	in_func()

```

- 단, 내부 함수를 밖에서 호출 할 수 없음 

### 예시 : 계산기
> calculator() 함수 선언
> 안에서 덧셈 / 뺄샘 / 나눗샘 / 곱셈 함수 선언 


```python
def calculator(n1,n2,operator):
	def addcal():
		print(f"덧셈 : {n1+n2}")
	def subcal():
		print(f"덧셈 : {n1+n2}")
	def mulcal():
		print(f"덧셈 : {n1+n2}")
	def dvical():
		print(f"덧셈 : {n1+n2}")

	if operator == 1:
		addcal()
	elif operator ==2 :
		subcal()
	elif operator ==3:
		mulcal()
	elif operator == 4 :
		dvical()
	else 

while True :
	n1=float(input("실수1 : "))
	n2=float(input("실수2 : "))
	operator=int(input("연산자 1. 덧셈 \t 2.뺄샘\t 3.곱셈\t 4.나눗셈\t 5.종료 : "))
	if operator == 5 :
		print("종료")
		break
	calculator(n1,n2,operator)

```

## lambda 함수
> [!note] Lambda 함수 
> 함수 선언을 보다 간단하게 


```python
def cal(n1,n2)
    return n1 + n2
returnvalue = cal(10,10)
print(f'returnvalue : {returnvalue}')

### --------------------------------
cal = lambda n1,n2 : n1 + n2
returnvalue = cal(10,10)
print(f'returnvalue : {returnvalue}')
```

- 함수의 입력부, 반환부 등을 제외 할 수 있음 

### 예시 : 삼각형 , 사각형, 원의 넓이 출력 람다 함수 
```python
getTri = lambda n1,n2 : n1 *n2 /2
getSqu = lambda n1,n2 : n1 *n2 
getCir = lambda r: r *r*3.14

width = int(input("가로 :"))
height = int(input("세로 :"))
r = int(input("반지름 :"))

getTriValue = getTri(width,height)
getSquValue = getSqu(width,height)
getCirValue  = getCir(r)

print (f"삼각형 : {getTriValue}" )
print (f"사각형 : {getSquValue}" )
print (f"원 : {getCirValue}" )

```

# 모듈 (Module)

> [!note] 모듈 
> 이미 만들어진 기능
> - 이미 만들어진 파이썬 파일을 모듈이라고 할 수 있음 


## 모듈의 구분 

| 구분     | 설명               |
| ------ | ---------------- |
| 내부 모듈  | 파이썬 설치 시, 기본 제공  |
| 외부 모듈  | 별도 설치 후 사용 되는 모듈 |
| 사용자 모듈 | 사용자가 직접 만든 모듈    |

```python
### 모듈을 가져옴
import random

### random 모듈의 특정 함수를 가져옴
rNum = random.randint(1,10)
print("난수 : ",rNum)
```


## 모듈 제작 
- 특정 기능을 가진 파이썬 파일을 만듦

```python title:"calculator.py"
### cal 
def addcal(n1,n2):  
    print(f"덧셈 : {n1 + n2}")  
  
def subcal(n1,n2):  
    print(f"뺄셈 : {n1 + n2}")  
  
def mulcal(n1,n2):  
    print(f"곱셈 : {n1 + n2}")  
  
def divcal(n1,n2):  
    print(f"나눗셈 : {n1 + n2}")
```

```python title:"module.py"
import calculator  
  
calculator.addcal(10,20)  
calculator.subcal(10,20)  
calculator.mulcal(10,20)  
calculator.divcal(10,20)
```


## 모듈 사용
> [!note] 모듈 호출 키워드 
> - import
> - from
> - as

### as 키워드
- 모듈의 이름을 단축 가능


```python title:"calculator.py"
### cal 
def addcal(n1,n2):  
    print(f"덧셈 : {n1 + n2}")  
  
def subcal(n1,n2):  
    print(f"뺄셈 : {n1 + n2}")  
  
def mulcal(n1,n2):  
    print(f"곱셈 : {n1 + n2}")  
  
def divcal(n1,n2):  
    print(f"나눗셈 : {n1 + n2}")
```


```python title:"module.py"
import calculator as cal
  
cal.addcal(10,20)  
cal.subcal(10,20)  
cal.mulcal(10,20)  
cal.divcal(10,20)
```


### from ~ as 키워드 
- 특정 함수만 가져오는 경우 
```python title:"module.py"
from calculator import addcal 
  
addcal(10,20)  
```

## \_\_main\_\_ 파일 
### `__name__` 을 통한 실행파일 지정
- 파이썬에서는 `__name__` 전역변수를 이용해 실행 파일을 지정이 가능 

- `__name__`
 에는 모듈 이름이 저장되거나 `__main__`이 저장된다
 - 일반적인 모듈은 파일명이 들어가지만 실행파일의 경우 `__main__`이 들어간다
```python title:"module.py"
__name__='__main__'
```

#### 실행파일이란?
- 하나의 프로젝트 안에서 어떤 파일을 먼저 실행할 지 표시함
	- java 같은 경우에는 main 함수가 있음 

```python title:"add.py"
def add(n1,n2):
	return n1+n2

if __name__=="__main__":
	print(f'__name__{__name__}')
```

```python title:"mul.py"
def mul(n1,n2):
	return n1*n2

if __name__=="__main__":
	print(f'__name__{__name__}')
```

```python title:"module.py"
import add
import mul

if __name__=="__main__":
	print(add.add(10,20))
	print(mul.mul(10,20))

def mod(n1,n2):
	return n1%n2
```

#### 예시 : 단위 환산 

```python title:"uniconv.py"
def cmToMm(n):
	return round(n*10,3)
def cmToInch(n):
	return round(n*0.393,3)
def cmToM(n):
	return round(n*0.01,3)
def cmToFit(n):
	return round(n*0.032,3)

if __name__ == "__main__":
	print(f'10cm:{cmToMm(10)mm})
	print(f'10cm:{cmToInch(10)inch})
	print(f'10cm:{cmToM(10)m})
	print(f'10cm:{cmToFit(10)fit})
```

```python title:"module.py"
import uniconv as uc

if __name__ == "__main__":
	inputnumber = int(input("길이 입력 : "))
	
	returnValue = uc.cmToMm
	print(f"returnValue: {returnValue}")
	
	returnValue = uc.cmToInch
	print(f"returnValue: {returnValue}")
	
	returnValue = uc.cmToM
	print(f"returnValue: {returnValue}")
	
	returnValue = uc.cmToFit
	print(f"returnValue: {returnValue}")
```

## 패키지 
> [!note] 패키지
> 모듈을 묶어서 관리하는 것 

![[패키지.png]]

- 파일 예시
![[image.png|174x235]]
### 패키지 참조
- `from` 키워드를 통해 호출
```python title:"module.py"
from CalculatorForInt import addcal  
from CalculatorForInt import subcal  
from CalculatorForInt import mulcal  
from CalculatorForInt import divcal  
  
print(addcal.add(10,20))  
print(subcal.sub(10,20))  
print(mulcal.mul(10,20))  
print(divcal.div(10,20))  
  
from CalculatorForFloat import addcal  
from CalculatorForFloat import subcal  
from CalculatorForFloat import mulcal  
from CalculatorForFloat import divcal  
  
print(addcal.add(10,20))  
print(subcal.sub(10,20))  
print(mulcal.mul(10,20))  
print(divcal.div(10,20))
```

### site-packages
> [!note] 
>어디서나 사용 할 수 있는 범용 패키지
>위치 : \project\venu\lib\site-packages

```python
import sys ###시스템 정보에 관한 모듈  
  
for path in sys.path:  
    print(path)### system의 경로를 출력
```

- 결과값 
```text
C:\pythonEx\project\.venv\Scripts\python.exe C:\pythonEx\project\5_015\sitepackage.py 
C:\pythonEx\project\5_015
C:\pythonEx\project
C:\pythonEx\project\.venv\Scripts\python313.zip
C:\Users\skssk\AppData\Local\Programs\Python\Python313\DLLs
C:\Users\skssk\AppData\Local\Programs\Python\Python313\Lib
C:\Users\skssk\AppData\Local\Programs\Python\Python313
C:\pythonEx\project\.venv
C:\pythonEx\project\.venv\Lib\site-packages
```

- `C:\pythonEx\project\.venv\Lib\site-packages`
	- venv : virtual environment
		- 가상환경
		- 각 버전 별 가상환경을 만들어 놓고 가상환경만 바꿔가며 실행 할 수 있음
		- 환경세팅이 독립적임
	- `site-packages` : 프로젝트에서 범용적으로 사용 할 수 있는 곳임

```python
from calcul import cal  
print(f"cal.add(10,20) : {cal.add(10,20)}")  
print(f"cal.sub(10,20) : {cal.sub(10,20)}")  
print(f"cal.mul(10,20) : {cal.mul(10,20)}")  
print(f"cal.div(10,20) : {cal.div(10,20)}")  
  
### 다른 경로에서 쓸 수 없음
```

- 패키지를 `site-package` 밑으로 옮기면 다른 경로에서도 사용 할 수 있음 
![[image-1.png]]

#### 실습 : 약수와 소수 리스트 반환
```python
def divisor(n1):  
    outputlist=[]  
    for i in range(1,n1+1):  
        if n1%i== 0:  
            outputlist.append(i)  
        else:  
            pass  
    return outputlist  
  
def prime_number(n1):  
    outputlist=[]  
    for i in range(2,n1+1):  
        if len(divisor(i))==2:  
            outputlist.append(i)  
        else:  
            pass  
    return outputlist  
  
if __name__ == "__main__":  
    print("약수 : ", divisor(50))  
    print("소수 : ", prime_number(50))
```

- 만들면서 잘 못한 것 
	- range() 대신에 [1:20] 이런식으로 줌...
	- range(1,20)이렇게 안하고 range(20) 해서 Zero 문제 발생

## 자주 사용하는 모듈
>[!tip] 주로 사용하는 기본 모듈
>- math : 수학 관련 모듈
>- random : 난수 생성 모듈
>- time : 시간 관련 모듈


### 수학 관련 내장 함수 
```python
#수학 내장 함수  
### 합 - sum  
###리스트 안에 있는걸 알아서 더함  
listVar=[2,4,7,10]  
print(f"{sum(listVar)}")  
  
### 최대값 -max  
print(f"{max(listVar)}")  
  
### 최소값 -min  
print(f"{min(listVar)}")  
  
### 거듭제곱 -pow  
print(f"{pow(13,2)}")  
print(f"{pow(13,4)}")  
  
### 반올림 - round  
print(f"round(3.14592,1) {round(3.14592,1)}")  
print(f"round(3.14592,2) {round(3.14592,2)}")  
print(f"round(3.14592,3) {round(3.14592,3)}")
```

### math 모듈

```python
#### math 함수  
import math  
  
### 절댓값 fabs  
print(f"math.fabs(-10) {math.fabs(-10)}")  
  
### 올림 - ceil  
print(f"math.cell(5.21) {math.ceil(5.21)}")  
print(f"math.cell(5.21) {math.ceil(-5.21)}")  
  
### 내림 - floor  
print(f"math.floor(5.21) {math.floor(5.21)}")  
print(f"math.floor(-5.21) {math.floor(-5.21)}")  
  
  
### 최대공약수-gcd  
print(f"math.gcd(14,21) {math.gcd(14,21)}")  
  
### 팩토리얼 - factorial  
print(f"math.factorial(10) {math.factorial(10)}")  
  
### 루트 - sqrt  
print(f"math.sqrt(10) {math.sqrt(10)}")
```

### random
```python
### random 모듈

## 난수 발생  0이상 1미만 난수
print(f'random.random(): {random.random()}')

##1이상 20이하 난수
print(f'random.randint(1, 20): {random.randint(1, 20)}')

# 1이상 20미만 난수
print(f'random.randrange(1, 20): {random.randrange(1, 20)}')

# 1이상 21미만 난수 5개
print(f'random.sample(range(1, 21), 5): {random.sample(range(1, 21), 5)}')

# 무작위 한개 추출
listVar = [0, 1, 2, 3, 4, 5, 6]
print(f'random.choice(listVar): {random.choice(listVar)}')

# 섞음.
print(f'listVar: {listVar}')
random.shuffle(listVar)
print(f'shuffle listVar: {listVar}')
```
### time
```python
import time  
  
###현재 기기 시간 - localtime()  
lt = time.localtime()  
print(f"time.localtime() {time.localtime()}" )  
  
### 특정 단위만 출력  
##연  
print(f"lt.tm_year {lt.tm_year}")  
##월  
print(f"lt.tm_mon {lt.tm_mon}")  
##월  
print(f"lt.tm_mon {lt.tm_mon}")  
##일  
print(f"lt.tm_mday {lt.tm_mday}")  
#시  
print(f"lt.tm_hour {lt.tm_hour}")  
##분  
print(f"lt.tm_min {lt.tm_min}")  
##초  
print(f"lt.tm_sec {lt.tm_sec}")  
##요일  
print(f"lt.tm_wday {lt.tm_wday}")
```

# 객체지향 프로그래밍

## 객체지향 프로그래밍이란?
>[!info] 객체지향이란
> 객체를 이용한 프로그래밍으로 객체는 속성과 기능으로 이뤄짐 
> 
> 객체 (Object) = 속성 (Attribute) + 기능(Function)

![[image-2.png]]

## 객체의 생성
- 객체는 클래스에서 생성됨
	- 클래스는 하나면 되지만 객체는 여러 개 생성 할 수 있음 
![[image-3.png]]

### 객체 사용의 장점
- 코드 재사용 및 모듈화에 좋음 
## 클래스와 객체의 생성
### 클래스 만들기 
>[!check] 클래스 생성
> `class` 키워드와 속성(변수) 그리고 기능(함수)를 이용해 만든다

- 클래스의 첫글자는 알파벳 대문자

![[image-4.png]]

- `__init__` 이라는 특수한 함수를 먼저 작성 - 생성자
	- self를 사용해 스스로를 받음 
- 객체가 아니기 때문에 실행해도 결과가 없음

```python
class Car:  
    def __init__(self,col,len):  
        self.color=col  
        self.length=len  
  
    def doStop(self):  
        print("Stop")  
  
    def soStart(self):  
        print("Start")  
  
    def printCarInfo(self):  
        print(f"self.color : {self.color}")  
        print(f"self.length : {self.length}")
```


### 객체의 생성 
- 객체는 클래스의 생성자를 호출 
- 매개변수가 없다면 그냥 생성하면됨
```python
### def __init__(self,col,len):  으로 연결됨
car1 = Car("red",200)
car2 = Car("Blue",500)  
  
car1.printCarInfo()  
car2.printCarInfo()

```

- 결과 값
```text
self.color : Red
self.length : 200
self.color : Blue
self.length : 500
```

### 객체 속성 변경
- 다시 선언하면 속성을 변경 할 수 있음 
```python title:"class선언언.py"
class NewPC:  
    def __init__(self, name,cpu,memory,ssd):  
        self.name=name #self.name = 객체의 이름 name = 매개변수로 받은 이름  
        self.cpu = cpu  
        self.memory = memory  
        self.ssd = ssd  
  
    def doExcel(self):  
        print("Excel")  
  
    def doPhotoshop(self):  
        print("Photoshop")  
  
    def printInfo(self):  
        print(f"self.name {self.name}")  
        print(f"self.cpu {self.cpu}")  
        print(f"self.memory {self.memory}")  
        print(f"self.ssd {self.ssd}")  
  
```

```python title:"변경전.py"
mypc=NewPC("mypc","15","16G","256G")  
friendpc=NewPC("friendpc","17","32G","512G")  
  
mypc.printInfo()  
print("="*10,"="*10)  
friendpc.printInfo()  
```

```text title:"결과값"
self.name mypc
self.cpu 15
self.memory 16G
self.ssd 256G
========== ==========
self.name friendpc
self.cpu 17
self.memory 32G
self.ssd 512G
```

```python title:"변경후.py"
print("="*10,"pc업그레이드","="*10)  
mypc.cpu="19"  
mypc.memory="64GB"  
mypc.ssd="1TB"  
mypc.printInfo()
```

```text title:결과값
========== pc업그레이드 ==========
self.name mypc
self.cpu 19
self.memory 64GB
self.ssd 1TB
```

#### 계산기 실습
- 클래스 선언
```python title:클래스
class Cacul :  
    def __init__(self):  
        self.n1=0  
        self.n2=0  
        self.result=0  
  
    def add(self):  
        self.result=self.n1+self.n2  
        return self.result  
  
    def sub(self):  
        self.result=self.n1-self.n2  
        return self.result  
  
    def mul(self):  
        self.result=self.n1*self.n2  
        return self.result  
  
    def div(self):  
        self.result=self.n1/self.n2  
        return self.result  

```

```python title:계산실행
## 매개 변수가 없다면 그냥 선언하면됨  
calcul=Cacul()  
calcul.n1=10  
calcul.n2=20  
print(f"calcul.add() {calcul.add()}")  
print(f"calcul.sub() {calcul.sub()}")  
print(f"calcul.mul() {calcul.mul()}")  
print(f"calcul.div() {calcul.div()}")
```

```text title:결과값
calcul.add() 30
calcul.sub() -10
calcul.mul() 200
calcul.div() 0.5
```

## 객체와 메모리
- 변수는 객체의 메모리에 주소를 저장하고 객체를 참조함 
 
- ![[image-5.png]]
- 메모리의 주소만 변수에 저장됨
	- 변수에 저장된 주소를 찾아가서 참조함
	- 레퍼런스 변수라고 함

### 특징 (이자 문제)
- 복사 시에 주소값을 복사함
```python title:클래스선언
class Robot:  
    def __init__(self, color, height, weight):  
        self.color=color  
        self.height=height  
        self.weight=weight  
  
    def printInfo(self):  
        print(f"self.color {self.color}")  
        print(f"self.height {self.height}")  
        print(f"self.weight {self.weight}")  

```

- `rb3=rb1` 과 같이 복사하면 객체의 속성이 복사되는 것이 아닌 객체의 주소값만 복사됨
```python title:1차_출력
rb1 =Robot("red",200,200)  
rb2 =Robot("blue",230,500)  
### 객체의 속성을 복사한 것이 아니라 객체의 주소값만 복사함  
rb3 =rb1  
  
rb1.printInfo()  
rb2.printInfo()  
rb3.printInfo()  
```

```text title:출력값
self.color red
self.height 200
self.weight 200
self.color blue
self.height 230
self.weight 500
self.color red
self.height 200
self.weight 200
```

```python title:변경후_출력
  rb1.color="green"  
rb1.printInfo()  
rb2.printInfo()  
rb3.printInfo()
```

- 주소 값이 동일 하기 때문에 동일하게 변경됨

```text title:출력값
self.color green
self.height 200
self.weight 200
self.color blue
self.height 230
self.weight 500
self.color green
self.height 200
self.weight 200
```

#### `copy()` : 객체의 복사 
- 주소 값이 아닌 실제 객체를 복사하고 싶다면 `copy()` 를 이용해야함

##### 예시
- 국영수 점수를 입력 받아 저장 후 원본 유지 
- 복사본을 만들어 각 과목별 점수가 10% 올랐을 때 평균 출력 
```python 
scores = [int(input("국어 : ")),  
         int(input("영어 : ")),  
         int(input("수학 : "))]  
print(scores)  
  
copysocre=scores.copy()  
  
for idx,score in enumerate(copysocre):  
    result=score*1.1  
    copysocre[idx]= 100 if result > 100 else result  
  
print(f"이전 평균 : {round(sum(scores) / len(scores),1)}")  
print(f"이후 평균 : {round(sum(copysocre) / len(copysocre),2)}")
```

```text title:출력값
국어 : 40
영어 : 88
수학 : 100
[40, 88, 100]
이전 평균 : 76.0
이후 평균 : 80.27
```

### 얕은 복사와 깊은 복사 
#### 얕은 복사 
- 객체의 주소만 복사함 
- 객체가 생성되지 않음
- 참조한 객체가 변경되면 복사된 객체도 변경됨

```python title:얕은복사_변경전
### 얕은 복사  
tc1=TemCls(10,"Hello Python")  
tc2=tc1  
  
tc1.printInfo()  
tc2.printInfo()
```

```text
self.number :10
self.str :Hello Python
self.number :10
self.str :Hello Python
```

```python title:얕은복사_변경후
### 값 변경  
tc2.number=3.14  
tc2.str="Bye"  
  
tc1.printInfo()  
tc2.printInfo()
```

```text
self.number :3.14
self.str :Bye
self.number :3.14
self.str :Bye
```
#### 깊은 복사 
- 객체 자체를 복사함
- 새로운 객체가 생성되어 메모리를 차지함
- 참조한 객체가 변경되더라도 독립적으로 진행됨


```python title:깊은복사_변경전
### 깊은 복사  
import copy  
tc3 =TemCls(10,"Hello Python")  
tc4 = copy.copy(tc3)  
  
tc3.printInfo()  
tc4.printInfo()
```

```text
self.number :10
self.str :Hello Python
self.number :10
self.str :Hello Python
```

```python title:깊은복사_변경후
### 값 변경  
tc4.number=3.14  
tc4.str="Bye"  
  
tc3.printInfo()  
tc4.printInfo()
```

```text
self.number :10
self.str :Hello Python
self.number :3.14
self.str :Bye
```

## 클래스
### 클래스 상속 
>[!note] 상속이란
>클래스 또는 다른 클래스를 상속하여 내 것처럼 사용 

![[image-6.png]]

```python
### 부모클래스
class NormalCar:  
    def drive(self):  
        print("[NormalCar] drive() called")  
    def back(self):  
        print("[NormalCar] back() called")

### 자식 클래스
### 상속받는 클래스를 ()안에 넣음  
class Turbocar(NormalCar):  
    def turbo(self):  
        print("[Turbocar] turbo() called")


myTurboCar =Turbocar()  
myTurboCar.drive()  
myTurboCar.back()  
myTurboCar.turbo()

```

```text title:"결과값"
[NormalCar] drive() called
[NormalCar] back() called
[Turbocar] turbo() called
```


#### 실습
- 계산기 프로그램
```python
class CalculatorSuper:  
    def add(self,n1,n2):  
        return n1 + n2  
  
    def sub(self,n1,n2):  
        return n1 - n2  
  
class CalculatorChild(CalculatorSuper):  
    def mul(self,n1,n2):  
        return n1 * n2  
    def div(self,n1,n2):  
        return n1 / n2  
  
cal = CalculatorChild()  
print(f"cal.add(10,20) : {cal.add(10,20)}")  
## print(f"cal.sub(10,20) : {cal.sub(10,20)}")  
print(f"cal.mul(10,20) : {cal.mul(10,20)}")  
print(f"cal.div(10,20) : {cal.div(10,20)}")
```

```text
cal.add(10,20) : 30
cal.sub(10,20) : -10
cal.mul(10,20) : 200
cal.div(10,20) : 0.5
```

### 생성자
>[!info] 생성자란?
> 객체가 생성될때 생성자를 호출하면 `__init__()`가 자동으로 호출됨 

![[image-7.png|320x338]]

#### 역할 
- `__init()__()` 가 속성을 초기화함 

```python
class Caculator:  
    def __init__(self,n1,n2):  
        print("[Caculator] Called")  
        self.num1=n1  
        self.num2=n2  
  
cal=Caculator(10,20)  
print(f"cal.num1 : {cal.num1}")  
print(f"cal.num2 : {cal.num2}")
```

```text
[Caculator] Called
cal.num1 : 10
cal.num2 : 20
```


#### `super()`
- 상위 클래스의 속성을 초기화 하기 위해서 사용

```python
class P_Class:  
    def __init__(self,pNum1,pNum2):  
        print("[P_Class] : __init__() Called")  
        self.pNum1 = pNum1  
        self.pNum2 = pNum2  
  
class C_Class(P_Class):  
    def __init__(self,cNum1,cNum2):  
        print("[C_Class] : __init__() Called")  

### 부모 클래스를 호출하여 가능  

		#P_Class.__init__(self,cNum1,cNum2)### super 키워드를 통해 서도 가능  
        
        super().__init__(cNum1,cNum2)  
        self.cNum1 = cNum1  
        self.cNum2 = cNum2
```

#### 실습
- 중간고사 클래스와 기말고사 클래스를 만들고 각각 점수를 초기화 
- 총점 및 평균 반환 
```python
class Midterm:  
    def __init__(self,s1,s2,s3):  
        print("------- Midterm Called ------- ")  
        self.mid_kor = s1  
        self.mid_eng = s2  
        self.mid_math = s3  
  
    def printMidScore(self):  
        print(f"Midterm Kor : {self.mid_kor}")  
        print(f"Midterm Eng : {self.mid_eng}")  
        print(f"Midterm Math : {self.mid_math}")  
  
class EndExam(Midterm):  
    def __init__(self,s1,s2,s3,s4,s5,s6):  
        print("------- EndExam Called ------- ")  
        super().__init__(s1,s2,s3)  
        self.end_kor = s4  
        self.end_eng = s5  
        self.end_math = s6  
  
    def getTotlaScore(self):  
        total = self.mid_kor + self.mid_math + self.mid_eng  
        total += self.end_kor + self.end_math + self.end_eng  
        return total  
  
    def getAverage(self):  
        return self.getTotlaScore()/6  
  
exam = EndExam(90,80,70,100,29,70)  
print(f"Total : {exam.getTotlaScore()}")  
print(f"Average : {round(exam.getAverage(),1)}")
```

- 결과값
```text
------- EndExam Called ------- 
------- Midterm Called ------- 
Total : 439
Average : 73.2
```

### 다중 상속
>[!tip] 다중 상속
>2개 이상의 클래스를 상속하는 것 
- 사용 방법 : 동일하게 클래스 선언 후 `( )` 안에 여러 클래스를 선어남 

```python
class Car01:  
    def drive(self):  
        print("drive() method called")  
  
class Car02:  
    def turbo(self):  
        print("turbo() method called")  
  
class Car03:  
    def fly(self):  
        print("fly() method called")  
  
class Car(Car01,Car02,Car03):  
    def __init__(self):  
        pass  
  
 ### 3개의 클래스의 것을 마치 자신의 것처럼 사용 가능 
mycar = Car()  
mycar.drive()  
mycar.turbo()  
mycar.fly()
```

#### 실습 
- Basic Calculator 와 DeveloperCaCulator클래스를 만들고 상속하여 Calculator 클래스 만들기 
```python
class BasicCalculator:  
    def add(self,n1,n2):  
        return n1+n2  
    def sub(self,n1,n2):  
        return n1-n2  
    def mul(self,n1,n2):  
        return n1*n2  
    def div(self,n1,n2):  
        return n1/n2  
  
class DeveloperCalculator:  
    def mod(self,n1,n2):  
        return n1%n2  
    def flo(self,n1,n2):  
        return n1//n2  
    def exp(self,n1,n2):  
        return n1**n2  
  
class Calculator(BasicCalculator,DeveloperCalculator):  
    def __init__(self):  
        pass  
  
  
cal=Calculator()  
print(f"cal.add(10,20) : {cal.add(10,20)}")  
print(f"cal.sub(10,20) : {cal.sub(10,20)}")  
print(f"cal.mul(10,20) : {cal.mul(10,20)}")  
print(f"cal.div(10,20) : {cal.div(10,20)}")  
print(f"cal.mod(10,20) : {cal.mod(10,20)}")  
print(f"cal.flo(10,20) : {cal.flo(10,20)}")  
print(f"cal.exp(10,20) : {cal.exp(10,20)}")
```

### 오버라이딩(Override)
>[!note] 오바라이딩
>하위 클래스에서 상위 클래스의 매서드를 재정의함

![[image-8.png|265x240]]

```python title:"오버라이딩 전"
class Robot:  
    def __init__(self,c,h,w):  
        self.color=c  
        self.height=h  
        self.weight=w  
  
    def fire(self):  
        print("Fire in the hole")  
  
    def printRobotInfo(self):  
        print(f"self.color : {self.color}")  
        print(f"self.height : {self.height}")  
        print(f"self.weight : {self.weight}")  
  
class NewRobot(Robot):  
    def __init__(self,c,h,w):  
        super().__init__(c,h,w)  
  
myrobot=NewRobot("Red",200,300)  
myrobot.fire()
```

```text
Fire in the hole
```

```python title:"오버라이딩 후"
class NewRobot(Robot):  
    def __init__(self,c,h,w):  
        super().__init__(c,h,w)  
  
    ### fire 함수 오버 라이딩  
    def fire(self):  
        print("You got the fire")  
  
myrobot=NewRobot("Red",200,300)  
myrobot.fire()
```

```text
You got the fire
```

### 추상 클래스 
>[!note] 정의
>상위 클래스에서 하위클래스 매서드 구현 강요 

![[image-9.png]]

#### 구현 방법 
- 구현을 위한 패키지 import
	- from abc import ABCMeta  
	- from abc import abstractmethod
```python
from abc import ABCMeta  
from abc import abstractmethod
```

- 해당 클래스에 표시
```python
## 강제성을 띄게 하는 클래스에  
# metaclass=ABCMeta  
class AirPlane(metaclass=ABCMeta):  
  
    #추상 클래스 표시  
    @abstractmethod  
    def flight(self):  
        pass
```


```python
from abc import ABCMeta  
from abc import abstractmethod  
  
## 강제성을 띄게 하는 클래스에  
# metaclass=ABCMeta  
class AirPlane(metaclass=ABCMeta):  
  
    #추상 클래스 표시  
    @abstractmethod  
    def flight(self):  
        pass  
  
    def forward(self):  
        print("전진")  
  
    def flight(self):  
        print("후진")  
  
class Airliner(AirPlane):  
    def __init__(self,c):  
        self.color=c  
      
    def flight(self):  
        print("시속 400km/h")  
  
al=Airliner("red")
```


#### 추상 클래스를 사용하는 이유
- 같은 함수라도 서로 다른 기능이 필요 할 수도 있음 
```python
class Airliner(AirPlane):  
    def __init__(self,c):  
        self.color=c  
  
    def flight(self):  
        print("시속 400km/h")  
  
class filghterPlane(AirPlane):  
    def __init__(self,c):  
        self.color=c  
    def flight(self):  
        print("시속 800km/h")
```

# 예외

## 예외란? 
>[!note] 예외란
> 예상하기 어려운 문제로 프로그램 실행이 어려운 상태 
> - 문법적인 문제는 없으나 실행 중 발생하는 예상치 못한 문제

- Error 와는 다름
	- ex) 네트워크 문제 등 소프트웨어적이지 않은 문 

- 예외 관련 클래스에는 각각 관련된 클래스가 있다.
![[image-10.png]]

### 실습
-  ZeroDivisionError : 0으로 나눌 수 없는 문제
```python
def add(n1,n2):  
    return n1+n2  
  
def div(n1,n2):  
    return n1/n2  
  
fn = int(input("첫번째 숫자 : "))  
sn = int(input("두번째 숫자 : "))  
  
print(f"add(fn,sn) : {add(fn,sn)}")  
print(f"div(fn,sn) : {div(fn,sn)}")

```

```text title:"결과값"
첫번째 숫자 : 19
두번째 숫자 : 0
add(fn,sn) : 19
Traceback (most recent call last):
  File "C:\pythonEx\project\5\5_028\exception.py", line 11, in <module>
    print(f"div(fn,sn) : {div(fn,sn)}")
                          ~~~^^^^^^^
  File "C:\pythonEx\project\5\5_028\exception.py", line 5, in div
    return n1/n2
           ~~^~~
ZeroDivisionError: division by zero
```


## 예외 처리
>[!note] 예외처리
>발생된 예외를 별도 처리 함으로서 프로그램 실행에 영향이 없도록 처리 

### `try ~ except ` 구문 
- 예외 발생 예상 구문을 try~except 구문으로 감싼다.

```python
n1=10;n2=0  
  
try:  
    print(n1/n2)  
except:  
    print("예외 처리 발생")  
print(n1*n2)
```

```text
예외 처리 발생
0
```

#### 실습
- 숫자가 아닌 자료형을 받으면 예외처리를 하는 프로그램

```python
nums=[]  
  
n=1  
while n < 6:  
    try:  
        num = int(input("숫자 입력 : "))  
    except:  
        print("숫자를 입력해 주세요")  
        continue  
    nums.append(num)  
    n+=1  
print (f"nums : {nums}")
```

### `try ~ except ~ else`  구문
>[!note] else
> 예외가 발생하지 않는 경우 실행하는 구문 

```python
nums=[]  
  
n=1  
while n < 6:  
    try:  
        num = int(input("짝수 입력 : "))  
    except:  
        print("숫자를 입력해 주세요")  
        continue  
    else:  
        if num % 2 ==0:  
            nums.append(num)  
            n += 1  
        else:  
            print("입력한 숫자는 홀수 입니다",end=" ")  
            print("숫자 다시 입력")  
print (f"nums : {nums}")
```

#### 실습 
- 짝수
- 홀수
- 실수
- 로 구해서 리스트로 저장하는 프로그램 
```python
eveList=[]; oddList=[];floatList=[]  
  
n=1  
while n < 6:  
    try:  
        num = float(input("숫자 입력 : "))  
    except:  
        print("숫자를 입력해 주세요")  
        continue  
    else:  
        if num - int(num) !=0 :  
            floatList.append(num)  
            n += 1  
        elif num % 2 ==0 :  
            oddList.append(int(num))  
            n += 1  
        else :  
            eveList.append(int(num))  
            n += 1  
  
print (f"floatList : {floatList}")  
print (f"oddList : {oddList}")  
print (f"eveList : {eveList}")
```

```text
숫자 입력 : 3
숫자 입력 : 6
숫자 입력 : 8
숫자 입력 : 12.34
숫자 입력 : 짝수
숫자를 입력해 주세요
숫자 입력 : 15
floatList : [12.34]
oddList : [6, 8]
eveList : [3, 15]
```


### finally 구문
>[!hint] finally 구문
> 예외 발생과 상관 없이 실행되는 구문 
- 예시 : 네트워크 연결 후 connection을 close 하는 것

```python
try:  
    inputData=input("숫자 입력 : ")  
    numInt =int(inputData)  
except:  
    print("예외 발생 : 숫자가 아님")  
else:  
    if numInt%2==0:  
        print("짝수임")  
    else :  
        print("홀수임")  
finally:  
    print(f"들어간 데이터 : {inputData}")
```

```text
숫자 입력 : 24
짝수임
들어간 데이터 : 24
```
#### 실습
- 5개 숫자를 받음
- 짝수 홀수 실수 구분
- 나중에 입력된 모든 데이터를 출력
```python
eveList=[]; oddList=[];floatList=[];dataList=[]  
  
n=1  
while n < 6:  
    try:  
        data=input("숫자 입력 : ")  
        num = float(data)  
    except:  
        print("숫자를 입력해 주세요")  
        continue  
    else:  
        if num - int(num) !=0 :  
            floatList.append(num)  
            n += 1  
        elif num % 2 ==0 :  
            oddList.append(int(num))  
            n += 1  
        else :  
            eveList.append(int(num))  
            n += 1  
    finally :  
        dataList.append(data)  
  
print (f"floatList : {floatList}")  
print (f"oddList : {oddList}")  
print (f"eveList : {eveList}")  
print (f"dataList : {dataList}")
```

## Exception 클래스
>[!tldr] Exception 클래스
> 예외를 담당하는 클래스 

- `except Exception as e: `
	- 와 같이 쓰면 어떤 이유로 예외처리 되었는지 알 수 있음
- 알아서 예외처리를 한다는 장점이 있음
```python
num1=int(input("숫자 입력 : "))  
num2=int(input("숫자 입력 : "))  
  
try:  
    print(f"num1 / num2 = {num1 / num2}")  
except Exception as e:  
    print(f"Excepttion : {e}")
```

```text
숫자 입력 : 2
숫자 입력 : 0
Excepttion : division by zero
```

### raise 
>[!fail] raise
>에러를 발생시키는 키워드


```python
def divCalcul(n1,n2):  
    if n2 !=0:  
        print(f"{n1} / {n2} = {n1/n2}")  
    else :  
        raise Exception("0으로 나눌 수 없음")  
  
num1=int(input("숫자 입력 : "))  
num2=int(input("숫자 입력 : "))  
  
try:  
     divCalcul(num1,num2)  
except Exception as e :  
    print(f"Exception : {e}")
```

```text
숫자 입력 : 2
숫자 입력 : 0
Exception : 0으로 나눌 수 없음
```

#### 실습
- 10글자 이하  SMS
- 10글자 초과 MMS
- 예외처리 

- 예외가 발생 때, 에러코드를 만들어냄
	- `e.args[1]` 로 에러 코드를 받아 자연스럽게 전환
```python
def sendSMS(msg):  
    if len(msg) > 10 :  
        raise Exception("길이가 초과되어 MMS로 전환됩니다1",1)  
    else:  
        print("SMS 전송 완료 ")  
  
def sendMMS(msg):  
    if len(msg) <= 10 :  
        raise Exception("길이가 미달로 SMS로 전환됩니다1",2)  
    else:  
        print("MMS 전송 완료 ")  
  
msg = input("메세지를 입력해주세요 : ")  
  
try:  
    sendSMS(msg)  
except Exception as e :  
    print(f"e: {e.args[0]}")  
    print(f"e: {e.args[1]}")  
  
    if e.args[1] == 1:  
        sendMMS(msg)  
    elif e.args[1]==2:  
        sendSMS(msg)
```

```text
메세지를 입력해주세요 : 끝까지 가볼래 포기는 안할래 난 쓰러져도 일어날 위고 위하이 고마이온온 오오 라라라라라라라랄 걸스네버다이 절대 네벌크라이
e: 길이가 초과되어 MMS로 전환됩니다1
e: 1
MMS 전송 완료 
```


## 사용자 예외 클래스 
>[!note] 사용자 예외 클래스
> 나만의 예외 클래스 만들기 
> - Exception 클래스를 상속해서 사용자 예외 클래스를 만들 수 있다.


```python
### Exception 클래스를 상속
class ZeroIsNewAttitude(Exception):  
    def __init__(self,n):  
        super().__init__(f"{n} Is New Attitude")  
  
def divCal(num1,num2):  
    if num2 == 0:  
		## 상속받은 예외클래스로 발생
        raise ZeroIsNewAttitude(num2)  
    else:  
        print(f"{num1} / {num2} = {num1/num2}")  
  
num1=int(input("숫자 입력 : "))  
num2=int(input("숫자 입력 : "))  
  
try:  
    divCal(num1,num2)  
except ZeroIsNewAttitude as e :  
    print(e)
```

```text
숫자 입력 : 13
숫자 입력 : 0
0 Is New Attitude
```

# 텍스트 파일 다루기

## 텍스트 파일 기본 함수 
- `open()` : 파일 열기
	-  open(파일 인수, 모드)
	- w : 쓰기 모드 / r : 읽기 모드
	- w: 모드 일 경우 없으면 만듧
		- 기존에 있던 걸 없애버리고 새로운 문자열로 덮음
- `read()` : 파일 읽기
- `write()` : 파일 쓰기
- `close()` : 파일 닫기

## 쓰기 모드 
- w: 모드 일 경우 없으면 만듧
 - 기존에 있던 걸 없애버리고 새로운 문자열로 덮음
```python
### 쓸 파일 열기 

file = open("C:/pythonEx/test.txt","w")  

### 글자수 세기
strCnt=file.write("Hello Python")  
print(f"strCnt : {strCnt}")  
  
file.close()
```

## 읽기 모드
- r : 모든 문자열을 사져옴 
```python
file = open("C:/pythonEx/test.txt","r")  
  
strData=file.read()  
print(f"strData : {strData}")  
  
file.close()
```

```text
strData : Hello Python
```

#### 실습
- 텍스트 파일의 Python을 파이썬으로 변경한 뒤 다시 저장 하기 
- `replace()` 함수를 이용해 글자 바꾸기
```python
file = open("C:/pythonEx/python이란.txt","r",encoding="UTF-8")  
  
orignStr=file.read()  
print(f"orignStr : {orignStr}")  
  
newStr=orignStr.replace("Python","파이썬",2)  
print(f"newStr : {newStr}")  
  
file.close()  
  
file = open("C:/pythonEx/python이란.txt","w",encoding="UTF-8")  
file.write(newStr)  
file.close()  
  
file = open("C:/pythonEx/python이란.txt","r",encoding="UTF-8")  
print(f"변경된 문구 : {file.read()}")  
file.close()
```

```text
orignStr : 파이썬[2](영어: Python)은 1991년[3] 네덜란드계 소프트웨어 엔지니어인 귀도 반 로섬[4]이 발표한 고급 프로그래밍 언어로, '인터프리터를 사용하는 객체지향 언어'이자 플랫폼에 독립적인, 동적 타이핑(dynamically typed) 대화형 언어다. 파이썬이라는 이름은 귀도가 좋아하는 코미디인〈Monty Python's Flying Circus〉에서 따온 것이다. 이름에서 고대신화에 나오는 커다란 뱀을 연상하겠지만 이와는 무관하다. 다만 로고에는 뱀 두마리가 형상화되어 있다. 간결하고 읽기 쉬운 문법이 특징인 프로그래밍 언어로 데이터 분석, 웹 개발, 인공지능 등 다양한 분야에서 활용된다.
newStr : 파이썬[2](영어: 파이썬)은 1991년[3] 네덜란드계 소프트웨어 엔지니어인 귀도 반 로섬[4]이 발표한 고급 프로그래밍 언어로, '인터프리터를 사용하는 객체지향 언어'이자 플랫폼에 독립적인, 동적 타이핑(dynamically typed) 대화형 언어다. 파이썬이라는 이름은 귀도가 좋아하는 코미디인〈Monty 파이썬's Flying Circus〉에서 따온 것이다. 이름에서 고대신화에 나오는 커다란 뱀을 연상하겠지만 이와는 무관하다. 다만 로고에는 뱀 두마리가 형상화되어 있다. 간결하고 읽기 쉬운 문법이 특징인 프로그래밍 언어로 데이터 분석, 웹 개발, 인공지능 등 다양한 분야에서 활용된다.
변경된 문구 : 파이썬[2](영어: 파이썬)은 1991년[3] 네덜란드계 소프트웨어 엔지니어인 귀도 반 로섬[4]이 발표한 고급 프로그래밍 언어로, '인터프리터를 사용하는 객체지향 언어'이자 플랫폼에 독립적인, 동적 타이핑(dynamically typed) 대화형 언어다. 파이썬이라는 이름은 귀도가 좋아하는 코미디인〈Monty 파이썬's Flying Circus〉에서 따온 것이다. 이름에서 고대신화에 나오는 커다란 뱀을 연상하겠지만 이와는 무관하다. 다만 로고에는 뱀 두마리가 형상화되어 있다. 간결하고 읽기 쉬운 문법이 특징인 프로그래밍 언어로 데이터 분석, 웹 개발, 인공지능 등 다양한 분야에서 활용된다.
```


## 열기 모드 
>[!note] 목적에 따라 열기 모드를 정할 수 있음
>- w : 쓰기 전용
>	- 파일이 있으면 덮어씀
>- a : 쓰기 전용
>	- 파일이 있으면 append함
>- x : 쓰기 전용
>	- 파일이 있으면 에러 발생
>- r : 읽기 전용
>	- 파일이 없으면 에러 발생

```python
uri="C:/pythonEx/"  
  
### W : 쓰기  
file =open(uri + "w+a_mode","w")  
file.write("w모드는 파일을 새로 만듦")  
file.close()  
  
### A : 추가 쓰기  
file =open(uri + "w+a_mode","a")  
file.write("a모드는 파일 뒤에 새로 작성")  
file.close()  
  
### X : 새로 만들기  
file =open(uri + "x_mode","x")  
file.write("x모드는 파일을 새로 만듦/n파일이 있으면 오히려 예외 발생")  
file.close()  
  
### R : 파일 읽기  
file=open(uri+"w+a_mode","r")  
print(f"file.read() : {file.read()}")  
file.close()  
  
file=open(uri+"x_mode","r")  
print(f"file.read() : {file.read()}")  
file.close()
```

```text
file.read() : w모드는 파일을 새로 만듦a모드는 파일 뒤에 새로 작성
file.read() : x모드는 파일을 새로 만듦/n파일이 있으면 오히려 예외 발생
```


## with as 문 
>[!note] with as 문 
>파일 닫기(close)를 생략 

- with ~ as 문을 이용해 파일 닫기 생략

```python
uri="C:/pythonEx/"  
with open(uri + "5_037.txt","a") as file:  
    file.write("with as 문을 이용하면 close를 생략 할 수 있습니다.")  
  
with open(uri + "5_037.txt","r") as file:  
    print(file.read())
```

```text
with as 문을 이용하면 close를 생략 할 수 있습니다.
```

#### 실습 
- 로또 번호 생성기 
```python
import random  
  
uri = "C:/pythonEx/"  
  
def lotoGen(nums):  
    for idx, num in enumerate(nums):  
        with open(uri + "lotto.txt","a") as f :  
            if idx < (len(nums)-2):  
                f.write(str(num)+", ")  
            elif idx == (len(nums) -2):  
                f.write(str(num))  
            elif idx == (len(nums)-1):  
                f.write("\n")  
                f.write("보너스 :" + str(num))  
                f.write("\n")  
  
rNums=random.sample(range(1,46),7)  
print(f"rNum : {rNums}")  
lotoGen(rNums)  
  
with open(uri + "lotto.txt","r") as f :  
    print("당첨 번호 \n" , f.read())
```

```text
rNum : [21, 39, 37, 36, 33, 16, 41]
당첨 번호 
 21, 39, 37, 36, 33, 16
보너스 :41
```


## writelines( )
>[!note] writelines
>반복 가능한 자료형의 데이터를 파일에 쓰기

- 리스트 또는 튜플 데이터를 파일에 쓰기 위함
	- f.write(item)  와 f.write("\n") 를 짧게 만듦
	- `( )` 안에 for문을 사용하여 개행 할 수 있음

```python
uri="C:/pythonEx/"  
lang = ["c","java","c#","python","js"]  

with open(uri + "lang.txt","a") as f:  
    #f.write(item)  
    #f.write("\n")    # 를 아래와 같이 짧게
    f.writelines(item + "\n" for item in lang)  
  
with open(uri + "lang.txt","r") as f:  
    print(f.read())
```

```text
c
java
c#
python
js

```

- `print(<딕셔너리/리스트>,file=f)` 형식으로 딕셔너리나 리스트 같은 형식으로 출력 할 수 있음 
#### 실습 
- 딕셔너리를 키 : 밸류 형식으로 바꾸기 
```python
scoreDic = {"kor" : 85, "math" : 85, "eng" : 85, "hist" : 85, "science" : 85,}  
uri="C:/pythonEx/"  
with open(uri + "/scoreDic.txt","a") as f:  
    f.writelines(key +"\t:" +str(scoreDic[key])+"\n" for key in scoreDic.keys())  
#   딕셔러니 자체를 파일로  
#   print(scoreDic, file=f)  
with open(uri + "/scoreDic.txt","r") as f:  
    print(f.read())
```

```text
kor	:85
math	:85
eng	:85
hist	:85
science	:85
```


## readlines(), readline()
>[!note] 여러줄/한줄 읽기
> readlines( ) : 여러줄 읽기
> readline() : 한 줄 읽기 

### readlines() 
- 파일의 모든 데이터를 읽어서 `리스트` 형식으로 반환 

```python
uri="C:/pythonEx/"  
  
with open(uri + "lans.txt","r") as f:  
    lanlist=f.readlines()  
      
print(f"lanlist : {lanlist}")  
print(f"lanlist Type : {type(lanlist)}")
```

```text
lanlist : ['kor\n', 'math\n', 'eng\n', 'hist\n', 'science\n']
lanlist Type : <class 'list'>
```


### readline()
- 한 줄만 읽기
```python
uri="C:/pythonEx/"  
  
with open(uri + "lans.txt","r") as f:  
    line=f.readline()  
    while line !="":  
        print(f"line : {line}",end="")  
        line = f.readline()
```

```text
line : kor
line : math
line : eng
line : hist
line : science
```
