"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

"""
import heapq

class Solution:
    """
    use heapq, 280ms beat 20.99%
    """
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not k:
            return None

        m = len(matrix)
        if m == 0:
            return None
        n = len(matrix[0])
        if n == 0:
            return None

        min_heap = [(matrix[0][0], (0, 0))]
        visited = set([0])
        num = None

        for _ in range(k):
            num, (x, y) = heapq.heappop(min_heap)
            if x + 1 < m and (x + 1) * n + y not in visited:
                heapq.heappush(min_heap, (matrix[x + 1][y], (x + 1, y)))
                visited.add((x + 1) * n + y)

            if y + 1 < n and x * n + y + 1 not in visited:
                heapq.heappush(min_heap, (matrix[x][y + 1], (x, y + 1)))
                visited.add(x * n + y + 1)

        return num

class Solution1:
    """
    use binary search 二分答案, 196ms beat 91.77%
    """

    def kthSmallest(self, matrix, k):
        # write your code here
        start = matrix[0][0]
        end = matrix[-1][-1]

        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.get_num_less_equal(matrix, mid) < k:
                start = mid
            else:
                end = mid
        if self.get_num_less_equal(matrix, start) >= k:
            return start
        return end

    def get_num_less_equal(self, matrix, mid):
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        count = 0
        while i < m and j >= 0:
            if matrix[i][j] <= mid:
                i += 1
                count += j + 1
            else:
                j -= 1
        return count
