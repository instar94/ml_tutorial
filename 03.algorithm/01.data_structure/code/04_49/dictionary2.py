### 아이디 / 패스워드  입력 받아서 프로그램 만들기
members ={"id1":"pw1","id2":"pw2","id3":"pw3","id4":"pw4"}

inputId = input("아이디 입력 : ")
inputPw = input("패스워드 입력 : ")

if inputId in members:
    if members[inputId]==inputPw:
        print("로그인 성공")
    else:
        print("비밀번호 확인 필요")
else:
    print("아이디 확인 필요")