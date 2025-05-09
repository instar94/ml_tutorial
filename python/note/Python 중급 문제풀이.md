# 1 함수
## 1.1 산술 연산 계산기 함수 
```python
def add(n1,n2):  
    return n1+n2  
def sub(n1,n2):  
    return n1-n2  
def mul(n1,n2):  
    return n1*n2  

def div(n1,n2):  
    return n1/n2  
def mod(n1,n2):  
    return n1%n2  
def flo(n1,n2):  
    return n1//n2  
def exp(n1,n2):  
    return n1**n2  
  
while True:  
    print("="*30)  
    selectName = int(input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.나머지 6.몫 7.거듭제곱 8.종료"))  
    if selectName==8:  
        print("종료")  
        print("=" * 30)  
        break  
    num1=float(input("숫자 입력 1 : "))  
    num2 = float(input("숫자 입력 2 : "))  
  
    if selectName==1:  
        print(f"{add(num1,num2)}")  
    elif selectName==2:  
        print(f"{sub(num1,num2)}")  
    elif selectName == 3:  
        print(f"{mul(num1, num2)}")  
    elif selectName==4:  
        print(f"{div(num1,num2)}")  
    elif selectName==5:  
        print(f"{mod(num1,num2)}")  
    elif selectName==6:  
        print(f"{flo(num1,num2)}")  
    elif selectName==7:  
        print(f"{exp(num1,num2)}")  
    else :  
        print("잘못된 입력")  
    print("=" * 30)
```

```text
==============================
1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.나머지 6.몫 7.거듭제곱 8.종료1
숫자 입력 1 : 10
숫자 입력 2 : 20
30.0
==============================
==============================
1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.나머지 6.몫 7.거듭제곱 8.종료7
숫자 입력 1 : 4
숫자 입력 2 : 10
1048576.0
==============================
==============================
1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.나머지 6.몫 7.거듭제곱 8.종료8
종료
==============================
```

## 1.2 이동 거리 - 시간 반환 프로그램
```python
def getDistance(speed,hour,minute):  
    distance = speed * (hour + minute / 60)  
    return distance  
def getTime(speed,distance):  
    time=distance / speed  
    h= int(time)  
    m= int((time-h)*100 * 60 / 100)  
    return [h,m]  
  
print("="*60)  
### 거리 = 속력*시간  
s = float(input("속도 (km/h):"))  
h = float(input("시간 (시):"))  
m = float(input("시간 (분):"))  
d=getDistance(s,h,m)  
print(f"{s}km/h로 {h}시간 {m}분 이동하여 {d}km/h 이동 가능")  
print("="*60)  
  
print("="*60)  
### 거리 = 속력*시간  
s = float(input("속도 (km/h):"))  
d= float(input("이동 거리"))  
t=getTime(s,d)  
print(f"{s}km/h로 {t[0]}시간 {t[1]}분 이동하여 {d}km/h 이동 가능")  
print("="*60)
```

## 1.3 비행기 티켓 영수증 함수 
```python
childPrice=18000  
infantPrice=25000  
adultPrice=50000  
saleRatio=0.5  
  
def getTotalCnt(childCnt,infantCnt,adultCnt):  
    return childCnt+infantCnt+adultCnt  
  
def getTotalPrice(childCnt,infantCnt,adultCnt,childSale,infantSale,adultSale):  
    totalPrice=childCnt*childPrice+infantCnt*infantPrice+adultCnt*adultPrice  
    salePrice=(childSale*childPrice+infantSale*infantPrice+adultSale*adultPrice)*(1-saleRatio)  
    return totalPrice-salePrice  
print("="*60)  
childCnt=int(input("유아 : "))  
childSale=int(input("유아 할인 대상 : "))  
infantCnt=int(input("소아 : "))  
infantSale=int(input("소아 할인 대상 : "))  
adultCnt=int(input("성인 : "))  
adultSale=int(input("성인 할인 대상 : "))  
print("="*60)  
total=int(getTotalCnt(childCnt,infantCnt,adultCnt))  
totalPrice=int(getTotalPrice(childCnt,infantCnt,adultCnt,childSale,infantSale,adultSale))  
print(f"Total : {total}명")  
print(f"TotalPrice : {totalPrice}원")  
print("="*60)
```

```text
============================================================
유아 : 10
유아 할인 대상 : 2
소아 : 4
소아 할인 대상 : 3
성인 : 10
성인 할인 대상 : 0
============================================================
Total : 24명
TotalPrice : 724500원
============================================================
```

## 1.4 재귀함수로 팩토리얼 만들기
```python
##재귀함수  
def recuFx(n):  
    if n==1:  
        return n  
    return n * recuFx(n-1)  
  
  
num=int(input("숫자 입력 : "))  
print(f"팩토리얼 : {recuFx(num)}")
```

```text
숫자 입력 : 10
팩토리얼 : 3628800
```


## 1.5 단리 / 월복리 계산기 

```python
def formatNum(n):  
    return format(n,",")  
  
### 단리  
def singleRate(m,t,r):  
    totalMoney=0  
    totalRateMoney=0  
  
    for i in range(t):  
        totalRateMoney += m*(r*0.01)  
  
    totalMoney=m+totalRateMoney  
    return int(totalMoney)  
  
### 월복리  
def multiRate(m,t,r):  
    ### 월단위로 변경  
    t=t*12  
    rpm = (r/12)*0.01  
    totalMoney = m  
  
    for i in range(t):  
        totalMoney += totalMoney * rpm  
  
    return int(totalMoney)  
  
money=int(input("예치금 (원) : "))  
term=int(input("기간 (연) : "))  
ratio=int(input("연이율 (%) : "))  
  
print(f"단리 총 수령 금액 : {formatNum(singleRate(money,term,ratio))}")  
print(f"월복리 총 수령 금액 : {formatNum(multiRate(money,term,ratio))}")
```

