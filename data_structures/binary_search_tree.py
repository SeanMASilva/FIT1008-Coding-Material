""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""

from __future__ import annotations

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev, further modified by Jackson Goerner'
__docformat__ = 'reStructuredText'

import math
from typing import TypeVar, Tuple

from data_structures.linked_stack import LinkedStack
from data_structures.node import BinaryNode
from data_structures.abstract_hash_table import HashTable
from data_structures.referential_array import ArrayR

# generic types
K = TypeVar('K')
V = TypeVar('V')
T = TypeVar('T')


class BSTPreOrderIterator:
    """ Pre-order iterator for the binary search tree.
        Performs stack-based BST traversal.
    """

    def __init__(self, root: BinaryNode[K, V] | None) -> None:
        """ Iterator initialiser. """

        self.stack = LinkedStack[BinaryNode]()
        if root is not None:
            self.stack.push(root)

    def __iter__(self) -> BSTPreOrderIterator:
        """ Standard __iter__() method for initialisers. Returns itself. """

        return self

    def __next__(self) -> BinaryNode[K, V]:
        """ The main body of the iterator.
            Returns keys of the BST one by one respecting the pre-order.
        """

        if self.stack.is_empty():
            raise StopIteration
        current = self.stack.pop()
        if current._right:
            self.stack.push(current._right)
        if current._left:
            self.stack.push(current._left)
        return current


class BSTInOrderIterator:
    """ In-order iterator for the binary search tree.
        Performs stack-based BST traversal.
    """

    def __init__(self, root: BinaryNode[K, V]) -> None:
        """ Iterator initialiser. """

        self.stack = LinkedStack[BinaryNode]()
        self.current = root

    def __iter__(self) -> BSTInOrderIterator:
        """ Standard __iter__() method for initialisers. Returns itself. """

        return self

    def __next__(self) -> BinaryNode[K, V]:
        """ The main body of the iterator.
            Returns keys of the BST one by one respecting the in-order.
        """

        while self.current:
            self.stack.push(self.current)
            self.current = self.current._left

        if self.stack.is_empty():
            raise StopIteration

        result = self.stack.pop()
        self.current = result._right

        return result


class BSTPostOrderIterator:
    """ Post-order iterator for the binary search tree.
        Performs stack-based BST traversal.
    """

    def __init__(self, root: BinaryNode[K, V] | None) -> None:
        """ Iterator initialiser. """

        self.stack = LinkedStack[Tuple[BinaryNode, bool]]()
        if root is not None:
            self.stack.push((root, False))

    def __iter__(self) -> BSTPostOrderIterator:
        """ Standard __iter__() method for initialisers. Returns itself. """
        return self

    def __next__(self) -> BinaryNode[K, V]:
        """ The main body of the iterator.
            Returns keys of the BST one by one respecting the post-order.
        """

        while True:
            if self.stack.is_empty():
                raise StopIteration
            current, expanded = self.stack.pop()
            if expanded:
                return current
            else:
                self.stack.push((current, True))
                if current._right:
                    self.stack.push((current._right, False))
                if current._left:
                    self.stack.push((current._left, False))


