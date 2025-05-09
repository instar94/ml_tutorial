
# 반복문
## 무한 루프
### 정의 
> 빠져나올 수 없는 무한 반복 진행 
- 종종 while 문에서 발생하는 경우가 있음 
	- 예시) 결과가 항상 True인 경우

```python
n=1
while n < 10 :
    print ("무한 반복 >>> ")
    n+=1 ## 이와 같은 구문으로  무한루프를 막을 수 있음
```

### 논리형 데이터의 사용 
- 논리형 데이터를 사용해서 무한 반복을 실행 할 수 있음 
- flag가 False 일 때까지 영원히 반복하게 됨 

```python
flag = True 
num = 0  
sum = 0  
while flag :   ###flag가 False 일때 까지 반복
    num +=1  
    sum +=num  
    print('{}까지의 합은 {}'.format(num,sum))  
      
    if sum >=1000:  
        flag = False
```

결과 값
```
43까지의 합은 946
44까지의 합은 990
45까지의 합은 1035
```

### 실습
- 독감으로 병원에 내방 환자 수 50 ~ 100명 사이 
- 누적 독감 환자가 최초로 1만명 넘는 날짜 

```python
## 난수 발생 패키지 
import random  
  
sum =0  
date =1 
flag =True   

while flag:  
    patientCount = random.randint(50,100)  
    sum += patientCount  
    date +=1  
    print ('{} 날짜 \t오늘 환자 수 {} \t누적 환자 수 {}'.format(date,patientCount,sum))  
      
    if sum >=10000 :
        flag=False
```

- 출력 예시 
```
130 날짜 	오늘 환자 수 78 	누적 환자 수 9817
131 날짜 	오늘 환자 수 99 	누적 환자 수 9916
132 날짜 	오늘 환자 수 70 	누적 환자 수 9986
133 날짜 	오늘 환자 수 91 	누적 환자 수 10077
```

-----
## 반복문의 제어 
### Continue
#### 정의 
> 반복문에서 실행을 종료하고 다음 실행으로 넘어감 
-  실행 없이 다음으로 넘어감 

```python
for i in range(100):
    if i % 7 !=0:
        continue
    ### 7의 배수가 아닌 경우에는 해당 구문에 도달 X
    print('{}는 7의 배수 입니다.'.format(i))
```
### else 
#### 정의 
> 반복문이 종료된 후에 실행 

```python
cnt = 0
for i in range(100):
    if i % 7 !=0:
        continue
    ### 7의 배수 일 때만 카운트 가능 
    print('{}는 7의 배수'.format(i))
    cnt += 1
else
    print('99까지의 정수 중 7의 배수는 {}개'.format(cnt))
```

#### continue & else 실습
> 3과 7의 공배수 구하기  + 최소 공배수 구하기

```python
####최소 공배수 구하기 
minNum=0

for i in (1,101):
    if i % 3 !=0 or i%7 !=0 :
        continue
    print('공배수 : {}'.format(i))
    if minNum == 0:
        minNum = i
else:
    print('최소 공배수 : {}'.format(minNum))
```

### break 
#### 정의 
>  실행문 중단 후 `반복문` 자체를 중단 

-  반복 횟수와 상관 없음 
```python
num=0

### 무한 루프임 
while True:
    print ("Hello")
    num +=1
    ### 무한 루프를 끝내버림 - 반복문 자체 종료
    if num>=5:
        break
print("Loop End")
```

#### break 실습
> 1부터 100까지 정수가 다 더할 때 100이 넘는 최초의 정수 찾기 

```python
sum = 0 
searchNum = 0
for i in range(100):
    sum +=i
    #### 반복문을 종료하는 조건 설정 
        if sum > 100:
	        #### 100 을 넘는 최초의 숫자 
            searchNum=i
            break
print('searchNum : {}'.fomat(searchNum))
```

-----
## 중첩 반복문
### 정의 
>  반복문 안에 또 다른 반복문 

```python 
for i in range(1,10):
    for j in range(i):
	    print('*'. end='')
	    print()
```

결과물 
```text
*
**
***
****
....(생략)....
*********
```

- 반복문이 너무 많아지면 코드의 부하가 심해질 수 있음 
	- 일반적으로 2~3개 까지만 중첩
### 실습 
```python 

for i in range(10,0,-1):
    for i in range(i):
        print('*', end='')
        print()
```

> 구구단 만들기 

```python 
for i in range(1,10):
    for j in range(2,10):
       result = j* i
       print (`{}*{} ={}\t`.format(j,i,result), end='')
       print()
```

-----