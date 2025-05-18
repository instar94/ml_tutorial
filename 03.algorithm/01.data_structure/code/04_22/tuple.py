### 튜플
students = ("John", "Jane", "Doe","Smith","Emily","Michael")
print(f"students: {students}")

searchName="Jane"
if searchName in students:
    print(f"{searchName} 있음")
else:
    print(f"{searchName} 없음")
