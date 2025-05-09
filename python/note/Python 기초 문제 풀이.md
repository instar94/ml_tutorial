# 파이썬 기초 

## 파이썬 개요 
> 파이썬의 특징 

- 문법 구조가 쉬움 
- 언어가 뛰어나고 모듈이 많음 
- 무한 정수를 처리 가능 
- 온라인상에 커뮤니티 형성이 잘 되어 있음 

> 명령 프롬프트를 이용해 python 설치 확인 

```cmd
python
```

> 파이썬 쉘로 출력하기 

```python 
5*3 
### 16

3*8
###24

print("Hello Python")
print("나의 이름은 무능한 일반인 입니다.")
```

> 코드 편집기에서 현재 시간을 알려주는 코드 

```python 
print("=======RESTART: ")

```

# 데이터와 변수 
### 주문 확인서 만들기 
> ,로 변수를 print와 함께 쓸 수 있음 
```python
price=1000
print("가격 : ",price)
```

> 주문확인서 템플릿을 만들고 변경되는 정보만 입력하면 완성되도록 만들지 

```python 
clientName=""
productName=""
price=0
orderNum=0
payPrice=0
usePoint=0

print("{} 고객님 안녕하세요".format(clientName))
print("{} 고객님 주문을 완료하였습니다 ".format(clientName))
print("주문 상세 내역")
print("=====================")
print("상품명 :",productName)
print("가격 : {}".format(price))
print("결제 금액 : {}".format(payPrice))
print("포인트 : {}".format(usePoint))
```


### 데이터의 가공 

#### 길이 반환
>ㅣlen() 함수를 이용해 길이 반환

```python
### userMgs = input(메세지 입력 : )
#print("문자 길이 : {}".foirmat(len(userMgs)))

str13="Hello Python!"
print("문자 길이는 ",len(str13))

```

#### 객체지향 문자열 찾기 
> find() 함수를 이용해 특정 문자열의 위치를 찾아냄 

```python
msg="이렇게 길게쓰면 찾기 힘들수도 있는데 파이썬에서는 find() 함후를 이용해서 찾을 수 있다."

strIdx=msg.find("파이썬")
print("문자의 위치는 {}".format(strIdx)
```

#### 형변환
> float()로 실수로 형변환 가능
> -print 시 %.2f 와 같은 형식으로 소숫점 처리 가능

```python
width=float(input=("가로 : "))
height=input=float(("세로 : "))

samGacArea = width * height / 2
nemoArea = width * height 

print("="*25)
print("삼각형 넓이 : %.2f" %samGacArea)
print("사각형 넓이 : %.2f" %nemoArea)
print("="*25)
```

#### 형변환2
정수, 소수점 1자리, 소수점 셋째자리 

```python 
pi=3.14
redius = float(input(반지름 : ))

circleArea = pi * redius * redius
circleLenght = 2 * pi * redius

print('원 넓이 %d:" %circleArea)
print('원 둘레 %d:" %circleLength)

print('원 넓이 %.1f:" %circleArea)
print('원 둘레 %.1f:" %circleLength)

print('원 넓이 %.3f:" %circleArea)
print('원 둘레 %.3f:" %circleLength)

```

#### 개인정보 마스킹 
```python
name = "홍길동"
mail = "honggil@email.com"
userId = hongID
pw = honghonghong
maskPW="*"*len(pw)
jubunF = 12345678
jubunB = 1234567
maskJUBUN = jubunB[0]+"*"*(len(jubunB)-1)
print("-" * 25)
print("이름 : ", name)
print ("이메일 : ", mail)
print("아이디 : ", userId)
print("비밀 번호: ",maskPW)
print(f"주민등록번호 : ",{jubunF} - {maskJUBUN}")
```

#### BMI 출력 프로그램 
- 체중은 g으로 받아서 kg으로 
- 신장은 cm로 받아서 cm로 환산 
- weight가 숫자/height가 숫자인지 체크
- BMI 계산 = (몸무게 / 신장) \*신창
- isdigit() : 숫자이면 True 를 반환
```python

weight=input("몸무게 (g)")
height=input("키(cm)")

if weghit.isdigit():
    weight = int(weight) / 1000
if height.isdigit():
    height=int(height)/100

bmi=weight / (height *height)
print("체중 : {} kg".format(weghit))
print("신장 : {} kg".format(height))
print("bmi : {} kg".format(bmi))
```

