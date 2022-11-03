def generate(numRows):
        res = [[1]]
        for num in range(2, numRows + 1):
            prev_row = res[num - 2]
            curr_row = [1] * num
            mid = (num + 1) // 2
            for i in range(1, mid):
                curr_row[i] = curr_row[num - 1 - i] = prev_row[i - 1] + prev_row[i]
            res.append(curr_row)
        return res


print(generate(7))
