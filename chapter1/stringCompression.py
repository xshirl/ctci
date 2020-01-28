def stringCompression(string):
    dic = {}
    newStr = ''
    for char in string:
        if not char in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    for key, value in dic.items():
        newStr += key
        newStr += str(value)

    if len(string) == len(newStr):
        return string
    else:
        return newStr


print(stringCompression("aabbcc"))
print(stringCompression("aaabbbbbcc"))

# so given the string, you want to return the first character and the number of times the character shows up in the string.
# to do that, you should create a dictionary, because the dictionary would have a key which is equal to the char and
# the value would equal the count of the char. then you can iterate through the dictionary with a for loop and return the
# key and the value.
