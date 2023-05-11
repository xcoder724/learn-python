import random
target = random.randint(1,5)
chance = 1

while chance<4:
    message = "请使用第"+ str(chance) +"机会，说出你心中的数字：\n"
    chance += 1
    guess = int(input(message))
    if guess == target :
        print("恭喜你猜对了")
        break

if chance > 3 :
    print("抱歉，你的机会用完了，下次再来哟！")