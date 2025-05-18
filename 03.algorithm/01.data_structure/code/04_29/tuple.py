minScore = 60

scores=(("국어", 90),
        ("영어", 80),
        ("수학", 70),
        ("과학", 45))

for subject, score in scores:
    if score<minScore:
        print(f"과락\t과목명:{subject}\t점수:{score}")