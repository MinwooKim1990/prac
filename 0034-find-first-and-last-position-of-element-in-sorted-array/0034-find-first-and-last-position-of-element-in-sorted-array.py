class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Sort the list of numbers
        nums.sort()

        # Define the search range as the entire list
        left, right = 0, len(nums) - 1

        # Use binary search to find the target value
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # If the target value is found, search for its left and right indices
                left_index, right_index = mid, mid
                while left_index > 0 and nums[left_index - 1] == target:
                    left_index -= 1
                while right_index < len(nums) - 1 and nums[right_index + 1] == target:
                    right_index += 1
                return [left_index, right_index]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If the target value is not found, return [-1, -1]
        return [-1, -1]
