# Check to see if one string is permutation of other string

def permutation(str1, str2):
    newStr1 =  ''.join(sorted(str1))
    newStr2 =  ''.join(sorted(str2))

    if newStr1 == newStr2:
        return True
    else:
        return False

print(permutation('god', 'dog'))

print(permutation('cat', 'dog'))