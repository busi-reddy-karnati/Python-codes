def first_occurance(a, target):
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


def last_occurance(self, nums, target):
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