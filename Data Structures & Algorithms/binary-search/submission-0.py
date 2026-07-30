class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The recursive binary search
        return self.binarySearch(0, len(nums) - 1, nums, target)

    def binarySearch(self, low, high, nums, target):
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(mid + 1, high, nums, target)
        else:
            return self.binarySearch(low, mid - 1, nums, target)