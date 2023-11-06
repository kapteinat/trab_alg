def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].chave < right[j].chave:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr, compare_func=lambda x, y: x.chave <= y.chave):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if compare_func(x, pivot)]
        greater = [x for x in arr[1:] if not compare_func(x, pivot)]
        return quick_sort(lesser, compare_func) + [pivot] + quick_sort(greater, compare_func)
