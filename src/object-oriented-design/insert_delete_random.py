from random import choice


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indx = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        Time: O(1)
        """
        if self.indx.get(val) is not None:
            return False
        else:
            self.data.append(val)
            self.indx[val] = len(self.data) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        Time: O(1)
        """
        if self.indx.get(val) is not None:
            # rewrite the value to be deleted by the last element
            # first retrieve the index of the element to be deleted
            deletion_indx = self.indx[val]
            # then swap the last element and the element to be deleted (so to pop from the list)
            # but there is no need to swap,
            # just rewrite the element to be deleted by the last one would be enough
            self.data[deletion_indx] = self.data[-1]
            # assign the index to the original last element
            self.indx[self.data[-1]] = deletion_indx
            self.data.pop()
            del self.indx[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        Time: O(1)
        """
        if self.data:
            return choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
