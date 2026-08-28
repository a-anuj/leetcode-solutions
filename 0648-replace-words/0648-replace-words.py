class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        root = TrieNode()

        for word in dictionary:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                
            node.isEnd = True
        
        def search(word):
            node = root
            result = ""
            for char in word:
                if char not in node.children:
                    return word
                
                result += char
                node = node.children[char]
                if node.isEnd:
                    return result
            return word
                
        
        lst = sentence.split(" ")
        for i in range(len(lst)):
            lst[i] = search(lst[i])
        return " ".join(lst)


