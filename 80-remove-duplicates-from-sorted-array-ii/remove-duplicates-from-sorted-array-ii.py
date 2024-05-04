class Solution(object):
    def removeDuplicates(self, nums):
    
        if len(nums) <= 2:
            return len(nums)

        # Initialize two pointers: one for iterating the array and one for keeping track of the position to overwrite
        slow = 2
        for fast in range(2, len(nums)):
            # If the current number is different from the number two positions before,
            # update the slow pointer and overwrite the value at the slow pointer with the current number
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow

    