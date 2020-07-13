# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList):
        """
        Constructor, store the reversed nestedList to a stack
        Time: O(n + l) in worst case, n the number of integers (nested or not), l the number of lists (nested or not)
        in the worst case all integers are not nested and all lists are empty
        Space: O(n + l)
        """
        # nestedList is of type List[NestedInteger]
        assert(isinstance(nestedList, list))
        # this is equivalent to self.stack = list(reversed(nestedList))
        self.stack = [nestedList[i] for i in range(len(nestedList), -1, -1)]

    def next(self) -> int:
        """
        Time: O(1) not considering hasNext()
        """
        # the condition can be removed if the user will surely call hasNext() before calling next()
        # if hasNext() returns true then we are sure the top of the stack will be an integer
        if self.hasNext():
            return self.stack.pop()

    def hasNext(self) -> bool:
        """
        Time: O(1), when the top of the stack is an integer or O(l/n) (amortised), otherwise
        The total time to make sure all integers are out from nested list is O(l + n) and there will be n calls
        (to get all n integers) so the amortised time is O((l + n) / n) = O(l/n)
        """
        # hasNext() check if there is any other integer (nested or not) left in the stack,
        # and move the closest (leftmost) integer to the top of the stack

        # is stack is not empty and the top is a nested list
        while self.stack and not self.stack[-1].isInteger():
            # see if stack[-1] is [[]] or []
            # however nested empty list such as [[[]], [[]]] will be flattened first and removed in the next iteration
            if self.stack[-1].getList():
                # popped the nested list and flatten it, push back to stack in reverse order (left to right)
                curr = self.stack.pop()
                # or use self.stack.extend() here
                self.stack += (reversed(curr.getList()))

            # else stack[-1] is [[]] or [], simply remove it from the stack
            else:
                self.stack.pop()

        # after the while loop, the stack is either empty or the top is an integer
        # actually we only need to check if the stack is empty or not in the if statement (no need for isInteger())
        if self.stack and self.stack[-1].isInteger():
            return True
        # we enter the else statement if the stack is empty
        else:
            return False

    def flatten_list(self, nestedList):
        """
        Recursively flatten the list
        (not used above, but if used: self.stack = list(reversed(self.flatten_list(nestedList))))
        (then hasNext() returns True if the stack is non-empty and next() returns the popped top of stack)

        Time: O(n + l) n: total number of integers, l: total number of lists;
        getInteger() for every integer (nested or not, O(n)) and  getList() for every list (nested or not)

        Space: O(n + d) d: maximal nesting depth; space for the flattened list (n) and recursion stack (d)

        Time for hasNext() and next(): O(1)
        """
        flattened = []
        for nested_integer in nestedList:
            if nested_integer.isInteger():
                flattened.append(nested_integer.getInteger())
            else:
                flattened += self.flatten_list(nested_integer.getList())
        return flattened


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
