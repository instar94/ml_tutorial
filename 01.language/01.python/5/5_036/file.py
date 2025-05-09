uri="C:/pythonEx/"


### W : 쓰기
file =open(uri + "w+a_mode","w")
file.write("w모드는 파일을 새로 만듦")
file.close()

### A : 추가 쓰기
file =open(uri + "w+a_mode","a")
file.write("a모드는 파일 뒤에 새로 작성")
file.close()

### X : 새로 만들기
file =open(uri + "x_mode","x")
file.write("x모드는 파일을 새로 만듦/n파일이 있으면 오히려 예외 발생")
file.close()

### R : 파일 읽기
file=open(uri+"w+a_mode","r")
print(f"file.read() : {file.read()}")
file.close()

file=open(uri+"x_mode","r")
print(f"file.read() : {file.read()}")
file.close()