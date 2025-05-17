### for를 이용한 내부 리스트 출력

studentCnt = [[1,10],[2,20],[3,30],[4,40]]

for i in range(len(studentCnt)):
    print(f"{studentCnt[i][0]} 학년: {studentCnt[i][1]} 명")

for classNo, cnt in studentCnt:
    print(f"{classNo} 학년: {cnt} 명")