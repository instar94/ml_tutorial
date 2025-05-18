pw=("pw1","pw2","pw3","pw4")
print(f"pw : {pw}")

#### 1~3학년 성적 > 졸업 학점 평균이 4.0이 되도록하는 1,2 학기 최소 학점
scores = ((3.7,4.2),(2.9,4.3),(4.1,4.2))
total=0

for i in scores:
    for j in i:
        total+=j

total=round(total,1)
avg = round((total/6),1)
print(f"3학년 총 학점 : {total}")
print(f"3학년 평균 학점 : {avg}")

x = round((4.0 * 8) - total,1)
print(f"4학년 목표 학점 : {x}")
y = round(x/2,1)
print(f"한 학기당 : {y}학점 필요")

scores = list(scores)
scores.append((y,y))
scores = tuple(scores)
print(f"scores : {scores}")