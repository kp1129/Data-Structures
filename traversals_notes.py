"""
Depth first - an algorithm for traversing or searching
tree or graph data structures. The algorithm starts at
the root node and explores as far (deep) as possible along
each branch until it hits a leaf before backtracking

Breadth first - an algorithm for traversing or searching
tree or graph data structures. It starts at the tree root,
and explores all of the neighbor nodes at the present depth
prior to moving on to the nodes at the next depth level
__________________________________________________________

Depth First Variants:

Preorder Traversal (current - left - right): visit the current
node before visiting any node inside left or right subtrees

Inorder Traversal (left - current - right): visit the current
node after visiting all nodes inside left subtree but
before visiting any node within the right subtree

Postorder Traversal (left - right - current): visit the current
node after visiting all the nodes of left and right subtrees
"""

"""
Tree Traversal = the process of visiting each node in the tree
exacctly once in some order. The order in which the nodes are 
visited defines the type of tree traversal: breadth-first or 
depth-first.

Breadth-first or Depth-first are techniques to traverse trees
and graphs.

Visiting a node = reading or processing data in some way.
_______________________________________________________________

Breadth-first, or BFS, or Level-order
In a tree, in a breadth-first approach, we would visit all the
nodes of the same level first before going to the next level.

Implementation: a queue!
As we visit a node, we can reference or address of all of its 
children in a queue so we can visit them later.
A node in the queue can be called disccovered node whose address
is known to us BUT we have not visited it yet (remember, 'visited'
refers to reading or in some way processing the data stored in 
that node).
-create a queue, push the first element (root) to the queue
-while the queue is not empty (if we have at least one discovered
node in the queue - discovered but not read, fyi), 'while' loop:
---take the first item from the queue, read its data in some way
---if it has a left child, add that child to the back of the queue
---if it has a right child, add that child to the back of the queue
behind the left child
---finally, remove the current item from the front of the queue
because we're done with it.

Time complexity: if there are n Nodes in the tree and in this 
algorithm visiting a node is reading its data and then enqueueing
its children in the queue, then visit each child node...
-visit to a node will take constant time and each node will be
visited only once. So time taken will be proportional to the number
of nodes (this makes sense).
_______________________________________________________________

Depth-first, or DFS
In a tree, in a depth-first approach, we would visit all the
nodes in a subtree of a child before we go to the next child node.

The order in which you complete depth-first traversal can vary.
-Preorder: root, left subtree, right subtree
-Inorder: left subtree, root, right subtree
-Postorder:left subtree, right subtree, root

In total, there are six possible permutations for left, right,
and root. But conventionally we visit the left subtree before the 
right subtree. So these are the three main strategies we can use
to complete a depth-first traversal -- you can see, only the
position of the root is changing.

If you print the data using Inorder traversal of a binary tree,
you will get a sorted list.

"""