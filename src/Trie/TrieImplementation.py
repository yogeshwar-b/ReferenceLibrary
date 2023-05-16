# Basic Trie Implementation in Python
class TrieNode:
    def __init__(self):
        self.children = {}  # Empty child dictionary
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isEnd = True

    def search(self, word):
        # Searching upto word,then doing the dfs on that node to get all possible branches from that letter.
        self.results = []
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return []
        self.dfs(node, word)
        return self.results

    def dfs(self, node, wordsofar):
        if node.isEnd:
            self.results.append(wordsofar)
        for letter in node.children:
            self.dfs(node.children[letter], wordsofar+letter)

    def remove_word(self, word):
        self.__removeword(self.root, word, 0)

    def __removeword(self, node, word, pos):
        if pos == len(word):
            node.isEnd = False
            if len(node.children) == 0:
                return True
            else:
                return False

        if word[pos] in node.children:
            if self.__removeword(node.children[word[pos]], word, pos+1):
                del node.children[word[pos]]
                if len(node.children) == 0:
                    return True
                else:
                    return False
        else:
            return False


wordlist = ["hello", "hella", "word", "hell", "hexa", "hexagon"]
MyTrie = Trie()
for w in wordlist:
    MyTrie.insert(w)

print(MyTrie.search("he"))
print(MyTrie.search("xyz"))

print(MyTrie.search("hel"))
MyTrie.remove_word("hell")
print(MyTrie.search("hel"))

MyTrie.remove_word("hella")
print(MyTrie.search("hel"))

print(MyTrie.search("hex"))
MyTrie.remove_word("hexa")
print(MyTrie.search("hex"))

MyTrie.remove_word("xyz")
