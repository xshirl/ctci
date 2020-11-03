def magic_index_distinct(array):
    if len(array) == 0 or array[0] > 0 or array[-1] < len(array) - 1:
        return None
    return magic_index_distinct_bounds(array, 0, len(array))


def magic_index_distinct_bounds(array, low, high):
    if low == high:
        return None
    mid = (low + high) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return magic_index_distinct_bounds(array, low, mid)
    else:
        return magic_index_distinct_bounds(array, mid+1, high)


def magic_index(array):
    i = 0
    while i < len(array):
        if i == array[i]:
            return i
        i = max(array[i], i+1)
