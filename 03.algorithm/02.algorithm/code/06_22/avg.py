import random
import near

### 점수 생성
scores=[]
for i in range(10):
    tempNum=round((random.uniform(7,10)),1)
    scores.append(tempNum)

print(scores)

### 플레이어 순위 생성
top5Player=[]
for i in range(5):
    tempNum=round((random.uniform(7,10)),1)
    top5Player.append(tempNum)

print(top5Player)

### 평균구하기
totalScore=sum(scores)
avgScore= round(totalScore/len(scores),3)
print(f"총점 : {totalScore}\t평균 : {avgScore}")

### 순위 구하기 - 근사값 알고리즘
tp=near.Grade(top5Player,avgScore)
tp.setGrade()
top5Player=tp.getFinalScore()
print(f"{top5Player}")