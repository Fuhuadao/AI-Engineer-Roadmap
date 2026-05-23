# if elif else 多条件判断
print("欢迎来到动物园")
height = int(input("请输入你的身高："))
vip_level = int(input("请输入你的vip等级（1-5）："))
day = int(input("请告诉我今天是几号："))
if height < 120:
    print("身高小于120cm，可以免费游玩")
elif vip_level > 3:
    print("vip等级大于3，可以免费游玩")
elif day == 1:
    print("今天是1号免费日，可以免费游玩")
else:
    print("不好意思，你未满足条件，需要购票10元")
print("祝你游玩愉快！")

# 代码简化
print("欢迎来到动物园")
if int(input("请输入你的身高：")) < 120:
    print("身高小于120cm，可以免费游玩")
elif int(input("请输入你的vip等级（1-5）：")) > 3:
    print("vip等级大于3，可以免费游玩")
elif int(input("请告诉我今天是几号：")) == 1:
    print("今天是1号免费日，可以免费游玩")
else:
    print("不好意思，你未满足条件，需要购票10元")
print("祝你游玩愉快！")

# 猜猜心里数字案例
num = 20
if int(input("请输入第一次猜想的数字（1-100）：")) == num:
    print("恭喜你答对了")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对了")
else:
    print(f"Sorry，全部猜错了，我想的是：{num}")

# 判断语句的嵌套
print("欢迎来到动物园")
if int(input("请输入你的身高：")) > 120:
    print("你的身高超出限制，不可以免费游玩")
    print("不过如果你的vip等级超过3级，可以免费游玩")
    if int(input("请输入你的vip等级：")) > 3:
        print("你的vip等级大于3，可以免费游玩")
    else:
        print("抱歉，你需要购票10元")
else:
    print("满足要求，你可以免费游玩")
print("祝你游玩愉快！")

# 多条件判断语句嵌套
if int(input("请输入你的年龄：")) >= 18:
    print("恭喜你成年了")
    if int(input("请再次输入你的年龄：")) < 30:
        print("你的年龄达标了")
        if int(input("你入职了多长时间：")) > 2:
            print("恭喜你，年龄和入职时间达标，可以领取礼物")
        elif int(input("你的级别是：")) > 3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，你的入职时间和级别不达标，无法领取礼物")
    else:
        print("不好意思，你超过规定年龄，无法领取礼物")
else:
    print("不好意思，你未成年，无法领取礼物")