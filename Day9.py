# 判断语句综合案例：猜数字
import  random
num = random.randint(1, 10)
guss_num = int(input("将从整数1~10随机给出一个数，请你输入所猜想的数字："))
if guss_num == num:
    print(f"恭喜你，你猜对了，答案就是{num}")
else:
    if guss_num > num:
        print("你数字太大了")
    else:
        if guss_num < num:
            print("你数字太小了")

    guss_num = int(input("请你再次输入所猜想的数字："))
    if guss_num == num:
        print(f"恭喜你，你猜对了，答案就是{num}")
    else:
        if guss_num > num:
            print("你数字太大了")
        else:
            if guss_num < num:
                print("你数字太小了")

        guss_num = int(input("请你再次输入所猜想的数字："))
        if guss_num == num:
            print(f"恭喜你，你猜对了，答案就是{num}")
        else:
            print("很抱歉，你的三次机会用完了")

# while循环
f = 0
while f < 100:
    print("距离成功还差亿点")
    f += 1

# 求1~100的和
a = 0
i = 1
while i < 101:
    a = i*(i+1)/2
    i += 1
print(f"1~100的和为：{a}")