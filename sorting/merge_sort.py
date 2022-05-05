def merge(array_a, array_b):
    i,j = 0, 0
    merged_array = []
    while i < len(array_a) and j < len(array_b):
        if array_a[i] < array_b[j]:
            merged_array.append(array_a[i])
            i+=1
        else:
            merged_array.append(array_b[j])
            j+=1
    return merged_array + array_a[i:] + array_b[j:]

def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
