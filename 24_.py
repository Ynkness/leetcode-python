# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        # 找到中点作为根节点
        mid = len(nums) // 2
        node = TreeNode(nums[mid])

        # 左侧数组作为左子树
        left = nums[:mid]
        right = nums[mid+1:]

        # 递归调用
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)

        return node

a = Solution()
result = a.sortedArrayToBST([-10,-3,0,5,9])
print(result)