## 1.6 등차수열 출력
### 1.6.1 내가 짠 것
```python
def seq(a1,d,n):  
    num=0  
    for i in range(n):  
        print(f"{i+1}번째 항의 값 : {a1+i*d}")  
        num +=a1+i*d  
        print(f"{i+1}번째 항까지 합 : {num}")  
  
  
a1=int(input("a1 입력 : "))  
d=int(input("공차 입력 : "))  
n=int(input("n 입력 : "))  
  
seq(a1,d,n)
```
### 1.6.2 소스코드
```python
def seq(a1,d,n):  
    valueN=0;sumN=0;  
    i=1  
    while i <=n:  
        if i==1:  
            valueN=a1  
            sumN=valueN  
            print(f"{i}번째 값 : {valueN}")  
            print(f"{i}번째 합 : {sumN}")  
            i+=1  
            continue  
        valueN+= d  
        sumN +=valueN  
        print(f"{i}번째 값 : {valueN}")  
        print(f"{i}번째 합 : {sumN}")  
        i += 1
```

```text
a1 입력 : 2
공차 입력 : 3
n 입력 : 7
1번째 항의 값 : 2
1번째 항까지 합 : 2
2번째 항의 값 : 5
2번째 항까지 합 : 7
3번째 항의 값 : 8
3번째 항까지 합 : 15
4번째 항의 값 : 11
4번째 항까지 합 : 26
5번째 항의 값 : 14
5번째 항까지 합 : 40
6번째 항의 값 : 17
6번째 항까지 합 : 57
7번째 항의 값 : 20
7번째 항까지 합 : 77

```


# 2 모듈

## 점수를 입력하면 합격여부를 출력하는 모듈 
```python
def exampleResult(s1,s2,s3,s4,s5):  
    passAvgScore=60;limitScore=40;  
  
    def getTotalScore(s1,s2,s3,s4,s5):  
        print(f"총점 {s1+s2+s3+s4+s5}")  
        return s1+s2+s3+s4+s5  
  
    def getAverageScore(s1,s2,s3,s4,s5):  
        print(f"평균 {getTotalScore(s1,s2,s3,s4,s5)/5}")  
        return getTotalScore(s1,s2,s3,s4,s5)/5  
  
    def checkPass():  
        print(f"{s1} : PASS") if s1 >=limitScore else print(f"{s1} : fail")  
        print(f"{s2} : PASS") if s2 >= limitScore else print(f"{s2} : fail")  
        print(f"{s3} : PASS") if s3 >= limitScore else print(f"{s3} : fail")  
        print(f"{s4} : PASS") if s4 >= limitScore else print(f"{s4} : fail")  
        print(f"{s5} : PASS") if s5 >= limitScore else print(f"{s5} : fail")  
  
    def printFinalPass():  
        if getAverageScore(s1,s2,s3,s4,s5) >= passAvgScore:  
            if s1 >=limitScore and s2 >=limitScore and s3 >=limitScore and s4 >=limitScore and s5 >=limitScore:  
                print("PASS")  
            else :  
                print("Fail")  
        else:  
            print("Fail")  
    getAverageScore(s1,s2,s3,s4,s5)  
    checkPass()  
    printFinalPass()
```

- 실행부
```python 
import porf as pf  
  
if __name__=="__main__" :  
    sub1= int(input("과목 점수 입력 : "))  
    sub2 = int(input("과목 점수 입력 : "))  
    sub3 = int(input("과목 점수 입력 : "))  
    sub4 = int(input("과목 점수 입력 : "))  
    sub5 = int(input("과목 점수 입력 : "))  
  
    pf.exampleResult(sub1,sub2,sub3,sub4,sub5)
```

```text
과목 점수 입력 : 40
과목 점수 입력 : 50
과목 점수 입력 : 100
과목 점수 입력 : 20
과목 점수 입력 : 30
총점 240
평균 48.0
총점 240
40 : PASS
50 : PASS
100 : PASS
20 : fail
30 : fail
총점 240
평균 48.0
총점 240
Fail

```

### tip 과목이 몇 개 들어 올지 모를때
```python
def exampleResult(*s):
```

## 상품 개수에 따라 할인율이 결정되는 모듈
```python
def calculatorTotalPrice(gs):  
    if len(gs) <=0:  
        print("구매 상품 없음")  
        return  
  
    rate=25  
    totalPrice=0  
  
    rates={1:5,2:10,3:15,4:20}  
  
    if len(gs) in rates:  
        rate= rates[len(gs)]  
  
    for g in gs:  
        totalPrice += g * (1-rate *0.01)  
  
    return [rate, int(totalPrice)]

def formatNum(n):  
    return format(n,",")
```

```python
import saleratio as sr  
  
if __name__=="__main__" :  
    flag=True  
    gs=[]  
  
    while flag:  
        selectNum=int(input("1.구매 \t2.종료"))  
        if selectNum==1:  
            goods_price=int(input("상품가격 : "))  
            gs.append(goods_price)  
        elif selectNum==2:  
            result= sr.calculatorTotalPrice(gs)  
            flag=False  
  
    print(f"할인률 : {result[0]}%")  
    print(f"합계 가격 : {sr.formatNum(result[1])}원")
```

