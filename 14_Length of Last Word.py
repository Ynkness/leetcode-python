def lengthOfLastWord(s):
    s = s.strip(' ')
    l = s.split(' ')[-1]
    print(s, l)
    return len(l)

word = 'hello world'
result = lengthOfLastWord(word)
print(result)