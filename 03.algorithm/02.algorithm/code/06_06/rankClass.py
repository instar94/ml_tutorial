class RankDeviation:
    def __init__(self, ms,fs):
        self.midScore=ms
        self.finScore=fs
        self.midRank=[0 for i in range(20)]
        self.finRank = [0 for i in range(20)]
        self.rankDevi = [0 for i in range(len(ms))]

    ### 랭크 계산
    def setRank(self, score, rank):
        for idx, sco1 in enumerate(score):
            for sco2 in score:
                if sco1<sco2:
                    rank[idx]+=1


    ### 등수 계산
    def setMid(self):
        self.setRank(self.midScore,self.midRank)

    def setFin(self):
        self.setRank(self.finScore,self.finRank)

    def getMidRank(self):
        return self.midRank

    def getFinRank(self):
        return self.finRank

    def printDevi(self):
        for idx, mrank in enumerate(self.midRank):
            devi = mrank - self.finRank[idx]
            if devi > 0 :
                devi = "[상승]" + str(abs(devi))
            elif devi < 0 :
                devi = "[하락]" + str(abs(devi))
            else:
                devi = "[유지]" + str(abs(devi))

            print(f"중간고사 : {mrank}\t기말고사 : {self.finRank[idx]}\t편차 : {devi}")

