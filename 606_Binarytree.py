class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorderTraversal(root):
    result = []
    if root is not None:
        # Visit the root node
        result.append(str(root.value))
        # Recursively traverse the left subtree
        result += preorderTraversal(root.left)
        # Recursively traverse the right subtree
        result += preorderTraversal(root.right)
    return result


def testing(root):
    final_str = ""
    if root is None:
        return ""

    final_str = str(root.value)

    if root.left or root.right:
        final_str += "(" + testing(root.left) + ")"
    
    if root.right:
        final_str += "(" + testing(root.right) + ")"

    return final_str

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
result = testing(root)
print(result)

