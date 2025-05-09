# def formatNum(n):
#     return format(n,",")
#
# def wageNFeeRatio():
#     w=0;f1=0;f2=0;f3=0;
#     def getWageNFee():
#         w = int(input("수입 : "))
#         f1 = int(input("수도요금 : "))
#         f2 = int(input("전기요금 : "))
#         f3 = int(input("가스요금 : "))
#         return w, f1, f2, f3
#
#     def getTotalFee(f1, f2, f3):
#         total = f1 + f2 + f3
#         return total
#     getWageNFee()
#
#     t = getTotalFee(f1,f2,f3)
#     r = round(w / t * 100,2)
#     return [t,r]

w=0;f1=0;f2=0;f3=0;

def setIncome(ic):
    global w
    w =ic

def getIncome():
    return w


def setf1(f):
    global f1
    f1 = f


def getf1():
    return f1

def setf2(f):
    global f2
    f2 = f


def getf2():
    return f2

def setf3(f):
    global f3
    f3 = f


def getf3():
    return f3

def getFee():
    result = f1 + f2 + f3
    return int(result)

def getrate():
    result = getFee() / getIncome() * 100
    return result