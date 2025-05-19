### 1~10까지의 약수를 저장하는 딕셔너리

dic = {}

for i in range(2,11):
    tempList=[]
    for j in range(1,i+1):
        if i%j == 0 :
            tempList.append(j)
    dic[i] = tempList
print(dic)