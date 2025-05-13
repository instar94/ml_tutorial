### 등비 수열
### 일반항 구하기
### n번째 항 구하기
### n항까지 합 구하기
### {2, 6, 18, 54, 162, 486, 1458, 4374, 13122}
numA1=2;numR=3;numN=9;numAn=0;numSn=0

### n번째항 구하기
### arn=a1*r^(n-1)
numAn=numA1*numR**(numN-1)
print(f"{numN} 항 : {numAn}")

### n항까지 합 구하기
### Sn=a1*(r^n)/(r-1)
numSn=numA1*(numR**(numN))/(numR-1)
print(f"{numN} 항까지 합 : {int(numSn)}")