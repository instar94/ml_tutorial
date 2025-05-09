import random

uri = "C:/pythonEx/"

def lotoGen(nums):
    for idx, num in enumerate(nums):
        with open(uri + "lotto.txt","a") as f :
            if idx < (len(nums)-2):
                f.write(str(num)+", ")
            elif idx == (len(nums) -2):
                f.write(str(num))
            elif idx == (len(nums)-1):
                f.write("\n")
                f.write("보너스 :" + str(num))
                f.write("\n")

rNums=random.sample(range(1,46),7)
print(f"rNum : {rNums}")
lotoGen(rNums)

with open(uri + "lotto.txt","r") as f :
    print("당첨 번호 \n" , f.read())

