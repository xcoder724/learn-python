str1 = "hello world"
str2 = "abcdefghijklmnopqrstuvwxyz"
str3 = "012345678901234567890123456789"
str4 = "1 2 3 4 5 6 7 8 9 0"

s1 = "llo"
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")
print(s1 in str1)

print(s1 not in str2)

print(str1 + str2)

print(s1 * 2)


print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")
print(" * 字符串下标 * \n")
print(str2[0])

print(str3[1:3])

print(str3[0:13:3])

print(str3.count("012", 2, 13))

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")
print(" * 字符串判断 * \n")
print("str3都是数字,", str3.isalnum())
print("str1都是字母,", str1.isalpha())
print("str2都是字母,", str2.isalpha())

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")
print(" * 字符串常用 * \n")
print(str1.join("12345"))
print(str1.join(["1", "2", "3", "4", "5"]))

print(str4.split(" "))
print(str4.split(" ",1))

print(str4.startswith("1",0, 4))

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n")
print(" * 作业 * \n")

article = "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\n"
print(article.count("better"))



