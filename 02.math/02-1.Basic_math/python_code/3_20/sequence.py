inputA1=int(input("a1 :"))
inputAn=int(input("n항까지 실행 :"))
inputB1=int(input("b1 :"))
inputBn=int(input("b 공차 :"))

valueAn=0
valueBn=0

# ### 1부터 An까지 실행
# n=1
# while n<=inputAn:
#     ### n=1 일때 실행
#     if n==1:
#         valueAn=inputA1
#         valueBn=inputB1
#         print(f"a{n} : {valueAn} \tb{n} : {valueBn}")
#         n+=1
#     ### 계차수열 계산 값을 a에 합
#     valueAn=valueAn+valueBn
#     ### valueBn에 b의 공차를 더함
#     valueBn=valueBn+inputBn
#     print(f"a{n} : {valueAn} \tb{n} : {valueBn}")
#     n+=1
#
# print(f"a{n} : {valueAn} \tb{n} : {valueBn}")

### 일반항을 이용한 방식
###b의 일반항
### 계차수열의 첫항에는 a1이 이미 포함됨
### 따라서 bn의 n-1만큼까지 합만 필요함
valueBn = inputB1+(inputAn-2)*inputBn
### 등차 계차수열 B의 합
sumBn = (inputAn-1) * ((valueBn + inputB1) / 2)
### a의 일반항
valueAn = inputA1 + sumBn
print(f"a{inputAn}항 : {valueAn}")