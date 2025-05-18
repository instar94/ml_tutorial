student={"s1":"윤서연","s2":"정혜린","s3":"이지우","s4":"김채연","s5":"김유연"}
print(f"student : {student}")

### in / not in 존재 여부
print("s5 in student : ", "s5" in student)
print("s6 in student : ", "s6" in student)

### len() 길이 및 갯수
print("len(student) : ", len(student))

### 모든 아이템 삭제
student.clear()
print("student : ", student)