### 숫자 4개로 2개를 선택해 만들 수 있는 모든 경우의 수 출력
num = [4,6,7,9]
result=[]

for i in num:
    for j in num:
        if i == j:
            continue
        result.append([i,j])

print(f"result : {result}")
print(f"조합 수 : {len(result)} ")