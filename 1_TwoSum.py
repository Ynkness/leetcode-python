a = [3,3]
b = 6

def twoSum(nums,target):
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []

result = twoSum(a,b)
print(result)