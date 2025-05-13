nums=[]

n=1
while n < 6:
    try:
        num = int(input("짝수 입력 : "))
    except:
        print("숫자를 입력해 주세요")
        continue
    else:
        if num % 2 ==0:
            nums.append(num)
            n += 1
        else:
            print("입력한 숫자는 홀수 입니다",end=" ")
            print("숫자 다시 입력")
print (f"nums : {nums}")
