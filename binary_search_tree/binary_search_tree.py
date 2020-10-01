"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys

sys.path.append('queue')
sys.path.append('stack')

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BSTNode(value)
        if value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        currentMax = self.value
        while current is not None:
            if current.value > currentMax:
                currentMax = current.value
            current = current.right
        return currentMax

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.right is not None:
            self.right.for_each(fn)
        
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()

        print(self.value)
        
        if self.right is not None:
            self.right.in_order_print()


    """
        queue
        grab starting node and put it in a queue

        if there are items in the queue
        dequeue what the current node is
        mark it as visited
        print the value
        check left
            enqueue the left
        check right
            enqueue the right
    """

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = Queue()
        q.enqueue(self)
        while q.size != 0:
            nextNode = q.dequeue()
            print(nextNode.value)
            if nextNode.left is not None:
                q.enqueue(nextNode.left)
            if nextNode.right is not None:
                q.enqueue(nextNode.right)


    """
        stack
        grab starting node and put it in a stack

        if there are items in the stack
        pop what the current node is
        mark it as visited
        print the value
        check left
            push the left
        check right
            push the right
    """

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = Stack()
        s.push(self)
        while s.size != 0:
            nextNode = s.pop()
            print(nextNode.value)
            if nextNode.left is not None:
                s.push(nextNode.left)
            if nextNode.right is not None:
                s.push(nextNode.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
