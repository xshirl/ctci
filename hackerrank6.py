def count_substring(string, sub_string):
    substringLen = len(sub_string)
    count = 0
    for i in range(len(string)):
        if(string[i:i+substringLen]) == sub_string:
            # print(string[i: i+substringLen])
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

    # In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

    # While starting this problem, I knew I wanted to use a for loop to
    # loop through the characters in the string. and i knew i wanted to
    # separate each of the characters by the length of the substring
    # so i make a variable equal to the length of the substring. I also
    # know I want a count variable because we're counting number of times
    # the substring shows up in the string, so I set a count equal to 0.
    # in my for loop, i set the i equal to a number in the range of
    # the length of the string. i iterate thorugh the string and set an
    # if statement if the substring of the string that starts at the index
    # i and ends at the index i+ the length of the substring is equal to the
    # substirng, I add one to the count variable.
    # I then return the count.
