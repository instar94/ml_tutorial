### 중간 기말 고사 성적 난수 발생
### 중간 기말 각각의 순위
### 중간 - 기말간 순위 편차
import random
import rankClass as rc

midScore=random.sample(range(50,100),20)
finScore=random.sample(range(50,100),20)
print(f"중간고사 : {midScore}")
print(f"기말고사 : {finScore}")

rankDevi=rc.RankDeviation(midScore,finScore)
rankDevi.setMid()
rankDevi.setFin()
rankDevi.printDevi()
