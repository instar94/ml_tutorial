input_a1=int(input("a1 : "))
input_r =int(input("r : "))
input_n =int(input("n : "))

n=1
output_a=0

# while n <= input_n:
#     if n==1:
#         output_a = input_a1
#         print(f"{n}번째 항 : {output_a}")
#         n+=1
#         continue
#
#     output_a *= input_r
#     print(f"{n}번째 항 : {output_a}")
#     n += 1


# ### 일반항의 공식을 이용한 버전
# ### a_r = a_1 * r^(n-1)
output_a = input_a1 * input_r**(input_n - 1)
print(f"{input_n}번째 항 : {output_a}")