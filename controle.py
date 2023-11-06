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
    

    ###hash####

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def get_sorted_table(self):
        sorted_table = []
        for bucket in self.table:
            if bucket is not None:
                sorted_table.extend(bucket)
        sorted_table.sort(key=lambda x: x[0])  # Ordena com base nas chaves
        return sorted_table

