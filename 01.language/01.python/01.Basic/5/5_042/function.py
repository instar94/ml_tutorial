childPrice=18000
infantPrice=25000
adultPrice=50000
saleRatio=0.5

def getTotalCnt(childCnt,infantCnt,adultCnt):
    return childCnt+infantCnt+adultCnt

def getTotalPrice(childCnt,infantCnt,adultCnt,childSale,infantSale,adultSale):
    totalPrice=childCnt*childPrice+infantCnt*infantPrice+adultCnt*adultPrice
    salePrice=(childSale*childPrice+infantSale*infantPrice+adultSale*adultPrice)*(1-saleRatio)
    return totalPrice-salePrice
print("="*60)
childCnt=int(input("유아 : "))
childSale=int(input("유아 할인 대상 : "))
infantCnt=int(input("소아 : "))
infantSale=int(input("소아 할인 대상 : "))
adultCnt=int(input("성인 : "))
adultSale=int(input("성인 할인 대상 : "))
print("="*60)
total=int(getTotalCnt(childCnt,infantCnt,adultCnt))
totalPrice=int(getTotalPrice(childCnt,infantCnt,adultCnt,childSale,infantSale,adultSale))
print(f"Total : {total}명")
print(f"TotalPrice : {totalPrice}원")
print("="*60)
