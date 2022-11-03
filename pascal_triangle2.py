def getRow(rowIndex):
        res = [1] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            mid = i // 2
            for j in range(mid, 0, -1):
                print('i:', i)
                print('j:', j)
                print('res:', res)
                res[j] = res[i - j] = res[j - 1] + res[j]

        return res


print(getRow(4))
