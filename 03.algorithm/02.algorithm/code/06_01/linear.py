datas=[3,2,5,7,9,1,0,8,6,4]
print(f"datas : {datas}")

findNum=int(input("찾으려는 값 : "))
searchIdx=-1
n=0

while True:
    if n == len(datas):
        searchIdx==-1
        break
    elif datas[n] == findNum:
        searchIdx=n
        break
    n += 1

print(f"searchIdx : {searchIdx}")
