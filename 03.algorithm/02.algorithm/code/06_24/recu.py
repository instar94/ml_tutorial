def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)

print(f"gcd(82,32) : {gcd(82,32)}")