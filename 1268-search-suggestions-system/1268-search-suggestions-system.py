class Trie:
    def __init__(self):
        self.children = {}
        self.words = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        root = Trie()
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = Trie()
                
                node = node.children[char]

                if len(node.words) < 3:
                    node.words.append(product)
        

        result = []
        node = root
        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                result.append(node.words)
            else:
                node = None
                result.append([])
        return result
