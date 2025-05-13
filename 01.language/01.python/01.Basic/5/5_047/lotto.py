import random as rd

userNums=[];randomNums=[];collectNums=[];randBonusNum=0

def setUserNum(ns):
    global userNums
    userNums = ns

def getUserNum():
    return userNums

def setRandomNum():
    global randomNums
    randomNums = rd.sample(range(1,46),6)

def getRandomNum():
    return randomNums

def setBonusNum():
    global randBonusNum

    while True:
        randBonusNum=rd.randint(1,45)
        if randBonusNum not in randomNums:
            break

def getBonusNum():
    return randBonusNum

def lottoResult():
    global userNums
    global randomNums
    global randBonusNum

    collectNums=[]
    for un in userNums:
        if un in randomNums:
            collectNums.append(un)

    if len(collectNums)=="6":
        print("1등 당첨")
        print(f"번호 {collectNums}")
    elif(len(collectNums)==5 and (randBonusNum in userNums)):
        print("2등 당첨")
        print(f"번호 {collectNums}, 보너스 번호 : {randomNums}")
    elif len(collectNums)==5:
        print("3등 당첨")
        print(f"번호 {collectNums}")
    elif len(collectNums)==4:
        print("4등 당첨")
        print(f"번호 {collectNums}")
    elif len(collectNums)==3:
        print("5등 당첨")
        print(f"번호 {collectNums}")
    else:
        print("낙첨")
        print(f"당첨 번호 : {randomNums}")
        print(f"보너스번호 : {randBonusNum}")
        print(f"선택 번호 : {userNums}")
        print(f"맞는 번호 : {collectNums}")

def startlotto():
    n1=int(input("번호 선택 (1~45)"))
    n2 = int(input("번호 선택 (1~45)"))
    n3 = int(input("번호 선택 (1~45)"))
    n4 = int(input("번호 선택 (1~45)"))
    n5 = int(input("번호 선택 (1~45)"))
    n6 = int(input("번호 선택 (1~45)"))
    selectNum=[n1,n2,n3,n4,n5,n6]

    setUserNum(selectNum)
    setRandomNum()
    setBonusNum()

    lottoResult()