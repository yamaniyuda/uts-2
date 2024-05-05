from enum import Enum


class Sort(Enum):
    ASC = 'asc'
    DSC = 'dsc'


def quicksort(arr: list, key: str, sort: Sort = Sort.ASC) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0][key]

        if sort == Sort.ASC:
          less_than_pivot = [x for x in arr[1:] if x[key] <= pivot]
          greater_than_pivot = [x for x in arr[1:] if x[key] > pivot]
        
        if sort == Sort.DSC:
          less_than_pivot = [x for x in arr[1:] if x[key] >= pivot]
          greater_than_pivot = [x for x in arr[1:] if x[key] < pivot]

        return quicksort(less_than_pivot, key) + [arr[0]] + quicksort(greater_than_pivot, key)
