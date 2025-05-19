### 삼각형부터 십각형
### 내각의 합을 딕셔너리로 저장

dic = {}

for i in range(3,11):
    ### 내각의 합 : 180 * (n-2)
    angleSum = 180 * (i-2)
    angle = int(angleSum/i)
    dic[i]=[angleSum,angle]

print(dic)