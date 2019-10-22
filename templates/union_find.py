class UnionFind:
    def __init__(self, n):
        self.father = {i: i for i in range(n)}

    def union(self, a, b):
        self.father[self.find(a)] = self.find(b)

    def find(self, node):
        path = []

        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for n in path:  # 路径压缩
            self.father[n] = node

        return node

    def query(self, a, b):
        return self.find(a) == self.find(b)
