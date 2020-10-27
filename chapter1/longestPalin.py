
def palinPerm(str):
    chars = {}
    mulligan = False
    isPerm = True

    arr = [i for i in str]

    for char in arr:
        if char != " ":
            currChar = char.lower()
            if currChar not in chars:
                chars[currChar] = 1
            else:
                chars[currChar] += 1

    for key, value in chars.items():
        if value % 2 > 0:
            if mulligan:
                isPerm = False
            else:
                mulligan = True

    return isPerm


print(palinPerm("Tact Coa"))
print(palinPerm("Tact boa"))
print(palinPerm("cattac"))


def stringCompression(str):
    chars = {}
    newStr = ''

    for char in str:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    for key, value in chars.items():
        newStr += key
        newStr += str(value)

    return newStr


def isSubstring(string, sub):
    return string.find(sub) != -1


def stringRotation(str1, str2):
    if len(str1) == len(str2) != 0:
        return isSubstring(str1+str1, str2)
    return False
