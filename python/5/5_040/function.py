def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def mod(n1,n2):
    return n1%n2
def flo(n1,n2):
    return n1//n2
def exp(n1,n2):
    return n1**n2

while True:
    print("="*30)
    selectName = int(input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.나머지 6.몫 7.거듭제곱 8.종료"))
    if selectName==8:
        print("종료")
        print("=" * 30)
        break
    num1=float(input("숫자 입력 1 : "))
    num2 = float(input("숫자 입력 2 : "))

    if selectName==1:
        print(f"{add(num1,num2)}")
    elif selectName==2:
        print(f"{sub(num1,num2)}")
    elif selectName == 3:
        print(f"{mul(num1, num2)}")
    elif selectName==4:
        print(f"{div(num1,num2)}")
    elif selectName==5:
        print(f"{mod(num1,num2)}")
    elif selectName==6:
        print(f"{flo(num1,num2)}")
    elif selectName==7:
        print(f"{exp(num1,num2)}")
    else :
        print("잘못된 입력")
    print("=" * 30)