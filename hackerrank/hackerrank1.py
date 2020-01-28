if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    avg_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        avg_scores = sum(scores) / float(len(scores))
        avg_marks[name] = avg_scores
    query_name = input()
    print("%.2f" % avg_marks[query_name])

#     3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# they give you a dictionary student marks where each name corresponds to 
# an arry of scores. I created a new dictionary avg marks where each name
# corresponds to the avg of the person's scores. you create the avg by
# taking the sum function and dividing it by the length of the scores array
# you want a float number so use float function. 
# i make the dictionary key to be the name and the value is the avg as a 
# float. 
# i print the number as a float with two decimal points and call the 
# dictionary with the key as the query name. this gives the avg with two
# decimal points. 
