### 오름차 순으로 숫자를 추가 하는 프로그램

num=[1,3,6,11,46,54,74,85]
inputnum=int(input("숫자를 입력하세요 : "))
insertIdx=0

for i, n in enumerate(num):
    if insertIdx == 0 and inputnum < n:
        insertIdx = i

num.insert(insertIdx,inputnum)
print(f"num : {num}")