## 로또 생성 
``` python
import random as rd  
  
userNums=[];randomNums=[];collectNums=[];randBonusNum=0  
  
def setUserNum(ns):  
    global userNums  
    userNums = ns  
  
def getUserNum():  
    return userNums  
  
def setRandomNum():  
    global randomNums  
    randomNums = rd.sample(range(1,46),6)  
  
def getRandomNum():  
    return randomNums  
  
def setBonusNum():  
    global randBonusNum  
  
    while True:  
        randBonusNum=rd.randint(1,45)  
        if randBonusNum not in randomNums:  
            break  
  
def getBonusNum():  
    return randBonusNum  
  
def lottoResult():  
    global userNums  
    global randomNums  
    global randBonusNum  
  
    collectNums=[]  
    for un in userNums:  
        if un in randomNums:  
            collectNums.append(un)  
  
    if len(collectNums)=="6":  
        print("1등 당첨")  
        print(f"번호 {collectNums}")  
    elif(len(collectNums)==5 and (randBonusNum in userNums)):  
        print("2등 당첨")  
        print(f"번호 {collectNums}, 보너스 번호 : {randomNums}")  
    elif len(collectNums)==5:  
        print("3등 당첨")  
        print(f"번호 {collectNums}")  
    elif len(collectNums)==4:  
        print("4등 당첨")  
        print(f"번호 {collectNums}")  
    elif len(collectNums)==3:  
        print("5등 당첨")  
        print(f"번호 {collectNums}")  
    else:  
        print("낙첨")  
        print(f"당첨 번호 : {randomNums}")  
        print(f"보너스번호 : {randBonusNum}")  
        print(f"선택 번호 : {userNums}")  
        print(f"맞는 번호 : {collectNums}")  
  
def startlotto():  
    n1=int(input("번호 선택 (1~45)"))  
    n2 = int(input("번호 선택 (1~45)"))  
    n3 = int(input("번호 선택 (1~45)"))  
    n4 = int(input("번호 선택 (1~45)"))  
    n5 = int(input("번호 선택 (1~45)"))  
    n6 = int(input("번호 선택 (1~45)"))  
    selectNum=[n1,n2,n3,n4,n5,n6]  
  
    setUserNum(selectNum)  
    setRandomNum()  
    setBonusNum()  
  
    lottoResult()
```

- 실행부 
```python
import lotto as lt  
lt.startlotto()
```

## 순열 만들기
- `logprint` 를 통해 로깅 할 수 있음
- 진짜 순열 `from itertools import permutations  `

```python
def getPerCnt(n,r,logprint=True):  
    result=1  
    for n in range(n, (n-r), -1):  
        if logprint: print(f"n : {format(n)}")  
        result = result * n  
  
    return result  
  
from itertools import permutations  
def getPer(ns,r):  
    plist=list(permutations(ns,r))  
    print(f"{len(ns)}P{r} 개수 : {len(plist)}")  
    for n in permutations(ns,r):  
        print(n, end="")
```



# 클래스 
## 회원가입 
- 회원가입 클래스
- 회원정보 관리 클래스 
- 로그인 기능 구현

```python
class Member:  
    def __init__(self,i,p):  
        self.id=i  
        self.pw=p  
  
class MemberRepository:  
  
    def __init__(self):  
        self.members = {}  
  
    def addMember(self, m):  
        self.members[m.id] = m.pw  
  
    def loginMember(self, i, p):  
        isMember = i in self.members  
  
        if isMember and self.members[i] == p:  
            print(f'{i}: Log-in success!!')  
  
        else:  
            print(f'{i}: Log-in fail!!')  
  
    def removeMember(self, i, p):  
        del self.members[i]  
  
    def printMembers(self):  
        for mk in self.members.keys():  
            print(f'ID: {mk}')  
            print(f'PW: {self.members[mk]}')
```

## TV 만들기 
```python
class NormalTV:  
    def __init__(self,i=32, c="bk", r="fhd"):  
        self.inch=i  
        self.color=c  
        self.resol=r  
        self.smartTV="off"  
        self.aiTV="off"  
  
    def turnON(self):  
        print("TV 켜짐")  
  
    def turnOff(self):  
        print("TV 꺼짐")  
  
    def printTVInfo(self):  
        print(f"inch={self.inch}")  
        print(f"color={self.color}")  
        print(f"resol={self.resol}")  
        print(f"smartTV={self.smartTV}")  
        print(f"aiTV={self.aiTV}")  
  
class Tv4K(NormalTV):  
    def __init__(self,i,c,r="4K"):  
        super().__init__(i,c,r)  
  
    def setSmartTv(self,s):  
        self.smartTV=s  
  
  
class Tv7K(NormalTV):  
    def __init__(self, i, c, r="8K"):  
        super().__init__(i, c, r)  
  
    def setSmartTv(self, s):  
        self.smartTV = s  
  
    def setAiTv(self, a):  
        self.aiTV = a
```

``` python
import tv  
  
myTv=tv.Tv4K("65","sv","4K")  
myTv.setSmartTv("On")  
myTv.turnON()  
myTv.printTVInfo()  
myTv.turnOff()
```

```text
TV 켜짐
inch=65
color=sv
resol=4K
smartTV=On
aiTV=off
TV 꺼짐
```

