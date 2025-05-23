### 이진검색 알고리즘 실습
import binarclass as bc

if __name__ == "__main__":
    nums = [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]
    inputNum=int(input("찾을 값 : "))
    print(f"nums : {nums}")
    findIdx=bc.binarFuc(nums,inputNum)
    if findIdx != -1:
        print(f"findIdx : {findIdx}")
    else:
        print("findIdx : -1")
