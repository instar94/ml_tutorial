import diary

member={}
url = "C:/pythonEx/"

def printMember():
    for i in member.keys():
        print(f"ID : {i} / PW : {member[i]}")

while True:
    selectNum = int(input("1.회원가입 2.읽기쓰기 3.읽기보기 4. 종료 : "))
    if selectNum == 1:
        mId=input("아이디를 입력하세요 : ")
        mPw=input("비밀번호를 입력하세요 : ")
        member[mId]=mPw

    elif selectNum == 2:
        mId=input("아이디를 입력하세요 : ")
        mPw=input("비밀번호를 입력하세요 : ")
        if mId in member and member[mId] == mPw:
            fileName = "myDiary_"+mId+".txt"
            data = input("일기를 입력하세요 : ")
            diary.writeDiary(url, fileName,data)
        else:
            print("아이디 또는 비밀번호가 틀렸습니다.")
    elif selectNum == 3:
        mId = input("아이디를 입력하세요 : ")
        mPw = input("비밀번호를 입력하세요 : ")
        if mId in member and member[mId] == mPw:
            fileName = "myDiary_"+mId+".txt"
            data=diary.readDiary(url, fileName)
            print(data)
            for d in data:
                print(d, end="")
        else:
            print("아이디 또는 비밀번호가 틀렸습니다.")
            printMember()
    elif selectNum == 4:
        print("종료합니다.")
        break