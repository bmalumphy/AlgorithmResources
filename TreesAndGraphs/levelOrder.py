import collections

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        levelOrder = [[root.val]]
        queue.append(root.left)
        queue.append(root.right)
        
        while queue:
            newLevel = []
            newQueue = collections.deque()
            for i in queue:
                if i:
                    print(i.val)
                    newLevel.append(i.val)
                    newQueue.append(i.left)
                    newQueue.append(i.right)
            if newLevel:
                levelOrder.append(newLevel)
            queue = newQueue
        return levelOrder