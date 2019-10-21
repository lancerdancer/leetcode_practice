"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:
            return 0
        n = len(s)
        if k >= n:
            return n

        j = 0
        counter = {}
        max_len = 0

        for i in range(n):
            while j < n and len(counter) <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                j += 1

            if j >= n and len(counter) <= k:
                max_len = max(max_len, j - i)
                break

            if len(counter) > k:
                max_len = max(max_len, j - i - 1)
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]

        return max_len
