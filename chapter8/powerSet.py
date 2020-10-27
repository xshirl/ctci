def powerSet(nums):
    ans = []
    ans.append([])
    if not nums:
        return ans
    for num in nums:
        ans.extend([curr+[num] for curr in ans])

    return ans


print(powerSet([1, 2, 3, 4, 5]))
