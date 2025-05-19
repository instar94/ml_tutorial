import random
nums=random.sample(range(50,100),20)
print(nums)

### 순위용 자료형
### 0인 원소가 20개인 리스트 선언
ranks=[0 for i in range(20)]

for idx,i in enumerate(nums):
    for j in nums:
        if i < j:
            ranks[idx]+=1

print(f"nums : {nums}")
print(f"ranks : {ranks}")

for i,n in enumerate(nums):
    print(f"nums {n} \t rank: {ranks[i]+1}")