## 도서관 프로그램
```python
class Book:  
    def __init__(self,n,p,i):  
        self.name=n  
        self.price=p  
        self.isbn=i  
  
class BookRepository:  
  
    def __init__(self):  
        self.bDic={}  
  
    def registBook(self,b):  
        self.bDic[b.isbn]=b  
  
    def removeBook(self):  
        del self.bDic[isbn]  
  
    def printList(self):  
        for isbn in self.bDic.keys():  
            b=self.bDic[isbn]  
            print(f"{b.name}, {b.price}, {b.isbn}")  
  
    def printInfo(self,isbn):  
        if isbn in self.bDic:  
            b=self.bDic[isbn]  
            print(f"{b.name}, {b.price}, {b.isbn}")  
        else:  
            print("404 Not Found")
    
```

```python
import libaray as lb  
  
bookRepo=lb.BookRepository()  
  
bookRepo.registBook(lb.Book("python",20000,"12341234"))  
bookRepo.registBook(lb.Book("java",27000,"45674567"))  
bookRepo.registBook(lb.Book("C++",32000,"78907890"))  
  
bookRepo.printList()  
bookRepo.printInfo("45674567")  
bookRepo.removeBook("12341234")  
print("="*30)  
bookRepo.printList()
```

```text
python, 20000, 12341234
java, 27000, 45674567
C++, 32000, 78907890
java, 27000, 45674567
==============================
java, 27000, 45674567
C++, 32000, 78907890
```

## 사전만들기

```python
from abc import ABCMeta  
from abc import abstractmethod  
  
class AbsDictionary (metaclass=ABCMeta):  
    def __init__(self):  
        self.wordDic={}  
  
    @abstractmethod  
    def registWord(self,w1,w2):  
        pass  
  
    @abstractmethod  
    def removeWord(self, w1, w2):  
        pass  
  
    @abstractmethod  
    def updateWord(self, w1, w2):  
        pass  
  
    @abstractmethod  
    def searchWord(self, w1, w2):  
        pass  
  
class KorToEng(AbsDictionary):  
    def __init__(self):  
        super().__init__()  
  
    def registWord(self,w1,w2):  
        print(f"[한영사전] 등록 : {w1} > {w2}")  
        self.wordDic[w1]=w2  
  
    def removeWord(self, w1, w2):  
        print(f"[한영사전] 삭제 : {w1}")  
        del self.wordDic[w1]  
  
    def updateWord(self, w1, w2):  
        print(f"[한영사전] 수정 : {w1} > {w2}")  
        self.wordDic[w1] = w2  
  
    def searchWord(self, w1):  
        print(f"[한영사전] 검색 : {w1}")  
        return self.wordDic[w1]  
  
    def printWords(self):  
        for k in self.wordDic:  
            print(f"{k} : {self.wordDic[k]}")  
  
  
class KorToJpn(AbsDictionary):  
    def __init__(self):  
        super().__init__()  
  
    def registWord(self, w1, w2):  
        print(f"[한일사전] 등록 : {w1} > {w2}")  
        self.wordDic[w1] = w2  
  
    def removeWord(self, w1, w2):  
        print(f"[한일사전] 삭제 : {w1}")  
        del self.wordDic[w1]  
  
    def updateWord(self, w1, w2):  
        print(f"[한일사전] 수정 : {w1} > {w2}")  
        self.wordDic[w1] = w2  
  
    def searchWord(self, w1):  
        print(f"[한일사전] 검색 : {w1}")  
        return self.wordDic[w1]  
  
    def printWords(self):  
        for k in self.wordDic:  
            print(f"{k} : {self.wordDic[k]}")
```

```python
from abc import ABCMeta  
from abc import abstractmethod  
  
class AbsDictionary (metaclass=ABCMeta):  
    def __init__(self):  
        self.wordDic={}  
  
    @abstractmethod  
    def registWord(self,w1,w2):  
        pass  
  
    @abstractmethod  
    def removeWord(self, w1, w2):  
        pass  
  
    @abstractmethod  
    def updateWord(self, w1, w2):  
        pass  
  
    @abstractmethod  
    def searchWord(self, w1, w2):  
        pass  
  
class KorToEng(AbsDictionary):  
    def __init__(self):  
        super().__init__()  
  
    def registWord(self,w1,w2):  
        print(f"[한영사전] 등록 : {w1} > {w2}")  
        self.wordDic[w1]=w2  
  
    def removeWord(self, w1, w2):  
        print(f"[한영사전] 삭제 : {w1}")  
        del self.wordDic[w1]  
  
    def updateWord(self, w1, w2):  
        print(f"[한영사전] 수정 : {w1} > {w2}")  
        self.wordDic[w1] = w2  
  
    def searchWord(self, w1):  
        print(f"[한영사전] 검색 : {w1}")  
        return self.wordDic[w1]  
  
    def printWords(self):  
        for k in self.wordDic:  
            print(f"{k} : {self.wordDic[k]}")  
  
  
class KorToJpn(AbsDictionary):  
    def __init__(self):  
        super().__init__()  
  
    def registWord(self, w1, w2):  
        print(f"[한일사전] 등록 : {w1} > {w2}")  
        self.wordDic[w1] = w2  
  
    def removeWord(self, w1, w2):  
        print(f"[한일사전] 삭제 : {w1}")  
        del self.wordDic[w1]  
  
    def updateWord(self, w1, w2):  
        print(f"[한일사전] 수정 : {w1} > {w2}")  
        self.wordDic[w1] = w2  
  
    def searchWord(self, w1):  
        print(f"[한일사전] 검색 : {w1}")  
        return self.wordDic[w1]  
  
    def printWords(self):  
        for k in self.wordDic:  
            print(f"{k} : {self.wordDic[k]}")
```

