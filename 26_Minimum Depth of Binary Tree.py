# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue, res = [root], 0
        while root and len(queue) > 0:
            n, res = len(queue), res + 1
            for i in range(n):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return res
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
        return 0
        