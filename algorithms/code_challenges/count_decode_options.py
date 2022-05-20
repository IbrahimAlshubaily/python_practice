def count_decode_options_dp(nums: str) -> int:
    n = len(nums)
    count = [0] * n
    count[0] = 1 if nums[0] > '0' else 0
    for i in range(1, n):
        count[i] = count[i - 1] if nums[i] > '0' else 0
        if 9 < int(nums[i - 1:i + 1]) < 27:
            count[i] += count[i - 2] if i > 1 else 1
    return count[-1]


print(count_decode_options_dp('111'))
print(count_decode_options_dp('12'))
print(count_decode_options_dp('1234'))

