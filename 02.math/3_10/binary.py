num = 30

print("2진수 {}".format(bin(num)))
print("8진수 {}".format(oct(num)))
print("16진수 {}".format(hex(num)))

print("2진수 {}".format(type(bin(num))))
print("8진수 {}".format(type(oct(num))))
print("16진수 {}".format(type(hex(num))))

print("2진수 {}".format(format(num,"#b")))
print("8진수 {}".format(format(num,"#o")))
print("16진수 {}".format(format(num,"#x")))

print("{0:#b} {0:#o} {0:#x}".format(num))

print("{0:b} {0:o} {0:x}".format(num))

print("2진수 0b11110 > 10진수 {}".format(int("0b11110",2)))
print("8진수 0o36 > 10진수 {}".format(int("0o36",8)))
print("16진수 0x1e > 10진수 {}".format(int("0x1e",16)))


print("2진수 0b11110 > 8진수 {}".format(oct(0b11110)))
print("2진수 0b11110 > 16진수 {}".format(hex(0b11110)))
print("8진수 0o36 > 2진수 {}".format(bin(0o36)))
print("8진수 0o36 > 16진수 {}".format(hex(0o36)))
print("16진수 0x1e > 2진수 {}".format(bin(0x1e)))
print("16진수 0x1e > 8진수 {}".format(oct(0x1e)))