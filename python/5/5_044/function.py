
def seq(a1,d,n):
    valueN=0;sumN=0;
    i=1
    while i <=n:
        if i==1:
            valueN=a1
            sumN=valueN
            print(f"{i}번째 값 : {valueN}")
            print(f"{i}번째 합 : {sumN}")
            i+=1
            continue
        valueN+= d
        sumN +=valueN
        print(f"{i}번째 값 : {valueN}")
        print(f"{i}번째 합 : {sumN}")
        i += 1


a1=int(input("a1 입력 : "))
d=int(input("공차 입력 : "))
n=int(input("n 입력 : "))

seq(a1,d,n)