```text
[한영사전] 등록 : 책 > Book
[한영사전] 등록 : 폰 > Phone
[한영사전] 등록 : 인형 > Doll
[한영사전] 등록 : 꽃 > Flower
[한영사전] 등록 : 돌 > Rock
책 : Book
폰 : Phone
인형 : Doll
꽃 : Flower
돌 : Rock
[한영사전] 수정 : 돌 > RoCK
[한영사전] 검색 : 돌
책 RoCK

```

## 주사위 게임
```python
import random as rd   
  
class Dice:  
    def __init__(self):  
        self.cNum=0  
        self.uNum = 0  
    def setCnum(self):  
        self.cNum=rd.randint(1,6)  
        print(f"[주사위] 컴퓨터의 주사위 : {self.cNum}")  
      
    def setUnum(self):  
        self.uNum=rd.randint(1,6)  
        print(f"[주사위] 사용자의 주사위 : {self.uNum}")  
          
    def startGame(self):  
        print("[주사위] 게임 시작")  
        self.setCnum()  
        self.setUnum()  
      
    def printResult(self):  
        print("[주사위] 게임 시작")  
        if self.cNum==0 or self.uNum==0:  
            print("[주사위] 게임 결렬")  
        else:  
            if self.cNum > self.uNum:  
                print(f"[주사위] 컴퓨터 승리 컴퓨터 : {self.cNum} VS 사용자 : {self.uNum}")  
            elif self.cNum < self.uNum:  
                print(f"[주사위] 사용자 승리 컴퓨터 : {self.cNum} VS 사용자 : {self.uNum}")  
            if self.cNum == self.uNum:  
                print(f"[주사위] 무승부 : {self.cNum} VS 사용자 : {self.uNum}")
        
```

```python
import dice as dc  
  
dc =dc.Dice()  
dc.startGame()  
dc.printResult()
```

```text
[주사위] 게임 시작
[주사위] 컴퓨터의 주사위 : 6
[주사위] 사용자의 주사위 : 1
[주사위] 게임 시작
[주사위] 컴퓨터 승리 컴퓨터 : 6 VS 사용자 : 1
```

## 자동차 경주 

```python
import random  
  
  
class Car :  
    def __init__(self,n="fire car",c="red",s=200):  
        self.name=n  
        self.color=c  
        self.speed=s  
        self.distance=0  
  
    def printCarInfo(self):  
        print(f"name {self.name}")  
        print(f"color {self.color}")  
        print(f"speed {self.speed}")  
  
    def controlSpeed(self):  
        return random.randint(0,self.speed)  
  
  
    def getDistanceForHour(self):  
        return self.controlSpeed()*1
```

```python
from time import sleep  
class CarRacing:  
    def __init__(self):  
        self.cars=[]  
        self.ranking=[]  
  
    def startRacing(self):  
        for i in range(10):  
            print(f"racing : {i+1} 바퀴")  
            for car in self.cars:  
                car.distance += car.getDistanceForHour()  
            sleep(1)  
            self.printCurrentCarDistance()  
  
    def printCurrentCarDistance(self):  
        for car in self.cars:  
            print(f"{car.name} : {car.distance} \t\t", end=" ")  
        print()  
  
    def addCar(self,c):  
        self.cars.append(c)
```

```python
import carrace as cr  
import racing as rc  
  
myCarGame=rc.CarRacing()  
  
car01=cr.Car("car01","red",100)  
car02=cr.Car("car02","blue",200)  
car03=cr.Car("car03","gray",300)  
car04=cr.Car("car04","white",400)  
car05=cr.Car("car05","black",500)  
  
myCarGame.addCar(car01)  
myCarGame.addCar(car02)  
myCarGame.addCar(car03)  
myCarGame.addCar(car04)  
myCarGame.addCar(car05)  
  
myCarGame.startRacing()
```

```text
racing : 1 바퀴
car01 : 89 		 car02 : 177 		 car03 : 162 		 car04 : 238 		 car05 : 95 		 
racing : 2 바퀴
car01 : 123 		 car02 : 339 		 car03 : 345 		 car04 : 599 		 car05 : 527 		 
racing : 3 바퀴
car01 : 219 		 car02 : 516 		 car03 : 460 		 car04 : 754 		 car05 : 991 		 
racing : 4 바퀴
car01 : 315 		 car02 : 588 		 car03 : 479 		 car04 : 789 		 car05 : 1339 		 
racing : 5 바퀴
car01 : 324 		 car02 : 619 		 car03 : 700 		 car04 : 1081 		 car05 : 1349 		 
racing : 6 바퀴
car01 : 380 		 car02 : 678 		 car03 : 740 		 car04 : 1192 		 car05 : 1745 		 
racing : 7 바퀴
car01 : 451 		 car02 : 750 		 car03 : 915 		 car04 : 1287 		 car05 : 2097 		 
racing : 8 바퀴
car01 : 512 		 car02 : 918 		 car03 : 1021 		 car04 : 1307 		 car05 : 2389 		 
racing : 9 바퀴
car01 : 581 		 car02 : 1111 		 car03 : 1114 		 car04 : 1642 		 car05 : 2802 		 
racing : 10 바퀴
car01 : 600 		 car02 : 1136 		 car03 : 1190 		 car04 : 1835 		 car05 : 2959 		 

```

