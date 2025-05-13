input_a1=int(input("a1 : "))
input_d =int(input("d : "))
input_n =int(input("n : "))

# n=1
# output_a=0
# sumN=0
#
# while n <= input_n:
#     if n==1:
#         output_a = input_a1
#         print(f"{n}번째 항 : {output_a}")
#         n+=1
#         sumN+=output_a
#         continue
#
#     output_a += input_d
#     sumN += output_a
#     print(f"{n}번째 항 : {output_a}\t 누적합 : {sumN}")
#     n += 1
#
# print(f"{input_n}번째 항까지 합 : {sumN}")

### 일반항의 공식을 이용한 버전
### a_n = a_1 + (n-1)d
### S_n = n/2 * (a_1 + a_n)
output_a = input_a1 + (input_n - 1) * input_d
sumN=input_n/2 * (input_a1 + output_a)
print(f"{input_n}번째 항 : {int(sumN)}")