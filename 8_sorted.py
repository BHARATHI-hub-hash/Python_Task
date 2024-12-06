#defining a function

def find_min_in_rotated_sorted(nums):
    low, high = 0, len(nums) - 1

    #if list empty return none
    if not nums:
        return None

    #if the list is already sorted
    if nums[low] < nums[high]:
        return nums[low]

    #Binary search approach
    while low <= high:
        mid = (low + high) // 2

        #Check if the mid is the minimum element
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # Decide which half to search
        if nums[mid] >= nums[low]:
            low = mid + 1
        else:
            high = mid - 1

    return None

nums = [4, 5, 6, 7, 0, 1, 2]
min_element = find_min_in_rotated_sorted(nums)

print(f"The minimum element is : {min_element}")
