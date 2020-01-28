def oneEditAway(s1, s2):
    if len(s1) == len(s2):
        return oneEditReplace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return oneEditInsert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return oneEditInsert(s2, s1)
    return False


def oneEditReplace(s1, s2):
    diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diff:  # So if there is 1 character difference, it is True, if more than 1 char difference, return False
                return False
            diff = True
    return True


def oneEditInsert(s1, s2):
    index1 = 0
    index2 = 0
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


print(oneEditAway("pale", "ple"))

print(oneEditAway("pales", "pale"))

print(oneEditAway("pale", "bale"))

print(oneEditAway("pale", "bake"))
