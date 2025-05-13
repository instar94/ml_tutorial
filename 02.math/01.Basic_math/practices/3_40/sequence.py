### 피보나치 수열
input_n = int(input("피보나치 수열 n항까지 실행 :"))

### n항 값
value_n=0
value_n1=0
value_n2=0

### n항까지의 합
sum_n=0
### n값
n=1

while n<= input_n:
    ### n=1
    if n==1 or n==2:
        value_n=1
        value_n1=value_n
        value_n2=value_n
        sum_n+=value_n
        print(f"n{n} : {value_n} \t합 : {sum_n}")
        n+=1
    else :
        ### n=3 부터는 n-1과 n-2의 합
        value_n=value_n2+value_n1
        value_n2=value_n1
        value_n1=value_n
        sum_n+=value_n
        print(f"n{n} : {value_n} \t합 : {sum_n}")
        n+=1

print(f"{n-1}항 : {value_n} \t합 : {sum_n}")
