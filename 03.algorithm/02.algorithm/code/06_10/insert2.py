import insert as ins
import random as rd

sList=[]
for i in range(100):
    sList.append(rd.randint(1,1000))
print(f"sList : {sList}")

sortList=ins.Insert(sList,True)

sortList.setSort()
sortListAsc=sortList.getSortNum()
print(f"오름차순 : {sortListAsc}")

sortList.isAscFunc(False)
sortList.setSort()
sortListDESC=sortList.getSortNum()
print(f"내림차순 : {sortListDESC}")