## 원판 개수 / 출발 기능 / 도착 기둥 / 경유 기둥)
def hanoiTop(discCnt, fromBar,toBar, viaVar):
    if discCnt==1:
        print(f"{discCnt} 원판을 {fromBar}에서 {toBar}로 이동")

    else:
        hanoiTop(discCnt-1,fromBar,viaVar,toBar)
        print(f"{discCnt} 원판을 {fromBar}에서 {toBar}로 이동")
        hanoiTop(discCnt-1,viaVar,toBar,fromBar)


hanoiTop(3,1,3,2)