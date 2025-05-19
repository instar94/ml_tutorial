### 문자열을 공백으로 구분하여 리스트에 저장
### 인덱스와 단어를 이용해 딕셔너리 저장
str = "파이썬은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다."
dic={}

### 공백 기준 split
tempList=str.split(" ")

for i,v in enumerate(tempList):
    dic[i]=v

print(dic)