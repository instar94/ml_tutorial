### 등차 수열
### 일반항 구하기
### n번째 항 구하기
### n항까지 합 구하기
### {4,  10, 16, 22, 28, 34, 40, 46, 52, 58}

numA1=4;numD=6;numN=10;numAn=0;numSn=0

### n번째항 구하기
### an=a1+(n-1)d
numAn=numA1+(numN-1)*numD
print(f"{numN} 항 : {numAn}")

### n항까지 합 구하기
### Sn=n/2*(a1+an)
numSn=numN/2*(numA1+numAn)
print(f"{numN} 항까지 합 : {int(numSn)}")