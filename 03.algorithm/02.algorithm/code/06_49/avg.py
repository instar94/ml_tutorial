sales=[12000,13000,12500,11000,10500,98000,91000,91500,10500,11500,12000,12500]

def salesUpDown(n):
    if len(n)==1:
        return n
    print(f"sales : {sales}")
    currentSales = n.pop(0)
    nextSalse = n[0]
    increase = nextSalse - currentSales
    print(f"매출 증감액 : {increase}")

    return salesUpDown(n)

if __name__=="__main__":
    salesUpDown(sales)