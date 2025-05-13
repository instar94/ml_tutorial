numN=int(input("n값 : "))
numR=int(input("r값 : "))

### 결과 변수
result=1

### nPr : n * n-1 * n-2 * ... * n-r+1
# for i in range(numN, numN-numR, -1):
#     result *= i
#     print(f"i: {i}")
#
# print(f"{numN}P{numR} = {result}")

### nPr : n! / (n-r)!
import math
result=int(math.factorial(numN)/math.factorial(numN-numR))
print(f"{numN}P{numR} = {result}")
