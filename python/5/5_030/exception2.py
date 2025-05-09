eveList=[]; oddList=[];floatList=[]

n=1
while n < 6:
    try:
        num = float(input("숫자 입력 : "))
    except:
        print("숫자를 입력해 주세요")
        continue
    else:
        if num - int(num) !=0 :
            floatList.append(num)
            n += 1
        elif num % 2 ==0 :
            oddList.append(int(num))
            n += 1
        else :
            eveList.append(int(num))
            n += 1

print (f"floatList : {floatList}")
print (f"oddList : {oddList}")
print (f"eveList : {eveList}")
