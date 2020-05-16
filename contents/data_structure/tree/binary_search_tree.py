#!/bin/python3


class BinaryTreeNode:
    """Class represent's node of the binary tree."""
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        """Return the string representation of the data."""
        return repr(self.key)


class BinarySearchTree:
    """Class represent's the Binary Search Tree"""
    def __init__(self, root=None):
        self.root = root
        self.dflag = False
        self.sflag = False
        self.inorder_lst = []

    def __repr__(self):
        return repr(self.root)

    def _set_key(self, key, root=None):
        """Function gets called in recursive manner."""
        if not root:
            self.root = BinaryTreeNode(key=key)
        elif root.key > key:
            if not root.left:
                root.left = BinaryTreeNode(key=key)
            else:
                self._set_key(key, root.left)
        else:
            if not root.right:
                root.right = BinaryTreeNode(key=key)
            else:
                self._set_key(key, root.right)

    def insert_key(self, key):
        """Function to add a node to the BST."""
        self._set_key(key, self.root)
        print("{} added".format(key))

    def _search_key(self, key=None, root=None):
        """Return key else None"""
        if not root:
            return
        elif root.key == key:
            self.sflag = True
            return root
        elif root.key > key:
            return self._search_key(key, root.left)
        else:
            return self._search_key(key, root.right)

    def search_key(self, key):
        """Function to search given key in BST."""
        self._search_key(key, self.root)
        return True if self.sflag else False

    def _delete_key(self, key, root=None):
        # Base case
        if not root:
            return root
        # If given key is smaller than root key go to left subtree.
        elif key < root.key:
            root.left = self._delete_key(key, root.left)
        # Ff given key is greater than root key go to left subtree.
        elif key > root.key:
            root.right = self._delete_key(key, root.right)
        else:
            self._del_flag = True
            # If node with one or zero child.
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            # If node with two children.
            temp = self.get_min(root.right)
            root.key = temp.key
            root.right = self._delete_key(key, root.right)
        return root

    def delete_key(self, key):
        """Function to delete key node in BST"""
        self._delete_key(key, self.root)
        return "{} deleted".format(key) \
            if self.dflag else "{} not found.".format(key)

    def get_min(self, root=None):
        """Return minimum value node."""
        if not root:
            root = self.root
        while root.left:
            root = root.left
        return root

    def inorder(self, root=None):
        """Function to print inorder tree."""
        if root:
            self.inorder(root.left)
            self.inorder_lst.append(root)
            self.inorder(root.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    lst = [50, 30, 70, 20, 40, 60, 80, 10, 45]
    for item in lst:
        bst.insert_key(item)
    print("Search 100")
    print(bst.search_key(3))
    print("Delete 100")
    print(bst.delete_key(100))
    bst.inorder(bst.root)
    print(bst.inorder_lst)
