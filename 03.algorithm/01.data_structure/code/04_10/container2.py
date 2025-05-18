### append() 함수 : 리스트 안에 리스트
socre = [["국어", 80], ["영어", 90], ["수학", 85]]
socre.append(["과학", 95])

print("socre : ", socre)
for i,d in socre:
    print(f"과목 : {i}, 점수 : {d}")