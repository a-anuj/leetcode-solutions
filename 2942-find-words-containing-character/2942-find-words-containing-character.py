class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for index,word in enumerate(words):
            if x in word:
                arr.append(index)
        return arr