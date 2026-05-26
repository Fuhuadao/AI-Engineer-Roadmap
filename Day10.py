# while猜数字案例
import random
computer = random.randint(1,100)
print("系统将在1~100中随机生成一个整数，开始你的猜测")
count = 0
while 1:
    a = int(input("请输入你的数字:"))
    count += 1
    if a > computer:
        print("数字太大了，请重新输入")
    else:
        if a < computer:
            print("数字太小了，请重新输入")
        else:
            if a == computer:
                print(f"恭喜你答对了,答案是{computer},你一共猜测了{count}次")
            break

# while循环的嵌套使用
i = 1
while i <= 100:
    print(f"这是我喜欢小美的第{i}天，我要....")
    j = 1
    while j < 10:
        print(f"送给小美第{j}朵玫瑰花")
        j += 1
    print("小美，我喜欢你")
    i += 1
print(f"坚持{i}天，表白成功")

