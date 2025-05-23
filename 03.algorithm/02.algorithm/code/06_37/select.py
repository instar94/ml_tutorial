### 선택 정렬
### i번째로 정렬될 수와 자리를 바꿈
import random
import selectmodule as sm

if __name__ == "__main__":
    nums=random.sample(range(1,21),10)
    print(f"정렬 전 nums : {nums}")
    resultASC=sm.selectSort(nums,True)
    print(f"오름차순 nums : {resultASC}")
    resultDESC=sm.selectSort(nums,False)
    print(f"내림차순 nums : {resultDESC}")

