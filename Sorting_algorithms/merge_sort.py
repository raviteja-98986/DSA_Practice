def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge_array(left_half, right_half)


def merge_array(left_half, right_half):
    l = r = 0
    m, n = len(left_half), len(right_half)
    res = []

    while l < m and r < n:
        if left_half[l] <= right_half[r]:
            res.append(left_half[l])
            l += 1
        else:
            res.append(right_half[r])
            r += 1

    while l < m:
        res.append(left_half[l])
        l += 1

    while r < n:
        res.append(right_half[r])
        r += 1

    return res


arr = [1, 5, 8, 9, 3, 2]
print(merge_sort(arr))