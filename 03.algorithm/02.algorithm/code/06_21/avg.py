###평균 구하기 알고리즘
### 10개 난수 생성
import random
nums=random.sample(range(0,100),10)

### 합 구하기
total= sum(nums)

### 평균 구하기
avg=total/len(nums)
print(f"총합 : {total}\t평균 : {avg}")

### 특정조건에 맞는 수의 평균
### 90이하의 수 평균 구하기
###난수 발생
nums2=random.sample(range(0,100),30)
print('nums2 : ',nums2)
### 합 구하기
total2=0
for i in nums2:
    if i<=90:
        total2+=i

### 평균 구하기
avg2=total2/len(nums2)
print(f"총합2 : {total2}\t평균2 : {avg2}")

### 정수들의 평균만 구하기
nums3=[3,5,10,12.3,15.9,20.3]

### 합 구하기
total3=0
for i in nums3:
    if i-int(i)==0:
        total3+=i

### 평균 구하기
avg3=total3/len(nums3)
print(f"총합 : {total3}\t평균 : {avg3}")