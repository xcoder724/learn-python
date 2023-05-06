print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'white']
print(colors)
print(type(colors))

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

reds = list('red')
print(reds)

b = [x for x in range(1, 10)]
print(b)
print("b[0] = ", b[0])
print("b[1] = ", b[1])
print("b[2] = ", b[2])

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

listNested = ['a', 'b', ['c', 'd']]
print(listNested[0])
print(listNested[0][0])
print(listNested[1])
print(listNested[1][0])
print(listNested[2][0])
print(listNested[2][1])

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
print(" * 列表 添加 操作 * ")
ages = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 添加在索引位置
#  0 -> max ,从前往尾部添加，超过长度加在尾部
# -1 -> min ,从尾部往前添加，超过长度加在首位
ages.insert(14, 12)
print(ages)

# 添加在末尾
ages.append(1999)
print(ages)

# append追加可迭代对象，是在尾部增加一个对象整体，而不是依次添加可迭代对象里面的元素
ages.append([1, 2, 3])
print(ages)

# 添加可迭代对象的元素依次添加到尾部
ages.extend([1, 2, 3])    
print(ages)

print(" * 列表 删除 操作 * ")

# 删除指定元素（值相等），存在多个，只删除按索引找到的第一个
ages.remove(2)
print(ages)

