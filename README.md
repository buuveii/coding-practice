# coding-practice
This is a Tree
Trees are hierarchical data structures.
Main uses of trees include maintaining hierarchical data, providing moderate access and insert/delete operations.

# def binary_tree:
    - a tree whose elements have at most 2 children (usually named left children and right children)
    - maximum number of nodes at level l is 2**l (level of the root is 0)
    - maximum number of nodes in a binary tree of height h is 2**h - 1 

# def binary_search_tree:
    - the left subtree of a node contains only nodes with keys less than the node's key  
    - the right subtree of a node contains only nodes with keys greater than the node's key 
    - the left and right subtree must be a binary search tree
    - no duplicate nodes

# def complete_binary_tree:
    - all the levels are completely filled except the last level
    - last level has all keys as left as possible
    - examples: (binary heap)

              18                                  
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40

              18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40
     /  \   /
    8   7  9 

# def full_binary_tree:
    - every node has 0 or 2 children (all the nodes except leaf nodes have 2 children)
    - examples:
             18
           /    \   
         15     20    
        /  \       
      40    50   
    /   \
   30   50

# def perfect_binary_tree:
    - all the internal nodes have 2 children 
    - all leaf nodes are at the same level
    - examples:
               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40

               18
           /       \  
         15         30  

# def AVL_tree:

# def_red_black_tree:

# def splay_tree:

# inorder_traversal:
    left -> root -> right

# preorder_traversal:
    root -> left -> right

# postorder_traversal:
    left -> right -> root




# URL:
- https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/?ref=lbp
traversals:
- https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm#:~:text=Finally%20the%20Inorder%20traversal%20logic,all%20the%20nodes%20are%20traversed.

