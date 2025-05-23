### 숫자로 이뤄진 리스트
### 사용자가 입력한 숫자를 검색하는 모듈
### 선형 검색 모듈 사용
### 숫자 리스트 1~20까지 정수 10개 난수
### 검색과정 로깅
### 성공하면 인덱스 출력
### 실패하면 -1 출력
import random
###검색 할 숫자
inputNum=int(input("검색할 숫자 : "))
### 숫자 난수 10개
nums=random.sample(range(0,20),10)
print(nums)

### 찾는 값의 인덱스
findIdx=-1

### 비교 진행
for i in nums:
    if i == inputNum:
        findIdx=nums.index(i)
        break

if findIdx != -1:
    print(f"검색된 값의 인덱스 : {findIdx}")
else:
    print(f"검색된 값이 없습니다.")