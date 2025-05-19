nums = [10,2,7,21,0]
print(f"정렬 전 : {nums}")

len=len(nums)-1
for i in range(len):
    for j in range(len-i):
        if nums[j]>nums[j+1]:
            ### 둘의 위치를 바꾸는 방법
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            # temp=nums[j]
            # nums[j] = nums[j+1]
            # nums[j+1] =temp

print(f"정렬 후 : {nums}")