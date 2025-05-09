scores = [int(input("국어 : ")),
         int(input("영어 : ")),
         int(input("수학 : "))]
print(scores)

copysocre=scores.copy()

for idx,score in enumerate(copysocre):
    result=score*1.1
    copysocre[idx]= 100 if result > 100 else result

print(f"이전 평균 : {round(sum(scores) / len(scores),1)}")
print(f"이후 평균 : {round(sum(copysocre) / len(copysocre),2)}")