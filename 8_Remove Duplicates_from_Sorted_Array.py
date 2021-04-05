def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 快 慢 指针
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            print(nums[i])
            j += 1
            nums[j] = nums[i]
    return j + 1


num = [1,1,1,2,3,5,8]
print(removeDuplicates(num))