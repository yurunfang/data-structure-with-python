
class Book:
    def __init__(self, isbn, title, price):
        self.book_id = isbn
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.book_id} {self.title} {self.price:.2f}"

class BookNode:
    def __init__(self, book_info=None):
        self.book = book_info  # 结点的数据域
        self.next = None  # 结点的指针域

    def __str__(self):
        return str(self.book)


class LinkList:
    def __init__(self):
        # 生成新结点作为头结点并初始化指针域和数据区域为None，头指针head指向头节点
        self.head = BookNode(None)
        self.size = 0

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p
            p = p.next

    def __str__(self):
        output = ''
        for idx, item in enumerate(self):
            output += '{arrow}{data}'.format(arrow=' --> ' if idx else '', data=item.data)
        return output

    def __len__(self):
        cnt = 0
        for p in self:
            cnt += 1
        return cnt - 1

    def get_size(self):
        return self.size


    # def create_list_h(self, l_data: list):
    #     # 前插法，根据l_data数据列表创建链表
    #     for data in l_data:
    #         p = BookNode(data)  # 生成新结点p，并将p结点的数据域赋值为data
    #         p.next = self.head.next  # 将新结点p插入到头结点之后
    #         self.size += 1
    #         self.head.next = p
    #
    # def create_list_r(self, l_data: list):
    #     # 后插法，根据l_data数据列表创建链表
    #     r = self.head  # 尾指针r指向头结点
    #     for data in l_data:
    #         p = BookNode(data)  # 生成新结点，并初始化p的数据域为data
    #         r.next = p  # 将新结点p插入尾结点r之后
    #         self.size += 1
    #         r = r.next  # r指向新的尾结点p

    ###边输入边创建
    def create_list_rear(self):
        # 后插法，键盘输入创建链表
        r = self.head  # 尾指针r指向头结点
        print("请输入图书信息（书号、书名、价格），每行输入一项，用空格分隔，输入0 0 0结束：")
        while True:
            book_id, title, price_str = input().split()
            if book_id == '0' and title == '0' and price_str == '0':
                return
            price = float(price_str)
            p = BookNode(Book(book_id, title, price))  # 生成新结点，并初始化p的数据域为data
            r.next = p  # 将新结点p插入尾结点r之后
            self.size += 1
            r = r.next  # r指向新的尾结点p




    def print_books(self):
        current = self.head
        while current.next:
            print(current.next.book)
            current = current.next

    def sort_by_price_desc(self):
        if self.size <= 1:
            return

            # Using bubble sort for simplicity (can be optimized with other sorting algorithms)
        for i in range(self.size - 1):
            current = self.head.next
            for j in range(self.size - 1 - i):
                if current.book.price < current.next.book.price:
                    # Swap books
                    current.book, current.next.book = current.next.book, current.book
                current = current.next

    def modify_prices(self):
        total_price = sum(p.book.price for p in self if p.book is not None)

        average_price = total_price / self.size

        for p in (p for p in self if p.book is not None):
            if p.book.price < average_price:
                p.book.price *= 1.20
            else:
                p.book.price *= 1.10
        return average_price

    def find_most_expensive_books(self):
        if self.size == 0:
            return []
        max_price = max(p.book.price for p in self if p.book is not None)

        return [p.book for p in self if p.book is not None and p.book.price == max_price]

    def find_by_title(self, titles):
        results = []
        for title in titles:
            found_books = []
            books_num = 0
            for p in (p for p in self if p.book is not None):
                if p.book.title == title:
                    found_books.append(p.book)
                    books_num+=1
            if found_books:
                results.append(books_num)
                results.extend(str(book) for book in found_books)
            else:
                results.append("抱歉，没有找到此书!")
        for result in results:
            print(result)



    def find_by_position(self, position):
        # 在带头结点的单链表中根据序号i获取元素的值
        for idx, item in enumerate(self):  # 遍历链表
            if idx == position:  # 当下标加1等于i时，返回该数据元素
                return item.book
       # raise Exception('抱歉，最佳位置上的图书不存在!')


    def list_insert(self, i, e):
        # 在带头结点的单链表中第i个位置插入值为e的新结点
        for idx, p in enumerate(self):  # 遍历链表
            if idx + 1 == i:
                s = BookNode(e)  # 生成新结点s并将s的数据域设置为e
                s.next = p.next  # 将结点s的指针域指向结点ai
                p.next = s  # 将结点p的指针域指向结点s
                self.size+=1
                return
        raise Exception('位置不合法')

    def insert_by_position(self, position, book):
        # 在带头结点的单链表中第position个位置插入值为book的新结点
        for idx, p in enumerate(self):  # 遍历链表
            if idx + 1 == position:
                s = BookNode(book)  # 生成新结点s并将s的数据域设置为book
                s.next = p.next  # 将结点s的指针域指向结点ai
                p.next = s  # 将结点p的指针域指向结点s
                self.size+=1
                return True,""
        return False, "抱歉，入库位置非法!"



    def delete_by_position(self, position):
        # 删除单链表中的第position个结点
        for idx, p in enumerate(self):  # 查找第position−1个结点，p指向该结点
            if idx + 1 == position and p.next is not None:
                p.next = p.next.next  # 改变删除结点前驱结点的指针域
                self.size -= 1
                return True,""
        return False, "抱歉，出库位置非法!"


