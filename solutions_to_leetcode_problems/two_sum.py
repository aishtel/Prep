# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9
# Because nums[0] + nums[1] = 2 + 7 = 9
# return [0, 1]


class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


solution = Solution()
print "----------------------------------------------------------------------------"
print "Given an array of integers, "
print "return indices of the two numbers such that they add up to a specific target. \n"
print "Nums = [2, 7, 11, 15], Target = 9"
print "The indices of the two numbers are:", solution.two_sum([2, 7, 11, 15], 9)
print "----------------------------------------------------------------------------"

