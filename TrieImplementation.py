#Basic Trie Implementation in Python
class TrieNode:
    def __init__(self):
        self.children={} #Empty child dictionary
        self.isEnd=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        node=self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter]=TrieNode()
            node=node.children[letter]
        node.isEnd=True
    
    def search(self,word):
        #Searching upto word,then doing the dfs on that node to get all possible branches from that letter. 
        self.results=[]
        node=self.root
        for letter in word:
            if letter in node.children:
                node=node.children[letter]
            else:
                return []
        self.dfs(node,word)
        return self.results
    
    def dfs(self,node,wordsofar):
        if node.isEnd:
            self.results.append(wordsofar)
        for letter in node.children:
            self.dfs(node.children[letter],wordsofar+letter)

wordlist=["hello","hella","word","hexa"]
MyTrie= Trie()
for w in wordlist:
    MyTrie.insert(w)
print(MyTrie.search("hel"))
print(MyTrie.search("he"))
print(MyTrie.search("hex"))
print(MyTrie.search("xyz"))