#### num1 과 num2의 값을 바꾸기 
```python
num1 = 10 
num2 = 20 
print("num1 : {} , num2 : {}".format(num1, num2))

tmpNum1 = 10
num1 = num2
num2 = tmpNum1

print("num1 : {} , num2 : {}".format(num1, num2))
```


#### 성적표 만들기 
```python
score1 = input("중간 점수 : " )
score2 = input("기말점수 : " )

if score1.isdigit() and score.isdigit():
    score1=int(score1)
    score2=int(score2)
    totalScore = score1 + score2
    avgScore = totalScore /2 
    print("총 점 : {} , 평균점수 {}".format(totalScore,avgScore))
else :
    print("입력 실패")
```

#### 키오스크 언어 선택 
```python 
langSelect = input(" 1.한국어 \t2.Eng")
if langSelect=="1":
    menu ="1.샌드위치\t2.햄버거"
elif langSelect=="2":
     menu="1.Sandwich\t2.Hamburger"
 print(menu)
```

#### 100세되는 나이 구하기 
>datetime 패키지 : 시스템 시간 구하기 

```python 
import datatime

today = datetime.datetime.today
myAge = input("나이 : ")
if myAge.isdigit():
    afterAge = 100-int(myAge)
    my100=today.year + afterAge

     print("{}년 {}년 후에 100살".format(my100,afterAge))
else:
    print("입력 실패")
```

# 연산자 

## 산술, 비교, 논리 연산자 
### 거스름돈 계산 
- 가격 지불 금액 > 거스름돈 계산
- 단 지폐, 동전 갯수 최소화
- 1원 단위 절사  - 10으로 나눈 몫을 다시 10을 곱함
```python
mon50000=50000;mon10000=100000;mon5000=5000;mon1000=1000;mon500=500;mon100=100,,mon10=10

mon50000cnt=0;mon10000cnt=0;mon5000cnt=0;mon1000cnt=0;mon500cnt=0;mon100cnt=0,,mon10cnt=0

price = int(input("상품가격 입력 :  "))
paymon = int(input ("지불 금액 : " ))

if price > paymon:
    changeMon = paymon - price
    changeMon = ( changeMon // 10 ) * 10
    print(changeMon)

if changeMon > mon50000
     mon50000cnt = changeMon//mon50000
     changeMon %= mon50000

if changeMon > mon10000
     monn10000cnt = changeMon//monn10000
     changeMon %= monn10000
#### 중략
```

### 다양한 연산자를 이용한 프로그래밍 

#### 성적표 
- 최고 점수 과목
- 최저 점수 과목
- 최고 점수 - 최저점수 차이 
```python

korScore = int(input("국어 점수 : "))
engScore = int(input("영어 점수 : "))
mathScore = int(input("수학 점수 : "))

totalScore = korScore+engScore+mathScore
avgScore = totalScore / 3

maxScore =koreScore
maxSubject="국어"
if engScore > maxScore
    maxScore=engScore
    maxSubject="영어"

if mathScore > maxScore
    maxScore=mathScore
    maxSubject="수학"

minScore =koreScore
minSubject="국어"
if engScore < minScore
    minScore=engScore
    minSubject="영어"

if mathScore < minScore
    minScore=mathScore
    minSubject="수학"
    

diffScore = maxScore - minScore 

print("*"*30)
print("국어 점수 : ",korScore)
print("영어 점수 : ",engScore)
print("수학 점수 : ",mathScore)
print("총 점수 : ",totalScore)
print("평균 점수 : %.2f"%avgScore)
print(f"최고 과목 : {maxSubject}, 최고 점수{mathScore}")
print(f"최고 과목 : {minSubject}, 최고 점수{minScore}")
print("차이 점수 : ",diffScore)
print("*"*30)
```

#### 초로 환산
```python
hou=int(input("시간 입력 : "))
minu=int(input("분 입력 : "))
sec=int(input("초 입력 : "))

#print("{} 초 ".format(hou*60*60+minu*60+sec))
print("{} 초 ".format(format(hou*60*60+minu*60+sec),","))
```

