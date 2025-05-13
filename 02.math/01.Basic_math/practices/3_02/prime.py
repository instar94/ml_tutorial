num=int(input("약수/소수를 구할 정수 입력 : "))

### 약수
### 1부터 num까지 반복 실행 (num+1로 해야 num도 포함됨)
for i in range(1,num+1):
    ### num을 i로 나누었을 때 나머지가 0이면 약수
    if num%i==0:
        print(f"{i}는 약수")

### 소수
### range(2,num+1) : 2부터 num까지 시행해야함 (1은 소수 아님)
for i in range(2,num+1):
    ### i가 2부터 i-1까지 나누었을 때, 어떠한 값도 약수가 없음 = 소수
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
    if flag:
        print(f"{i}는 소수")
    else:
        print(f"{i}는 소수가 아님")