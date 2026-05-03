class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        print(1+max(left, right))
        return 1 + max(left, right)

# 1. Instantiate the class with ()
sol = Solution()

# 2. Create a dummy tree and pass the root to the method
# Example: A single node tree
root_node = TreeNode(4,6,7,0,8,5,4,)
sol.maxDepth(root_node)