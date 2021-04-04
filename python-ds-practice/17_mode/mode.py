

def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most = nums[0]
    counts = {}

    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    for n in nums:
        if(counts[n] > counts[most]):
            most = counts[n]

    return most

print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))