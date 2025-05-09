import sys ###시스템 정보에 관한 모듈

for path in sys.path:
    print(path)### system의 경로를 출력


from calcul import cal
print(f"cal.add(10,20) : {cal.add(10, 20)}")
print(f"cal.sub(10,20) : {cal.sub(10, 20)}")
print(f"cal.mul(10,20) : {cal.mul(10, 20)}")
print(f"cal.div(10,20) : {cal.div(10, 20)}")

### 다른 곳에서 쓸 수 없음