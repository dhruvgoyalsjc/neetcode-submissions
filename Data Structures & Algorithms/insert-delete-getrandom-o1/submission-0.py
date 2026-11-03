class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.elems = []

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return
        self.mp[val] = len(self.elems)
        self.elems.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        idx = self.mp[val]
        last_elem = self.elems[-1]
        self.mp[last_elem] = idx
        self.elems[idx] = last_elem
        self.elems.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.elems)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()