studentList = ["Alice", "Bob", "Charlie", "David","Eve"]

for i in range(len(studentList)):
    if i % 2 == 0:
        print(f"짝수 인덱스: {studentList[i]}")
    else:
        print(f"홀수 인덱스: {studentList[i]}")