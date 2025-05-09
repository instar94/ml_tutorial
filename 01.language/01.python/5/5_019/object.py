class NewPC:
    def __init__(self, name,cpu,memory,ssd):
        self.name=name #self.name = 객체의 이름 name = 매개변수로 받은 이름
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doExcel(self):
        print("Excel")

    def doPhotoshop(self):
        print("Photoshop")

    def printInfo(self):
        print(f"self.name {self.name}")
        print(f"self.cpu {self.cpu}")
        print(f"self.memory {self.memory}")
        print(f"self.ssd {self.ssd}")

mypc=NewPC("mypc","15","16G","256G")
friendpc=NewPC("friendpc","17","32G","512G")

mypc.printInfo()
print("="*10,"="*10)
friendpc.printInfo()
print("="*10,"pc업그레이드","="*10)
mypc.cpu="19"
mypc.memory="64GB"
mypc.ssd="1TB"
mypc.printInfo()