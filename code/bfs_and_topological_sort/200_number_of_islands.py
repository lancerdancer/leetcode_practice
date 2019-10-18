"""
https://leetcode.com/problems/number-of-islands/


Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""
from collections import deque
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    bfs solution
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        visited = set()
        islands = 0

        for x in range(m):
            for y in range(n):
                if self.is_island(grid, x, y, visited):
                    islands += 1
                    self.bfs(grid, x, y, visited)

        return islands



    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                if not self.is_island(grid, x+dx, y+dy, visited):
                    continue
                queue.append((x+dx, y+dy))
                visited.add((x+dx, y+dy))


    def is_island(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])
        return 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == '1'


class Solution1:
    """
    dfs solution
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        visited = set()
        islands = 0

        for x in range(m):
            for y in range(n):
                if self.is_island(grid, x, y, visited):
                    islands += 1
                    self.dfs(grid, x, y, visited)

        return islands



    def dfs(self, grid, x, y, visited):
        for dx, dy in DIRECTIONS:
            if not self.is_island(grid, x + dx, y + dy, visited):
                continue
            visited.add((x + dx, y + dy))
            self.dfs(grid, x + dx, y + dy, visited)


    def is_island(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])
        return 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == '1'

