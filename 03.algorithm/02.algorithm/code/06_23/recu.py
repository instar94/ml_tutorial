### 재귀함수
def recu(num):
    ### num이 0이 아닐때 까지
    if num>0:
        print("*"*num)
        ### 실행 할 때 마다 1씩 줄임
        return recu(num-1)
    else:
        return 1

recu(10)

### 팩토리얼
def factorial(num):
    if num>0:
        return num*factorial(num-1)
    else:
        return 1
print(factorial(10))