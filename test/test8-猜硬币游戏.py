import random

guess = ''
while guess not in [1, 0]:
    print('------猜硬币游戏------')
    print('猜一猜硬币是正面还是反面？')
    guess = input('请输入“正面”或“反面”：')
    if guess == "正面":
        guess = 1
        break
    elif guess == "反面":
        guess = 0
        break

# 随机抛硬币，0代表反面，1代表正面
toss = random.randint(0, 1)
print("toss = %s,guess = %s" % (toss, guess))
if toss == guess:
    print('猜对了！你真棒')
else:
    print('没猜对，你还有一次机会。')
    guess = input('再输一次“正面”或“反面”：')
    if guess == "正面":
        guess = 1
    else:
        guess = 0
    if toss == guess:
        print('你终于猜对了！')
    else:
        print('大失败！')
