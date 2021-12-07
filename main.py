def give_ans(n,ar):
    if n == 1:
        return 0
    hmap = {}
    max_freq = 0
    for num in ar:
        if num in hmap:
            hmap[num]+=1
            max_freq = max(max_freq,hmap[num])
        else:
            hmap[num] = 1

    if max_freq < 2:
        return -1
    init_lists = n
    final_lists = max_freq//2
    return init_lists-final_lists
t = int(input())
for i in range(t):
    n = int(input())
    ar = list(map(int,input().split()))
    print(give_ans(n,ar))