class BinarySearchTree(HashTable[K,V]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        self.__root: BinaryNode[K, V] | None = None
        self.__length = 0

    @staticmethod
    def from_node(node: BinaryNode[K, V] | None, length: int = None) -> BinarySearchTree[K, V]:
        """
            Creates a binary search tree object from binary node.
            Useful if a bottom up construction of the tree can be done efficiently.
            Length argument is not checked if passed in.
            :complexity: 
                :best: O(1) when length is passed
                :worst: O(N) where N is the number of nodes in the tree
        """
        def len_aux(current: BinaryNode | None) -> int:
            if current is None:
                return 0
            return 1 + len_aux(current._left) + len_aux(current._right)
        
        if not isinstance(node, (BinaryNode, type(None))):
            raise TypeError(f"Cannot instantiate binary tree with node type: {type(node)}")
        tree = BinarySearchTree()
        tree.__root = node
        tree.__length = length if length else len_aux(node)

        return tree

    def is_empty(self) -> bool:
        """
            Checks to see if the bst is empty
            :complexity: O(1)
        """
        return self.__root is None

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.__length

    def __contains__(self, key: K) -> bool:
        """
            Checks to see if the key is in the BST
            :complexity: see __getitem__(self, key: K) -> (K, I)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self) -> BSTInOrderIterator:
        """ Create an in-order iterator. """
        return BSTInOrderIterator(self.__root)
    
    def post_iter(self) -> BSTPostOrderIterator:
        return BSTPostOrderIterator(self.__root)
    
    def pre_iter(self) -> BSTPreOrderIterator:
        return BSTPreOrderIterator(self.__root)

    def __getitem__(self, key: K) -> V:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
            :complexity best: O(CompK) finds the item in the root of the tree
            :complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        return self.get_tree_node_by_key(key).item

    def get_tree_node_by_key(self, key: K) -> BinaryNode:
        return self.get_tree_node_by_key_aux(self.__root, key)

    def get_tree_node_by_key_aux(self, current: BinaryNode, key: K) -> BinaryNode:
        if current is None:  # base case: empty
            raise KeyError(f'Key not found: {key}')
        elif key == current.key:  # base case: found
            return current
        elif key < current.key:
            return self.get_tree_node_by_key_aux(current._left, key)
        else:  # key > current.key
            return self.get_tree_node_by_key_aux(current._right, key)

    def __setitem__(self, key: K, item: V) -> None:
        self.__root = self.insert_aux(self.__root, key, item, 1)

    def insert_aux(self, current: BinaryNode, key: K, item: V, current_depth: int) -> BinaryNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
            :complexity: 
                :best: O(CompK) inserts the item at the root.
                :worst: O(CompK * D) inserting at the bottom of the tree
            where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = BinaryNode(item, key)
            self.__length += 1
        elif key < current.key:
            current._left = self.insert_aux(current._left, key, item, current_depth + 1)
        elif key > current.key:
            current._right = self.insert_aux(current._right, key, item, current_depth + 1)
        else:  # key == current.key
            current.item = item
        return current

    def __delitem__(self, key: K) -> None:
        self.__root = self.delete_aux(self.__root, key)

    def delete_aux(self, current: BinaryNode, key: K) -> BinaryNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete.
        """

        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current._left = self.delete_aux(current._left, key)
        elif key > current.key:
            current._right = self.delete_aux(current._right, key)
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.__length -= 1
                return None
            elif current._left is None:
                self.__length -= 1
                return current._right
            elif current._right is None:
                self.__length -= 1
                return current._left

            # general case => find a successor
            successor = self.get_successor(current)
            current.key = successor.key
            current.item = successor.item
            current._right = self.delete_aux(current._right, successor.key)

        return current

    def get_successor(self, current: BinaryNode) -> BinaryNode:
        """
            Get successor of the current node.
            It should be a node in the subtree rooted at current having the smallest key among all the
            larger keys.
            If no such node exists, then none should be returned.
        """
        if current is None:
            return None
        return self.get_minimal(current._right)
    
    def get_predecessor(self, current: BinaryNode) -> BinaryNode:
        """
            Get predecessor of the current node.
            It should be a node in the subtree rooted at current having the largest key among all the
            smaller keys.
            If no such node exists, then none should be returned.
        """
        if current is None:
            return None
        return self.get_maximal(current._left)

    def get_minimal(self, current: BinaryNode) -> BinaryNode | None:
        """
            Get a node having the smallest key in the current sub-tree.
        """
        if current is None:
            return None
        while current._left:
            current = current._left
        return current

    def get_maximal(self, current: BinaryNode) -> BinaryNode | None:
        """
            Get a node having the largest key in the current sub-tree.
        """
        if current is None:
            return None
        while current._right:
            current = current._right
        return current

    def is_leaf(self, current: BinaryNode) -> bool:
        """ Simple check whether or not the node is a leaf. """

        return current._left is None and current._right is None

    def items(self) -> ArrayR[Tuple[K, V]]:
        array = ArrayR(len(self))
        for i, node in enumerate(self):
            tup = (node.key, node.item)
            array[i] = tup
        return array

    def keys(self):
        return super().keys()
    
    def values(self):
        return super().values()

    def __str__(self):
        buffer = self.__str_aux(self.__root, [], prefix='', postfix='')
        return '\n'.join(buffer)
    
    def __str_aux(self, current:BinaryNode, buffer:list, prefix='', postfix=''):
        if current is not None:
            real_prefix = prefix[:-2] + postfix
            buffer.append(f'{real_prefix}{current.key}')
            if current._left or current._right:
                self.__str_aux(current._left, buffer, prefix=prefix + '\u2551 ', postfix='\u255f\u2550')
                self.__str_aux(current._right, buffer, prefix=prefix + '  ', postfix='\u2559\u2550')
        else:
            real_prefix = prefix[:-2] + postfix
            buffer.append(f'{real_prefix}')
        return buffer

