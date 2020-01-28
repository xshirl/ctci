def mutate_string(string, position, character):
    new_list = list(string)
    new_list[position] = character
    return ''.join(new_list)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# since strings are immutable, you have to convert a string to a list to change
# a character in the string. I made a new list and I set that to the list
# of the string. i set the new list's index equal to the position and
# then i set that equal to the character. I used join function to join
# the characters in the array together to make the string.