#
# def input_book_info():
#     book_info = list()
#     while True:
#         book_id, title, price_str = input().split()
#         if book_id == '0' and title == '0' and price_str == '0':
#             return book_info
#         price = float(price_str)
#         book = Book(book_id, title, price)
#         book_info.append(book)

if __name__ == "__main__":
    book_list = LinkList()
    # 1. Create and output book list
    #book_info = input_book_info()
    book_list.create_list_rear()
    print(book_list.get_size())
    book_list.print_books()
    print()

    # 2. Sort by price descending
    print("2.图书按价格排序显示如下：")
    book_list.sort_by_price_desc()
    book_list.print_books()
    print()

    # 3. Modify prices
    print("3.修改图书价格如下：")
    average_price=book_list.modify_prices()
    print(f"{average_price:.2f}")
    book_list.print_books()
    print()

    # 4. Find most expensive books
    print("4.输出最贵的书如下：")
    most_expensive_books = book_list.find_most_expensive_books()
    print(len(most_expensive_books))
    for book in most_expensive_books:
        print(book)
    print()

    # 5. 根据书名查找图书并输出
    titles_to_find = []
    print("5.根据图书名字查找如下：")
    num_searches = int(input("请输入要查找次数："))
    for _ in range(num_searches):
        titles_to_find.append(input("请输入要查找的书名："))
    book_list.find_by_title(titles_to_find)
    print()

    # 6. 根据位置查找图书并输出
    print("6.根据图书位置查找如下：")
    num_searches = int(input("请输入查找次数："))
    count = 0
    books = []
    while count < num_searches:
        positions_to_find = int(float(input("请输入要查找的位置（从1开始）: ")))
        book = book_list.find_by_position(positions_to_find)
        if book:
            books.append(book)
        else:
            books.append("抱歉，最佳位置上的图书不存在!")
        count += 1
    for book in books:
        print(book)
    print()

    # 7. Insert new book
    print("7.将图书插入指定位置如下：")
    position_to_insert = int(input("请输入新图书的入库位置（从1开始）： "))
    book_id, title, price_str = input("请输入新图书的信息（书号、书名、价格），用空格分隔：").split()
    price = float(price_str)
    new_book = Book(book_id, title, price)
    success, message = book_list.insert_by_position(position_to_insert, new_book)
    if success:
        print(book_list.get_size())
        book_list.print_books()
    else:
        print(message)
    print()

    # 8. Delete book by position
    print("8.删除指定位置图书如下：")
    position_to_delete = int(input("请输入旧图书的出库位置（从1开始）: "))
    success, message = book_list.delete_by_position(position_to_delete)
    if success:
        book_list.print_books()
    else:
        print(message)
