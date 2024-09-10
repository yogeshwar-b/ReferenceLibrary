from Trie import TrieImplementation
from BasicMathImplementations import BasicMath


def test_trie():
    wordlist = ["hello", "hella", "word", "hell", "hexa", "hexagon"]
    MyTrie = TrieImplementation.Trie()
    for w in wordlist:
        MyTrie.insert(w)

    assert MyTrie.search("he") == ['hell', 'hello', 'hella', 'hexa', 'hexagon']

def test_basicmath():
    TestMathFunctions = BasicMath.MathFunctions()
    assert TestMathFunctions.gcd(45,36)==9
    assert TestMathFunctions.gcd(72,16)==8
    assert TestMathFunctions.lcm(72,16)==144