# 예외처리
## 계산기 예외처리 
```python
def add(n1,n2):  
    try:  
        n1 = float(n1)  
    except:  
        print("첫번째 숫자가 없음")  
        return  
    try:  
        n2 = float(n2)  
    except:  
        print("두번째 숫자가 없음")  
        return  
    print(f"{n1}+{n2}={n1+n2}")  
def sub(n1,n2):  
    try:  
        n1 = float(n1)  
    except:  
        print("첫번째 숫자가 없음")  
        return  
    try:  
        n2 = float(n2)  
    except:  
        print("두번째 숫자가 없음")  
        return  
    print(f"{n1}-{n2}={n1 - n2}")  
def mul(n1,n2):  
    try:  
        n1 = float(n1)  
    except:  
        print("첫번째 숫자가 없음")  
        return  
    try:  
        n2 = float(n2)  
    except:  
        print("두번째 숫자가 없음")  
        return  
    print(f"{n1}*{n2}={n1 * n2}")  
  
def div(n1,n2):  
    try:  
        n1 = float(n1)  
    except:  
        print("첫번째 숫자가 없음")  
        return  
    try:  
        n2 = float(n2)  
    except:  
        print("두번째 숫자가 없음")  
        return  
    try:  
        print(f"{n1}/{n2}={n1 / n2}")  
    except ZeroDivisionError as e :  
        print(e)  
        print("0으로 나눌 수 없음")  
def mod(n1,n2):  
    try:  
        n1 = float(n1)  
    except:  
        print("첫번째 숫자가 없음")  
        return  
    try:  
        n2 = float(n2)  
    except:  
        print("두번째 숫자가 없음")  
        return  
    try:  
        print(f"{n1}%{n2}={n1 % n2}")  
    except ZeroDivisionError as e :  
        print(e)  
        print("0으로 나눌 수 없음")  
  
def flo(n1,n2):  
    try:  
        n1 = float(n1)  
    except:  
        print("첫번째 숫자가 없음")  
        return  
    try:  
        n2 = float(n2)  
    except:  
        print("두번째 숫자가 없음")  
        return  
    try:  
        print(f"{n1}//{n2}={n1 // n2}")  
    except ZeroDivisionError as e :  
        print(e)  
        print("0으로 나눌 수 없음")  
def exp(n1,n2):  
    try:  
        n1 = float(n1)  
    except:  
        print("첫번째 숫자가 없음")  
        return  
    try:  
        n2 = float(n2)  
    except:  
        print("두번째 숫자가 없음")  
        return  
    print(f"{n1}**{n2}={n1 ** n2}")
```

## 소수인 난수 
- 소수인 난수 10개 생성 
- 소수 아니면 사용자 예외 발생 

```python
class NotPrimeException(Exception):  
    def __init__(self,n):  
        super().__init__(f"{n}은 소수 아님")  
  
class PrimeException(Exception):  
    def __init__(self,n):  
        super().__init__(f"{n}은 소수")  
  
  
def isPrime(number):  
    flag = True  
    for n in range(2,number):  
        if number % n ==0:  
            flag = False  
            break  
    if flag == False:  
        raise NotPrimeException(number)  
    else :  
        raise PrimeException(number)
        
```

```python
import random  
import primenum as pm  
  
primNum=[]  
  
n=0  
while n < 10:  
    rn=random.randint(1,1000)  
    if rn not in primNum:  
        try:  
            pm.isPrime(rn)  
        except pm.NotPrimeException as e:  
            print(e)  
            continue  
  
        except pm.PrimeException as e:  
            print(e)  
            primNum.append(rn)  
            continue  
    n+=1  
  
print(f"목록 = {primNum}")
```

## 영수증 
- 총 구매 금액 출력
- 개수가 잘 못 입력 된 경우 별도 출력 
```python
g1Price=1200; g2Price=1000; g3Price=800; g4Price=2000; g5Price=900;  
  
def calculator(*gcs):  
    gcsDice={}  
    againCntInput={}  
  
    for idx, gc in enumerate(gcs):  
        try:  
            gcsDice[f"g{idx+1}"]=int(gc)  
        except Exception as e:  
            againCntInput[f"g{idx+1}"]=gc  
            print(e)  
  
    totalPrice=0  
    for g in gcsDice.keys():  
        totalPrice+= globals()[f"{g}Price"]*gcsDice[g]  
  
    print("="*20)  
    print(f"총 구매 금액 : {totalPrice}원")  
    print("=" * 10,"미결제 항목","="*10)  
    for g in againCntInput.keys():  
        print(f"상품 : {g} \t구매 개수:{againCntInput[g]}")
```

```python
import recept as rc  
  
g1=input("g1 :")  
g2=input("g2 :")  
g3=input("g3 :")  
g4=input("g4 :")  
g5=input("g5 :")  
  
rc.calculator(g1,g2,g3,g4,g5)
```

```text
g1 :10
g2 :20
g3 :two
g4 :
g5 :두개
invalid literal for int() with base 10: 'two'
invalid literal for int() with base 10: ''
invalid literal for int() with base 10: '두개'
====================
총 구매 금액 : 32000원
========== 미결제 항목 ==========
상품 : g3 	구매 개수:two
상품 : g4 	구매 개수:
상품 : g5 	구매 개수:두개
```

