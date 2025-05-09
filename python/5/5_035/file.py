class ZeroIsNewAttitude(Exception):
    def __init__(self,n):
        super().__init__(f"{n} Is New Attitude")



def divCal(num1,num2):
    if num2 == 0:
        raise ZeroIsNewAttitude(num2)
    else:
        print(f"{num1} / {num2} = {num1/num2}")


num1=int(input("숫자 입력 : "))
num2=int(input("숫자 입력 : "))

try:
    divCal(num1,num2)
except ZeroIsNewAttitude as e :
    print(e)