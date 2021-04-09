import csv

# dir查看一个模块的所有变量，函数，类和方法
# for i in dir(csv):
#     # print(i)
#     print(1)

# with open("../csv/test1.csv", newline='') as f:
#     reader = csv.reader(f)
#     # 使用csv的reader()方法，创建一个reader对象
#     for row in reader:
#         # 遍历reader对象的每一行
#         print(row)

# 读取csv文件
with open("../csv/test2.csv", newline='') as f:
    reader = csv.reader(f)
    # 使用csv的reader()方法，创建一个reader对象
    for row in reader:
        # 遍历reader对象的每一行
        print(row)

# 向csv文件写入内容
# a代表追加写入文件
with open("../csv/test2.csv", "a", newline="") as f:
    # 实例化writer对象
    writer = csv.writer(f)
    # 调用“writer.writerow()”方法写入一行数据
    writer.writerow([1, 2, 3, 4, 5])

print("读取完毕！")
