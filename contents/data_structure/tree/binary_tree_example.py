#!/bin/python3


class BinaryTreeNode:
    """Class to represent node of the binary tree."""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """Return the string representation of the data."""
        return repr(self.data)


if __name__ == '__main__':
    # Create root
    root = BinaryTreeNode("Ned")
    # Link children
    root.left = BinaryTreeNode("Robb")
    root.right = BinaryTreeNode("John")
    root.left.left = BinaryTreeNode("John Jr. :)")
