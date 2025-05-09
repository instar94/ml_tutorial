"""
##print("이름 입력")
## 매개변수 > 출력 문구
userInputData=input("이름 입력")
print(userInputData)
"""

"""
### 입력한 데이터는 항상 문자열
userInputData=input("입력")
print(userInputData)
print(type(userInputData)) ### 무조건 str
"""

### str이 아닌 값을 원한다면 형변환
userInputData=int(input("숫자 입력"))
print(userInputData)
print(type(userInputData)) ### 무조건 str
