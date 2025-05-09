import dictionary as dic

krToEn=dic.KorToEng()
krToEn.registWord("책","Book")
krToEn.registWord("폰","Phone")
krToEn.registWord("인형","Doll")
krToEn.registWord("꽃","Flower")
krToEn.registWord("돌","Rock")

krToEn.printWords()

krToEn.updateWord("돌","RoCK")

print(f"책 {krToEn.searchWord("돌")}")
