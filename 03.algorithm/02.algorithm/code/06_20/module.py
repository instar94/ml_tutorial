def getGrade(num):
    baseScores=[95,85,75,65,55]
    nearNum=0
    minNum=100

    for n in baseScores:
        ### 차이의 절대값 구함
        absNum = abs(n-num)
        ### 이상 치가 아니라면 (100이상)
        if absNum<minNum:
            minNum=absNum
            nearNum=n

    if nearNum==95:
        return "A"
    elif nearNum==85:
        return "B"
    elif nearNum==75:
        return "C"
    elif nearNum==65:
        return "D"
    else:
        return "F"