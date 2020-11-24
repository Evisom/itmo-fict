def pow1(x, n):
    # x - число 
    # n - степень
    return round(x**n, 2)

def pow2(x, n, y=None):
    # x - число 
    # n - степень
    if n == 0:
        return 1
    if not(y):
        y = x
    if n == 1:
        return y
    return pow2(x, n-1, y*x)


for i in range(0, 12):
    print(pow1(2,i), pow2(2,i))