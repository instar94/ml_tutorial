class Member:
    def __init__(self,i,p):
        self.id=i
        self.pw=p

class MemberRepository:

    def __init__(self):
        self.members = {}

    def addMember(self, m):
        self.members[m.id] = m.pw

    def loginMember(self, i, p):
        isMember = i in self.members

        if isMember and self.members[i] == p:
            print(f'{i}: Log-in success!!')

        else:
            print(f'{i}: Log-in fail!!')

    def removeMember(self, i, p):
        del self.members[i]

    def printMembers(self):
        for mk in self.members.keys():
            print(f'ID: {mk}')
            print(f'PW: {self.members[mk]}')