### 숫자 정렬을 버블 정렬을 이용해
### 오름차순과 내림차순 정렬
### 정렬하는 과정도 출력할 것
import random
import bubblemodule as bm

if __name__ == "__main__":
    nums=random.sample(range(1,21),10)
    print(f"정렬 전 nums : {nums}")
    resultASC=bm.bubbleSort(nums,True)

