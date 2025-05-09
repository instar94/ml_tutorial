import time

startdate = time.mktime(time.strptime("2021-01-01", "%Y-%m-%d"))

fruit=3
fish=4
vegetable=5
url="C:/pythonEx/prot.txt"
with open(url, "w") as f:
    f.write("2021년 모든 선박 입항일\n")

for i in range(1, 366):
    if i % fruit == 0 and i % fish == 0 and i % vegetable == 0:
        target_timestamp = startdate + i * 24 * 60 * 60
        formatted = time.strftime('%Y-%m-%d 10:00:00', time.localtime(target_timestamp))
        print("formatted:", formatted)
        with open(url, "a") as f:
            f.write(f"{formatted}\n")