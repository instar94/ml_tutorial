# num1=int(input("숫자 입력 : "))
# num2=int(input("숫자 입력 : "))
#
# try:
#     print(f"num1 / num2 = {num1 / num2}")
# except Exception as e:
#     print(f"Excepttion : {e}")


def divCalcul(n1,n2):
    if n2 !=0:
        print(f"{n1} / {n2} = {n1/n2}")
    else :
        raise Exception("0으로 나눌 수 없음")

num1=int(input("숫자 입력 : "))
num2=int(input("숫자 입력 : "))

try:
     divCalcul(num1,num2)
except Exception as e :
    print(f"Exception : {e}")
