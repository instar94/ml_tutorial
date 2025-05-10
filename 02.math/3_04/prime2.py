### 특정값 X에 y를 곱하면 z의 제곱이 되도록 하기
### 소인수가 짝수개 씩 있도록 하면됨

### 소인수를 구하는 리스트 선언
numList=[]

num=int(input("소인수를 구할 정수 입력 : "))

### 2부터 실행 (1은 소수가 될 수 없음)
n=2

while n<=num:
    ### num이 n으로 나머지가 없으면 소인수
    ### 만약 num보다 작을 때 까지 실행하기 때문에 n보다 숫자가 작아질 때 까지 반복됨
    if num%n==0:
        num=num/n
        numList.append(n)
    else:
    ### n이 num보다 작을 때 까지 반복하기 때문에 n을 증가시킴
        n+=1


print("소인수 : ",numList)

### 각 소인수 숫자 세기
for i in numList:
    ### 소인수가 짝수 개가 있지 않은 경우 - 하나를 더 추가
    if numList.count(i) % 2 != 0:
        ### numList에 추가
        numList.append(i)
    ### 소인수가 짝수 개가 있는 경우 - 패스
    else:
        pass

print("소인수 : ",numList)

### numList의 모든 소인수의 곱을 구하기
result=1
for i in numList:
    result *= i

print("결과 : ",result," = ",result**(1/2),"의 제곱")