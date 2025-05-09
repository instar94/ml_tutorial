class EmptyDataException(Exception):
    def __init__(self,i):
        super().__init__(f"{i} 는 데이터가 없습니다")

def checkInputData(n,em,p,a,ph):
    if n =="":
        raise EmptyDataException("name")
    elif em =="":
        raise EmptyDataException("email")
    elif p =="":
        raise EmptyDataException("password")
    elif a =="":
        raise EmptyDataException("address")
    elif ph =="":
        raise EmptyDataException("phone")

class RegistMember():
    def __init__(self,n,em,p,a,ph):
        self.m_name=n
        self.m_email=em
        self.m_pw=p
        self.m_addr=a
        self.m_phone=ph
        print("회원 가입 완료 ")

    def printMemInfo(self):
        print(f"m_name : {self.m_name}")
        print(f"m_email : {self.m_email}")
        print(f"m_pw : {self.m_pw}")
        print(f"m_addr : {self.m_addr}")
        print(f"m_phone : {self.m_phone}")