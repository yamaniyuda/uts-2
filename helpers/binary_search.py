def binarySearch(arr, l, r, x, key):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid][key] == x:
            return mid
        elif arr[mid][key] > x:
            return binarySearch(arr, l, mid-1, x, key)
        else:
            return binarySearch(arr, mid + 1, r, x, key)

    else:
        return -1
