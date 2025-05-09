class Book:
    def __init__(self,n,p,i):
        self.name=n
        self.price=p
        self.isbn=i

class BookRepository:

    def __init__(self):
        self.bDic={}

    def registBook(self,b):
        self.bDic[b.isbn]=b

    def removeBook(self,isbn):
        del self.bDic[isbn]

    def printList(self):
        for isbn in self.bDic.keys():
            b=self.bDic[isbn]
            print(f"{b.name}, {b.price}, {b.isbn}")

    def printInfo(self,isbn):
        if isbn in self.bDic:
            b=self.bDic[isbn]
            print(f"{b.name}, {b.price}, {b.isbn}")
        else:
            print("404 Not Found")
