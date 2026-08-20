class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        self.values[self.idx[val]] = self.values[-1]
        self.idx[self.values[-1]] = self.idx[val]
        self.values.pop(-1)
        self.idx.pop(val)


    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()