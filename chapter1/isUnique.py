# Determine if a string has all unique characters.


def isUnique(str):
    letters = {}
    for char in str:
        if char in letters:
            return False
        letters[char] = True
    return True


print(isUnique('AAb'))
print(isUnique('abb'))
