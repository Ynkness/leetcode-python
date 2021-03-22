def isValid(s):
    a = {
    '{':'}',
    '[':']',
    '(':')',
    '?':'?'
    }
    b = ['?']
    for i in s:
        if i in a:
            b.append(i)
        elif a[b.pop()] != i:
            return False 
    return len(b) == 1

l = "()"
print(isValid(l))