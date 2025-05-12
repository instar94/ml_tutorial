def probability():
    numN=int(input("n값 : "))
    numR=int(input("r값 : "))

    resultP = 1
    resultR = 1
    resultC = 1

    ### nCr=nPr/numR)
    ### 순열 먼저 구하기
    for i in range(numN, numN-numR, -1):
        resultP=resultP*i

    ### r에 대한 팩토리얼 구하기
    for n in range(numR, 0, -1):
        resultR=resultR*n

    resultC=int(resultP/resultR)
    return resultC

sample=probability()
print(f"sample : {sample}")

event1 = probability()
print(f"event1 : {event1}")

event2= probability()
print(f"event2 : {event2}")

prob = round(((event1 * event2) /sample)*100,2)
print(f"확률 : {prob}%")