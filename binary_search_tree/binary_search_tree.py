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
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if self.value > value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)
        else:
            self.right = new_node



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        max = 0
        max = self.value

        while self.right is not None:
            max = self.right.value
            self.right = self.right.right
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
            
        
            


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)

        print(self.value)
        
        if self.right:
            self.right.in_order_print(self.right)
    
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()
        q.append(self)

        while len(q)>0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(self)

        while len(stack)>0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)
        
        

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left) 
        if self.right:
            self.right.post_order_dft(self.right)
        print(self.value)  

        
