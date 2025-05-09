num=int(input("0보다 큰 정수 입력 : "))
prime=[]

if num < 0:
    print("0보다 큰 정수를 입력하세요.")
else :
    for i in range(2,num+1):
       flag = True
       for n in range(2,i):
           if i%n==0:
               flag = False
               break
       if flag:
           prime.append(i)

print("Prime Write : ",prime)
with open("C:/pythonEx/prime.txt", "a") as f:
    f.write(f"{num}까지의 소수 : {prime}"+"\n")

with open("C:/pythonEx/prime.txt", "r") as f:
    data = f.read()
    print(data)
