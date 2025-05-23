### 삽입 정렬을통해서
import random
import insertmodule

if __name__=="__main__":
    nums=random.sample(range(1,21),10)
    print(f"정렬 전 nums : {nums}")
    result=insertmodule.insertSort(nums,True)
    print(f"오름차순 nums : {result}")
    result = insertmodule.insertSort(nums, False)
    print(f"내림차순 nums : {result}")