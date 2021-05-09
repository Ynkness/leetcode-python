def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tmp_sum = 0
    res = nums[0]
    for num in nums:
        # max函数返回最大值
        tmp_sum = max(tmp_sum + num, num)
        res = max(res, tmp_sum)
    return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))