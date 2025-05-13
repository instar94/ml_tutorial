class NotPrimeException(Exception):
    def __init__(self,n):
        super().__init__(f"{n}은 소수 아님")

class PrimeException(Exception):
    def __init__(self,n):
        super().__init__(f"{n}은 소수")


def isPrime(number):
    flag = True
    for n in range(2,number):
        if number % n ==0:
            flag = False
            break

    if flag == False:
        raise NotPrimeException(number)
    else :
        raise PrimeException(number)