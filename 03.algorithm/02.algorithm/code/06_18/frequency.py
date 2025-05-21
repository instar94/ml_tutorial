### 학생 100명의 점수분포 표시
### 점수는 80 ~ 100
import random
from maxclass import MaxClass as mc


nums = []
rn=-0
for i in range(100):
    rn = random.randint(71,101)
    if rn !=100:
        rn = rn - (rn%5)
        nums.append(rn)
mn=mc(nums)
mn.getMax()
maxN=mn.getMaNum()

### 0도 포함해야 해서 maxN + 1
indexes=[0 for i in range(maxN+1)]

### nums에서 i값이 나올 때마다 indexs[i]에 1을 추가
for i in nums:
    indexes[i]=indexes[i]+1

maxAlgo = mc(indexes)
maxAlgo.getMax()
idx=1
for i in range(0,len(maxAlgo.nums)):
    if maxAlgo.nums[i]!=0:
        print(f"{idx}.{i} 빈도수: {maxAlgo.nums[i]} {'+'*maxAlgo.nums[i]}")
        idx+=1