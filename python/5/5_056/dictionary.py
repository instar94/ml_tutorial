from abc import ABCMeta
from abc import abstractmethod

class AbsDictionary (metaclass=ABCMeta):
    def __init__(self):
        self.wordDic={}

    @abstractmethod
    def registWord(self,w1,w2):
        pass

    @abstractmethod
    def removeWord(self, w1, w2):
        pass

    @abstractmethod
    def updateWord(self, w1, w2):
        pass

    @abstractmethod
    def searchWord(self, w1, w2):
        pass

class KorToEng(AbsDictionary):
    def __init__(self):
        super().__init__()

    def registWord(self,w1,w2):
        print(f"[한영사전] 등록 : {w1} > {w2}")
        self.wordDic[w1]=w2

    def removeWord(self, w1, w2):
        print(f"[한영사전] 삭제 : {w1}")
        del self.wordDic[w1]

    def updateWord(self, w1, w2):
        print(f"[한영사전] 수정 : {w1} > {w2}")
        self.wordDic[w1] = w2

    def searchWord(self, w1):
        print(f"[한영사전] 검색 : {w1}")
        return self.wordDic[w1]

    def printWords(self):
        for k in self.wordDic:
            print(f"{k} : {self.wordDic[k]}")


class KorToJpn(AbsDictionary):
    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f"[한일사전] 등록 : {w1} > {w2}")
        self.wordDic[w1] = w2

    def removeWord(self, w1, w2):
        print(f"[한일사전] 삭제 : {w1}")
        del self.wordDic[w1]

    def updateWord(self, w1, w2):
        print(f"[한일사전] 수정 : {w1} > {w2}")
        self.wordDic[w1] = w2

    def searchWord(self, w1):
        print(f"[한일사전] 검색 : {w1}")
        return self.wordDic[w1]

    def printWords(self):
        for k in self.wordDic:
            print(f"{k} : {self.wordDic[k]}")