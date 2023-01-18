
def solution(S):

    string = S.lower()
    letters = set("abcdefghijklmnopqrstuvwxyz")
    words = []
    left = right = 0
    while right < len(string):
        if string[right] in letters:
            right += 1
        else:
            words.append(string[left: right])
            right += 1
            left = right
    if left != right:
        words.append(string[left: right])
    res = {}
    for word in words:
        for i in range(len(word)):
            for j in range(i, len(word)):
                if word[i:j + 1] not in res:
                    res[word[i:j + 1]] = 1
                else:
                    res[word[i:j + 1]] += 1

    ans = sorted(res.items(), key=lambda ele:ele[0])
    ans.sort(key=lambda ele: ele[1], reverse=True)
    output = "\n".join(str(ele[1]) + ": " + ele[0] for ele in ans)

    return output

print(solution("banana boat"))
