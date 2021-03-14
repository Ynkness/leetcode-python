def reverse(x):
    k = list(str(x))
    print(k)
    if x==0:
        return 0
    k.reverse()
    print(k)
    if '-' in k:
        k.pop(k.index('-'))
        result = int('-' + ''.join([str(t) for t in k]))
    else:
        result = int(''.join([str(t) for t in k]))
    if -2**31<=result<=2**31-1:
        return result
    return 0

result = reverse(90100)
print(result)