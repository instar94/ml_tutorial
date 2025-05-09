class Cacul :
    def __init__(self):
        self.n1=0
        self.n2=0
        self.result=0

    def add(self):
        self.result=self.n1+self.n2
        return self.result

    def sub(self):
        self.result=self.n1-self.n2
        return self.result

    def mul(self):
        self.result=self.n1*self.n2
        return self.result

    def div(self):
        self.result=self.n1/self.n2
        return self.result

## 매개 변수가 없다면 그냥 선언하면됨
calcul=Cacul()
calcul.n1=10
calcul.n2=20
print(f"calcul.add() {calcul.add()}")
print(f"calcul.sub() {calcul.sub()}")
print(f"calcul.mul() {calcul.mul()}")
print(f"calcul.div() {calcul.div()}")