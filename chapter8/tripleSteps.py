def tripleStep(n):
    counts = [1, 1, 2]
    if n < 3:
        return counts[n]
    i = 2
    while i < n:
        i += 1
        counts[i % 3] = sum(counts)
    return counts[i % 3]
