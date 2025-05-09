import time
def getTime():
    lt=time.localtime()
    timeStamp=time.strftime("%Y-%m-%d %H:%M:%S",lt)
    return timeStamp

def income(u,m,d,t):
    timeStamp=getTime()
    with open(u,"a") as f:
        f.write("="*20+"\n")
        f.write(f"{timeStamp}"+"\n")
        f.write(f"[입금] {d} : {m}"+"\n")
        f.write(f"[잔액] {t}"+"\n")

def outcome(u,m,d,t):
    timeStamp=getTime()
    with open(u,"a") as f:
        f.write("="*20+"\n")
        f.write(f"{timeStamp}"+"\n")
        f.write(f"[출금] {d} : {m}"+"\n")
        f.write(f"[잔액] {t}"+"\n")

