# Return true if permutation is a palindrome, false is not 

# to solve this problem, every character except for 1 character must appear even number of times, 
# or every character appears an even number of times. 


def palinPerm(string):
    chars = {}
    currChar = ""
    mulligan = False
    isPerm = True

    arr = [i for i in string]
    for char in arr:
        if (char != ' '):
            currChar = char.lower()
            if (currChar not in chars):
                chars[currChar] = 1
            else:
                chars[currChar] += 1
    print(chars)

    for key, value in chars.items():
        if (value % 2 > 0):
            if (mulligan):
                isPerm = False
            else:
                mulligan = True # first time a char appears odd num of times, mulligan is false so isPerm is still true, but second time is True, so isPerm is false.

    return isPerm


print(palinPerm("Tact Coa"))
print(palinPerm("Tact boa"))
print(palinPerm("cattac"))
