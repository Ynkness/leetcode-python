def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        result = nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        result = nums.index(target)
    return result

numlist = [1,3,5,6]
t = 2
print(searchInsert(numlist,t))