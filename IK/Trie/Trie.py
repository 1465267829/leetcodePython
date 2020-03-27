"""
https://leetcode.com/problems/implement-trie-prefix-tree/

208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class TrieNode:
  def __init__(self):
      self.children = {}
      self.is_word = False


class Trie:
  def __init__(self):
      self.root = TrieNode()

  def insert(self, word):
    current = self.root
    for letter in word:
      if letter not in current.children:
        # current letter is not in the trie. Create the key
        # with TrieNode as default value
        current.children[letter] = TrieNode()
      current = current.children[letter]
    # Set end ot word marker
    current.is_word = True

  def search(self, word):
    current = self.root
    for letter in word:
      # Get if current letter exists in the Trie Node children
      # If not get None as default
      current = current.children.get(letter, None)
      if current is None: return False
    return current.is_word

  def startsWith(self, prefix):
    current = self.root
    for letter in prefix:
      current = current.children.get(letter)
      if current is None: return False
    return True


if __name__ == '__main__':
  trie = Trie()
  trie.insert("apple")
  print(trie.search("apple"))
  print(trie.search("app"))
  print(trie.startsWith("app"))
  trie.insert("app")
  print(trie.search("app"))