from collections import Counter

#defining function
def first_non_repeating(nums):
    # Count the frequency of each element using COunter
    count  = Counter(nums)

    for num in nums:
        if count[num] == 1:
            return num
    return None

nums = [4, 5, 6, 5, 4, 7, 8, 7]
result  = first_non_repeating(nums)

if result is not None:
    print(f"The first non-repeating number is: {result}")
else:
    print("No non-repeating number.")