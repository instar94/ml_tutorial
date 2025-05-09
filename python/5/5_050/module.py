import wagefeeratio as wf

w = int(input("수입 : "))
f1 = int(input("수도요금 : "))
f2 = int(input("전기요금 : "))
f3 = int(input("가스요금 : "))

wf.setIncome(w)
wf.setf1(f1)
wf.setf2(f2)
wf.setf3(f3)

print(f"비율 : {round(wf.getrate(),2)}%")