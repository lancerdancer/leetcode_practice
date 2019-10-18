"""
https://leetcode.com/problems/course-schedule/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

"""
from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        n = numCourses
        node_neighbors = {x: [] for x in range(n)}
        node_indegree = {x: 0 for x in range(n)}

        for pair in prerequisites:
            node_neighbors[pair[0]].append(pair[1])
            node_indegree[pair[1]] += 1

        start_nodes = [x for x in range(n) if node_indegree[x] == 0]
        queue = deque(start_nodes)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in node_neighbors[node]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0: # easy to forget
                    queue.append(neighbor)

        return n == len(order)





