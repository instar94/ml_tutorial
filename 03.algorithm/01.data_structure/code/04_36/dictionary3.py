scores={"kor":80,"eng":75,"math":90,"hist":50}
print(scores)

minScore=70
fDic={}
fStr="재시험"

for key in scores:
    if scores[key]<minScore:
        scores[key]=fStr
        fDic[key]=fStr

print(f"socres : {scores}")
print(f"fDic : {fDic}")