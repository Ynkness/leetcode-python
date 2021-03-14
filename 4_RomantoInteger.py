def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    s_list = list(s)
    roman_dict = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    s_list_len = len(s_list)
    m = 0
    for j in range(s_list_len):
        if j+1<s_list_len and roman_dict[s_list[j]]<roman_dict[s_list[j+1]]:
            m-=roman_dict[s_list[j]]
        else:
            m+=roman_dict[s_list[j]]
        print('--------------',j,s_list[j],roman_dict[s_list[j]],m)
    return m

result = romanToInt('MCMXCIV')
print(result)
