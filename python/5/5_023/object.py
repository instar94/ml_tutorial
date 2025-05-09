# class Caculator:
#     def __init__(self,n1,n2):
#         print("[Caculator] Called")
#         self.num1=n1
#         self.num2=n2
#
# cal=Caculator(10,20)
# print(f"cal.num1 : {cal.num1}")
# print(f"cal.num2 : {cal.num2}")

class P_Class:
    def __init__(self,pNum1,pNum2):
        print("[P_Class] : __init__() Called")
        self.pNum1 = pNum1
        self.pNum2 = pNum2

class C_Class(P_Class):
    def __init__(self,cNum1,cNum2):
        print("[C_Class] : __init__() Called")
### 부모 클래스를 호출하여 가능
        #P_Class.__init__(self,cNum1,cNum2)
### super 키워드를 통해 서도 가능
        super().__init__(cNum1,cNum2)
        self.cNum1 = cNum1
        self.cNum2 = cNum2