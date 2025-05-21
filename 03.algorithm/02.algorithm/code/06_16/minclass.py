class MinClass:
    def __init__(self,cs):
        self.chars=cs
        self.minChar=0

    def getMaxChar(self):
        self.minChar = self.chars[0]
        for i in self.chars:
            ###ord : 아스키코드로
            if ord(i) < ord(self.minChar):
                self.minChar = i
        return self.minChar

chars=["c","x","Q","A","e","P","p"]
mc = MinClass(chars)
maxChar=mc.getMaxChar()
print(f"maxChar : {maxChar}")
