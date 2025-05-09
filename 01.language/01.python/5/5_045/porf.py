def exampleResult(s1,s2,s3,s4,s5):
    passAvgScore=60;limitScore=40;

    def getTotalScore(s1,s2,s3,s4,s5):
        print(f"총점 {s1+s2+s3+s4+s5}")
        return s1+s2+s3+s4+s5

    def getAverageScore(s1,s2,s3,s4,s5):
        print(f"평균 {getTotalScore(s1,s2,s3,s4,s5)/5}")
        return getTotalScore(s1,s2,s3,s4,s5)/5

    def checkPass():
        print(f"{s1} : PASS") if s1 >=limitScore else print(f"{s1} : fail")
        print(f"{s2} : PASS") if s2 >= limitScore else print(f"{s2} : fail")
        print(f"{s3} : PASS") if s3 >= limitScore else print(f"{s3} : fail")
        print(f"{s4} : PASS") if s4 >= limitScore else print(f"{s4} : fail")
        print(f"{s5} : PASS") if s5 >= limitScore else print(f"{s5} : fail")

    def printFinalPass():
        if getAverageScore(s1,s2,s3,s4,s5) >= passAvgScore:
            if s1 >=limitScore and s2 >=limitScore and s3 >=limitScore and s4 >=limitScore and s5 >=limitScore:
                print("PASS")
            else :
                print("Fail")
        else:
            print("Fail")
    getAverageScore(s1,s2,s3,s4,s5)
    checkPass()
    printFinalPass()