"""
https://leetcode.com/problems/palindrome-pairs/

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

"""


class Solution:
    def palindromePairs(self, words):
        res = []
        table = {}
        if not words:
            return res

        for index, word in enumerate(words):
            table[word] = index

        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                left, right = word[:i], word[i:]

                if self.isPal(left):
                    reversedRight = right[::-1]
                    if reversedRight in table and table[reversedRight] != index:
                        res.append([table[reversedRight], index])

                if len(right) > 0 and self.isPal(right):
                    reversedLeft = left[::-1]
                    if reversedLeft in table and table[reversedLeft] != index:
                        res.append([index, table[reversedLeft]])
        return res

    def isPal(self, s):
        return s == s[::-1]
