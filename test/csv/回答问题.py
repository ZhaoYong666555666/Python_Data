# while True:
#     Q1 = input("你的小学老师是谁：")
#     if Q1 == "李老师":
#         print("回答正确")
#         print("下一个问题")
#         break
#     else:
#         continue
#
# while True:
#     Q2 = input("你的妈妈是谁：")
#     if Q2 == "冉妈妈":
#         print("回答正确")
#         print("下一个问题")
#         break
#     else:
#         continue
#
# while True:
#     Q3 = input("你老家哪里的：")
#     if Q3 == "天津":
#         print("全部回答正确")
#         break
#     else:
#         continue


# def question(index):
#     if index == 0:
#         name = "你的小学老师是谁:"
#     elif index == 1:
#         name = "你的妈妈是谁:"
#     else:
#         name = "你老家哪里的:"
#     while True:
#         Q = input(name)
#         if Q == "李老师":
#             print("回答正确，继续回答第二个问题")
#             break
#         elif Q == "冉妈妈":
#             print("回答正确，继续回答第三个个问题")
#             break
#         elif Q == "天津":
#             print("全部回答正确")
#             break
#         else:
#             continue
#
#
# for i in range(3):
#     question(i)

# 怎么用python计算100以内所有奇数的和
# sum = 0
# for i in range(1, 101):
#     print(i)
#     if i % 2 != 0:
#         sum += i
# print(sum)

# num = 0
# sum = 0
# while True:
#     num += 1
#     if num % 2 != 0:
#         sum += num
#     if num > 99:
#         break
# print(sum)

# all_sum = 0
# odd_sum = 0
# for i in range(1, 101):
#     all_sum += i
#     if i % 2 == 0:
#         odd_sum += i
# print(all_sum - odd_sum)

# i = 1
# for i in range(3):
#     username = input("请输入用户名：")
#     password = input("去输入密码：")
#     if username != "abc" or password != 123:
#         print("输入有误")
#         continue
#     else:
#         print("登录成功")
#         break
#
# if i == 2:
#     print("三次机会用完，登录失败")

times = 0
while True:
    username = input("请输入用户名：")
    password = input("去输入密码：")
    if username != "abc" or password != 123:
        times += 1
        if times < 3:
            print("输入有误")
            continue
        else:
            print("3次机会已经用完")
            break
    else:
        print("登录成功")
        break
