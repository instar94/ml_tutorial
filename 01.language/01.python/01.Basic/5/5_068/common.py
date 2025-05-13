num1=int(input("1보다 큰 정수 : "))
num2=int(input("1보다 큰 정수 : "))

u1="C:/pythonEx/common_div.txt"
u2="C:/pythonEx/common_mul.txt"

common=[]
maxNum=0

for i in range(1, num1+1):
    if num1 % i == 0 and num2 % i == 0:
        common.append(i)
if len(common) > 0:
    try:
        with open(u1, "a") as f:
            f.write(f"{num1}과 {num2}의 공약수는 : {common}"+"\n")
    except Exception as e :
        print(e)
for i in range(1, num1+1):
    if num1 % i == 0 and num2 % i == 0:
        maxNum=i

try:
    with open(u2, "a") as f:
        f.write(f"{num1}과 {num2}의 최대공약수는 : {maxNum}"+"\n")
except Exception as e :
    print(e)

print("common fator complete :")