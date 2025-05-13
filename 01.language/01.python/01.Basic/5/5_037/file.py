uri="C:/pythonEx/"
with open(uri + "5_037.txt","a") as file:
    file.write("with as 문을 이용하면 close를 생략 할 수 있습니다.")

with open(uri + "5_037.txt","r") as file:
    print(file.read())