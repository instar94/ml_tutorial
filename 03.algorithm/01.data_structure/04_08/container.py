### while - if 문을 이용하여 조건에 맞는 값만 출력

### 과락점수
minScore = 60
### 과목별 점수
score=[
    ["국어",58],
    ["영어",70],
    ["수학",90],
    ["과학",50]]

n=0

### 과락점수보다 낮은 점수만 출력
while n < len(score):
    if score[n][1] < minScore:
        print(f"과락 과목 : {score[n][0]} 점수 : {score[n][1]}")
    n+=1


