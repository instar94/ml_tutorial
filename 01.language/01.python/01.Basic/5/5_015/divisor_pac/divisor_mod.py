def divisor(n1):
    outputlist=[]
    for i in range(1,n1+1):
        if n1%i== 0:
            outputlist.append(i)
        else:
            pass
    return outputlist

def prime_number(n1):
    outputlist=[]
    for i in range(2,n1+1):
        if len(divisor(i))==2:
            outputlist.append(i)
        else:
            pass
    return outputlist

if __name__ == "__main__":
    print("약수 : ", divisor(50))
    print("소수 : ", prime_number(50))
