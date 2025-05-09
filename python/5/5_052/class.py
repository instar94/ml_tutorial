import member as mb

mems=mb.MemberRepository()

for i in range(3):
    mId=input("ID 입력 : ")
    mPw=input("PW 입력 : ")

    mem = mb.Member(mId,mPw)
    mems.addMember(mem)

mems.printMembers()
