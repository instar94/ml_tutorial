### 계차 수열
### 일반항 구하기
### n번째 항 구하기
### n항까지 합 구하기
### {2, 5, 11, 20, 32, 47, 65, 86,110,137,167}
### 계차수열 {3,6,9,12,15,18...}
numAn=0;numBk=0;numASn=0;numBSn=0

def seqFun(numA1,numN,numB1,numD):
    ### a의 n항 : a1항 + bk의 n-1번째항까지의 합
    numBk = numB1 + (numN - 2) * numD
    numBSn = int((numN - 1) / 2 * (numB1 + numBk))

    numAn = numA1 + numBSn
    print(f"{numN}항 : {numAn}")
    return numAn

def sigmaFun(numA1,numN,numB1,numD):
    totalSum = 0
    for i in range(1,numN+1):
        addNum=seqFun(numA1,i,numB1,numD)
        totalSum+=addNum
    print(f"totol : {totalSum} ")

### a의 n항까지의 합
sigmaFun(2,11,3,3)
