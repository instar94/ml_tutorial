def sendSMS(msg):
    if len(msg) > 10 :
        raise Exception("길이가 초과되어 MMS로 전환됩니다1",1)
    else:
        print("SMS 전송 완료 ")

def sendMMS(msg):
    if len(msg) <= 10 :
        raise Exception("길이가 미달로 SMS로 전환됩니다1",2)
    else:
        print("MMS 전송 완료 ")

msg = input("메세지를 입력해주세요 : ")

try:
    sendSMS(msg)
except Exception as e :
    print(f"e: {e.args[0]}")
    print(f"e: {e.args[1]}")

    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1]==2:
        sendSMS(msg)
