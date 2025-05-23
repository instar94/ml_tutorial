### 직원 나이 분포 그래프 출력
### 나이가 많은 순으로 출력 할 것
### 나이는 난수 20 ~ 50 사이 40명
import random
import freqmodule

if __name__ == "__main__":
    ### 리스트 세팅
    nums=[]
    for i in range(40):
        nums.append(random.randint(20,50))
    print(nums)
    fq=freqmodule.FreqAlgorithm(nums)

    ###최고 숫자 구하기
    maxNum = fq.getMaxNum()
    print(f"maxNum : {maxNum}")

    ### 인덱스 리스트 구하기
    freq=fq.getFreqNum()
    print(f"freq : {freq}")

    ### 그래프로 출력하기
    for i,v in enumerate(freq):
        if v != 0:
            print(f"{i}세 : {v}명 {'*'*v}")
