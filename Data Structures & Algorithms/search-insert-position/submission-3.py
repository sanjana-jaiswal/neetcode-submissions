import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # The built in binary search
        return bisect.bisect_left(nums,target)