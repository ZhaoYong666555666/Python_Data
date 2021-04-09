import random

times = 0
computer_win_number = 0
user_win_number = 0
while True:
    punches = ['石头', '剪刀', '布']
    computer_choice = random.choice(punches)
    user_choice = input("请输出你猜拳的类型（石头，剪刀，布）：")
    if user_choice == "石头" or user_choice == "剪刀" or user_choice == "布":
        # 平局情况
        if user_choice == computer_choice:
            print("平局，继续出拳")
            print("-----------------------")
        # 玩家赢的所有情况
        elif ((user_choice == "石头" and computer_choice == "剪刀") or (user_choice == "剪刀" and computer_choice == "布") or (
                user_choice == "布" and computer_choice == "石头")):
            print("你赢了，电脑输了！！！")
            user_win_number += 1
        # 剩余的就是电脑赢
        else:
            print("你输了，电脑赢了！！！")
            computer_win_number += 1
        times += 1
        if times == 5:
            if user_win_number > computer_win_number:
                print("五次猜拳，你赢了")
            else:
                print("五次猜拳，你输了")
            break
    else:
        print("输入有误，请重新出拳!!!!!!!!!!!!!!")
        print("-----------------------")
