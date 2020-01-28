def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# explanation
# You want to return strings with width equal to max width. So you should
# have a value from 0 to max-width - 1 and onward until the last letter in string
# YOu should have a for loop where for index in range(0, len(string, max-width))
# because this will give you the index at every max-width interval.
# then you want to create substrings, so you have string[i: i+ max-width], which
# will return a substring that contains max-width nubmer of letters.
# Then you have to have a new line so use join to join all the substrings with
# a new line separating each substring.

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
