import copy

### 깊은 복사를 통해서 새롭게 정렬된 데이터를 받고 싶음
def bubblesort(ns,deepCopy=True):
    if deepCopy:
        cns = copy.copy(ns)
    else:
        cns=ns

    length=len(cns)-1
    for i in range(length):
        for j in range(length-i):
            if cns[j]>cns[j+i]:
                cns[j],cns[j+1]=cns[j+1],cns[j]
    return cns
