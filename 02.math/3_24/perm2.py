numN=int(input("사람 수 : "))

### 결과 변수
result=1

### 원순열 = (i-1)!
for i in range(1,numN):
    result *= i

print("결과 : ",result)