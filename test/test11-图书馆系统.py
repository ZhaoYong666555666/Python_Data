class Book:
    # 对实例属性进行初始化
    # bookName      书名
    # bookAuthor    作者
    # bookComment   推荐语
    # bookState     借阅状态   0-未借阅    1-已借阅  默认值为 0
    # 初始化
    def __init__(self, bookName, bookAuthor, bookComment, bookState=0):
        self.bookName = bookName
        self.bookAuthor = bookAuthor
        self.bookComment = bookComment
        self.bookState = bookState

    # 显示每本书的描述
    # def show_book_info(self):
    #     if self.bookState == 0:
    #         status = "未借阅"
    #     else:
    #         status = "已借阅"
    #     return "书名：《%s》 \n作者：%s \n推荐语：%s \n状态：%s" % (self.bookName, self.bookAuthor, self.bookComment, status)

    # 创建的实例，输出的这个实例就是它，其功能也是现实每本书籍的信息
    def __str__(self):
        if self.bookState == 0:
            status = "未借阅"
        else:
            status = "已借阅"
        return "------------------------------------\n书名：《%s》 \n作者：%s \n推荐语：%s \n借阅状态：%s" % (
            self.bookName, self.bookAuthor, self.bookComment, status)


class BookManager:
    # 创建一个列表，列表里每个元素都是Book类的一个实例
    books = []

    def __init__(self):
        # 创建三个实例
        book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)

        # 往列表依次添加元素，注意调用类属性books时，self不能丢
        # self.books = [book1, book2, book3]
        # 上面三行代码，可简化为一行，即直接创建列表。这种情况下，可不用在前面创建空列表。
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    # 显示选择菜单，根据不同的选项调用不同的方法
    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            # print("1、查阅所有书籍  2、添加书籍  3、借阅书籍  4、归还书籍  5、退出系统")
            print("*************************************************************")
            choice = int(input("1.查询所有书籍 \n2.添加书籍 \n3.借阅书籍 \n4.归还书籍 \n5.退出系统 \n \n请输入数字选择对应的功能："))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_bool()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            else:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
                break

    # 显示选择菜单，根据不同的选项调用不同的方法
    def show_all_book(self):
        print("所有图书信息如下，请查阅：")
        for book in self.books:
            # self是实例对象的替身
            print(book)

    # 添加书籍
    def add_bool(self):
        bookName = input("请输入书籍名称：")
        bookAuthor = input("请输入书籍作者：")
        bookComment = input("请输入书籍推荐语：")
        book = Book(bookName, bookAuthor, bookComment)
        self.books.append(book)
        print("书籍录入成功")

    # 借阅图书和归还图书，查询图书的公共方法
    def check_book(self, name):
        for book in self.books:
            # 遍历列表的每个元素，即每个Book实例
            if book.bookName == name:
                # 如果存在有实例名称与输入书籍名称是一样的
                return book
                # 返回该实例对象，遇到return语句方法停止执行
        else:
            # 若for循环中，没有返回满足条件的对象，则执行else子句
            return None
            # 返回None值

    # 借阅书籍
    def lend_book(self):
        lend_book_name = input("请输入你要借阅的书籍名称：")

        # 将name作为参数调用check_book方法，并将返回值赋值给变量res
        result = self.check_book(lend_book_name)
        # 如果返回值不等于None值，即返回的是实例对象
        if result != None:
            if result.bookState == 1:
                print("真不好意思，您来晚一步，这本书已经被借走了")
            else:
                print("书籍《%s》已被您借阅成功，记得看哦！！" % lend_book_name)
                result.bookState = 1

        else:
            print("对不起，您要借的这本书压根不在图书系统里面")

        # 遍历列表，此时books有三个元素，即book1,book2,book3三个实例
        # for book in self.books:
        #     # 如果列表中有实例的属性name和输入的书籍名称相等
        #     if lend_book_name == book.bookName:
        #         if book.bookState == 1:
        #             print("真不好意思，您来晚一步，这本书已经被借走了")
        #             break
        #         else:
        #             print("书籍《%s》已被您借阅成功，记得看哦！！" % lend_book_name)
        #             book.bookState = 1
        #             break
        #     else:
        #         continue
        # else:
        #     print("对不起，您要借的这本书压根不在图书系统里面")

    # 归还书籍
    def return_book(self):
        print("归还书籍")
        return_book_name = input("请输入你要归还的书籍名称：")
        # 将name作为参数调用check_book方法，并将返回值赋值给变量res
        result = self.check_book(return_book_name)
        if result != None:
            if result.bookState == 1:
                result.bookState = 0
                print("书籍《%s》归还成功！" % return_book_name)
            else:
                print("不好意思啊，这本书压根就没借出去，不用还")
        else:
            print("您从哪弄的书，这就不是咱们图书馆的书籍")


book = Book("看不见的城市", "卡尔维诺", "献给城市的最后一首爱情诗")
# print(book.bookAuthor)
# print(book.show_book_info())
# print(book)

# 图书管理

bookManager = BookManager()
bookManager.menu()
