## 숫자 2개에 대하여 최대 공약수 및 최대 공배수를 출력
fruit = 3
vegi = 4
toy = 5

### 변수 선언
maxNum = 0

### 최대 공약수 구하기
for i in range(1, fruit+1):
    if fruit%i==0 and vegi%i==0:
        maxNum=i

### 최대 공배수 구하기
### 최대 공배수 = fruit * vegi // 최대공약수
minNum=fruit*vegi//maxNum

### 3개의 경우 : 두 개의 최소공배수 > 나머지와의 공배수를 구함
### toy와의 공배수를 구함
newNum=minNum
### 최대 공약수 구하기
for i in range(1, toy+1):
    if newNum%i==0 and toy%i==0:
        maxNum=i

minNum=newNum*toy//maxNum
print(f"함께 입항하는 날짜는 {minNum}일입니다.")