uri="C:/pythonEx/"
lang = ["c","java","c#","python","js"]


with open(uri + "lang.txt","a") as f:
    #f.write(item)
    #f.write("\n")
    # 를 아래와 같이 짧게
    f.writelines(item + "\n" for item in lang)

with open(uri + "lang.txt","r") as f:
    print(f.read())