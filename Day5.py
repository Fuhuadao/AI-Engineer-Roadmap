# 通过占位的形式，完成拼接
name = "小紮"
massage = "我的名字叫%s"%name
print(massage)

# 通过占位的形式，完成数字和字符串的拼接
name = "小紮"
age = 20
massage = "我的名字叫%s,今年%s"%(name,age)
print(massage)

# 用不同占位符进行拼接
name = "中华人民共和国"
age = 77
time = 1949.0
massage = "我的祖国名为%s,成立于%.1f,到2026年祖国已%d岁"%(name, time, age)
print(massage)

# 对以下数字进行精度控制
num1 = 520
num2 = 1949.10
print("数字520的宽度限制3，结果为：%6d"%num1)
print("数字1949.10小数精度2，结果为：%.2f"%num2)

# 字符串格式化方式：f"{}"
name = "小紮"
age = 20
time = 2006.6
print(f"我的名字叫{name},我出生于{time}年,今年{age}岁")

# 表达式对字符串进行格式化
print("2 * 2的结果为：%d"%(2 * 2))
print(f"2 * 3的结果为:{2 * 3}")
print("在python中的类型名为：%s"%type("小紮"))

# 练习：股价计算小程序
name = "zhizui播客"
stock_code = 876050
stock_price = 100
stock_price_daily_growth_factor = 1.5
growth_days = 9
price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司是{name},股票代码为{stock_code},当前股价为{100}")
print("每日增长系数为%.1f,经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,price))
