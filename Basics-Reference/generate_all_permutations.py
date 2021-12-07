"""
This comes from the logic that permutations of [1,2,3] = 1+permutations[2,3], 2+permutations[1,3], 3+permutations[1,2]
"""


def generate_permutations(nums, start):
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
        # nums[start], nums[i] = nums[i], nums[start]
    return ret


print(generate_permutations([1, 2, 3], 0))
