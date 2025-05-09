###.format()을 이용한 데이터 출력
###.format()안에 있는 데이터가 {}로 전달 된다.
userName="이즈나"
userAge=30
pi = 3.14

### 인덱스가 없으면 순차적으로 들어감
print("이름 : {} , 나이 {} ".format(userName, userAge))
### 인덱스를 넣으면 수를 바꿀 수 있음 
print("이름 : {1} , 나이 {0} ".format(userName, userAge))

### 형식문자
### 나는 이런 형식으로 데이터를 넣을것이다.
### %s 문자열 %d 정수 %f 실수
### %.2f : 소수점 2째짜리 까지 출력
print("이름 : %s , 나이 %d , 파이는 %.2f"%(userName,userAge,pi))
