def splitAndSort(string):
    words = split(string)
    words_sorted = sorted(words.items(), key=lambda item: (item[1], item[0]))
    return words_sorted



def split(string):
    left = right = 0
    res = {}
    delim = set([" ", "&"])
    while right < len(string):
        curr_char = string[right]
        if curr_char in delim:
            curr_word = string[left:right]
            if curr_word in res:
                res[curr_word] += 1
            else:
                res[curr_word] = 1
            right += 1
            left = right
        else:
            right += 1
    curr_word = string[left:right]
    if curr_word in res:
        res[curr_word] += 1
    else:
        res[curr_word] = 1
    if "" in res:
        del res[""]
    return res






str1 = "    abc       abc a&&&&&&&&&&a&cd&nvbdk     "
print(splitAndSort(str1))
