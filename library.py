def first_occurance(a, target):
    """

    :param a: array
    :param target: target integet
    :return: index of first occurance of a number or -1
    """
    hi = len(a) - 1
    lo = 0
    ans = -1
    while lo <= hi:
        mid = int((lo + hi) / 2)
        if a[mid] == target:
            ans = mid
            hi = mid - 1
        elif a[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return ans


def last_occurance(nums, target):
    """

    :param nums: array
    :param target: the target integer
    :return: index of last occurance or -1
    """
    ans = -1
    hi = len(nums) - 1
    lo = 0
    while hi >= lo:
        mid = int((lo + hi) / 2)
        if nums[mid] == target:
            ans = mid
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


def generate_permutations(nums, start):
    """

    :param nums: array
    :param start: index from which the permutations should start
    :return: a list of lists that is permutations
    """
    if start == len(nums):
        return [[]]
    ret = []
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        perms = generate_permutations(nums, start + 1)
        for perm in perms:
            perm.append(nums[start])
        ret.extend(perms)
        # In the step before, you swapped [1,2,3] => [2,1,3] Now 2 and 3 will get swapped, which is not expected, so
        # Swap again
        nums[start], nums[i] = nums[i], nums[start]
    return ret
