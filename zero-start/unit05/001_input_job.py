print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

while True:
    args = str(input("请输入内容：\n"))
    if args == "q" or args == "quit" :
        print("程序结束...")
        break
    print("你输入的内容是: ", args)