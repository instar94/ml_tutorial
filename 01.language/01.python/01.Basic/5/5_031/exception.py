try:
    inputData=input("숫자 입력 : ")
    numInt =int(inputData)
except:
    print("예외 발생 : 숫자가 아님")
else:
    if numInt%2==0:
        print("짝수임")
    else :
        print("홀수임")
finally:
    print(f"들어간 데이터 : {inputData}")