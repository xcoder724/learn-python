print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
if True:
    print("True")
else:
    print("False")

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
number = 0
if number % 2 == 1 :
    print("奇数")
elif number % 2 == 0 :
    print("偶数")
else :
    print("number is {}",number)

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
import random
number = int(random.random()*100+1)
if number % 2 == 1 :
    print("奇数")
else :
    print("偶数")

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
x = int(random.random()*5+1)
match x:
    case 1:
        print(x)
    case 2:
        print(x)
    case 3:
        print(x)
    case 4:
        print(x)
    case 5:
        print(x)
    case _:
        print("default")

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
x = int(random.random()*12+1)
match x:
    case 1 | 2 | 3:
        print("春季：", x)
    case 4 | 5 | 6 :
        print("夏季：", x)
    case 7 | 8 | 9 :
        print("秋季：", x)
    case 10 | 11 | 12 :
        print("冬季：", x)
    case _:
        print("default")
