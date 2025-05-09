def formatNum(n):
    return format(n,",")

### 단리
def singleRate(m,t,r):
    totalMoney=0
    totalRateMoney=0

    for i in range(t):
        totalRateMoney += m*(r*0.01)

    totalMoney=m+totalRateMoney
    return int(totalMoney)

### 월복리
def multiRate(m,t,r):
    ### 월단위로 변경
    t=t*12
    rpm = (r/12)*0.01
    totalMoney = m

    for i in range(t):
        totalMoney += totalMoney * rpm

    return int(totalMoney)

money=int(input("예치금 (원) : "))
term=int(input("기간 (연) : "))
ratio=int(input("연이율 (%) : "))

print(f"단리 총 수령 금액 : {formatNum(singleRate(money,term,ratio))}")
print(f"월복리 총 수령 금액 : {formatNum(multiRate(money,term,ratio))}")