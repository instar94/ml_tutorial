### ,를 통한 연속 출력
userName="이즈나"
userAge=20
print("유저 이름 : ",userName)
print("유저 나이 : ",userAge)

### 개행 강제로 없애기 end=""
### 디폴트가 end="\n"
print("3 * 5 = ", end="")
print(3*5)
### 3 * 5 = 15

### 포멧 문자열 출력
### f를 붙이고 {}안에 변수를 넣음
print(f"user name : {userName}")
print(f"user age : {userAge}")

### 중간에 개행 \n
### 중간에 탭 \t
print(f"user name\t:\t{userName} \nuser age\t:\t{userAge}")

