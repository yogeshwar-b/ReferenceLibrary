from Trie import TrieImplementation


def test_trie():
    wordlist = ["hello", "hella", "word", "hell", "hexa", "hexagon"]
    MyTrie = TrieImplementation.Trie()
    for w in wordlist:
        MyTrie.insert(w)

    assert MyTrie.search("he") == ['hell', 'hello', 'hella', 'hexa', 'hexagon']
