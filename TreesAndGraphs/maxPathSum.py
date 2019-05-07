def maxPathSum(self, root: TreeNode) -> int:
        self.cur_max = float('-inf')
        self.post_order(root)
        return self.cur_max
def post_order(self, root):
    if not root:
        return float('-inf')
    left = self.post_order(root.left)
    right = self.post_order(root.right)
        
    self.cur_max = max(self.cur_max, left, right, 
        root.val, root.val+left, 
        root.val+right, root.val+right+left)
    return max(root.val, root.val+left, root.val+right)