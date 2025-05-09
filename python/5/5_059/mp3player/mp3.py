from time import sleep
import random
class Player:
    def __init__(self):
        self.songList=[]
        self.isLoop=False

    def addSong(self, s):
        self.songList.append(s)

    def play(self):
        if self.isLoop:
            while self.isLoop:
                for s in self.songList:
                    print(f"제목 : {s.title}\t가수 : {s.singer}\t재생시간 : {s.playTime}")
                    sleep(s.playTime)
        else:
            for s in self.songList:
                print(f"제목 : {s.title}\t가수 : {s.singer}\t재생시간 : {s.playTime}")
                sleep(s.playTime)

    def suffle(self):
        ### shuffle : 리스트 순서 섞기
        random.shuffle(self.songList)

    def setIsLooP(self, flag):
        self.isLoop=flag