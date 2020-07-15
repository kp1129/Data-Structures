"""
TreeNodes have a collection of pointers that reference other TreeNodes.
-Can have more than 2 pointers

Path refers to the sequence of TreeNodes

Subtree is a collection of descendants of a TreeNode

Visiting refers to checking the value of a TreeNode
when control is on the node

Traversing means passing through TreeNodes in a specific order

Levels refer to generation of a TreeNode (root is 0, next child is 1, etc)


In a binary tree, the TreeNodes have a maximum of 2 nodes, left and right

Perfect tree has the maximum number of TreeNodes that it possibly could.
It is completely full.
-each level doubles the number of TreeNodes as we move down
-num of TreeNodes on the last level is equal to
the sum of all other TreeNodes + 1

Binary Search Tree
-binary tree with additional rules
-all the values on the left subtree are less than the root
-all the values on the right subtree are greater than the root
"""