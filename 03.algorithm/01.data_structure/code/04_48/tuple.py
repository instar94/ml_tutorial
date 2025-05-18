### 전체 학생수 , 평균 학생수, 학생수가 가장 적은 학급, 학생수가 가장 많은 학급, 학급별 편차
studnetCnt = ({"class01" : 18},
              {"class02" : 21},
              {"class03" : 20},
              {"class04" : 19},
              {"class05" : 22},
              {"class06" : 20},
              {"class07" : 23},
              {"class08" : 17})

totalCnt = 0;avgCnt=0
minCnt=0;minClass=""
maxCnt=0;maxClass=""
deviation=[]

for dix,dic in enumerate(studnetCnt):
    for k,v in dic.items():
        totalCnt = totalCnt + v

        if maxCnt < v:
            maxCnt=v
            maxClass=k

        if minCnt > v or minCnt == 0 :
            minCnt=v
            minClass=k

avgCnt=round(totalCnt/len(studnetCnt),2)
print(f"전체 학생 수 : {totalCnt}")
print(f"평균 학생 수 : {avgCnt}")
print(f"최대 학생 수 : {maxClass} , {maxCnt}")
print(f"최저 학생 수 : {minClass} , {minCnt}")

for idx,dic in enumerate(studnetCnt):
    for k,v in dic.items():
        deviation.append(v-avgCnt)

print(f"학급별 편차 : {deviation}")