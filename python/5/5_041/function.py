def getDistance(speed,hour,minute):
    distance = speed * (hour + minute / 60)
    return distance
def getTime(speed,distance):
    time=distance / speed
    h= int(time)
    m= int((time-h)*100 * 60 / 100)
    return [h,m]

print("="*60)
### 거리 = 속력*시간
s = float(input("속도 (km/h):"))
h = float(input("시간 (시):"))
m = float(input("시간 (분):"))
d=getDistance(s,h,m)
print(f"{s}km/h로 {h}시간 {m}분 이동하여 {d}km/h 이동 가능")
print("="*60)

print("="*60)
### 거리 = 속력*시간
s = float(input("속도 (km/h):"))
d= float(input("이동 거리"))
t=getTime(s,d)
print(f"{s}km/h로 {t[0]}시간 {t[1]}분 이동하여 {d}km/h 이동 가능")
print("="*60)
