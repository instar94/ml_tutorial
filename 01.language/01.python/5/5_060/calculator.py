def add(n1,n2):
    try:
        n1 = float(n1)
    except:
        print("첫번째 숫자가 없음")
        return
    try:
        n2 = float(n2)
    except:
        print("두번째 숫자가 없음")
        return
    print(f"{n1}+{n2}={n1+n2}")
def sub(n1,n2):
    try:
        n1 = float(n1)
    except:
        print("첫번째 숫자가 없음")
        return
    try:
        n2 = float(n2)
    except:
        print("두번째 숫자가 없음")
        return
    print(f"{n1}-{n2}={n1 - n2}")
def mul(n1,n2):
    try:
        n1 = float(n1)
    except:
        print("첫번째 숫자가 없음")
        return
    try:
        n2 = float(n2)
    except:
        print("두번째 숫자가 없음")
        return
    print(f"{n1}*{n2}={n1 * n2}")

def div(n1,n2):
    try:
        n1 = float(n1)
    except:
        print("첫번째 숫자가 없음")
        return
    try:
        n2 = float(n2)
    except:
        print("두번째 숫자가 없음")
        return
    try:
        print(f"{n1}/{n2}={n1 / n2}")
    except ZeroDivisionError as e :
        print(e)
        print("0으로 나눌 수 없음")
def mod(n1,n2):
    try:
        n1 = float(n1)
    except:
        print("첫번째 숫자가 없음")
        return
    try:
        n2 = float(n2)
    except:
        print("두번째 숫자가 없음")
        return
    try:
        print(f"{n1}%{n2}={n1 % n2}")
    except ZeroDivisionError as e :
        print(e)
        print("0으로 나눌 수 없음")

def flo(n1,n2):
    try:
        n1 = float(n1)
    except:
        print("첫번째 숫자가 없음")
        return
    try:
        n2 = float(n2)
    except:
        print("두번째 숫자가 없음")
        return
    try:
        print(f"{n1}//{n2}={n1 // n2}")
    except ZeroDivisionError as e :
        print(e)
        print("0으로 나눌 수 없음")
def exp(n1,n2):
    try:
        n1 = float(n1)
    except:
        print("첫번째 숫자가 없음")
        return
    try:
        n2 = float(n2)
    except:
        print("두번째 숫자가 없음")
        return
    print(f"{n1}**{n2}={n1 ** n2}")