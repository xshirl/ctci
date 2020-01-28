cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    fib = []
    for i in range(n):
        if i == 0:
            fib.append(0)
        if i == 1:
            fib.append(1)
        if i > 1:
            fib.append(fib[i-1] + fib[i-2])
    return fib


    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# the lambda function is simple, just do x**3 to cube it
# for the fibonacci function, create an empty array. 
# you need a for loop, set i to loop through range of n. 
# if i = 0, have fib append 0. and if i = 1, have fib append
# 1. then if i is greater than 1, have fib append the previous
# two numbers, equal to fib[i-1] and fib[i-2]. that's how
# you sum up the previous two numbers and append the new numbers
