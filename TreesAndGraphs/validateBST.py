import sys

class Solution:
    def isValidBST(self, root: TreeNode, lower: int = None, upper: int = None) -> bool:
        if not root:
            return True
        if lower != None and root.val <= lower:
            return False
        elif upper != None and root.val >= upper:
            return False
        
        return self.isValidBST(root.right, root.val, upper) and self.isValidBST(root.left, lower, root.val)