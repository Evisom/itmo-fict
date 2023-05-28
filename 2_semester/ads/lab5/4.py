def stair(s, n):
    if s > n:
        return 0
    elif s == n:
        return 1
    else:
        return stair(s+1, n) + stair(s+2, n) + stair(s+3, n)


print(stair(0, 5))
