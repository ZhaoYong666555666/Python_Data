# 函数名：1. 名字最好能体现函数的功能，一般用小写字母和单下划线、数字等组合
#      2. 不可与内置函数重名（内置函数不需要定义即可直接使用）
def math(x):
    # 参数：根据函数功能，括号里可以有多个参数，也可以不带参数，命名规则与函数名相同
    # 规范：括号是英文括号，后面的冒号不能丢
    y = 3
    x + 5
    # 函数体：函数的执行过程，体现函数功能的语句，要缩进，一般是四个空格
    return y


# return语句：后面可以接多种数据类型，如果函数不需要返回值的话，可以省略

# 计算字符串的长度
# def my_len(words):
#     my_number = 0
#     for i in words:
#         print(i)
#         my_number = my_number + 1
#     return my_number
#
# a = my_len("三根皮带，四斤大豆")
# print(a)

# 计算利润率
def div(num1, num2):
    # 计算利润率
    gorw_number = (num1 - num2) / num2
    pecent = str((gorw_number * 100)) + "%"
    return pecent


def warning():
    print("Error:你确定你上个月利润为0")


def main():
    while True:
        num1 = int(input("请输入本月的利润："))
        num2 = int(input("请输入上个月的利润："))
        if num2 == 0:
            warning()
        else:
            print("本月的利润增长率是：" + div(num1, num2))
            break


main()

import math

f = 11.2
print(math.ceil(f))  # 向上取整
print(math.floor(f))  # 向下取整
print(round(f))  # 四舍五入


# 将计算时间和人力的函数合并自来
# 1代表计算人力，2代表计算时间
# type--1:工时   2:人力    size--项目大小     other--工时或者人力数
def choiceFn(type=1, size=1, other=None):
    # 通过type判断是计算人力还是计算时间
    if type == 1:
        number = math.ceil(size * 80 / other)
        print("项目大小为%.1f个的标准项目，如果需要在%.1f个工时完成，则需要人力为：%d人" % (size, other, number))
        print("----------------------------------------")
    else:
        time = math.ceil(size * 80 / other)
        print("项目大小为%.1f个的标准项目，如果安排人力%d人，则需要工时：%.1f个工时" % (size, other, time))
        print("----------------------------------------")


# 参数全部需要输入（类型，项目大小，工时或者人力）
# '请选择计算类型：（1-人力计算，2-工时计算）'
# '请输入项目大小：（1代表标准大小，可以输入小数）'
# '请输入人力数量：（请输入整数）'
# '请输入工时数量：（请输入小数）'
def inputChoiceFn():
    times = int(input("请您说一下一共有多少项目要做？："))
    while True:
        type = int(input("请选择计算类型(1代表计算人力，2代表计算工时)："))
        size = float(input("请输入项目大小(可以输入小数)："))
        # 根据输入的计算类型判断是输入人力还是工时
        if type == 1:
            other = math.ceil(float(input("请输入工时数量(请输入整数)：")))
        else:
            other = int(input("请输入人力数量(请输入整数)："))

        choiceFn(type, size, other)
        times -= 1
        if times <= 0:
            print("计算完毕")
            break


inputChoiceFn()

