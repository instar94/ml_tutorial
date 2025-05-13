### 유클리드 호제법을 이용한 최대공약수 구하기
num1=int(input("1보다 큰 정수 입력 1 : "))
num2=int(input("1보다 큰 정수 입력 2 : "))

### 유클리드 호제법에서 x%y = temp1%temp2
temp1=num1
temp2=num2

''' 
r(x,y) = x와 y를 나눈 나머지
x % y = r(x,y) 를 수행 후 
y % r(x,y) = r(y,r(x,y)) 를 수행
r이 0이 될 때까지 반복 
'''
### temp2가 0이 될 때까지 반복
while temp2>0:
    ### 계산 수행 후 temp1에 들어가기 위해 temp2를 temp에 저장
    temp=temp2
    ### r(x,y) = x%y 시행
    temp2=temp1%temp2
    ### temp1에 temp2를 대입
    temp1=temp

### 최대 공약수 출력
print(f"{num1}과 {num2}의 최대 공약수 : {temp1}")

### 공약수 출력
for n in range(1,(temp1+1)):
    if temp1 % n == 0:
        print(f"공약수 : {n}")
