datas=[3,2,5,7,9,1,0,8,6,4]
print(f"datas : {datas}")

findNum=int(input("찾으려는 값 : "))
searchIdx=-1
n=0

### 보초법을 위한 데이터 추가
datas.append(findNum)
print(f"datas : {datas}")
while True:
    if datas[n] == findNum:
        if n != len(datas) -1 :
            searchIdx=n
        break
    n += 1

print(f"searchIdx : {searchIdx}")
