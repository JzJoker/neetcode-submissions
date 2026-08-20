class RandomizedSet:

    def __init__(self):
        self.vals = set()

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.vals:
            self.vals.remove(val)
            return True

    def getRandom(self) -> int:
        valuesList = list(self.vals)
        i = random.randint(0, len(valuesList) - 1)
        return valuesList[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()