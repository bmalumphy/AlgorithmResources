from collections import deque

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = deque()
        

    def push(self, x: int) -> None:
	   
        if len(self._stack) == 0:
            min_item = x
        else:
            min_item = min(x, self._stack[-1][1])
        self._stack.append((x, min_item))

    def pop(self) -> None:
        self._stack.pop()
        

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()