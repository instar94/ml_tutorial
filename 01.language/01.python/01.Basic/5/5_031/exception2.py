eveList=[]; oddList=[];floatList=[];dataList=[]

n=1
while n < 6:
    try:
        data=input("숫자 입력 : ")
        num = float(data)
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
    finally :
        dataList.append(data)

print (f"floatList : {floatList}")
print (f"oddList : {oddList}")
print (f"eveList : {eveList}")
print (f"dataList : {dataList}")