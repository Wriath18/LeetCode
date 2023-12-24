class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorderTraversal(root):
    result = []
    if root is not None:
        result += preorderTraversal(root.left)
        result.append(str(root.value))
        result += preorderTraversal(root.right)
    return result




# Example usage:
# Assuming you have a tree like this:    1
#                                      / \
#                                     2   3
#                                      \  
#                                       4

# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

# Example usage:
result = preorderTraversal(root)
print(result)

