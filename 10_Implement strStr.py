def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    result = haystack.find(needle)
    if not result and result != 0:
        return -1
    return result


haystack = 'a'
needle = 'a'
print(strStr(haystack, needle))
