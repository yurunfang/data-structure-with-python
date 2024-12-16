
#step 1：将伪代码改为计算机可执行的语句
class Book:			# 图书信息定义
    def __init__(self, book_id, title, price):
        self.no = book_id       # 图书ISBN
        self.name = title       # 图书名字
        self.price = price      # 图书价格
    def __repr__(self):  #重写 __repr__ 方法，以便在打印 Book 对象时能够以一种易读的格式显示其信息
        return f"{self.no} {self.name} {self.price:.2f}"

class SqList:
    def __init__(self, max_size):
        self.max_size = max_size  # 存储最大容量
        self.books = [None] * max_size  # 初始化一个固定大小的列表，所有元素初始化为None
        self.length = 0  # 空表长度为0


    def list_insert(self, i, e):
        # 在顺序表中第i个位置插入新的元素e，i值的合法范围是1≤i≤self.length+1

        if i > len(self.books):  # 存储空间已满
            print("空间已满!")
            return False

        if i < 1 or i > self.length + 1:
            #raise Exception('位置不合法')
            print("抱歉，入库位置非法!")
            return False

        for idx in range(self.length - 1, i - 2, -1):
            self.books[idx + 1] = self.books[idx]  # 插入位置及之后的元素后移
        self.books[i - 1] = e  # 将新元素e放入第i个位置
        self.length += 1  # 表长加1
        return True

        # 显示图书信息表中的图书

    def display_book_list(self):
        print(self.length)
        for book in self.books[:self.length]:
            print(book)

    #查找顺序表中首个值为e的数据元素，返回其序号
    def locate_elem(self, e):
        # 在顺序表中查找值为e的数据元素，返回其序号
        for i, elem in enumerate(self.books[:self.length]):
            if elem == e:
                return i + 1  # 查找成功，返回序号i+1
        raise Exception('元素不存在')

    #########修改
    def locate_books_by_title(self, title):
        # 在顺序表中查找所有值为e的数据元素，返回它们的信息列表
        found_books = [] # 用于存储所有匹配元素的信息
        for book in self.books[:self.length]:
            if book and book.name == title:  # 检查book是否为None
                found_books.append(book)
        return found_books


    def list_delete(self, i):
        # 删除顺序表中第i个元素
        if i < 1 or i > self.length:
            print('抱歉，出库位置非法!')
            return False
        for idx in range(i, self.length):
            self.books[idx - 1] = self.books[idx]  # 被删除元素之后的元素前移
        self.length -= 1  # 表长减1
        return True

    def clear_list(self):
        self.length = 0

    def list_empty(self):
        return self.length == 0

    def get_elem(self, i):
        # 返回顺序表self中的第i个元素
        if 1 <= i <= self.length:
            return self.books[i - 1]
        raise Exception('位置不合法')

    def __len__(self):
        return self.length

    def __str__(self):
       # 定制输出格式
        return '\n'.join(str(book) for book in self.books[:self.length])




if __name__ == "__main__":
    book_list = SqList(100)

    # 基于顺序存储的图书信息表的创建
    print("请输入图书信息（书号、书名、价格），每行输入一项，用空格分隔，输入0 0 0结束：")
    i=0
    while True:
          book_id, title, price_str = input().split()
          if book_id == '0' and title == '0' and price_str == '0':
             break
          i+=1
          price = float(price_str)
          book_list.list_insert(i,Book(book_id, title, price))
    book_list.display_book_list()
    print()

    # 5. 根据书名查找图书并输出
    titles_search_results = []
    num_searches = int(input("请输入要查找书名的次数："))
    for _ in range(num_searches):
        found_books = book_list.locate_books_by_title(input("请输入要查找的书名："))
        if found_books:
            titles_search_results.append(len(found_books))
            titles_search_results.extend(str(book) for book in found_books)
        else:
            titles_search_results.append("抱歉，没有找到此书!")
    for result in titles_search_results:
        print(result)
    print()


    # 7. 新图书入库并输出
    position = int(input("请输入新图书的入库位置（从1开始）："))
    book_id, title, price = input("请输入新图书的信息（书号、书名、价格），用空格分隔：").split()
    result = book_list.list_insert(position,Book(book_id, title, float(price)))
    if result:
       book_list.display_book_list()
    print()

    # 8. 旧图书出库并输出
    position = int(input("请输入旧图书的出库位置（从1开始）："))
    result = book_list.list_delete(position)
    if result:
       book_list.display_book_list()

