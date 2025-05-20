nums=[-2,-4,5,7,10,0,8,20,-11]

maxNum=nums[0]

for i in nums:
    if i > maxNum:
        maxNum=i

print(f"maxNum : {maxNum}")