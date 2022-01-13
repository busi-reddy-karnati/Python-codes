def give_all_substrings(s):
    if not s:
        return []
    ans = []
    n = len(s)
    for left in range(n - 1):
        for right in range(left, n - 1):
            substring = s[left:right + 1]
            ans.append(substring)
    return ans


print(give_all_substrings("abcdef"))

