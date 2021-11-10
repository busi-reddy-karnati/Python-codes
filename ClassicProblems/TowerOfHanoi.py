def tower_of_hanoi(N, src, temp, dest) -> None:
    if N == 1:
        print("{} Moved from {} to {}".format(N, src, dest))
        return
    tower_of_hanoi(N - 1, src, dest, temp)
    print("{} Moved from {} to {}".format(N, src, dest))
    tower_of_hanoi(N - 1, temp, src, dest)


tower_of_hanoi(3, 'A', 'B', 'C')
