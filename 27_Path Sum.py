from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([[root, targetSum]])
        while queue:
            for i in range(len(queue)):
                child, num = queue.popleft()
                num -= child.val
                if not (child.left or child.right) and num == 0:
                    return True
                if child.left:
                    queue.append([child.left, num])
                if child.right:
                    queue.append([child.right, num])
        return False