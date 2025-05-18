### 1~100사이 난수 10개 생성
### 짝수 홀수 리스트 구분
import random

### 1~100사이 난수 10개 생성 - 리스트형 반환
rNum=random.sample(range(1,101),10)
print(rNum)

### 리스트 선언
oddList=[]
evenList=[]

### rNum만큼 반복
for i in rNum:
    ### 2로 나눠 떨어지면 짝수
    if i%2==0:
        evenList.append(i)
    ### 2로 나눠 떨어지지 않으면 홀수
    else:
        oddList.append(i)

print("짝수 리스트 : ", evenList)
print("홀수 리스트 : ", oddList)