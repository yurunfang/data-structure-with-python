INF = 0x3f3f3f3f  # 无穷大
max_size = 100




class Edge:
    def __init__(self, head, tail, lowcost):
        self.head = head  # 边的始点
        self.tail = tail  # 边的终点
        self.lowcost = lowcost  # 边上的权值


class AMGraph:
    def __init__(self):
        self.vexs = []  # 顶点表
        self.arcs = []  # 邻接矩阵
        self.vexnum = 0  # 图的当前点数
        self.arcnum = 0  # 图的当前边数

    def locate_vex(self, name):
        # 定位顶点在顶点数组中的下标
        for i in range(0, self.vexnum):
            if self.vexs[i] == name:
                return i

    def create_dn(self,n,m):
        # 采用邻接矩阵表示法，创建有向网
        self.vexnum = n  # 输入总顶点数
        self.arcnum = m  # 输入总边数
        cities = input().split()
        self.vexs = cities

        self.arcs = [[INF for i in range(self.vexnum)] for i in range(self.vexnum)]  # 初始化邻接矩阵，边的权值均置为无穷大
        for k in range(0, self.arcnum):  # 构造邻接矩阵
            v1, v2, w = input().split() # 输入一条边依附的顶点及权值
            i = self.locate_vex(v1)
            j = self.locate_vex(v2)  # 确定v1和v2在图中的位置，即顶点数组的下标
            self.arcs[i][j] = int(w)   # 边<v1,v2>的权值为w


def show_path(graph, begin, end,path):
    # 递归显示最短路径
    if path[end] != -1:
        show_path(graph, begin, path[end],path)
        print(graph.vexs[path[end]], end="-->")


def shortest_path_dij(graph, start, end):
    # 用Dijkstra算法求有向网G的v0顶点到其余顶点的最短路径
    n = graph.vexnum  # n为graph中顶点的个数
    dist = [0] * max_size
    s = [False] * max_size
    path = [-1] * max_size

    for v in range(n):  # n个顶点依次初始化
        s[v] = False  # S初始为空集
        dist[v] = graph.arcs[start][v]  # 将start到各个终点的最短路径长度初始化为弧上的权值
        if dist[v] < INF:
            path[v] = start  # 如果v0和v之间有弧，则将v的前驱置为v0
        else:
            path[v] = -1  # 如果v0和v之间无弧，则将v的前驱置为-1
    s[start] = True  # 将v0加入S
    dist[start] = 0  # 源点到源点的距离为0
    for i in range(1, n):  # 辅助数组，表示各顶点自成一个连通分量
        min = INF
        for w in range(n):
            if not s[w] and dist[w] < min:
                v = w
                min = dist[w]  # 选择一条当前的最短路径，终点为v
        s[v] = True  # 将v加入S
        if v == end:# 如果当前节点是终点，则提前结束
            return dist,path
        for w in range(n):  # 更新从start出发到集合V−S上所有顶点的最短路径长度
            if not s[w] and (dist[v] + graph.arcs[v][w] < dist[w]):
                dist[w] = dist[v] + graph.arcs[v][w]  # 更新dist[w]
                path[w] = v  # 更改w的前驱为v

    return 0,path


if __name__ == '__main__':

    while True:
        # 读取输入
        n, m = map(int, input().split())
        # 输入总顶点数、总边数
        if n == 0 and m == 0:
            break
        G = AMGraph()
        G.create_dn(n,m)
        #print("请输入起始点、终点名：")
        start, end = input().split()
        start_num = G.locate_vex(start)
        end_num = G.locate_vex(end)
        dist,path = shortest_path_dij(G, start_num, end_num)  # dijkstra算法求最短路径
        print(dist[end_num])
        #print("生成的最短路径为：")
        show_path(G, start_num, end_num,path)  # 输出最短路径
        print(end)
