class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {}
        for i in range(len(order)):
            idx[order[i]] = i
        for i in range(len(words) - 1):
            if not self.comesBefore(words[i], words[i + 1], idx):
                return False
        return True

    def comesBefore(self, word1, word2, idx):
        i = 0
        while i < len(word1) and i < len(word2):
            if idx[word1[i]] > idx[word2[i]]:
                return False
            elif idx[word1[i]] < idx[word2[i]]:
                return True
            i += 1
        if len(word1) > len(word2):
            return False
        return True