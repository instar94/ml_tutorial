### 1~50 사이 난수 30개 중복 허용
### 최대값과 최대값의 개수
import random
import maxmodule
if __name__ == "__main__":
    nums=[]
    for i in range(30):
       nums.append(random.randint(1,50))
    print(f"nums : {nums}")
    ma = maxmodule.MaxAlgorithm(nums)
    ma.setMaxNum()
    print(f"maxNum : {ma.getMaxNum()}")
    print(f"maxCnt : {ma.getMaxCnt()}")

