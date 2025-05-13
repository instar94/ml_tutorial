numN=int(input("n값 : "))
numR=int(input("r값 : "))

### 결과 변수
resultC=1
resultP=1
resultR=1

### nPr 구하기
for n in range(numN, numN-numR, -1):
    resultP=resultP*n

print("nPr : ", resultP)

### r값 구하기
for n in range(numR, 0, -1):
    resultR=resultR*n

print("r값 : ", resultR)

### nCr 구하기
resultC = int(resultP/resultR)

print("nCr : ", resultC)