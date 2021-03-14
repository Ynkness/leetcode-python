def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if -2**31<=x<=2**31-1:
        y = list(str(x))
        y.reverse()
        b = list(str(x))
        if y == b:
            return True
        if y != b:
            return False
    return 0

result = isPalindrome(-101)
print(result)