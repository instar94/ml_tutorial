def getPerCnt(n,r,logprint=True):
    result=1
    for n in range(n, (n-r), -1):
        if logprint: print(f"n : {format(n)}")
        result = result * n

    return result

from itertools import permutations
def getPer(ns,r):
    plist=list(permutations(ns,r))
    print(f"{len(ns)}P{r} 개수 : {len(plist)}")
    for n in permutations(ns,r):
        print(n, end="")
