lst = [1, 5, 2, 7, 1, 9, 0, 0, -5, 20, 36, 0]
lst.sort()


def binary_search(arr, item):
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= item:
            r = mid
        else:
            l = mid + 1
    return (True, item) if arr[l] == item else False


print(binary_search(lst, 9))


def rec(arr, item):
    if len(arr) == 1:
        return True, arr[0]
    mid = len(arr) // 2
    if arr[mid] >= item:
        return rec(arr[:mid + 1], item)
    elif arr[mid] < item:
        return rec(arr[mid + 1:], item)


print(rec(lst, 9))
