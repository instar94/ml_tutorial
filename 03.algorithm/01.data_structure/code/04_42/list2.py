### 중복 원소 제거
### 마지막 원소만 살림
num = [2,22,7,8,9,2,7,3,5,2,7,1,3]
print(f"num : {num}")

idx=0
while True:
    ### num 리스트의 길이만큼 실행 
    if idx >= len(num):
        break
    ### 해당 인덱스의 값이 2개 이상 > 제거 
    ### continue : 3개 이상 있을 수 있으니 1개 남을 때까지 반복
    if num.count(num[idx]) >= 2:
        num.remove(num[idx])
        continue
    idx += 1

print(f"num : {num}")