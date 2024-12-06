#defining a function
def has_zero_sum_sublist(nums):
    prefix_sum = 0
    seen_sums = set()

    for num in nums:
        # Adding current number
        prefix_sum += num

        # Check if the prefix sum is 0
        if prefix_sum == 0 or prefix_sum in seen_sums:
            return True

        # Adding current prefix sum
        seen_sums.add(prefix_sum)

    # If no sublist with sum 0 is found
    return False



nums = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(nums)

if result:
    print("There is a sublist with sum equal to zero.")
else:
    print("No sublist with sum equal to zero.")

