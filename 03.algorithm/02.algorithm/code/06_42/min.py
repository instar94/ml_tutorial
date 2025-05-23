### 1~50 사이 난수 30개 중복 허용
### 최대값과 최대값의 개수
import random
import minmodule
if __name__ == "__main__":
    nums=[]
    for i in range(30):
       nums.append(random.randint(60,100))
    print(f"nums : {nums}")
    ### 평균 구하기
    sumScore=sum(nums)
    avgScore=round(sumScore/len(nums),2)

    ma = minmodule.MinAlgorithm(nums)
    minScore=ma.getMinNum()
    diffScore=abs(minScore-avgScore)

    print(f"평균 점수 : {avgScore}")
    print(f"최저 점수 : {minScore}")
    print(f"편차 : {diffScore}")