## 회원가입 프로그램
- 값이 비어진 부분을 에러 메세지로 알려주기
```python
class EmptyDataException(Exception):  
    def __init__(self,i):  
        super().__init__(f"{i} 는 데이터가 없습니다")  
  
def checkInputData(n,em,p,a,ph):  
    if n =="":  
        raise EmptyDataException("name")  
    elif em =="":  
        raise EmptyDataException("email")  
    elif p =="":  
        raise EmptyDataException("password")  
    elif a =="":  
        raise EmptyDataException("address")  
    elif ph =="":  
        raise EmptyDataException("phone")  
  
class RegistMember():  
    def __init__(self,n,em,p,a,ph):  
        self.m_name=n  
        self.m_email=em  
        self.m_pw=p  
        self.m_addr=a  
        self.m_phone=ph  
        print("회원 가입 완료 ")  
  
    def printMemInfo(self):  
        print(f"m_name : {self.m_name}")  
        print(f"m_email : {self.m_email}")  
        print(f"m_pw : {self.m_pw}")  
        print(f"m_addr : {self.m_addr}")  
        print(f"m_phone : {self.m_phone}")
```

```python
import member  
  
m_name=input("이름 : ")  
m_email=input("메일 : ")  
m_pw=input("비번 : ")  
m_addr=input("주소 : ")  
m_phone=input("번호 : ")  
  
  
try:  
    member.checkInputData(m_name,m_email,m_pw,m_addr,m_phone)  
    newMem=member.RegistMember(m_name,m_email,m_pw,m_addr,m_phone)  
    newMem.printMemInfo()  
except member.EmptyDataException as e :  
    print(e)
```

## 은행계좌 개설

```python
import random  
  
  
class Bank:  
    def __init__(self):  
        self.accounts={}  
  
    def addAccount(self,privateBank):  
        self.accounts[privateBank.account_no]=privateBank  
  
    def isAccount(self,ano):  
        return ano in self.accounts  
  
    def doDeposit(self,ano,m):  
        pb = self.accounts[ano]  
        pb.totalMoney = pb.totalMoney+m  
  
    def doWithdraw(self,ano,m):  
        pb=self.accounts[ano]  
        if pb.totalMoney-m <0:  
            raise LackException(pb.totalMoney,m)  
  
  
class LackException(Exception):  
    def __init__(self,m1,m2):  
        super().__init__(f"잔고 부족\t잔액 : {m1}\t출금액 : {m2}")  
  
class PrivateBank:  
    def __init__(self,bank,account_name):  
        self.bank=bank  
        self.account_name=account_name  
  
        while True:  
            newAccountNo=random.randint(10000,99999)  
            if bank.isAccount(newAccountNo):  
                continue  
            else:  
                self.account_no = newAccountNo  
                break  
  
        self.totalMoney=0  
        bank.addAccount(self)  
    def printBankInfo(self):  
        print("="*40)  
        print(f"account_name : {self.account_name}")  
        print(f"account_no : {self.account_no}")  
        print(f"totalMoney : {self.totalMoney}")  
        print("=" * 40)
```

``` python
import bank  
  
koreaBank=bank.Bank()  
  
newAccount_name=input("예금주 명 : ")  
myAccount=bank.PrivateBank(koreaBank,newAccount_name)  
myAccount.printBankInfo()  
  
  
while True:  
    selectNum = int(input("1.입금\t2.출금\t3.종료"))  
    if selectNum==1:  
        m=int(input("입금액 :"))  
        koreaBank.doDeposit(myAccount.account_no,m)  
        myAccount.printBankInfo()  
    elif selectNum==2:  
        m=int(input("출금액 :"))  
        try:  
            koreaBank.doWithdraw(myAccount.account_no,m)  
        except bank.LackException as e :  
            print(e)  
        finally:  
            myAccount.printBankInfo()  
    elif selectNum==3:  
        print("종료")  
        break  
    else :  
        print("입력 오류")
```

# 파일 읽기 쓰기

## 회원 별 한줄 일기 
```python
import time  
  
def writeDiary(u,f,d):  
    lt = time.localtime()  
    timeStr=time.strftime("%Y-%m-%d %I:%M:%S %p", lt)  
    filePath= u+f  
    with open(filePath, "a") as f:  
        f.write(f"[{timeStr}] {d}\n")  
  
def readDiary(u,f):  
    filePath=u+f  
    dates=[]  
    with open(filePath, "r") as f:  
        dates=f.readlines()  
    return dates
```

```python
import diary  
  
member={}  
url = "C:/pythonEx/"  
  
def printMember():  
    for i in member.keys():  
        print(f"ID : {i} / PW : {member[i]}")  
  
while True:  
    selectNum = int(input("1.회원가입 2.읽기쓰기 3.읽기보기 4. 종료 : "))  
    if selectNum == 1:  
        mId=input("아이디를 입력하세요 : ")  
        mPw=input("비밀번호를 입력하세요 : ")  
        member[mId]=mPw  
  
    elif selectNum == 2:  
        mId=input("아이디를 입력하세요 : ")  
        mPw=input("비밀번호를 입력하세요 : ")  
        if mId in member and member[mId] == mPw:  
            fileName = "myDiary_"+mId+".txt"  
            data = input("일기를 입력하세요 : ")  
            diary.writeDiary(url, fileName,data)  
        else:  
            print("아이디 또는 비밀번호가 틀렸습니다.")  
    elif selectNum == 3:  
        mId = input("아이디를 입력하세요 : ")  
        mPw = input("비밀번호를 입력하세요 : ")  
        if mId in member and member[mId] == mPw:  
            fileName = "myDiary_"+mId+".txt"  
            data=diary.readDiary(url, fileName)  
            print(data)  
            for d in data:  
                print(d, end="")  
        else:  
            print("아이디 또는 비밀번호가 틀렸습니다.")  
            printMember()  
    elif selectNum == 4:  
        print("종료합니다.")  
        break
```


