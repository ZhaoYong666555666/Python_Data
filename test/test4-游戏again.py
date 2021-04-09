# **********************玩家和敌人的战斗********************** #
# 分析游戏步骤
# 1、展示玩家的血量和战斗力，血量和战斗力都是随机的     random模块的randint()
# 2、展示敌人的血量和战斗力，血量和战斗力都是随机的     random模块的randint()
# 3、为了游戏的体验，加上延迟属性      time模块的sleep()函数
# 4、计算战斗后玩家和敌人的血量，谁的血量先到0谁就输了
# 5、才去三局两胜的比赛制度
# 6、是否在进行一局游戏，yes或者no
import random
import time

# 统计玩家和敌人赢的次数
play_win_number = 0
enemy_win_number = 0

# 是否继续游戏
again = True

while again:
    for i in range(3):
        time.sleep(2)
        print("——————游戏开始，第%d局开始——————" % (i + 1))
        time.sleep(2)
        # 玩家的血量和战斗力
        play_blood = random.randint(100, 150)
        play_attack = random.randint(30, 50)
        # 敌人的血量和战斗力
        enemy_blood = random.randint(100, 150)
        enemy_attack = random.randint(30, 50)
        print("【玩家】血量:%d\n" % play_blood)
        print("【玩家】战斗力:%d\n" % play_attack)
        print("—————————————————")
        time.sleep(1.5)
        print("【敌人】血量:%d\n" % enemy_blood)
        print("【敌人】战斗力:%d\n" % enemy_attack)
        print("—————————————————")

        # 计算战斗之后的血量，只要血量不为0，战斗都会一直持续下去
        while play_blood > 0 and enemy_blood > 0:
            play_blood = play_blood - enemy_attack
            enemy_blood = enemy_blood - play_attack
            print('玩家发起了攻击，【敌人】剩余血量%s' % enemy_blood)
            print('敌人向玩家发起了攻击，【玩家】的血量剩余%s' % play_blood)
            print('—————————————————')
            time.sleep(1.2)
        # 判断战斗之后谁赢了
        if play_blood > 0 and enemy_blood < 0:
            print("【玩家赢了】")
            play_win_number += 1
        elif play_blood < 0 and enemy_blood > 0:
            print("【敌人赢了】")
            enemy_win_number += 1
        else:
            print("不好意思哦，平局")

    # 根据三局两胜的制度判定谁输谁赢
    print("***\n***\n***\n***\n***\n***\n***\n***")
    if play_win_number > enemy_win_number:
        print("【最终结果---你赢了】")
    elif play_win_number < enemy_win_number:
        print("【最终结果---敌人赢了】")
    else:
        print("【最终结果---平局】")

    # 是否要再来一局
    isAgain = input("是否要继续再玩一局，yes或者no：")
    if isAgain == "yes":
        again = True
        print("游戏继续")
        time.sleep(2)
    else:
        again = False
        print("游戏结束")
