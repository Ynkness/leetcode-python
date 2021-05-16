def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    for i in range(len(digits)-1,-1,-1):
        digits[i] += 1
        digits[i] %= 10
        print(digits[i])
        if digits[i] != 0:
            # 如果【1，2，9】，9+1 %10 进不了判断，会进行下一次判断 
            return digits
    # 如果循环结束都没有返回，说明是999这样的数，所以需要在最前面插入1
    digits.insert(0,1)
    return digits


digits = [1,2,3,9]
print(plusOne(digits))