class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val not in self.idx:
            self.idx[val] = len(self.values)
            self.values.append(val)
            print(self.values, "added to", self.idx[val])
            return True
        return False

    def remove(self, val: int) -> bool:
        print('removing', val)
        if val not in self.idx:
            return False
        i = self.idx[val]
        self.values[i] = self.values[-1]
        self.idx[self.values[-1]] = i
        self.values.pop(-1)
        self.idx.pop(val)
        return True

    def getRandom(self) -> int:
        i = random.randint(0, len(self.values) - 1)
        return self.values[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()