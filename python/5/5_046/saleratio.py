def calculatorTotalPrice(gs):
    if len(gs) <=0:
        print("구매 상품 없음")
        return

    rate=25
    totalPrice=0

    rates={1:5,2:10,3:15,4:20}

    if len(gs) in rates:
        rate= rates[len(gs)]

    for g in gs:
        totalPrice += g * (1-rate *0.01)

    return [rate, int(totalPrice)]

    def formatNum(n):
        return format(n,",")