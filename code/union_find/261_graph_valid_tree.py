"""
https://leetcode.com/problems/graph-valid-tree/

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0,1] is the same as [1,0] and thus will not appear together in edges.

"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        self.father = {i: i for i in range(n)}
        self.size = n

        for a, b in edges:
            self.union(a, b)

        return self.size == 1

    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root != b_root:
            self.father[a_root] = b_root
            self.size -= 1

    def find(self, node):
        path = []

        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
