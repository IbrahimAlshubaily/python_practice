def product_except_index_division(nums):
    product = 1
    for v in nums:
        product*=v
    return [int(product/num) for num in nums]

def product_except_index_no_division(nums):
    prefix = [1] + nums.copy()
    suffix = nums.copy() + [1]
    for i in range(1,len(prefix)):
        prefix[i] *= prefix[i-1]
        suffix[-i-1] *= suffix[-i]
    return [prefix[i]*suffix[i+1] for i in range(len(nums))] 

def product_except_index_optimal(nums):
    prod = [0]*len(nums)
    curr = 1 
    for i in range(len(nums)):
        prod[i] = curr
        curr *= nums[i]
    curr = 1
    for i in range(1, len(nums)+1):
        prod[-i] *= curr
        curr *= nums[-i]
    return prod
    
test_case_one = [1, 2, 3, 4, 5]
test_case_two = [10, 3, 5, 6, 2]
for test_case in [test_case_one, test_case_two]:
    print(product_except_index_division(test_case))
    print(product_except_index_no_division(test_case))
    print(product_except_index_optimal(test_case))

