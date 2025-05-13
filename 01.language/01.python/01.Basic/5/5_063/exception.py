import member

m_name=input("이름 : ")
m_email=input("메일 : ")
m_pw=input("비번 : ")
m_addr=input("주소 : ")
m_phone=input("번호 : ")


try:
    member.checkInputData(m_name, m_email, m_pw, m_addr, m_phone)
    newMem= member.RegistMember(m_name, m_email, m_pw, m_addr, m_phone)
    newMem.printMemInfo()
except member.EmptyDataException as e :
    print(e)
