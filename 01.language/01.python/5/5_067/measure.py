num=int(input("0보다 큰 정수 입력 : "))
measure=[]

if num < 0:
    print("0보다 큰 정수를 입력하세요.")
else :
    for i in range(1,num):
        if num%i==0:
            measure.append(i)

print("measure Write : ",measure)
with open("C:/pythonEx/measure.txt", "a") as f:
    f.write(f"{num}까지의 약수 : {measure}"+"\n")

with open("C:/pythonEx/measure.txt", "r") as f:
    data = f.read()
    print(data)
