### for - if 문을 이용하여 조건에 맞는 값만 출력

### 과락점수
minScore = 60
### 점수 입력
korScore = int(input("국어 점수 : "))
engScore = int(input("영어 점수 : "))
mathScore = int(input("수학 점수 : "))
scienceScore = int(input("과학 점수 : "))

### 과목별 점수
score=[
    ["국어",korScore],
    ["영어",engScore],
    ["수학",mathScore],
    ["과학",scienceScore]]

### 과락점수보다 낮은 점수만 출력
for subject, value in score:
    if value >= minScore: continue
    print(f"과락 과목 : {subject} 점수 : {value}")


