### 근사값 알고리즘
import module as m
scores=[]

### 점수 입력
kor = int(input("점수 입력 :"))
eng = int(input("점수 입력 :"))
mat = int(input("점수 입력 :"))
hist = int(input("점수 입력 :"))
sci = int(input("점수 입력 :"))

### scores에 추가
scores.append(kor)
scores.append(eng)
scores.append(mat)
scores.append(hist)
scores.append(sci)

### 평균 구하기
totalScore=sum(scores)
avgScore=(totalScore/5)
print(f"총점 : {totalScore}\t평균 : {avgScore}")

### 학점 근사값 찾기
grade=m.getGrade(avgScore)
print(f"학점 : {grade}")