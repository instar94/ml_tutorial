###최대공약수와 공약수를 구할 숫자 입력
num1=int(input("1보다 큰 정수 입력 1 : "))
num2=int(input("1보다 큰 정수 입력 2 : "))

### 변수 선언
maxNum=0 ### 최대 공약수
numList=[] ### 공약수

### 1부터 num1까지 반복
### 어짜피 num2가 더 작다고 해도 공약수는 num2보다 작음
for i in range(1, num1+1):
    ### num1과 num2를 나눴을 때 둘 다 나머지 0이면 공약수
    if num1%i==0 and num2%i==0:
        print(f"{num1}과 {num2}의 공약수 : {i}")
        ### 공약수 리스트 추가
        numList.append(i)
        ### 가장 마지막으로 나눠져 maxNum에 들어가는 수가 최대 공약수
        maxNum=i

print(f"num1과 num2의 최대 공약수 : {maxNum}")
print(f"num1과 num2의 공약수 리스트 : {numList}")

