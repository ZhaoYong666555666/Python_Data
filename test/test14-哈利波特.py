file = open("txt\\halibote.txt", "r", encoding="utf-8")
# 读取到的是一个数组
file_lines = file.readlines()
file.close()
# 将算出来的总分和平均分放在一个列表里面
final_scores = []
for i in file_lines:
    # 将遍历完的数组拆分成单个数组
    data = i.split()
    # 每个学员
    data_name = data[0]
    # 每个学员的所有成绩
    data_number = data[1:]
    # 总分数
    data_sum = 0
    # 将所有成绩加起来算平均分
    for num in data_number:
        data_sum += int(num)
    print("%s的总分为%d，平均分为%.2f" % (data_name, data_sum, data_sum / len(data_number)))

    result = "\n %s总分%d,平均分%.2f \n" % (data_name, data_sum, data_sum / len(data_number))
    final_scores.append(result)
print(final_scores)
# 读取文件，将算完的总分平均分写入文件
# 方法一
# write_file = open("txt\\halibote_sum.txt", "a", encoding="utf-8")
# write_file.write(str("\n".join(final_scores)))
# write_file.close()

# 方法二
# write()写入的是字符串，writelines()写入的列表
write_file = open("txt\\halibote_sum.txt", "w", encoding="utf-8")
write_file.writelines(final_scores)
write_file.close()

# import random
# punches = ["石头", "剪刀", "布"]
# computer_choice = random.choice(punches)
# user_choice = ""
#
# def myinput():
#     while True:
#         # computer_choice = random.randint(punches)
#         user_choice = input("请玩家输入石头，剪刀，布：")
#         if user_choice not in punches:
#             print("输入有误")
#             continue
#         else:
#             print("电脑：%s" % computer_choice)
#             print("玩家：%s" % user_choice)
#             return user_choice
#
# def judge(input):
#     if input == computer_choice:
#         print("平局")
#     elif ((input == "石头" and computer_choice == "剪刀") or (input == "剪刀" and computer_choice == "布") or (
#             input == "布" and computer_choice == "石头")):
#         print("你赢了")
#     else:
#         print("你输了")
#
# def main():
#     input = myinput()
#     judge(input)
#
# main()
