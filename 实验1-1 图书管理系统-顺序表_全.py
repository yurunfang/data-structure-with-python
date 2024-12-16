class Book:
    def __init__(self, book_id, title, price):
        self.book_id = book_id
        self.title = title
        self.price = price

    def __repr__(self):
        return f"{self.book_id} {self.title} {self.price:.2f}"

#基本操作
class BookList:
    def __init__(self):
        self.books = []

    def create_book_list(self):
        print("请输入图书信息（书号、书名、价格），每行输入一项，用空格分隔，输入0 0 0结束：")
        while True:
            book_id, title, price_str = input().split()
            if book_id == '0' and title == '0' and price_str == '0':
                break
            price = float(price_str)
            self.books.append(Book(book_id, title, price))

    def display_book_list(self):
        print(len(self.books))
        for book in self.books:
            print(book)

    def sort_book_list_by_price_desc(self):
        self.books.sort(key=lambda x: x.price, reverse=True)
        for book in self.books:
            print(book)

    def update_book_prices(self):
        avg_price = sum(book.price for book in self.books) / len(self.books)
        for book in self.books:
            if book.price < avg_price:
                book.price *= 1.20
            else:
                book.price *= 1.10
        print(f"{avg_price:.2f}")
        for book in self.books:
            print(book)

    def find_most_expensive_book(self):
        if not self.books:
            return "书库为空，无法查找。"
        max_price = max(book.price for book in self.books)
        expensive_books = [book for book in self.books if book.price == max_price]
        print(len(expensive_books))
        for book in expensive_books:
            print(book)

    def find_book_by_title(self, titles):
        results = []
        for title in titles:
            found_books = [book for book in self.books if book.title == title]
            if found_books:
                results.append(len(found_books))
                results.extend(str(book) for book in found_books)
            else:
                results.append("抱歉，没有找到此书!")
        for result in results:
            print(result)

    def find_book_by_position(self, positions):
        results = []
        for pos in positions:
            if 1 <= pos <= len(self.books):
                 book = self.books[pos - 1]
                 results.append(str(book))
            else:
                results.append("抱歉，最佳位置上的图书不存在!")
        for result in results:
            print(result)

    def add_book(self, position, book_id, title, price):
        if 1 <= position <= len(self.books) + 1:
            new_book = Book(book_id, title, float(price))
            self.books.insert(position - 1, new_book)
            self.display_book_list()
        else:
            print("抱歉，入库位置非法!")

    def remove_book(self, position):
        if 1 <= position <= len(self.books):
            self.books.pop(position - 1)
            self.display_book_list()
        else:
            print("抱歉，出库位置非法!")


def main():
    book_list = BookList()

    # 1. 创建图书信息表并输出
    book_list.create_book_list()
    book_list.display_book_list()
    print()

    # 2. 按价格降序排序图书信息表并输出
    book_list.sort_book_list_by_price_desc()
    print()

    # 3. 修改图书价格并输出
    book_list.update_book_prices()
    print()

    # 4. 查找最贵图书并输出
    book_list.find_most_expensive_book()
    print()

    # 5. 根据书名查找图书并输出
    titles_to_search = []
    num_searches = int(input("请输入要查找书名的次数："))
    for _ in range(num_searches):
        titles_to_search.append(input("请输入要查找的书名："))
    book_list.find_book_by_title(titles_to_search)
    print()

    # 6. 根据位置查找图书并输出
    positions_to_search = []
    num_searches = int(input("请输入要查找位置的次数："))
    for _ in range(num_searches):
        positions_to_search.append(int(input("请输入要查找的位置（从1开始）：")))
    book_list.find_book_by_position(positions_to_search)
    print()

    # 7. 新图书入库并输出
    position = int(input("请输入新图书的入库位置（从1开始）："))
    book_id, title, price = input("请输入新图书的信息（书号、书名、价格），用空格分隔：").split()
    book_list.add_book(position, book_id, title, price)
    print()

    # 8. 旧图书出库并输出
    position = int(input("请输入旧图书的出库位置（从1开始）："))
    book_list.remove_book(position)


if __name__ == "__main__":
    main()