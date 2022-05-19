# given a list and a number k, check if there are two elements in the list that sum to k:
def two_sum_brute_force(nums, k):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False


def two_sum_sorted(nums, k):
    nums.sort()
    low, high = 0, len(nums) - 1
    while low < high:
        curr_sum = nums[low] + nums[high]
        if curr_sum < k:
            low += 1
        elif curr_sum > k:
            high -= 1
        else:
            return True
    return False


def two_sum_lookup(nums, k):
    lookup_table = {}
    for i in range(len(nums)):
        if nums[i] not in lookup_table:
            lookup_table[nums[i]] = [i]
        elif len(lookup_table[nums[i]]) < 3:
            lookup_table[nums[i]] = lookup_table[nums[i]] + [i]
        # else if the number exist more than twice, there is no need to track additional occurrences.
    for i in range(len(nums)):
        if k - nums[i] in lookup_table:
            for index in lookup_table[k - nums[i]]:
                if index != i:
                    return True
    return False


def two_sum_complement_lookup(nums, k):
    complements_set = set()
    for v in nums:
        if v in complements_set:
            return True
        complements_set.add(k - v)
    return False


k = 17
nums = [10, 5, 15, 3, 7, 7, 7]
# print(two_sum_brute_force(nums , k))
# print(two_sum_sorted(nums , k))
# print(two_sum_lookup(nums, k))
print(two_sum_complement_lookup(nums, k))
