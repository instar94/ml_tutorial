import random
import primenum as pm

primNum=[]

n=0
while n < 10:
    rn=random.randint(1,1000)
    if rn not in primNum:
        try:
            pm.isPrime(rn)
        except pm.NotPrimeException as e:
            print(e)
            continue

        except pm.PrimeException as e:
            print(e)
            primNum.append(rn)
            continue
    n+=1

print(f"목록 = {primNum}")
