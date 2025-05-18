### 입장 고객의 나이는 0~100세 사이 난수
### 총 100명 입장
### 1일 전체 입장 고객 입장료
### 0~7 : 0 / 8~13 : 200 / 14~19 : 300 / 20~64 : 500 / 65~100 : 0
import random

### 난수 생성 100명
rNum = []
for i in range(100):
    rNum.append(random.randint(0, 100))

### 나이별 입장료
kidPrice = 200
teenPrice = 300
adultPrice = 500

### 나이별 그룹 합
kid=0
teen=0
adult=0
senior=0
baby=0

for i in rNum:
    if i >= 0 and i <= 7:
        baby += 1
    elif i >= 8 and i <= 13:
        kid += 1
    elif i >= 14 and i <= 19:
        teen += 1
    elif i >= 20 and i <= 64:
        adult += 1
    else:
        senior += 1

print(f"영유아 : {baby}명 : 총 입장료 {baby * 0}원")
print(f"어린이 : {kid}명 : 총 입장료 {kid * kidPrice}원")
print(f"청소년 : {teen}명 : 총 입장료 {teen * teenPrice}원")
print(f"성인 : {adult}명 : 총 입장료 {adult * adultPrice}원")
print(f"노인 : {senior}명 : 총 입장료 {senior * 0}원")
print(f"총 입장 고객 수 : {baby + kid + teen + adult + senior}명")
print(f"총 입장료 : {baby * 0 + kid * kidPrice + teen * teenPrice + adult * adultPrice + senior * 0}원")

