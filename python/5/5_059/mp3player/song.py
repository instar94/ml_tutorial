class Song:
    def __init__(self,t,s,pt):
        self.title=t
        self.singer=s
        self.playTime=pt

    def printSongInfo(self):
        return print(f"제목 : {self.title}\t가수 : {self.singer}\t재생시간 : {self.playTime}")