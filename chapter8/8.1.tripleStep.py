

def countWays(n):
    memo = [-1] * (n+1)
    return count(n, memo)


def count(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count(n-1, memo) + count(n-2, memo) + count(n-3, memo)
        return memo[n]


print(countWays(3))
