g1Price=1200; g2Price=1000; g3Price=800; g4Price=2000; g5Price=900;

def calculator(*gcs):
    gcsDice={}
    againCntInput={}

    for idx, gc in enumerate(gcs):
        try:
            gcsDice[f"g{idx+1}"]=int(gc)
        except Exception as e:
            againCntInput[f"g{idx+1}"]=gc
            print(e)

    totalPrice=0
    for g in gcsDice.keys():
        totalPrice+= globals()[f"{g}Price"]*gcsDice[g]

    print("="*20)
    print(f"총 구매 금액 : {totalPrice}원")
    print("=" * 10,"미결제 항목","="*10)
    for g in againCntInput.keys():
        print(f"상품 : {g} \t구매 개수:{againCntInput[g]}")
