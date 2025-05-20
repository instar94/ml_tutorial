import select as st
import random as rd

scores=rd.sample(range(50,101),20)
sortedScore=st.Select(scores,True)
sortedScore.setSort(scores,False)
print(sortedScore.getSortNum())