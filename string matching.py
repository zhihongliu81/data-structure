# brute force method to determine whether word is substring of string,
# if it is , return the start index;
# if it is not, return -1.
def isSubString(word, string):
    m = i = 0
    while m <= len(string) - len(word):

        if word[i] == string[m + i]:
            i += 1
            if i == len(word):
                return m
        else:
            m += 1
            i = 0
    return -1

"""
KMP algorithm:
m, denoting the position within string where the prospective match for word begins,
i, denoting the index of the currently considered character in word
in each step, the algorithm compares string[m + i] with word[i],
and increments i if they are equal;
if they are not equal:
    use the failure table to determine where the m and i move to.
    failure table: a list with the same length of word,
    the value is the longest prefix suffix of the substring word[0: i + 1]
    if i equal 0: move m one step
    if i not equal 0:
        move m to m + i - table[ i - 1]
        move i to table[i - 1]
"""
def KMP(word, string):
    if len(word) == 0:
        return 0
    table = LPS(word)
    m = i = 0
    while m <= len(string) - len(word):

        if word[i] == string[m + i]:
            i += 1
            if  i == len(word):
                return m
        else:
            if i == 0:
                 m += 1
            else:
                m = m + i - table[i - 1]
                i = table[i - 1]

    return -1


"""
   LPS function is used for building a failure table for the word.
   When we match the character of word and string one by one,
   if the character of the word is not the same as the charater of the string,
   we use the failure table to determine the move of m and i.
   m is the index of string, i is the index of word.
   The failure table is a list with same length of word.
   The value of table[i] of the failure table is
   the longest prefix suffix of the substring word[0, i + 1]
   First, we set all the value in the failure table to 0.
   Then, start to check i = 1.  We use pre to record the last character of substring
   which we try to find a match of the charcter at index i.

"""
def LPS(word):
    table = [0 for _ in range(len(word))]  # failure table
    pre, i = 0, 1   # pre, i are the indexes of table,
                    # i is the index of current character,
                    # pre is the index of next character of the current candidate substring
    while i < len(word):

        if word[i] == word[table[pre]]:
            table[i] = table[pre] + 1
            pre = i
            i += 1
        else:
            if table[pre] == 0:
                table[i] = 0
                pre = i
                i += 1
            else:
                pre = table[pre] - 1

    return table

word = "ABCDABD"
string = "ABC ABCDAB ABCDABCDABDE"
# print(isSubString(word, string))
print(KMP(word, string))

# print(LPS("abcdef"))
