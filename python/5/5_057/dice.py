import random as rd 

class Dice:
    def __init__(self):
        self.cNum=0
        self.uNum = 0
    
    def setCnum(self):
        self.cNum=rd.randint(1,6)
        print(f"[주사위] 컴퓨터의 주사위 : {self.cNum}")
    
    def setUnum(self):
        self.uNum=rd.randint(1,6)
        print(f"[주사위] 사용자의 주사위 : {self.uNum}")
        
    def startGame(self):
        print("[주사위] 게임 시작")
        self.setCnum()
        self.setUnum()
    
    def printResult(self):
        print("[주사위] 게임 시작")
        if self.cNum==0 or self.uNum==0:
            print("[주사위] 게임 결렬")
        else:
            if self.cNum > self.uNum:
                print(f"[주사위] 컴퓨터 승리 컴퓨터 : {self.cNum} VS 사용자 : {self.uNum}")
            elif self.cNum < self.uNum:
                print(f"[주사위] 사용자 승리 컴퓨터 : {self.cNum} VS 사용자 : {self.uNum}")
            if self.cNum == self.uNum:
                print(f"[주사위] 무승부 : {self.cNum} VS 사용자 : {self.uNum}")