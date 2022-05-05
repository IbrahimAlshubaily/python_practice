def binary_search(sorted_array, value):
    return _binary_search(sorted_array, value, left=0, right=len(sorted_array)-1)

def _binary_search(sorted_array, value, left, right):
    if left > right:
        return -1
    mid = (left+right)//2
    if sorted_array[mid] == value:
        return mid
    return _binary_search(sorted_array, value, left, mid-1) if value < sorted_array[mid]  else _binary_search(sorted_array, value, mid+1, right)
    


n = 99
for v in range(n):
    assert(v == binary_search(list(range(n)), v))
