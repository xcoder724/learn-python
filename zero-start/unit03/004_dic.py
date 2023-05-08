print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
dic = {}
list1 = ['Wade','James','McGrady']
list2 = ['热火队','骑士队','火箭队']
for i in 0,1,2:
    dic[list1[i]] = list2[i]
print(dic)

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
print(dic.get('Wade'))
print(dic['Wade'])

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
print(" * 字典 遍历 操作 * ")
for k, v in dic.items():
    print("key = ", k, ", value = ", v)

dic['James'] = '湖人队'

for k, v in dic.items():
    print("key = ", k, ", value = ", v)

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
print(" * 字典 属性 操作 * ")
print('字典键值对, ', dic.items())
print('字典键, ', dic.keys())
print('字典值, ', dic.values())
print('字典长度, ', len(dic))
print('字典是否存在键, ', 'Wade' in dic)
print('字典是否存在键, ', 'Harden' in dic.values())
print('存在键，移除该键，返回对应的值, ', dic.pop('James'))
print(dic)
print('删除字典中最后一组键值对, ', dic.popitem())
print(dic)

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
print(" * 字典 高级 操作 * ")
dic['Harden'] =  '火箭队'
print(dic.setdefault('Harden', '雷霆队'))
print(dic)

newDic = {'Paul':'打铁队', 'Wade':'养老队', 'Iverson':'街球队'}
dic |= newDic
print(dic)