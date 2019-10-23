"""
Trie implementation with dictionary
"""


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if node.children.get(c) is None:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_word = True

    def find(self, word) -> TrieNode:
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return bool(self.find(prefix))
