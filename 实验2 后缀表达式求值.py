from array import array

max_size = 100


class SqStack:
    def __init__(self):
        # 初始化顺序栈
        self.elem = [None] * max_size  # 为顺序栈动态分配一个最大容量为max_size的数组空间
        self.top, self.base = 0, 0  # top和base都指向栈底元素在顺序栈中的位置，空栈
        self.stack_size = max_size  # stack_size置为栈的最大容量max_size

    def push(self, e):
        # 将元素压入栈
        if self.top - self.base == self.stack_size:  # 栈满
            raise Exception('栈空间已满')
        self.elem[self.top] = e  # 元素e压入栈顶,栈顶指针加1
        self.top += 1

    def pop(self):
        # 将栈顶元素弹出
        if self.top == self.base:
            raise Exception('栈已空')
        self.top -= 1  # 栈顶指针减1，并返回栈顶元素
        return self.elem[self.top]

    def get_top(self):
        # 返回栈顶元素
        if self.top != self.base:  # 栈非空
            return self.elem[self.top - 1]
        else:
            raise Exception('栈已空')

    def stack_empty(self):
        # 判断栈是否为空
        return self.top == self.base

    def __len__(self):
        # 栈的长度
        return self.top - self.base


def is_optr(c):
# 判断c是否为运算符
    return c in ['+', '-', '*', '/', '(', ')', '#']


def precede(theta1, theta2):
# 判断运算符优先级
    if (theta1 == '(' and theta2 == ')') or (theta1 == '#' and theta2 == '#'):
        return '='
    elif theta1 == '(' or theta1 == '#' or theta2 == '(' or ((theta1 == '+' or theta1 == '-') and (theta2 == '*' or theta2 == '/')):
        return '<'
    else:
        return '>'


def operate(a, theta, b):
#计算表达式 a treta b的结果
    if theta == '+':
        return a + b
    if theta == '-':
        return a - b
    if theta == '*':
        return a * b
    if theta == '/':
        return a / b

def infix_to_postfix(e):
# 将中缀表达式e的转化为后缀表达式，e以#结尾
    e="".join(e)
    postfix= ""  # 初始化Postfix字符串
    optr = SqStack()  # 初始化optr栈
    optr.push('#')  # 将表达式起始符“#”压入optr栈
    i = 0
    while e[i] != '#' or optr.get_top() != '#':
        if not is_optr(e[i]):  # 不是运算符则加入字符串
            postfix =postfix + e[i]
            i += 1
        else:
            if precede(optr.get_top(), e[i]) == '<':  # 比较optr的栈顶元素和e[i]的优先级
                optr.push(e[i])  # 当前字符e[i]压入OPTR栈
                i += 1  # 下标指向下一字符
                continue
            if precede(optr.get_top(), e[i]) == '>':
                theta = optr.pop()  # 弹出optr栈顶的运算符
                postfix =postfix + theta#将运算符加入Pistfix
                continue
            if precede(optr.get_top(), e[i]) == '=':  # optr的栈顶元素是“(”且e[i]是“)”
                optr.pop()  # 弹出optr栈顶的“(”
                i += 1  # 下标指向下一字符
                continue
    return postfix  # Postfix即为后缀表达式

def evaluate_expression(e):
# 求后缀表达式e的值，e以#结尾
    opnd = SqStack()  # 初始化opnd栈
    i = 0
    while i<len(e):
        if not is_optr(e[i]):  # 不是运算符则进opnd栈
            opnd.push(int(e[i]))
            i += 1
        else:
            b, a = opnd.pop(), opnd.pop()  # 弹出opnd栈顶的两个运算数
            opnd.push(operate(a, e[i], b))  # 将运算结果压入opnd栈
            i += 1  # 下标指向下一字符
            continue
    return opnd.get_top()  # opnd栈顶元素即为表达式求值结果



if __name__ == "__main__":
    print("请输入需要转换和求解的中缀表达式，多个表达式请换行，最后以=结束：")
    while True:
        expression = input().split()
        if expression[0] == '=' :
            break
        Postfix = infix_to_postfix(expression)
        print(Postfix)
        print(evaluate_expression(Postfix))
