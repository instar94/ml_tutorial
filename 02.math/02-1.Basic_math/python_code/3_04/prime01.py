num=int(input("소인수를 구할 정수 입력 : "))

### 2부터 실행 (1은 소수가 될 수 없음)
n=2

while n<=num:
    ### num이 n으로 나머지가 없으면 소인수
    ### 만약 num보다 작을 때 까지 실행하기 때문에 n보다 숫자가 작아질 때 까지 반복됨
    if num%n==0:
        print(f"{int(n)}은 소인수")
        num=num/n
    else:
    ### n이 num보다 작을 때 까지 반복하기 때문에 n을 증가시킴
        n+=1
