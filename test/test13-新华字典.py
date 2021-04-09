# 字符进行编码，通过encode方法
print('吴枫'.encode('utf-8'))
print('吴枫'.encode('gbk'))

# 字符进行解码，通过decode方法
print(b'\xe5\x90\xb4\xe6\x9e\xab'.decode('utf-8'))
print(b'\xce\xe2\xb7\xe3'.decode('gbk'))

# 读取文件
# 参数一：文件路径（绝对路径和相对路径）
# 参数二：表示 read，表示我们以读的模式打开了这个文件
# file = open("E:\ZYownStudy\风变编程资源\\test\\txt\\abc.txt", "r", encoding="utf-8")
file = open("txt\\abc.txt", "r", encoding="utf-8")
file_content = file.read()
print(file_content)
file.close()
# 为啥要关闭文件呢？原因有两个：
# 1.计算机能够打开的文件数量是有限制的，
# --open()过多而不close()的话，就不能再打开文件了。
# 2.能保证写入的内容已经在文件里被保存好了。


# 写文件
# w---这种写入方式会暴力清除之前的内容
# a---这种写入方式，是在文件后面追加，即append
file_w = open("txt\\abc.txt", "a", encoding="utf-8")
file_w.write("\n作者：李白")
file_w.write("\n字号：太白")
file_w.write("\n年代：唐朝")
file_w.close()
