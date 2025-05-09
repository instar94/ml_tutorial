class BasicCalculator:
    def add(self,n1,n2):
        return n1+n2
    def sub(self,n1,n2):
        return n1-n2
    def mul(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):
        return n1/n2

class DeveloperCalculator:
    def mod(self,n1,n2):
        return n1%n2
    def flo(self,n1,n2):
        return n1//n2
    def exp(self,n1,n2):
        return n1**n2

class Calculator(BasicCalculator,DeveloperCalculator):
    def __init__(self):
        pass


cal=Calculator()
print(f"cal.add(10,20) : {cal.add(10,20)}")
print(f"cal.sub(10,20) : {cal.sub(10,20)}")
print(f"cal.mul(10,20) : {cal.mul(10,20)}")
print(f"cal.div(10,20) : {cal.div(10,20)}")
print(f"cal.mod(10,20) : {cal.mod(10,20)}")
print(f"cal.flo(10,20) : {cal.flo(10,20)}")
print(f"cal.exp(10,20) : {cal.exp(10,20)}")