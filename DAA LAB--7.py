#!/usr/bin/env python
# coding: utf-8

# In[1]:


# BINARY SEARCH TREE NODE SEARCH
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root

def search(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
root = None


keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert(root, key)

search_key = 60
result = search(root, search_key)

if result:
    print(f"Node with key {search_key} found in the BST.")
else:
    print(f"Node with key {search_key} not found in the BST.")


# In[3]:


# LEAF NODE SUM IN A TREE
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def sum_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.value
    return sum_leaf_nodes(root.left) + sum_leaf_nodes(root.right)

root = Node(10)
root.left = Node(8)
root.right = Node(20)
root.left.left = Node(7)
root.left.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(21)

leaf_sum = sum_leaf_nodes(root)
print("Sum of leaf nodes:", leaf_sum)


# In[9]:


# SPINAL (ZIG-ZAG) ORDER TREE TRAVERSAL
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def zigzagTraversal(root):
    if not root:
        return []

    result = []
    queue = [root]
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            if left_to_right:
                node = queue.pop(0)
                current_level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                node = queue.pop()
                current_level.append(node.value)
                if node.right:
                    queue.insert(0, node.right)
                if node.left:
                    queue.insert(0, node.left)

        result.append(current_level)
        left_to_right = not left_to_right

    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = zigzagTraversal(root)
print("zigzagTraversal order:",result)


# In[ ]:




