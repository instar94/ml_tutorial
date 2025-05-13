import income as ic
u="C:/pythonEx/income.txt"
m="C:/pythonEx/money.txt"

while True:
    selectNum=int(input("1.입금 2.출금 3.종료 : "))
    if selectNum == 1:
        money = int(input("입금할 금액 : "))
        with open(m, "r") as f:
           totalMoney= f.read()
        with open(m, "w") as f:
           f.write(str(int(totalMoney) + money))
        data = input("입금 내역 : ")
        totalMoney = int(totalMoney) + money
        ic.income(u,money,data,totalMoney)

    elif selectNum == 2:
        money = int(input("출금할 금액 : "))
        with open(m, "r") as f:
           totalMoney= f.read()
        with open(m, "w") as f:
           f.write(str(int(totalMoney) - money))
        totalMoney=int(totalMoney) - money
        data = input("출금 내역 : ")
        ic.outcome(u,money,data,totalMoney)
    elif selectNum == 3:
        print("종료")
        break
    else:
        print("잘못된 입력입니다.")