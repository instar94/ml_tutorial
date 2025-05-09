class TemCls:
    def __init__(self,n,s):
        self.number=n
        self.str=s

    def printInfo(self):
        print(f"self.number :{self.number}")
        print(f"self.str :{self.str}")


### 얕은 복사
tc1=TemCls(10,"Hello Python")
tc2=tc1

tc1.printInfo()
tc2.printInfo()

### 값 변경
tc2.number=3.14
tc2.str="Bye"

tc1.printInfo()
tc2.printInfo()

### 깊은 복사
import copy
tc3 =TemCls(10,"Hello Python")
tc4 = copy.copy(tc3)

tc3.printInfo()
tc4.printInfo()

### 값 변경
tc4.number=3.14
tc4.str="Bye"

tc3.printInfo()
tc4.printInfo()
