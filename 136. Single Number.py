class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for x in nums:
            ans ^= x #亦或操作
        return ans
