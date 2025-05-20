class MaxClass:
    def __init__(self,cs):
        self.chars=cs
        self.maxchars=0

    def getMaxChar(self):
        self.maxchars = self.chars[0]
        for i in self.chars:
            ###ord : 아스키코드로
            if ord(i) > ord(self.maxchars):
                self.maxchars = i
        return self.maxchars

chars=["c","x","Q","A","e","P","p"]
mc = MaxClass(chars)
maxChar=mc.getMaxChar()
print(f"maxChar : {maxChar}")



