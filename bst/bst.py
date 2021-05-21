class BSTnode(object):
    """
Representation of a node in a binary search tree.
Has a left child, right child, parent, and key value.
"""
    def __init__(self, t):
        self.key = t
        self.left = None
        self.right = None
        self.parent = None
        self.disconnect()
    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None


class BST(object):
    """
Simple binary search tree implementation.
This BST supports insert, find, and delete-min operations.
Each tree contains some (possibly 0) BSTnode objects, representing nodes,
and a pointer to the root.
"""

    def __init__(self):
        self.root = None

    def insert(self, t):
        """
        Insert key t into this BST, modifying it in-place. O(h)
        """
        new = BSTnode(t)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if t < node.key:
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def find(self, t):
        """
        Return the node for key t if is in the tree, or None otherwise. O(h)
        """
        node = self.root
        while node is not None:
            if t == node.key:
                return node
            elif t < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete_min(self):
        """
        Delete the minimum key (and return the old node containing it).
        """
        if self.root is None:
            return None
        else:
            node = self.root
            while node.left is not None:
                node = node.left
            # remove that node and replace it with the right node
            if node.parent is not None:
                node.parent.left = node.right
            else: # if the node is the root node
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node, parent

# if __name__ == '__main__': 
