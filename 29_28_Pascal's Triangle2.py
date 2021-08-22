def getRow(rowIndex: int):
        ret = [1] * (rowIndex + 1)
        print(ret)
        for i in range(2, rowIndex + 1):
            print('i:',i)
            for j in range(i - 1, 0, -1):
                print('j:',j)
                ret[j] += ret[j - 1]
            print(ret)
        return ret

print(getRow(3))

for i in range(3, 0, -1):
    print(i)