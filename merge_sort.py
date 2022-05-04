def merge(arr_a, arr_b):
    i,j = 0, 0
    merged_arr = []
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] < arr_b[j]:
            merged_arr.append(arr_a[i])
            i+=1
        else:
            merged_arr.append(arr_b[j])
            j+=1
    merged_arr.extend(arr_a[i:])
    merged_arr.extend(arr_b[j:])
    return merged_arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

import random
for n in [20, 25, 50, 75]:
    test_case = list(range(n))
    random.shuffle(test_case)
    print(test_case)
    test_case_a = merge_sort(test_case)
    assert(test_case_a == list(range(n)))
    print(test_case_a)
    print('-'*25)
