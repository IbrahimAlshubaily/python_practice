#given a list l and number k, check if there are two elements in l that sum to k:
def two_sum_brute_force(nums , k):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False

def two_sum_sorted(nums , k):
    nums.sort()
    low, high = 0, len(nums)-1
    while low < high:
        curr_sum = nums[low] + nums[high]
        if curr_sum < k:
            low+=1
        elif curr_sum > k:
            high-=1
        else:
            return True
    return False

def two_sum_lookup(nums, k):
    lookup_table = {}
    for i in range(len(nums)):
        if nums[i] not in lookup_table:
            lookup_table[nums[i]] = [i]
        elif len(lookup_table[nums[i]]) < 3:
            lookup_table[nums[i]] + [i]
        #else if the number exist more than twice, there is no need to track additional occurences.
    
    for i in range(len(nums)):
        if k - nums[i] in lookup_table:
            for index in lookup_table[k - nums[i]]:
                if index != i:
                    return True

    return False
    

nums = [10, 7, 15, 3, 7, 7]
k  = 14
print(two_sum_brute_force(nums , k))
print(two_sum_sorted(nums , k))
print(two_sum_lookup(nums, k))