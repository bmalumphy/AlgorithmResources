# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        levelOrder = [[root.val]]
        queue.append(root.left)
        queue.append(root.right)
        switch = True
        while queue:
            newLevel = []
            newQueue = collections.deque()
            if(not switch):
                #print("Normally")
                for i in queue:
                    if i:
                        #print(i.val)
                        newLevel.append(i.val)
                        newQueue.append(i.left)
                        newQueue.append(i.right)
                #print(switch)
                switch = not switch
                #print(switch)
                if newLevel:
                    #print(newLevel)
                    levelOrder.append(newLevel)
                queue = newQueue
            else:
                #print("reversed")
                queue.reverse()
                for i in queue:
                    if i:
                        #print(i.val)
                        newLevel.append(i.val)
                        newQueue.append(i.right)
                        newQueue.append(i.left)
                #print(switch)
                switch = not switch
                #print(switch)
                if newLevel:
                    #print(newLevel)
                    levelOrder.append(newLevel)
                queue = newQueue
                queue.reverse()

            
                
        return levelOrder