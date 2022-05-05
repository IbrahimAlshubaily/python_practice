from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from random import shuffle

def test_method(sorting_function, inplace = False):
    for n in [20, 25, 75, 101, 1234]:
        test_case = list(range(n))
        shuffle(test_case)
        if inplace:
            sorting_function(test_case)
        else:
            test_case = sorting_function(test_case)
        assert(test_case == list(range(n)))


test_method(merge_sort, inplace = False)
test_method(quick_sort, inplace = True)
test_method(bubble_sort, inplace = True)
print('Unit tests passed!')