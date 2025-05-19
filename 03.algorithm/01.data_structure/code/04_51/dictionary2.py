### 비속어 필터링

words={"꺼지다":"가다",
       "쩔다":"엄청나다",
       "짭새":"경찰"}

txt = "강도는 짭새를 보고 꺼지다."

keys=list(words.keys())
print(txt)

for key in keys:
    if key in txt:
        print(f"key : {key}")
        print(f"word : {words[key]}")
        txt = txt.replace(key,words[key])


print(txt)