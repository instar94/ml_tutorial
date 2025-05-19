### 과목별 점수를 딕셔너리로 저장
### 출력하기
subject = ["국어","영어","수학","과학","국사"]
scores = {}

for i in subject:
    score = input(i+" 점수 입력 : ")
    scores[i]=score

print(f"과목별 점수 : {scores}")