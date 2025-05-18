### 사람 이름 5명 저장
### 오름차순과 내림차순으로 정렬
### student={"s1":"윤서연","s2":"정혜린","s3":"이지우","s4":"김채연","s5":"김유연"}

sList = []
for i in range(5):
    sList.append(input("S 입력 : "))

print(f"sList : {sList}")

sList.sort()
print(f"sList 오름차순 : {sList}")

sList.sort(reverse=True)
print(f"sList 내림차순 : {sList}")
