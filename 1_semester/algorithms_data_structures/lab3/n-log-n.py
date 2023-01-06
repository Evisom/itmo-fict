def f(s):
    if len(s) > 1:
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]
        f(left)
        f(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i += 1
            else:
                s[k] = right[j]
                j += 1
            k += 1
        if len(left) > i:
            s[k] = left[i]
        if len(right) > j:
            s[k] = right[j]
    return s


test = [4, 6, 7, 2, 5, 8]
print(f(test))