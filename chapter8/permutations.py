def partial_permutations(partial, letters_left):
    if len(letters_left) == 0:
        return [partial]
    permutations = []
    for i, letter in enumerate(letters_left):
        next_letters_left = letters_left[:i] + letters_left[(i+1):]
        permutations += partial_permutations(partial+letter, next_letters_left)

    return permutations


def permutations(string):
    return partial_permutations("", string)


print(permutations("abc"))


def permutations2(string):
    return partial_permutations("", sorted(string))


def partial_permutations2(partial, letters):
    if len(letters) == 0:
        return [partial]
    permutations = []
    previous_letter = None
    for i, letter in enumerate(letters):
        if letter == previous_letter:
            continue
        next_partial = partial + letter
        next_letters = letters[:i] + letters[(i+1):]
        permutations += partial_permutations2(next_partial, next_letters)
        previous_letter = letter
    return permutations


print(permutations2("abca"))
