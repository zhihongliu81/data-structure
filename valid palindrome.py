def isPalindrome(s):
    newStr = ''
    for letter in s:
        if letter.isalnum():
            newStr += letter

    newStr = newStr.lower()
    reversedStr = newStr[::-1]
    if newStr == reversedStr:
        return True

    return False
