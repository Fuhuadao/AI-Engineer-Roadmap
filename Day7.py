# if语句基本格式的应用
age = 19
print(f"我{age}岁了")
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")
print("时间过得真快")

# 成年人判断案例
print("欢迎来到游乐场，儿童免费，成人收费")
age =  int(input("请输入你的年龄："))
#通过if语句进行成年人判断
if age >= 18:
    print("你已成年，游玩需要补票10元")
else:
    print("您未成年，可以免费游玩")
print("祝你游玩愉快")

# 我要买票吗案例
print("欢迎来到动物园")
height = int(input("请输入你的身高(cm)："))
# 通过if else进行身高判断
if height > 120:
    print("你的身高超过120cm，游玩需要购票,10元")
else:
    print("你的身高未超出120从cm，可以免费游玩")
print("祝你游玩愉快")