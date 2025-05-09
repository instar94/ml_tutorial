file = open("C:/pythonEx/python이란.txt","r",encoding="UTF-8")

orignStr=file.read()
print(f"orignStr : {orignStr}")

newStr=orignStr.replace("Python","파이썬",2)
print(f"newStr : {newStr}")

file.close()

file = open("C:/pythonEx/python이란.txt","w",encoding="UTF-8")
file.write(newStr)
file.close()

file = open("C:/pythonEx/python이란.txt","r",encoding="UTF-8")
print(f"변경된 문구 : {file.read()}")
file.close()