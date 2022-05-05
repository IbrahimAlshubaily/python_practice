def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot: left+=1
        while array[right] > pivot: right-=1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left+=1
            right-=1
    return left

def __quick_sort(array, left, right):
    if left >= right:
        return
    partition_point = partition(array, left, right, pivot = array[(left+right)//2])
    __quick_sort(array, left, partition_point-1)
    __quick_sort(array, partition_point, right)

def quick_sort(array):
    __quick_sort(array, left=0, right = len(array)-1)



