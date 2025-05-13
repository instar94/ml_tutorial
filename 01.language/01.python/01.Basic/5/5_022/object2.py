class CalculatorSuper:
    def add(self,n1,n2):
        return n1 + n2

    def sub(self,n1,n2):
        return n1 - n2

class CalculatorChild(CalculatorSuper):
    def mul(self,n1,n2):
        return n1 * n2
    def div(self,n1,n2):
        return n1 / n2

cal = CalculatorChild()
print(f"cal.add(10,20) : {cal.add(10,20)}")
print(f"cal.sub(10,20) : {cal.sub(10,20)}")
print(f"cal.mul(10,20) : {cal.mul(10,20)}")
print(f"cal.div(10,20) : {cal.div(10,20)}")