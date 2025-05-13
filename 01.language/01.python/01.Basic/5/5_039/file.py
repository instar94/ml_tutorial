uri="C:/pythonEx/"

with open(uri + "lans.txt","r") as f:
#     lanlist=f.readlines()
#
# print(f"lanlist : {lanlist}")
# print(f"lanlist Type : {type(lanlist)}")
    line=f.readline()
    while line !="":
        print(f"line : {line}",end="")
        line = f.readline()