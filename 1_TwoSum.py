a = [3,3]
b = 6

def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

result = twoSum(a,b)
print(result)