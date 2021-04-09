import random

a = random.random()  # 随机从0-1之间抽取一个小数
print(a)

a = random.randint(0, 100)  # 随机从0-100之间抽取一个数字
print(a)

a = random.choice('abcdefg')  # 随机从字符串/列表/字典等对象中抽取一个元素（可能会重复）
print(a)

a = random.sample('abcdefg', 3)  # 随机从字符串/列表/字典等对象中抽取多个不重复的元素
print(a)

# seed--生成的随机数都是一样的
random.seed(100000)
print(random.random())
random.seed(100000)
print(random.random())
random.seed(100000)
print(random.random())

items = [1, 2, 3, 4, 5, 6]  # “随机洗牌”，比如打乱列表
random.shuffle(items)
print(items)
print("********")
print(dir(random))

class Temple:
    name = "老和尚"

    def do(self):
        print(self.name + "总爱讲故事")
