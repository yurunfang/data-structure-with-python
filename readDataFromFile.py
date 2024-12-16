# 读取书籍信息的函数
class Book:			# 图书信息定义
    def __init__(self, book_id, title, price):
        self.no = book_id       # 图书ISBN
        self.name = title       # 图书名字
        self.price = price      # 图书价格
    def __repr__(self):  #重写 __repr__ 方法，以便在打印 Book 对象时能够以一种易读的格式显示其信息
        return f"{self.no} {self.name} {self.price:.2f}"

def read_books_from_file(filename):
    books = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # 跳过第一行
            next(file)
            for line in file:
                # 去除行尾的换行符，并按空格分割字符串
                line = line.strip().split()
                if len(line) == 3:
                    isbn, title, price = line
                    book = Book(isbn, title, price)
                    books.append(book)
                else:
                    print(f"格式错误: {line}")
    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
    return books


# 主程序
if __name__ == "__main__":
    filename = 'books.txt'  # 替换为你的txt文件名
    books = read_books_from_file(filename)

    # 打印读取的书籍信息
    for book in books:
        print(f"ISBN: {book.no}, 书名: {book.name}, 价格: {book.price}")
