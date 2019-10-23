"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can
represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for c in word:
            current = current.children[c]

        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        """
        if word is None:
            return False
        current = self.root
        return self.dfs(current, word, 0)

    def dfs(self, node, word, index):
        if node is None:
            return False

        if index >= len(word):
            return node.is_word

        char = word[index]
        if char != '.':
            return self.dfs(node.children.get(char), word, index + 1)

        for child in node.children:
            if self.dfs(node.children[child], word, index + 1):
                return True

        return False
