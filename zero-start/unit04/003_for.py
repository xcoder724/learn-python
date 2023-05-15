print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
list1 = ["rachel","monica","Phoebe","joey"]
list1.sort()
for i, item in enumerate(list1):
    print("序号：",i,", val: ", item)

print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
    
for i, _ in enumerate(list1):
    print("序号：",i,", val: ", list1[i])