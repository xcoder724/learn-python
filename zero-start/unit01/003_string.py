str1 = "hello world"
str2 = "abcdefghijklmnopqrstuvwxyz"
str3 = "012345678901234567890123456789"

s1 = "llo"
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")
print(s1 in str1)

print(s1 not in str2)

print(str1 + str2)

print(s1 * 2)

print(str2[0])

print(str3[1:3])

print(str3[0:13:3])

print(str3.count("012", 2, 13))
print("str3都是数字,", str3.isalnum())
print("str1都是字母,", str1.isalpha())
print("")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")
