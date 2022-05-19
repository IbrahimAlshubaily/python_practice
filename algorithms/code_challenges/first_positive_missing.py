def first_positive_number_missing_sorted(numbers):
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i] > 0 and numbers[i + 1] > 0:
            if numbers[i] + 1 != numbers[i + 1]:
                return numbers[i] + 1
    return numbers[-1] + 1


def first_positive_number_missing_range(numbers) -> int:
    numbers = set(v for v in numbers if v > 0)
    max_num = max(numbers)
    for i in range(1, max(numbers)):
        if i not in numbers:
            return i
    return max_num + 1


def first_positive_number_missing_optimal(numbers) -> int:
    # move negative numbers to the beginning of the array and delete them:
    j = 0
    n = len(numbers)
    for i in range(n):
        if numbers[i] < 1:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
    del numbers[:j]
    # negate numbers[value] if value is positive (unvisited)
    for i, v in enumerate(numbers):
        curr_ind = abs(v) - 1
        if curr_ind < n - 1 and numbers[curr_ind] > 0:
            numbers[curr_ind] = -numbers[curr_ind]
    # if numbers[i] is positive, then i+1 was never visited
    for i, v in enumerate(numbers):
        if v > 0:
            return i + 1
    return n


print(first_positive_number_missing_sorted([3, 4, -1, 1]))
print(first_positive_number_missing_range([1, 2, 0]))
print(first_positive_number_missing_optimal([1, 2, 0]))
print(first_positive_number_missing_optimal([3, 4, -1, 1]))
print(first_positive_number_missing_optimal([0, 10, 2, -10, -20]))
print(first_positive_number_missing_optimal([2, 3, -7, 6, 8, 1, -10, 15]))
