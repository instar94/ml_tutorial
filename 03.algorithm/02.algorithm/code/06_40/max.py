### 1~50 사이 난수 30개 중복 허용
### 최대값과 최대값의 개수
import random
import maxmodule
if __name__ == "__main__":
    nums=[]
    for i in range(30):
       nums.append(random.randint(60,100))
    print(f"nums : {nums}")
    ### 평균 구하기
    sumScore=sum(nums)
    avgScore=round(sumScore/len(nums),2)

    ma = maxmodule.MaxAlgorithm(nums)
    maxScore=ma.getMaxNum()
    diffScore=abs(maxScore-avgScore)

    print(f"평균 점수 : {avgScore}")
    print(f"최고 점수 : {maxScore}")
    print(f"편차 : {diffScore}")
