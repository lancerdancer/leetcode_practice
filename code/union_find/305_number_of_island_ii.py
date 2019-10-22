"""
https://leetcode.com/problems/number-of-islands-ii/

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns
the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after
each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    """
    572 ms, faster than 71.19%
    """
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        self.father = {}
        self.island_num = 0
        grid = [[0] * n for _ in range(m)]
        output = []

        for x, y in positions:
            if grid[x][y] == 1:
                output.append(self.island_num)
                continue

            self.island_num += 1
            grid[x][y] = 1
            self.father[(x, y)] = (x, y)
            for dx, dy in DIRECTIONS:
                x1 = x + dx
                y1 = y + dy
                if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 1:
                    self.union((x1, y1), (x, y))

            output.append(self.island_num)

        return output

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_a] = root_b
            self.island_num -= 1

    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node