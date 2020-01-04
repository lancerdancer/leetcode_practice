"""
https://leetcode.com/problems/add-bold-tag-in-string/

Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].

"""


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        n = len(s)
        is_bold = [False] * len(s)

        for i in range(n):
            block = s[i:]
            for word in dict:
                if block.startswith(word):
                    is_bold[i: i + len(word)] = [True] * len(word)

        ans = []
        for i, c in enumerate(s):
            if is_bold[i] and (i == 0 or not is_bold[i - 1]):
                ans.append('<b>')

            ans.append(c)

            if is_bold[i] and (i == n - 1 or not is_bold[i + 1]):
                ans.append('</b>')

        return ''.join(ans)
