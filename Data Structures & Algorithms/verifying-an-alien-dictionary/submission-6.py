class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        for i in range(len(order)):
            ch = order[i]
            orderDict[ch] = i
        for i in range(len(words) - 1):
            if not self.lessThan(words[i], words[i + 1], orderDict):
                return False
        return True

    def lessThan(self, word1, word2, orderDict) -> bool:
        i = 0
        while i < len(word1) and i < len(word2):
            if orderDict[word1[i]] > orderDict[word2[i]]:
                return False
            elif orderDict[word1[i]] < orderDict[word2[i]]:
                return True
            i += 1
        if len(word1) > len(word2):
            return False
        return True