#### 복리 계산
- 금액, 이율, 거치기간 입력 - 복리 계산 
```python
mon=int(input("금액 입력 :))
rate=float(input("이율 입력 : "))
term=int(input("기간 입력 :"))

targetMon=mon

for in range(term):
    targetMon+=targetMon*rate*0.01 # 1년 이자 + 원금

targetMonFormed=format(int(targetMon),",")
print("{}년 후 금액 {}원".format(term,targetMonFormed))
```


#### 고도 - 온도 
> 고도 60m 당 기온이 0.8도 하강
> 고도 입력 후 기온이 출력되는 프로그램 
> 지면의 온도는 29m

```python
baseTemp=29
step=60
stepTemp=0.8

height=int(input("현재 고도 입력 : "))

targetTemp = baseTemp - (height // setp * 0.8)

#### 나머지가 0이 아니다 = 60m보다 더 올라감 
if height % step !=0:
    targetTemp -= stepTemp

print("고도 {}m의 온도는 {}도".format(height,targetTemp))

```


#### 빵 나눠주기 
> 197개 빵과 152개 우유를 17명에게 나눠줌
> 1인당 가지게 되는 빵과 우유의 수와 남는 수를 구하시오


```python
bread = 197
milk - 152
studentCnt = 17

### 1인당 빵과 우유
studentBread = bread // studentCnt
studentMilk = milk // studentCnt

### 남는거
breadnNamoge= bread % studentCnt
milkNamoge = milk % studentCnt

```

#### 접종 대상 구분 
> 19세 이하, 65세 이상 - 출생연도 끝자리에 따른 접종
> 다른 나이 대: 하반기 일정 확인 필요

```python
age = int(input("나이 입력 : "))
if age <= 19 or age >= 65:
    endNum=int(input("출생 연도 끝자리 입력 : "))
    elif endNum ==1 or endNum=6:
        print("월요일")
    elif endNum ==2or endNum=7:
        print("화요일")
    elif endNum ==3 or endNum=8:
        print("수요일")
    elif endNum ==4 or endNum=9:
        print("목요일") 
else:
    print ("하반기 일정 확인")
```

#### 환산
```python
btInch = 0.039
lengthmm = int(input("길이 입력 :"))
lengthInch=lengthmm*btInch

print('{}mm > {}inch'.format(lengthmm,lengthInch))

```


# 조건문

#### 교통 과속 위반 
>50이하 안전 속도 준수
>초과 위반 과태료 부과 대상 


```python
speedNum=int(input("속도 : "))
limitSpeed = 50
if speedNum >limitSpeed:
    print("속도 위반")
else:
    print("속도 준수")
```

#### 문자 길이 요금 결정 
> 50자 이상 100원
> 이하 50원

```python
message = input("메세지 입력" : )
lenMessage= len(message)
msgPrice=0

if lenMessage<=50:
    msgPrice=50
    print("SMS 발송")
else:
    msgPrice=100
    print("MMS 발송")

print("메세지 길이 {}, 요금 {}원".format(lenMessage,msgPrice))
```

#### 데이터 출력
- abs() : 절대값 

> 평균 : 
> 국어 85
> 영어 82
> 수학 89
> 과학 75
> 국사 94
> 편차 데이터는 막대그래프로 시각화 

```python 
korScore=int(input("국어 점수 : "))
engScore=int(input("영어 점수 : "))
mathScore=int(input("수학 점수 : "))
sciScore=int(input("과학 점수 : "))
histScore=int(input("국사 점수 : "))

totalScore=sum(korScore,engScore,mathScore,sciScore,histScore)
avgScore=totalScore/5

korAvg=85
engAvg=82
mathAvg=89
sciAvg=75
histAvg=94
totalAvg=sum(korAvg,engAvg,mathAvg,sciAvg,histAvg)
avgAvg=totalAvg/5

diffKor=korScore-korAvg
diffEng=engScore-engAvg
diffMath=mathScore-mathAvg
diffSci=sciScore-sciAvg
diffHist=histScore-histAvg
diffTotal=totalScore-totalAvg
diffAvg=avgScore-avgAvg

if diffKor > 0:
    print("국어 편차 : ","+"*diffKor,"()".format(diffKor))
else
    print("국어 편차 : ","-"*abs(diffKor),"()".format(diffKor))

```