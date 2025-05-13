import libaray as lb

bookRepo=lb.BookRepository()

bookRepo.registBook(lb.Book("python",20000,"12341234"))
bookRepo.registBook(lb.Book("java",27000,"45674567"))
bookRepo.registBook(lb.Book("C++",32000,"78907890"))

bookRepo.printList()
bookRepo.printInfo("45674567")
bookRepo.removeBook("12341234")
print("="*30)
bookRepo.printList()
