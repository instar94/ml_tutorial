import bank

koreaBank=bank.Bank()

newAccount_name=input("예금주 명 : ")
myAccount=bank.PrivateBank(koreaBank,newAccount_name)
myAccount.printBankInfo()


while True:
    selectNum = int(input("1.입금\t2.출금\t3.종료"))
    if selectNum==1:
        m=int(input("입금액 :"))
        koreaBank.doDeposit(myAccount.account_no,m)
        myAccount.printBankInfo()
    elif selectNum==2:
        m=int(input("출금액 :"))
        try:
            koreaBank.doWithdraw(myAccount.account_no,m)
        except bank.LackException as e :
            print(e)
        finally:
            myAccount.printBankInfo()
    elif selectNum==3:
        print("종료")
        break
    else :
        print("입력 오류")
