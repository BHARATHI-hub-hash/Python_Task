# defining a function
def find_triplet(nums, target):
    #sort the numbers
    nums.sort()

    #iterate through the list
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:

                return (nums[i], nums[left], nums[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return None

nums = [10, 20, 30, 9]
target = 59
result = find_triplet(nums, target)

if result:
    print(f"Triplet fount: {result}")

else:
    print("No triplet found")

