class Solution:
    @staticmethod
    def modifyArray(a):
        n = len(a)
        for i in range(n):
            if a[i] <= 0:
                a[i] = n + 1
        return a

    def firstMissingPositive(self, a):
        self.modifyArray(a)
        n = len(a)
        for i in range(n):
            val = abs(a[i])
            if val <= n:
                a[val - 1] = -(abs(a[val - 1]))
        for i in range(n):
            if a[i] > 0:
                return i + 1
        return n + 1
