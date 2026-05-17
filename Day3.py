# 数据类型的转换
# 将数字类型转换成字符串
num_str = str(10)
print(type(num_str), num_str)
num1_str = str(10.5)
print(type(num1_str), num1_str)
# 将字符串转换成数字
num1 = int("10")
print(type(num1), num1)
num2 = float("10.34")
print(type(num2), num2)
# 整数转换成浮点数
num_float = float(10)
print(type(num_float), num_float)
# 浮点数转换成整数
num_int = int(10.6)
print(type(num_int), num_int)



# type()的使用方式
# 方式1：使用print直接输出类型信息
print(type("海苔锅巴"))
print(type(123))
print(type(12.3))
# 方式2：使用变量存储type（）语句的结果
str_type = type("海苔锅巴")
float_type = type(123.0)
int_type = type(123)
print(str_type)
print(float_type)
print(int_type)
# 方式3：使用type（）语句，查看变量中存储的数据类型信息
name_type = "huawei"
print(name_type)





# 变量
# 钱包一共有50块钱
money = 50
print("当前钱包数额：", money, "元")
# 花十块钱买一根雪糕
money1 = 10
print("购买了冰淇淋，花费：", money, "元")
# 花5块钱买一瓶可乐
money2 = 5
print("购买了可乐，花费：", money, "元")
# 购买完雪糕和可乐后钱包余额
money = money - money1 - money2
print("最终，钱包剩余：", money, "元")