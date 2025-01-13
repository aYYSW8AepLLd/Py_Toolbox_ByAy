import time
import random
import sys

# 生成一个1到100之间的随机整数
pin = random.randint(1, 100)
    
# 今日人品显示
def renpin():
    print("今日人品:", pin)

# 计算
def basic_calc(fangfa, a, b):
    if fangfa == "+":
        jieguo = a + b
    elif fangfa == "-":
        jieguo = a - b
    elif fangfa == "*":
        jieguo = a * b
    elif fangfa == "/":
        if b == 0:
            print("除数不能为0")
            return
        jieguo = a / b
    elif fangfa == "mod":
        if b == 0:
            print("除数不能为0")
            return
        jieguo = a % b
    else:
        print("尚未开发")
        return

    print(f"{a} {fangfa} {b} = {jieguo}")

# 计时器
def time1(t):
    print(f"开始计时 {t} 秒")
    time.sleep(t)
    print("计时结束！")

#猜数字
def guess_number():
    jieguo = random.randint(1,100)
    cishu = 0
    print("欢迎来到猜数字游戏，范围是1~100，输入exit退出")
    while True:
        a = input("请输入数字，输入exit退出:")
        if a == "exit":
            break
        else:
            try:
                a = int(a)
                if a > jieguo:
                    print("大了")
                    cishu += 1
                elif a < jieguo:
                    print("小了")
                    cishu += 1
                else:
                    cishu += 1
                    print(f"通关，你用了{cishu}次")
                    break
                continue
            except ValueError:
                print("报错！你输入的不是正常数字，请重新输入。")
                continue

#鸡兔同笼
def solve_chicken_rabbit(heads, feet):
    for x in range(heads + 1):  # 鸡的数量从0到heads
        y = heads - x  # 兔的数量
        if 2 * x + 4 * y == feet:
            return x, y
    return None, None

# 输入转换函数
def input_number(prompt):
    while True:
        value = input(prompt)
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            print("报错！你输入的不是正常数字，请重新输入。")

# 工具选择
def tools(tool):
    if tool == 0:
        sys.exit()
    elif tool == 1:
        renpin()
    elif tool == 2:
        fangfa = input("请输入计算方法（加法输入+，减法输入-，乘法输入*，除法输入/，取模输入mod）: ")
        a = input_number("请输入数字1: ")
        b = input_number("请输入数字2: ")
        basic_calc(fangfa, a, b)
    elif tool == 3:
        t = input_number("你要计时几秒？: ")
        time1(t)
    elif tool == 4:
        guess_number()
    elif tool == 5:
        head = input("请输入一共有多少头:")
        feet = input("请输入一共有多少腿:")
        try:
            head = int(head)
            feet = int(feet)
            chickens, rabbits = solve_chicken_rabbit(head, feet)
            if chickens is not None:
                print(f"鸡有{chickens}只，兔有{rabbits}只")
            else:
                print("无解")
        except ValueError:
            print("报错！你输入的不是正常数字，请重新输入。")
    else:
        print("尚未开发")

print('欢迎使用Python工具箱Alpha3!')
print('温馨提示：本软件适用于看得懂人话的人类')

while True:
    try:
        tool = int(input("请选择 0.退出软件 1.今日人品 2.计算器 3.计时器 4.猜数字 5.计算鸡兔同笼: "))
        tools(tool)
    except ValueError:
        print("你输入的不是数字，请重新输入。")
