# for i in range(1, 3):
#     index = i
#     chengji = index * 2
#     print(("%s × 2 = %s" % (index, chengji)), end="  ")
#
# print("\n")
#
# for i in range(1, 4):
#     index = i
#     chengji = index * 3
#     print(("%s × 2 = %s" % (index, chengji)), end="  ")
#
# print("\n")
#
# for i in range(1, 4):
#     index = i
#     chengji = index * 3
#     print("%d × 3 = %d" % (index, chengji), end="  ")

# 九九乘法表最终版
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d × %d = %d" % (j, i, i * j), end="   ")
    print("")

print("\n")

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d X %d = %d' % (j, i, i * j), end='  ')
        j += 1
    print('')
    i += 1
