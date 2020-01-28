
d = {}

for i in range(int(input())):
    name = input()
    grade = float(input())
    d[name] = grade

v = d.values()

second = sorted(list(set(v)))[1]
second_lowest = []

for key, value in d.items():
    if value == second:
        second_lowest.append(key)
second_lowest.sort()
for name in second_lowest:
    print(name)

# you want to make a dictionary with the names of students
# and their scores. you create an array of their scores through 
# calling the values function. you create a set to get rid of 
# duplicate values, then call list function, and then call sorted
# function to sort the scores. you create an array to store
# the names of students with the second lowest score. you 
# create a for loop to loop through the dictionary and if the second
# lowest score is equal to the score of the student, append the 
# name of the student into the names array. then use a for loop 
# to print out all the names of the students with the second lowest 
# score. 