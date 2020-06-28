# Binary search tree, inorder traversal
from utils import list2binary_tree


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.sorted_nodes = []
        # T: O(1), S: O(H)
        self._left_inorder_stack(root)
        # T: O(1), S: O(N)
        # self._reverse_inorder(root)

    def _reverse_inorder(self, node):
        # Space: O(N)
        if node:
            # here we reverse the inorder traversal (right branch before left branch)
            # to have a list of nodes sorted in reverse
            self._reverse_inorder(node.right)
            self.sorted_nodes.append(node.val)
            self._reverse_inorder(node.left)

    def _left_inorder_stack(self, node):
        # Space: O(H) H could be logN
        while node:
            self.stack.append(node)
            node = node.left

    def next_fast(self):
        """
        @return the next smallest number
        Time: amortized O(1), not every node has right child
        Space: O(H), length of stack
        """
        curr_node = self.stack.pop()
        if curr_node.right:
            self._left_inorder_stack(curr_node.right)
        return curr_node.val

    def hasNext_fast(self):
        """
        @return whether we have a next smallest number
        Time: O(1)
        Space: O(H), length of stack
        """
        return len(self.stack) > 0

    def next(self):
        """
        @return the next smallest number
        Time: O(1)
        Space: O(N) for calling the sorted_nodes
        """
        return self.sorted_nodes.pop()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        Time: O(1)
        Space: O(N) for calling the sorted_nodes
        """
        return len(self.sorted_nodes) > 0


test = list2binary_tree([7, 3, 15, None, None, 9, 20])
a = BSTIterator(test)
print(a.next())
print(a.next())
print(a.hasNext())
print(a.next())
print(a.hasNext())
print(a.next())
print(a.hasNext())
print(a.next())
print(a.hasNext())
