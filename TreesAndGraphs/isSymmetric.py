import collections

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            p = queue.popleft()
            q = queue.popleft()
            if p == None and q == None:
                continue
            if p == None or q == None:
                print("one was None, other wasn't")
                return False
            if p.val != q.val:
                print("Nonequivalence")
                return False
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)
        return True