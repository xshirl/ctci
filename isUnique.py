def isUnique(str):
    dic = {}

    for char in str:
        if not char in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    
    for keys, values in dic.items():
        if values > 1:
            return False
        else:
            return True

print(isUnique('AAb'))
print(isUnique('ab'))