def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        len1 = m -1
        len2 = n -1
        k = m + n - 1
        while len1 > 0 or len2 >= 0: # 这个>=很重要，他是滤除其中一个数组长度为0的情况
            if len1 == -1:
                nums1[k] = nums2[len2]
                len2 -= 1
            elif len2 == -1:
                nums1[k] = nums1[len1]
                len1 -= 1
            elif nums1[len1] > nums2[len2]:
                # 获取到谁的len才让他移动指针，这里卡了很久
                nums1[k] = nums1[len1]
                len1 -= 1
            else:
                nums1[k] = nums2[len2]
                len2 -= 1
            k -= 1
        return nums1
            


nums1 = [0]
m = 0
nums2 = [1]
n = 1

print(merge(nums1, m, nums2, n))