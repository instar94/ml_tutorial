minScore = 60

scores=(("국어", 90),
        ("영어", 80),
        ("수학", 70),
        ("과학", 45))
n=0
while n<len(scores):
    if scores[n][1]<minScore:
        print(f"과락\t과목명:{scores[n][0]}\t점수:{scores[n][1]}")
    n+=1
