studentList = [
    [1,18],
    [2,19],
    [3,20],
    [4,21],
    [5,22],
    [6,23],
    [7,24]]

### 끝내기 위한 변수 n
n=1
sum=0

while n<=len(studentList):
    print(f"{studentList[n-1][0]}반 학생 수 : {studentList[n-1][1]}")

    ### while문 종료를 위한 주가
    sum+= studentList[n-1][1]
    n+=1


print(f"평균 학생 수 : {int(sum/len(studentList))}")
