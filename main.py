def isvalid(s):
    print(s)
    if len(set(list(s))) == 1:
        return True
    return False


def answer(s):
    n = len(s)
    if n % 2:
        print(-1)
        return
    div = 1
    ans = 1
    while div <= n:
        if n % div != 0:
            print(-1)
            return
        idx = 0
        for i in range(div):
            nu = int(idx + (n / div))
            print(idx,nu)
            if isvalid(s[idx:nu]):
                # print(s[idx:nu])
                print(ans - 1)
                return
            idx = int(idx + (n / div))
        ans += 1
        div *= 2
    print(-1)


t = int(input())
for i in range(t):
    s = input()
    answer(s)
