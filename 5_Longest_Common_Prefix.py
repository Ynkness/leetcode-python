strs = ["flower","flow","flight","flopp","flllll"]
def longestCommonPrefix(strs):
        if not strs:
            return ""
        strs.sort()
        start = strs[0]
        end = strs[-1]
        res = ""
        for i in range(len(start)):
            if i < len(end) and start[i] == end[i]:
                res += start[i]
                print(res)
            else:
                break
        return res
print(longestCommonPrefix(strs))