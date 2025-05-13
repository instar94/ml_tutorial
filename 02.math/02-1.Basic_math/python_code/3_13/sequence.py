input_a1=int(input("a1 : "))
input_d =int(input("d : "))
input_n =int(input("n : "))

# n=1
# output_a=0
#
# while n <= input_n:
#     if n==1:
#         output_a = input_a1
#         print(f"{n}번째 항 : {output_a}")
#         n+=1
#         continue
#
#     output_a += input_d
#     print(f"{n}번째 항 : {output_a}")
#     n += 1


### 일반항의 공식을 이용한 버전
### a_n = a_1 + (n-1)d
output_a = input_a1 + (input_n - 1) * input_d
print(f"{input_n}번째 항 : {output_a}")