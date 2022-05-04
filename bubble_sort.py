def bubble_sort(array):
    last_unsorted = len(array)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(last_unsorted-1):
            if array[i] > array[i+1]:
                is_sorted = False
                array[i], array[i+1] = array[i+1], array[i]
        last_unsorted-=1