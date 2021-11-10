"""
Rabin Karp is used for pattern matching.
This algorithm uses a Rolling Hash approach
"""


def rabin_karp_match(text, pattern):
    prime = 5381
    if len(pattern) > len(text):
        return False
    p_len = len(pattern)
    t_len = len(text)
    window_hash = 0
    p_hash = 0
    for i in range(p_len):
        weight = p_len - i - 1
        p_hash = (p_hash + (ord(pattern[i]) - ord('a') + 1) * (26 ** weight)) % prime
        window_hash = (window_hash + (ord(text[i]) - ord('a') + 1) * (26 ** weight)) % prime
    if window_hash == p_hash:
        for i in range(p_len):
            if pattern[i] != text[i]:
                break
            if i == p_len - 1:
                return True
    for i in range(1, t_len - p_len + 1):
        window_hash -= ((ord(text[i - 1]) - ord('a') + 1) * (26 ** (p_len - 1))) % prime
        window_hash = (window_hash * 26) % prime
        window_hash += (ord(text[i + (p_len - 1)]) - ord('a') + 1)
        if window_hash == p_hash:
            for j in range(p_len):
                if pattern[j] != text[j + i]:
                    break
                if j == p_len - 1:
                    return True

    return False


text = "abhjgjsjskkodaeijfoaujhsadkahjdsba"
pattern = "aeijfoaujhf"
print(rabin_karp_match(text, pattern))
