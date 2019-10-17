"""
https://leetcode.com/problems/word-break-ii/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, wordDict, {})


    def dfs(self, s, wordDict, memo):
        if s == '':
            return []
        if s in memo:
            return memo[s]

        partitions = []

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue

            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for p in sub_partitions:
                partitions.append(prefix + " " + p)

        if s in wordDict:
            partitions.append(s)

        memo[s] = partitions
        return partitions
