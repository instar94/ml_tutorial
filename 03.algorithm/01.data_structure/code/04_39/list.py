### 1부터 입력된 숫자까지 약수와 소수 리스트 저장 및 출력

### 사용자 입력 수
inputNum = int(input("숫자 입력 : "))

### 약수 리스트
divisorList = []
### 소수 리스트
primeList = []

for i in range(1, inputNum + 1):
    ### 약수 : inputNum을 i로 나눴을 때 나머지 0
    if i==1:
        divisorList.append(i)
    else:
        inputNum % i == 0
        divisorList.append(i)
### 소수 : 1과 자기 자신만으로 나누어 떨어지는 수
for j in range(2, inputNum + 1):
    flag = True
    ### j+1까지 나눠지는지 확인
    for n in range(2,j+1):
        ### 나누어 떨어지기만 하면 False
        ### 한 번도 안 나눠떨어지면 Ture
        if j % n == 0:
            flag = False
            break
    if flag:
        primeList.append(j)

print("약수 리스트 : ", divisorList)
print("소수 리스트 : ", primeList)