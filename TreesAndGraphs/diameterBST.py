import sys

class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.curMax = 0
        self.postOrder(root)
      
        return self.curMax
    def postOrder(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)

        self.curMax = max(self.curMax, left+right)
        return max(left, right)+1