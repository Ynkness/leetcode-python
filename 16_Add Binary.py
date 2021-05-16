def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 转换成二进制
        ia = int(a, 2)
        ib = int(b, 2)
        print(ia, ib)
        isum = ia + ib
        # 二进制转十进制
        result = "{0:b}".format(isum)
        return result

print(addBinary('11','10010'))