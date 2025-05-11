input_a1=int(input("a1 : "))
input_r =int(input("r : "))
input_n =int(input("n : "))

n=1
output_a=0
sumN=0

# while n <= input_n:
#     if n==1:
#         output_a = input_a1
#         print(f"{n}번째 항 : {output_a}")
#         n+=1
#         sumN+=output_a
#         continue
#
#     output_a *= input_r
#     sumN += output_a
#     print(f"{n}번째 항 : {output_a}\t 누적합 : {sumN}")
#     n += 1
#
# print(f"{input_n}번째 항까지 합 : {sumN}")

### 일반항의 공식을 이용한 버전
### a_n = a_1 * r^(n-1)
### S_n = a_1 * (1 - r^n) / (1 - r)
output_a = input_a1 * input_r**(input_n-1)
sumN=input_a1 * (1-input_r**input_n) / (1 - input_r)
print(f"{input_n}번째 항 : {int(sumN)}")