### 진법 변환하기
rNum=int(input("10진수: "))

print("2진수 : {}".format(bin(rNum)))
print("8진수 : {}".format(oct(rNum)))
print("16진수 : {}".format(hex(rNum)))

print("2진수 0b11110 > 10진수 : {}".format(int("0b11110",2)))
print("8진수 0o17 > 10진수 : {}".format(int("0o17",8)))
print("16진수 0x1E > 10진수 : {}".format(int("0x1E",16)))


print("2진수 0b11110 > 8진수 : {}".format(oct(int("0b11110",2))))
print("2진수 0b11110 > 16진수 : {}".format(hex(int("0b11110",2))))
print("8진수 0o17 > 2진수 : {}".format(bin(int("0o17",8))))
print("8진수 0o17 > 16진수 : {}".format(hex(int("0o17",8))))
print("16진수 0x1E > 2진수 : {}".format(bin(int("0x1E",16))))
print("16진수 0x1E > 8진수 : {}".format(oct(int("0x1E",16))))