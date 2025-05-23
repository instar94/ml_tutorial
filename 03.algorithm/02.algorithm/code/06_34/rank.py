### 50~100까지 난수 20개 리스트
### 순위에 따라 아이템 정렬
import random
import rankmodule

nums=random.sample(range(50,101),20)
print(f"nums : {nums}")

### rank에 따라 정렬하기
sNums=rankmodule.rankFuc(nums)
print(f"sNums : {sNums}")