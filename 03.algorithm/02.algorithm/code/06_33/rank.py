### 정수와 알파벳 순위 알고리즘
### 알파벳은 아스키코드값 사용
import rankmodule as rm
datas=[32,"a","z",45,"G",39,50,"T","t",22,31,55,"s",63,59,"E"]
print(f"datas : {datas}")

### 알파벳의 아스키코드 변경
aDatas=[]
for i in datas:
    ### 알파벳이면 아스키코드로 변경
    if str(i).isalpha():
        aDatas.append(ord(i))
    ### 아니면 그냥 추가
    else:
        aDatas.append(i)
print(f"aDatas : {aDatas}")

ranks=rm.rankFuc(aDatas)

for i,d in enumerate(datas):
    print(f"data : {d} \t ranks : {ranks[i]}")
