def coverPoints(A, B):
    ans = 0;
    for i in range(len(A) - 1):
        ans += max(abs(A[i] - A[i + 1]), abs(B[i]- B[i + 1]))

    return ans;
A = [0, 1, 1]
B = [0, 1, 2]
print(coverPoints(A,B))