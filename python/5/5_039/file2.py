scoreDic = {"kor" : 85, "math" : 85, "eng" : 85, "hist" : 85, "science" : 85,}
uri="C:/pythonEx/"
with open(uri + "/scoreDic.txt","a") as f:
    f.writelines(key +"\t:" +str(scoreDic[key])+"\n" for key in scoreDic.keys())
#   딕셔러니 자체를 파일로
#   print(scoreDic, file=f)
with open(uri + "/scoreDic.txt","r") as f:
    print(f.read())