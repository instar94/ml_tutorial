import random
import bubble as bb

sList=[]
for i in range(20):
    sList.append(random.randint(170,185))
print(f"sList : {sList}")

sListSorted=bb.bubblesort(sList)
print(f"sListSorted : {sListSorted}")

