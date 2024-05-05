def binary_search(list, value, key):
    start = 0
    last = len(list) - 1
    result_index = []
    result = []

    while start <= last:
        middle = (start + last) // 2
        if list[middle][key].startswith(value):
            result_index.append(middle)

            # check match entry in left
            i = middle - 1
            while i >= 0 and list[i][key].startswith(value):
                result_index.append(i)
                i -= 1

            # check match entry in right
            i = middle + 1
            while i < len(list) and list[i][key].startswith(value):
                result_index.append(i)
                i += 1

            for i in result_index:
                result.append(list[i])
            return result
        elif list[middle][key] < value:
            start = middle + 1
        else:
            last = middle - 1

    for i in result_index:
        print(i)
        result.append(list[i])

    return result
