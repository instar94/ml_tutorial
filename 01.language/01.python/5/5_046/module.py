import saleratio as sr

if __name__=="__main__" :
    flag=True
    gs=[]

    while flag:
        selectNum=int(input("1.구매 \t2.종료"))
        if selectNum==1:
            goods_price=int(input("상품가격 : "))
            gs.append(goods_price)
        elif selectNum==2:
            result= sr.calculatorTotalPrice(gs)
            flag=False

    print(f"할인률 : {result[0]}%")
    print(f"합계 가격 : {sr.formatNum(result[1])}원")

