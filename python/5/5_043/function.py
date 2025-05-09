##재귀함수
def recuFx(n):
    if n==1:
        return n
    return n * recuFx(n-1)


num=int(input("숫자 입력 : "))
print(f"팩토리얼 : {recuFx(num)}")