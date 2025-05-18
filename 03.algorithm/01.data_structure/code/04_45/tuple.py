### 교집합과 합집합 출력
### 교집합 : 겹치는 원소
### 합집합 : 중복 X
tuple1 = (1,3,2,6,12,5,7,8)
tuple2 = (0,5,2,9,8,6,17,3)

crossTuple=[]
### 합집합이라 tuple1 박고 시작
totalTuple=list(tuple1)

for i in tuple2:
    ### tuple 1과 겹치지 않음 > 합집합
    if i not in totalTuple:
        totalTuple.append(i)
    ### tuple 1과 겹침 > 교집합
    else :
        crossTuple.append(i)

crossTuple.sort()
totalTuple.sort()

crossTuple=tuple(crossTuple)
totalTuple=tuple(totalTuple)
print(f"교집합 : {crossTuple}")
print(f"합집합 : {totalTuple}")