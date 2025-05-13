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


#### math 함수

### 절댓값 fabs
print(f"math.fabs(-10) {math.fabs(-10)}")

### 올림 - ceil
print(f"math.cell(5.21) {math.ceil(5.21)}")
print(f"math.cell(5.21) {math.ceil(-5.21)}")

### 내림 - floor
print(f"math.floor(5.21) {math.floor(5.21)}")
print(f"math.floor(-5.21) {math.floor(-5.21)}")


### 최대공약수-gcd
print(f"math.gcd(14,21) {math.gcd(14, 21)}")

### 팩토리얼 - factorial
print(f"math.factorial(10) {math.factorial(10)}")

### 루트 - sqrt
print(f"math.sqrt(10) {math.sqrt(10)}")


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