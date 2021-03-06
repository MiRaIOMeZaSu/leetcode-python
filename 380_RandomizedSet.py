import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = list()
        self.hashtable = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if(val not in self.hashtable):
            self.hashtable.add(val)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if(val in self.hashtable):
            self.hashtable.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0, len(self.arr) - 1)
        while(self.arr[index] not in self.hashtable):
            index = random.randint(0, len(self.arr) - 1)
        return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
