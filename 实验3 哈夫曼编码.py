import collections

INF = 0x3f3f3f3f


class HuffmanNode:
    def __init__(self, char,weight, parent, lchild, rchild):
        self.char = char # 结点的字符
        self.weight = weight  # 结点的权值
        self.parent = parent  # 结点的双亲
        self.lchild = lchild  # 结点的左孩子的下标
        self.rchild = rchild  # 结点的右孩子的下标


class HuffmanTree:
    def __init__(self,str, n, weights):
        self.n = n  # 哈夫曼树的全部叶子结点个数
        self.ht = [HuffmanNode('', 0, 0, 0,0) for i in range(0, 2 * n)]  # 0号单元未用，所以需要动态分配2*n个单元
        self.hc = [' ' for i in range(0, self.n + 1)]  # 分配存储n个字符编码的编码表空间
        self.code_map= {}  # 哈夫曼编码字典表
        for i in range(1, n + 1):  # 初始化前n个单元中叶子结点的权值
            self.ht[i].char = str[i-1]
            self.ht[i].weight = weights[i - 1]

    def select(self, len):
        # 选择两个其双亲域为0且权值最小的结点
        min = INF  # 初始化最小值为无穷大
        s1 = 0  # 记录第一个权值最小结点下标
        s2 = 0  # 记录第一个权值最小结点下标
        for i in range(1, len + 1):  # 从1至i-1中个结点中顺序查找出权值最小的结点
            if self.ht[i].weight < min and self.ht[i].parent == 0:  # 找到最小权值
                min = self.ht[i].weight  # 更新min的大小
                s1 = i  # 更新s1的值
        temp = self.ht[s1].weight  # 将原值存放起来，然后先赋予最大值，防止s1被重复选择
        self.ht[s1].weight = INF
        min = INF
        for i in range(1, len + 1):  # 从1至i-1中个结点中顺序查找出权值最小的结点
            if self.ht[i].weight < min and self.ht[i].parent == 0:  # 找到最小权值
                min = self.ht[i].weight  # 更新min的大小
                s2 = i  # 更新s2的值
        self.ht[s1].weight = temp  # 恢复原来的值
        return s1, s2

    def create_huffmantree(self):
        # 构造哈夫曼树
        if self.n <= 1:
            return
        m = 2 * self.n - 1

        for i in range(self.n + 1, m + 1):  # 通过n-1次的选择、删除、合并来创建哈夫曼树
            s_1, s_2 = self.select(i - 1)  # 在ht[k](1≤k≤i-1)中选择两个其双亲域为0且权值最小的结点,并返回它们在ht中的序号s1和s2
            self.ht[s_1].parent = i
            self.ht[s_2].parent = i  # 得到新结点i，从森林中删除s_1，s_2，将s_1和s_2的双亲域由0改为i
            self.ht[i].lchild = s_1
            self.ht[i].rchild = s_2  # s_1,s_2分别作为i的左右孩子
            self.ht[i].weight = self.ht[s_1].weight + self.ht[s_2].weight  # i 的权值为左右孩子权值之和

    def create_huffmancode(self):
        # 从叶子到根逆向求每个字符的哈夫曼编码，存储在编码表hc中
        cd = [' ' for i in range(0, self.n - 1)]  # 分配临时存放每个字符编码的动态数组空间
        for i in range(1, self.n + 1):  # 逐个字符求哈夫曼编码
            start = self.n - 1  # start开始时指向最后，即编码结束符位置
            c = i
            f = self.ht[i].parent  # f指向结点c的双亲结点
            while f != 0:
                start -= 1  # 回溯一次start向前指一个位置
                if self.ht[f].lchild == c:
                    cd[start] = '0'  # 结点c是f的左孩子，则生成代码0
                else:
                    cd[start] = '1'  # 结点c是f的右孩子，则生成代码1
                c = f
                f = self.ht[f].parent  # 继续向上回溯
            self.hc[i] = ''.join(cd[start:])  # 为第i个字符编码分配空间
            #测试用
            #print(self.hc[i])

    def print_huffmantree(self):
        # 输出哈夫曼树状态表
        print("结点i  weight  parent  lchild  rchild")
        for i in range(1, 2 * self.n):
            print(" {0}      {1}        {2}       {3}       {4}".format(i, self.ht[i].weight, self.ht[i].parent,
                                                                        self.ht[i].lchild, self.ht[i].rchild))

    def build_codes(self):
        # 创建哈夫曼编码
        self.code_map = {}
        # 添加键值对
        for i in range(1, self.n + 1):
            self.code_map[self.ht[i].char] = self.hc[i]


    def print_haffmancode(self):
        # 输出哈夫曼编码
        haffman_code = " ".join(f"{key}:{value}" for key, value in self.code_map.items())
        print(haffman_code)

    def encode_string(self,str):
         # 输入文件进行编码
        encoded = ''.join(self.code_map[char] for char in str)
        return encoded

    def decode_string(self, encoded, root):
        decoded = ''
        current_node = root
        for bit in encoded:
            if bit == '0':
                index = current_node.lchild
                current_node = self.ht[index]
            else:
                index = current_node.rchild
                current_node = self.ht[index]
            if current_node.char:
                decoded += current_node.char
                current_node = root
        return decoded


if __name__ == "__main__":
    while True:
        input_str = input().strip()
        if input_str == "0":
            break

        freq_map = collections.Counter(input_str)

        ht = HuffmanTree(list(freq_map.keys()),len(freq_map), list(freq_map.values()))
        # Print frequencies
        print(' '.join(f"{char}:{freq}" for char, freq in sorted(freq_map.items())))

        # Build Huffman Tree
        ht.create_huffmantree()
        ht.print_huffmantree()
        huffman_tree_root = ht.ht[2*ht.n-1]

        # Build Huffman Codes
        ht.create_huffmancode()  # 求哈夫曼编码
        ht.build_codes()
        ht.print_haffmancode()


        # Encode the string
        encoded_str = ht.encode_string(input_str)

        # Decode the string
        decoded_str = ht.decode_string(encoded_str, huffman_tree_root)

        # Print encoded and decoded strings
        print(encoded_str)
        print(decoded_str)
        print()  # Add an empty line for better readability between sets of output



