### extend와 +
aList = [1, 2, 3]
bList = [4, 5, 6]
print(f"aList : {aList}")
print(f"bList : {bList}")

cList=aList + bList
print(f"cList : {cList}")

aList.extend(bList)
print(f"aList : {aList}")
print(f"bList : {bList}")
