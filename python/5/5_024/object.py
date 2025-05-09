class Midterm:
    def __init__(self,s1,s2,s3):
        print("------- Midterm Called ------- ")
        self.mid_kor = s1
        self.mid_eng = s2
        self.mid_math = s3

    def printMidScore(self):
        print(f"Midterm Kor : {self.mid_kor}")
        print(f"Midterm Eng : {self.mid_eng}")
        print(f"Midterm Math : {self.mid_math}")

class EndExam(Midterm):
    def __init__(self,s1,s2,s3,s4,s5,s6):
        print("------- EndExam Called ------- ")
        super().__init__(s1,s2,s3)
        self.end_kor = s4
        self.end_eng = s5
        self.end_math = s6

    def getTotlaScore(self):
        total = self.mid_kor + self.mid_math + self.mid_eng
        total += self.end_kor + self.end_math + self.end_eng
        return total

    def getAverage(self):
        return self.getTotlaScore()/6

exam = EndExam(90,80,70,100,29,70)
print(f"Total : {exam.getTotlaScore()}")
print(f"Average : {round(exam.getAverage(),1)}")