## 수입 지출 기록 가계부 
```python
import time  
def getTime():  
    lt=time.localtime()  
    timeStamp=time.strftime("%Y-%m-%d %H:%M:%S",lt)  
    return timeStamp  
  
def income(u,m,d,t):  
    timeStamp=getTime()  
    with open(u,"a") as f:  
        f.write("="*20+"\n")  
        f.write(f"{timeStamp}"+"\n")  
        f.write(f"[입금] {d} : {m}"+"\n")  
        f.write(f"[잔액] {t}"+"\n")  
  
def outcome(u,m,d,t):  
    timeStamp=getTime()  
    with open(u,"a") as f:  
        f.write("="*20+"\n")  
        f.write(f"{timeStamp}"+"\n")  
        f.write(f"[출금] {d} : {m}"+"\n")  
        f.write(f"[잔액] {t}"+"\n")
```

```python
import income as ic  
u="C:/pythonEx/income.txt"  
m="C:/pythonEx/money.txt"  
  
while True:  
    selectNum=int(input("1.입금 2.출금 3.종료 : "))  
    if selectNum == 1:  
        money = int(input("입금할 금액 : "))  
        with open(m, "r") as f:  
           totalMoney= f.read()  
        with open(m, "w") as f:  
           f.write(str(int(totalMoney) + money))  
        data = input("입금 내역 : ")  
        totalMoney = int(totalMoney) + money  
        ic.income(u,money,data,totalMoney)  
  
    elif selectNum == 2:  
        money = int(input("출금할 금액 : "))  
        with open(m, "r") as f:  
           totalMoney= f.read()  
        with open(m, "w") as f:  
           f.write(str(int(totalMoney) - money))  
        totalMoney=int(totalMoney) - money  
        data = input("출금 내역 : ")  
        ic.outcome(u,money,data,totalMoney)  
    elif selectNum == 3:  
        print("종료")  
        break  
    else:  
        print("잘못된 입력입니다.")
```

## 약수와 소수 텍스트 파일 기록
### 소수수
```python
num=int(input("0보다 큰 정수 입력 : "))  
prime=[]  
  
if num < 0:  
    print("0보다 큰 정수를 입력하세요.")  
else :  
    for i in range(2,num+1):  
       flag = True  
       for n in range(2,i):  
           if i%n==0:  
               flag = False  
               break       if flag:  
           prime.append(i)  
  
print("Prime Write : ",prime)  
with open("C:/pythonEx/prime.txt", "a") as f:  
    f.write(f"{num}까지의 소수 : {prime}"+"\n")  
  
with open("C:/pythonEx/prime.txt", "r") as f:  
    data = f.read()  
    print(data)
```

### 약수 
```python
num=int(input("0보다 큰 정수 입력 : "))  
measure=[]  
  
if num < 0:  
    print("0보다 큰 정수를 입력하세요.")  
else :  
    for i in range(1,num):  
        if num%i==0:  
            measure.append(i)  
  
print("measure Write : ",measure)  
with open("C:/pythonEx/measure.txt", "a") as f:  
    f.write(f"{num}까지의 약수 : {measure}"+"\n")  
  
with open("C:/pythonEx/measure.txt", "r") as f:  
    data = f.read()  
    print(data)
```

## 두 수의 공약수와 최대 공약수 
```python
num1=int(input("1보다 큰 정수 : "))  
num2=int(input("1보다 큰 정수 : "))  
  
u1="C:/pythonEx/common_div.txt"  
u2="C:/pythonEx/common_mul.txt"  
  
common=[]  
maxNum=0  
  
for i in range(1, num1+1):  
    if num1 % i == 0 and num2 % i == 0:  
        common.append(i)  
if len(common) > 0:  
    try:  
        with open(u1, "a") as f:  
            f.write(f"{num1}과 {num2}의 공약수는 : {common}"+"\n")  
    except Exception as e :  
        print(e)  
for i in range(1, num1+1):  
    if num1 % i == 0 and num2 % i == 0:  
        maxNum=i  
  
try:  
    with open(u2, "a") as f:  
        f.write(f"{num1}과 {num2}의 최대공약수는 : {maxNum}"+"\n")  
except Exception as e :  
    print(e)  
  
print("common fator complete")
```

## 입항 기록
- 과일 선박 3일 주기 
- 생선 선박 4일 주기 
- 야채 선박 5일 주기 
- 모든 배가 입항하는 날짜를 기록 
- 첫 입항일은 2021-01-01 10:00

```python
import time  
  
startdate = time.mktime(time.strptime("2021-01-01", "%Y-%m-%d"))  
  
fruit=3  
fish=4  
vegetable=5  
url="C:/pythonEx/prot.txt"  
with open(url, "w") as f:  
    f.write("2021년 모든 선박 입항일\n")  
  
for i in range(1, 366):  
    if i % fruit == 0 and i % fish == 0 and i % vegetable == 0:  
        target_timestamp = startdate + i * 24 * 60 * 60  
        formatted = time.strftime('%Y-%m-%d 10:00:00', time.localtime(target_timestamp))  
        print("formatted:", formatted)  
        with open(url, "a") as f:  
            f.write(f"{formatted}\n")
```