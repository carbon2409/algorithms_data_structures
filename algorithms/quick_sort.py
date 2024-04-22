import random

lst = [1, 5, 2, 7, 1, 9, 0, 0, -5, 20, 36, 0, 46, 574, -14]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr)-1)]
    left = [i for i in arr if i < pivot]
    equals = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + equals + quick_sort(right)


print(quick_sort(lst))

