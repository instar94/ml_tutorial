# n1=10;n2=0
#
# try:
#     print(n1/n2)
# except:
#     print("예외 처리 발생")
# print(n1*n2)

nums=[]

n=1
while n < 6:
    try:
        num = int(input("숫자 입력 : "))
    except:
        print("숫자를 입력해 주세요")
        continue
    nums.append(num)
    n+=1
print (f"nums : {nums}")
