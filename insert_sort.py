def insert_sort(array):
    for index in range(len(array)):
        min_value, min_index = 1e+6, -1
        for i, value in enumerate(array[index:]):
            if value < min_value:
                min_value = value
                min_index = index+i
        array[index], array[min_index] = array[min_index], array[index]